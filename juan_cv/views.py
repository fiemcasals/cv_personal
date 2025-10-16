from django.shortcuts import render

def cv_view(request):
    contexto = {
        'nombre': 'Juan Perez',
    }

    return render(request, 'juan_cv/juan_cv.html', contexto)
