from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from django_tables2.views import SingleTableView

from . import models, tables


class RepasView(SingleTableView):
    model = models.Repas
    table_class = tables.RepasTable


class CourseView(SingleTableView):
    model = models.Course
    table_class = tables.CourseTable


class UtilisateurView(SingleTableView):
    model = models.Utilisateur
    table_class = tables.UtilisateurTable


class RepasCreateView(LoginRequiredMixin, CreateView):
    model = models.Repas
    fields = ('date', 'mangeurs', 'courses')


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = models.Course
    fields = ('date', 'montant', 'payeur')
