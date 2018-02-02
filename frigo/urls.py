from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('courses', views.CourseView.as_view(), name='courses'),
    path('repas', views.RepasView.as_view(), name='repas'),
    path('utilisateurs', views.UtilisateurView.as_view(), name='utilisateurs'),
]
