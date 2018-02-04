from datetime import date
from decimal import Decimal

from django.conf import settings
from django.db import models
from django.urls import reverse

from ndh.utils import query_sum


class Utilisateur(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user)

    def solde(self):
        solde = Decimal()
        for course in Course.objects.all():
            if course.payeur == self:
                solde += course.montant
            solde -= course.part() * course.repas_set.filter(mangeurs=self).count()
        return solde


class Course(models.Model):
    date = models.DateField(default=date.today)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    payeur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return f'{self.date:%d/%m/%Y}: {self.montant} € par {self.payeur.user}'

    def get_absolute_url(self):
        return reverse('courses')

    def repas(self):
        return self.repas_set.count()

    def mangeurs(self):
        return sum(repas.mangeurs.count() for repas in self.repas_set.all())

    def part(self):
        return self.montant / self.mangeurs()


def last_course():
    return Course.objects.last()


class Repas(models.Model):
    date = models.DateField(default=date.today)
    mangeurs = models.ManyToManyField(Utilisateur)
    courses = models.ForeignKey(Course, default=last_course, on_delete=models.PROTECT)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        mangeurs = ', '.join(str(user) for user in self.mangeurs.all())
        return f'{self.date:%d/%m/%Y}: {mangeurs}'

    def get_absolute_url(self):
        return reverse('repas')
