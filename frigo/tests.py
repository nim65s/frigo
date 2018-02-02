from datetime import date

from django.test import TestCase
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils.timezone import now

from .models import Utilisateur, Course, Repas


class FrigoTests(TestCase):
    def setUp(self):
        for guy in 'abc':
            user = User.objects.create_user(guy, email=f'{guy}@example.org', password=guy)
            Utilisateur.objects.create(user=user)

    def test_models(self):
        a, b, c = User.objects.all()
        course = Course.objects.create(date=date(2017, 6, 2), montant=30, payeur=a.utilisateur)
        repas = Repas.objects.create(date=date(2017, 6, 2))
        repas.mangeurs.set(Utilisateur.objects.all())

        self.assertEqual(str(course), '02/06/2017: 30 € par a')
        self.assertEqual(str(repas), '02/06/2017: a, b, c')

        repas = Repas.objects.create(date=date(2017, 6, 3))
        repas.mangeurs.add(Utilisateur.objects.first())

        repas = Repas.objects.create(date=date(2017, 6, 4))
        repas.mangeurs.add(Utilisateur.objects.last())

        repas = Repas.objects.create(date=date(2017, 6, 5))
        repas.mangeurs.add(Utilisateur.objects.first())

        self.assertEqual(course.repas(), 4)
        self.assertEqual(course.mangeurs(), 6)
        self.assertEqual(course.part(), 5)

        self.assertEqual(a.utilisateur.solde(), 15)
        self.assertEqual(b.utilisateur.solde(), -5)
        self.assertEqual(c.utilisateur.solde(), -10)
