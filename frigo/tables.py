import django_tables2 as tables

from . import models


class UtilisateurTable(tables.Table):
    solde = tables.Column(accessor='solde', orderable=False)

    class Meta:
        model = models.Utilisateur
        fields = ('user',)


class PeriodeTable(tables.Table):
    repas = tables.Column(accessor='repas', orderable=False)
    mangeurs = tables.Column(accessor='mangeurs', orderable=False)
    courses = tables.Column(accessor='courses', orderable=False)
    montant = tables.Column(accessor='montant', orderable=False)
    part = tables.Column(accessor='part', orderable=False)

    class Meta:
        model = models.Periode
        fields = ('debut',)


class CourseTable(tables.Table):
    class Meta:
        model = models.Course
        fields = ('date', 'montant', 'payeur', 'periode')


class RepasTable(tables.Table):
    class Meta:
        model = models.Repas
        fields = ('date', 'mangeurs', 'periode')
