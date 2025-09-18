# portafolio_maia/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.portafolio_view, name='portafolio_maia'),
]