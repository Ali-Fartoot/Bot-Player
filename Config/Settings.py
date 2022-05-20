import json
from typing import List

# Create
class Setting:
    def __init__(self,address):
        self.address = address

    def ReadJSON(self, ):
        with open(self.address, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def WriteToJSON(self, data: List[str]):

        jsonFile = []
        for values in data:
            jsonFile.append(values)

        with open(self.address, "w", encoding='utf-8') as file:
            json.dump(jsonFile, file, indent=4)