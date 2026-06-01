import csv
from pathlib import Path

class DataIntoDictionary:
    def __init__(self):
        self.file_path = Path(__file__).parent / "../FileList/correos.csv"

    def convert_to_dictionary(self):
        try:
            with open(self.file_path, newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError as e:
            print(f"Ocurrió un error al intentar abrir el archivo: {e}")
            raise
        except PermissionError as e:
            print(f"Ocurrió un error de permisos al intentar abrir el archivo: {e}")
            raise
#data = DataIntoDictionary()
#print(data.convert_to_dictionary())