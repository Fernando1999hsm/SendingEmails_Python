from src.DataIntoDictionary import DataIntoDictionary
from src.Email_Config import ConfigEmail
try:
    contactos = DataIntoDictionary().convert_to_dictionary()
    correo = ConfigEmail()

    print("Enviando correos...")
    print(correo.configure_server(contactos))
except Exception as e:
    print(f"Ocurrió un error: {e}")