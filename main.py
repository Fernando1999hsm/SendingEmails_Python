from src.DataIntoDictionary import DataIntoDictionary
from src.Email_Config import ConfigEmail

contactos = DataIntoDictionary().convert_to_dictionary()

correo = ConfigEmail()
for contacto in contactos:
    nombre = contacto["Nombre"]
    apellidos = contacto["Apellidos"]
    email = contacto["Correo electronico"]

    asunto = "Bienvenido a nuestro servicio"
    cuerpo = f"Hola {nombre} {apellidos},\n\nGracias por registrarte en nuestra plataforma.\n\nSaludos cordiales,\nEl equipo"

    resultado = correo.configure_server(email, asunto, cuerpo)
    print(f"{resultado} -> {email}")
