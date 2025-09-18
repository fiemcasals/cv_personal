# CV Django (portfolio + contacto email/Telegram)

## Requisitos
- Python 3.10+
- pip, venv

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Abre http://127.0.0.1:8000/

## Email (desarrollo)
Por defecto se usa `EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend`, verás el email en la consola.
Para producción, define variables de entorno o un `.env` (no incluido) con:
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.tu-proveedor.com
EMAIL_PORT=587
EMAIL_HOST_USER=tuusuario
EMAIL_HOST_PASSWORD=tuclave
EMAIL_USE_TLS=1
DEFAULT_FROM_EMAIL=tu-remitente@dominio.com
```

## Telegram
Crea un bot con @BotFather y define:
```
TELEGRAM_BOT_TOKEN=123456:ABC...
TELEGRAM_CHAT_ID=TU_CHAT_ID
```

## Páginas
- `/` Inicio (perfil + contacto rápido)
- `/experiencia/`
- `/habilidades/`
- `/formacion/`
- `/contacto/` (formulario)
