from pathlib import Path

class ExtractData_File:
    def __init__(self, file_path):
        self.file_path = Path(__file__).parent / file_path

    def extract_data(self):
        data = []
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        return data
    
#extr=ExtractData_File("../FileList/correos.csv")
#print(extr.extract_data())