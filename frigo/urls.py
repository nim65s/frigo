from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('courses', views.CourseView.as_view(), name='courses'),
    path('courses/add', views.CourseCreateView.as_view(), name='add-course'),
    path('repas', views.RepasView.as_view(), name='repas'),
    path('repas/add', views.RepasCreateView.as_view(), name='add-repas'),
    path('', views.UtilisateurView.as_view(), name='utilisateurs'),
]
