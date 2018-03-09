from django.contrib.admin import site

from . import models

site.register(models.Utilisateur)
site.register(models.Periode)
site.register(models.Course)
site.register(models.Repas)
