import smtplib
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
        self.host = SMTP_HOST
        self.port = SMTP_PORT
        self.user = EMAIL_USER
        self.password = EMAIL_PASSWORD


    def configure_server(self, to, asunto, cuerpo):
        servidor = smtplib.SMTP(self.host, self.port)
        servidor.starttls()
        servidor.login(self.user, self.password)
        print("Login realizado com sucesso!")

        mensaje = EmailMessage()
        mensaje['From'] = EMAIL_USER
        mensaje['To'] = to
        mensaje['Subject'] = asunto
        mensaje.set_content(cuerpo)
        servidor.send_message(mensaje)
        return "Correo enviado con éxito!"
    
#correo = ConfigEmail()
#print(correo.configure_server("Asunto de prueba", "Cuerpo del mensaje de prueba"))