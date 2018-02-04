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
