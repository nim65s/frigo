from django.views.generic import CreateView

from django_tables2.views import SingleTableView

from . import models


class RepasView(SingleTableView):
    model = models.Repas


class CourseView(SingleTableView):
    model = models.Course


class UtilisateurView(SingleTableView):
    model = models.Utilisateur
