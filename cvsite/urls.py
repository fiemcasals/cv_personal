from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls), #es la direccion a mi administrador
    path('mauri/', include('portfolio.urls')),
    path('', include('presentacion.urls')),
=======
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('juan_cv/', include('juan_cv.urls')),
>>>>>>> juan_cv
]
