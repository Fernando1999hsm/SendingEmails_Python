import smtplib
import re
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

class ConfigEmail:
    def __init__(self):
        try:
            self.host = SMTP_HOST
            self.port = SMTP_PORT
            self.user = EMAIL_USER
            self.password = EMAIL_PASSWORD
        except ValueError as e:
            print(f"Ocurrió un error al cargar las variables de entorno: {e}")
            raise


    def configure_server(self, diccionario):
        try:
            servidor = smtplib.SMTP(self.host, self.port)
            servidor.starttls()
            servidor.login(self.user, self.password)
            print("Login realizado com sucesso!")
            patron_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            for contaco in diccionario:
                email = contaco.get("Correo electronico", "")
                if not patron_email.match(email):
                    print(f"Correo electrónico inválido, saltando: {email}")
                    continue
                mensaje = EmailMessage()
                mensaje['From'] = EMAIL_USER
                mensaje['To'] = email
                mensaje['Subject'] = "Bienvenido a nuestro servicio"
                mensaje.set_content(f"Hola {contaco['Nombre']} {contaco['Apellidos']},\n\nGracias por registrarte en nuestra plataforma.\n\nSaludos cordiales,\nEl equipo")
                servidor.send_message(mensaje)
            servidor.quit()
            return "Correo enviado con éxito!"
        except smtplib.SMTPConnectError as e:
            print(f"Ocurrió un error al conectar con el servidor de correo: {e}")
            raise
        except smtplib.SMTPAuthenticationError as e:
            print(f"Ocurrió un error de autenticación: {e}")
            raise
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Ocurrió un error, los destinatarios rechazaron el correo: {e}")
            raise
        except smtplib.SMTPSenderRefused as e:
            print(f"Ocurrió un error, el remitente fue rechazado: {e}")
            raise
#correo = ConfigEmail()
#print(correo.configure_server("Asunto de prueba", "Cuerpo del mensaje de prueba"))