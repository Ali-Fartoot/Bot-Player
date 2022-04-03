from typing import Dict
import json
class Movies:
    def __init__(self,address : str):
        self.address = address

    def WriteToJSON(self,data: Dict[int, list]):

        with open(self.address, "r",encoding='utf-8') as file:
            jsonFile = json.load(file)
            for keys, values in data.items():
                output = {self.FileNameCleaning(keys): [x for x in values]}
            jsonFile.append(output)
            print(jsonFile)

        with open(self.address, "w",encoding='utf-8') as file:
            json.dump(jsonFile, file, indent=4)




    def ReadJSON(self,):
        with open(self.address, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def FileNameCleaning(self,fileName : str):
        sections = fileName.split('/')
        return sections[-1].split('.')[0]


