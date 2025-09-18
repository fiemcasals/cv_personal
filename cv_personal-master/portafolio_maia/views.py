# portafolio_maia/views.py

from django.shortcuts import render

def portafolio_view(request):
    return render(request, 'portafolio_maia/index.html')