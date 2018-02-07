from django.contrib.admin import site

from .models import Course, Utilisateur, Repas

for model in [Course, Utilisateur, Repas]:
    site.register(model)
