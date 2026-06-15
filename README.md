# EnvioCorreosListas — Demo 001

Proyecto demo que automatiza el envío de correos electrónicos personalizados a una lista de contactos desde un archivo CSV.

## Descripción

Lee los contactos desde `FileList/correos.csv`, valida los correos electrónicos con expresiones regulares y envía un mensaje de bienvenida personalizado vía SMTP. Las credenciales del servidor de correo se configuran mediante variables de entorno (`.env`).

## Flujo de ejecución

1. `main.py` orquesta el proceso.
2. `DataIntoDictionary` convierte el CSV en una lista de diccionarios.
3. `ConfigEmail` configura el servidor SMTP, itera sobre los contactos y envía un correo de bienvenida a cada uno.

## Tecnologías

- Python 3
- `smtplib` — envío de correos
- `csv.DictReader` — parseo de CSV
- `email.message.EmailMessage` — construcción del mensaje
- `re` — validación de formato email
- `python-dotenv` — carga de variables de entorno
- Ethereal Email — servidor SMTP de pruebas

## Requisitos

```bash
pip install -r requirements.txt
```

Crear un archivo `.env` en la raíz del proyecto con:

```
SMTP_HOST=smtp.ethereal.email
SMTP_PORT=587
EMAIL_USER=tu_usuario@ethereal.email
EMAIL_PASSWORD=tu_contraseña
```

## Uso

```bash
python main.py
```

## Nota

Demo 001 — Proyecto resultado del aprendizaje en el certificado **"Google IT Automation with Python"**, impartido en Coursera.
