from django.template.defaultfilters import floatformat

import django_tables2 as tables

from . import models


class UtilisateurTable(tables.Table):
    solde = tables.Column(accessor='solde', orderable=False, attrs={'td': {'class': 'euro'}})

    class Meta:
        model = models.Utilisateur
        fields = ('user', )

    def render_solde(self, value):
        return floatformat(value, 2)


class PeriodeTable(tables.Table):
    mangeurs = tables.Column(accessor='mangeurs', orderable=False)
    courses = tables.Column(accessor='courses', orderable=False)
    montant = tables.Column(accessor='montant', orderable=False, attrs={'td': {'class': 'euro'}})
    part = tables.Column(accessor='part', orderable=False, attrs={'td': {'class': 'euro'}})

    class Meta:
        model = models.Periode
        fields = ('debut', )

    def render_montant(self, value):
        return floatformat(value, 2)

    def render_part(self, value):
        return floatformat(value, 2)


class CourseTable(tables.Table):
    montant = tables.Column(attrs={'td': {'class': 'euro'}})

    class Meta:
        model = models.Course
        fields = ('date', 'montant', 'payeur', 'periode')

    def render_montant(self, value):
        return floatformat(value, 2)


class RepasTable(tables.Table):
    class Meta:
        model = models.Repas
        fields = ('date', 'mangeurs', 'periode')
