from django.urls import path

from . import views

app_name = 'frigo'
urlpatterns = [
    path('courses', views.CourseView.as_view(), name='courses'),
    path('courses/add', views.CourseCreateView.as_view(), name='add-course'),
    path('repas', views.RepasView.as_view(), name='repass'),
    path('repas/add', views.RepasCreateView.as_view(), name='add-repas'),
    path('periode', views.PeriodeView.as_view(), name='periodes'),
    path('periode/add', views.PeriodeCreateView.as_view(), name='add-periode'),
    path('', views.UtilisateurView.as_view(), name='utilisateurs'),
]
