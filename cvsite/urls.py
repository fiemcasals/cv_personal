from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #es la direccion a mi administrador
    path('mauri/', include('portfolio.urls')),
    path('', include('presentacion.urls')),
]
