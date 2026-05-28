from ExtractData_File import ExtractData_File

class DataIntoDictionary:
    def __init__(self):
        self.file_path = "../FileList/correos.csv"

    def convert_to_dictionary(self):
        Directory = ExtractData_File(self.file_path).extract_data()
        ListaCompleta = []
        dictionary = {}
        keys = Directory[0].split(",")
        for line in Directory[1:]:
            values = line.split(",")
            for key, value in zip(keys, values):
                dictionary[key] = value
            ListaCompleta.append(dictionary)
        return ListaCompleta

data = DataIntoDictionary()
print(data.convert_to_dictionary())