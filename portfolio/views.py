import os, requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

# Datos base de tu CV (puedes moverlos a la DB más adelante)
CV = {
    "nombre": "Mauricio Casals",
    "email": "mauriciocasals90@gmail.com",
    "telefono": "3413524783",
    "ubicacion": "Palermo, Bs As",
    "perfil": "Estudiante avanzado de Ingeniería Informática, con experiencia en liderazgo y desarrollo de software.",
    "links": {
        "github": "https://github.com/",
        "linkedin": "https://www.linkedin.com/",
    },
    "skills": [
        "HTML/CSS", "Animaciones y transformaciones", "Git/GitHub", "JavaScript", "Bases de datos",
        "Java", "Python", "C/C++", "POO", "Docker", "UML (clases, secuencias, casos de uso)",
        "Django", "Redes"
    ],
    "idiomas": ["Inglés (intermedio)"],
    "experiencia": [
        {
            "rol": "Líder de entrenamiento",
            "org": "Ejército Argentino",
            "desc": "Coordinación de capacitaciones y programas de formación. Evaluación del desempeño."
        },
        {
            "rol": "Líder de sector",
            "org": "Ejército Argentino",
            "desc": "Gestión y supervisión de equipo, asignación de tareas y seguimiento de resultados."
        },
        {
            "rol": "Desarrollador Full Stack Java - Habilidades blandas",
            "org": "Codo a Codo",
            "fecha": "02/2024 - 07/2024",
            "desc": "Programa de formación intensiva."
        },
    ],
    "formacion": [
        {"titulo": "Ingeniería Informática", "inst": "Facultad de Ingeniería del Ejército", "estado": "En curso (5º año)"},
        {"titulo": "Lic. en Conducción y Gestión Operativa", "inst": "Colegio Militar de la Nación", "fecha": "2009-2012"},
    ]
}

def home(request):
    return render(request, 'home.html', {"cv": CV})

def experience(request):
    return render(request, 'experience.html', {"cv": CV})

def skills(request):
    return render(request, 'skills.html', {"cv": CV})

def education(request):
    return render(request, 'education.html', {"cv": CV})

def thanks(request):
    return render(request, 'thanks.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # ---- Enviar Email ----
            subject = f"Nuevo contacto desde tu CV: {nombre}"
            body = f"Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"
            try:
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [CV['email']])
                email_ok = True
            except Exception as e:
                email_ok = False
                messages.error(request, f"No se pudo enviar el email: {e}")

            # ---- Enviar Telegram ----
            tele_ok = False
            token = getattr(settings, "TELEGRAM_BOT_TOKEN", "")
            chat_id = getattr(settings, "TELEGRAM_CHAT_ID", "")
            if token and chat_id:
                try:
                    url = f"https://api.telegram.org/bot{token}/sendMessage"
                    payload = {"chat_id": chat_id, "text": f"📬 Nuevo mensaje CV\nNombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}"}
                    r = requests.post(url, json=payload, timeout=10)
                    r.raise_for_status()
                    tele_ok = True
                except Exception as e:
                    messages.error(request, f"No se pudo enviar a Telegram: {e}")
            else:
                messages.info(request, "Telegram no configurado. Define TELEGRAM_BOT_TOKEN y TELEGRAM_CHAT_ID.")

            if email_ok or tele_ok:
                messages.success(request, "¡Mensaje enviado! Te responderé a la brevedad.")
                return redirect('thanks')
        else:
            messages.error(request, "Revisa el formulario.")

    else:
        form = ContactForm()
    return render(request, 'contact.html', {"form": form})

# Vista para el CV de gchico
def cv_gchico(request):
    return render(request, 'cv_gchico.html', {"cv": CV})
