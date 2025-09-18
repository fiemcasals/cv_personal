from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_gchico, name='cv_gchico'),
]
