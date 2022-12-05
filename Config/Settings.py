import json
from typing import List

# Create
class Setting:
    def __init__(self,address):
        self.address = address

    def ReadJSON(self, ):
        with open(self.address, 'r', encoding='utf-8') as file:
            return json.load(file)

    def WriteToJSON(self, data: List[str]):

        jsonFile = list(data)
        with open(self.address, "w", encoding='utf-8') as file:
            json.dump(jsonFile, file, indent=4)