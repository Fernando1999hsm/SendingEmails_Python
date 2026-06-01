from pathlib import Path

class ExtractData_File:
    def __init__(self, file_path):
        self.file_path = Path(__file__).parent / file_path

    def extract_data(self):
        try:
            data = []
            with open(self.file_path) as file:
                for line in file:
                    data.append(line.strip())
            return data
        except FileNotFoundError as e:
            print(f"Ocurrió un error al intentar abrir el archivo: {e}")
            raise
        except PermissionError as e:
            print(f"Ocurrió un error de permisos al intentar abrir el archivo: {e}")
            raise
        except UnicodeDecodeError as e:
            print(f"Ocurrió un error de decodificación al leer el archivo: {e}")
            raise
    
#extr=ExtractData_File("../FileList/correos.csv")
#print(extr.extract_data())