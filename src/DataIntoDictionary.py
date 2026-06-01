from src.ExtractData_File import ExtractData_File

class DataIntoDictionary:
    def __init__(self):
        self.file_path = "../FileList/correos.csv"

    def convert_to_dictionary(self):
        try:
            Directory = ExtractData_File(self.file_path).extract_data()
            ListaCompleta = []
            keys = Directory[0].split(",")
            for line in Directory[1:]:
                values = line.split(",")
                dictionary = {}
                for key, value in zip(keys, values):
                    dictionary[key] = value
                ListaCompleta.append(dictionary)
            return ListaCompleta
        except IndexError as e:
            print(f"Ocurrió un error al procesar los datos: {e}")
            raise
        except ValueError as e:
            print(f"Ocurrió un error de formato en los datos: {e}")
            raise
#data = DataIntoDictionary()
#print(data.convert_to_dictionary())