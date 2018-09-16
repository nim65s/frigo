from datetime import date

from django.conf import settings
from django.db import models

from ndh.models import Links
from ndh.utils import query_sum


class Utilisateur(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user)

    def solde(self):
        solde = query_sum(self.course_set, 'montant')
        for periode in Periode.objects.all():
            solde -= periode.part() * periode.repas_set.filter(mangeurs=self).count()
        return solde


class Periode(Links, models.Model):
    absolute_url_detail = False
    debut = models.DateField('début', auto_now_add=True)

    class Meta:
        ordering = ('debut', )

    def __str__(self):
        return f'{self.debut:%d/%m/%Y}'

    def repas(self):
        return self.repas_set.count()

    def mangeurs(self):
        # TODO single query
        return sum(repas.mangeurs.count() for repas in self.repas_set.all())

    def courses(self):
        return self.course_set.count()

    def montant(self):
        return query_sum(self.course_set, 'montant')

    def part(self):
        return self.montant() / self.mangeurs()


def last_periode():
    return Periode.objects.last()


class Course(Links, models.Model):
    absolute_url_detail = False
    date = models.DateField(default=date.today)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    payeur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)
    periode = models.ForeignKey(Periode, on_delete=models.PROTECT, default=last_periode)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return f'{self.date:%d/%m/%Y}: {self.montant} € par {self.payeur.user}'


class Repas(Links, models.Model):
    absolute_url_detail = False
    date = models.DateField(default=date.today)
    mangeurs = models.ManyToManyField(Utilisateur)
    periode = models.ForeignKey(Periode, on_delete=models.PROTECT, default=last_periode)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        mangeurs = ', '.join(str(user) for user in self.mangeurs.all())
        return f'{self.date:%d/%m/%Y}: {mangeurs}'
