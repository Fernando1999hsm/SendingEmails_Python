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


    def configure_server(self, diccionario):
        servidor = smtplib.SMTP(self.host, self.port)
        servidor.starttls()
        servidor.login(self.user, self.password)
        print("Login realizado com sucesso!")
        for contaco in diccionario:
            mensaje = EmailMessage()
            mensaje['From'] = EMAIL_USER
            mensaje['To'] = contaco["Correo electronico"]
            mensaje['Subject'] = "Bienvenido a nuestro servicio"
            mensaje.set_content(f"Hola {contaco['Nombre']} {contaco['Apellidos']},\n\nGracias por registrarte en nuestra plataforma.\n\nSaludos cordiales,\nEl equipo")
            servidor.send_message(mensaje)
        return "Correo enviado con éxito!"
    
#correo = ConfigEmail()
#print(correo.configure_server("Asunto de prueba", "Cuerpo del mensaje de prueba"))