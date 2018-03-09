from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from django_tables2.views import SingleTableView
from ndh.mixins import NDHFormMixin

from . import models, tables


class PeriodeView(SingleTableView):
    model = models.Periode
    table_class = tables.PeriodeTable


class RepasView(SingleTableView):
    model = models.Repas
    table_class = tables.RepasTable


class CourseView(SingleTableView):
    model = models.Course
    table_class = tables.CourseTable


class UtilisateurView(SingleTableView):
    model = models.Utilisateur
    table_class = tables.UtilisateurTable


class RepasCreateView(LoginRequiredMixin, NDHFormMixin, CreateView):
    model = models.Repas
    fields = ('date', 'mangeurs', 'periode')
    title = 'Ajouter un repas'


class CourseCreateView(LoginRequiredMixin, NDHFormMixin, CreateView):
    model = models.Course
    fields = ('date', 'montant', 'payeur', 'periode')
    title = 'Ajouter des courses'


class PeriodeCreateView(LoginRequiredMixin, NDHFormMixin, CreateView):
    model = models.Periode
    fields = []
    title = 'Passer à un nouvelle Période'
