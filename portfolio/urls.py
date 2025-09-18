from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experiencia/', views.experience, name='experience'),
    path('habilidades/', views.skills, name='skills'),
    path('formacion/', views.education, name='education'),
    path('contacto/', views.contact, name='contact'),
    path('gracias/', views.thanks, name='thanks'),
    path('gchico/', views.cv_gchico, name='cv_gchico'),
]
