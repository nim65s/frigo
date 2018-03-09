from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Course, Periode, Repas, Utilisateur


class FrigoTests(TestCase):
    def setUp(self):
        for guy in 'abc':
            user = User.objects.create_user(guy, email=f'{guy}@example.org', password=guy)
            Utilisateur.objects.create(user=user)

    def test_all(self):
        a, b, c = Utilisateur.objects.all()

        # Models

        periode = Periode.objects.create(debut=date(2017, 5, 1))

        course = Course.objects.create(date=date(2017, 6, 2), montant=30, payeur=a)
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

        self.assertEqual(periode.repas(), 4)
        self.assertEqual(periode.mangeurs(), 6)
        self.assertEqual(periode.part(), 5)

        self.assertEqual(a.solde(), 15)
        self.assertEqual(b.solde(), -5)
        self.assertEqual(c.solde(), -10)

        # Views
        views = ['courses', 'repass', 'utilisateurs', 'periodes', 'add-course', 'add-repas', 'add-periode']
        for view in views:
            self.assertEqual(self.client.get(reverse(view)).status_code, 302 if 'add' in view else 200)
        self.client.login(username='a', password='a')
        for view in views:
            self.assertEqual(self.client.get(reverse(view)).status_code, 200)

        # Create

        repas = {'date': date.today(), 'mangeurs': [1, 2], 'periode': 1}
        self.assertEqual(Repas.objects.count(), 4)
        r = self.client.post(reverse('frigo:add-repas'), repas)
        self.assertEqual(Repas.objects.count(), 4)
        self.assertEqual(r.status_code, 302)

        self.client.login(username='a', password='a')

        r = self.client.post(reverse('frigo:add-repas'), repas)
        self.assertEqual(Repas.objects.count(), 5)
        self.assertEqual(r.status_code, 302)

        course = {'date': date.today(), 'montant': 10.42, 'payeur': 2, 'periode': 1}
        self.assertEqual(Course.objects.count(), 1)
        r = self.client.post(reverse('frigo:add-course'), course)
        self.assertEqual(periode.courses(), 2)
        self.assertEqual(r.status_code, 302)
