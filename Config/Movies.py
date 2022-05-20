from typing import Dict
import json
import os
import random


class Movies:
    def __init__(self, address: str):
        self.address = address
        self.currentMovie = None

    def ReadJSON(self, ):
        with open(self.address, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def WriteToJSON(self, data: Dict[int, list]):

        with open(self.address, "r", encoding='utf-8') as file:
            jsonFile = self.ReadJSON()
            for keys, values in data.items():
                for obj in jsonFile:
                    if keys in obj:
                        return
                output = {self.FileNameCleaning(keys): [x for x in values]}
            jsonFile.append(output)

        with open(self.address, "w", encoding='utf-8') as file:
            json.dump(jsonFile, file, indent=4)

    def FileNameCleaning(self, fileName: str):
        sections = fileName.split('/')
        return sections[-1].split('.')[0]

    def ReturnIndex(self, key):
        index = 0
        data = self.ReadJSON()
        for obj in data:
            if key in obj:
                return index
            else:
                index = index + 1

    def DeleteMovie(self, key):
        data = self.ReadJSON()
        output = []
        for obj in data:
            if key not in obj:
                output.append(obj)

        with open(self.address, 'w', encoding='utf-8') as file:
            json.dump(output, file)

    def ReturnLength(self, ):
        data = self.ReadJSON()
        return len(data)

    def SetCurrentMovie(self, address, movie):
        with open(address, "w", encoding='utf-8') as file:
            json.dump([movie], file, indent=4)

    def GetCurrentMovie(self, address):
        with open(address, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def SelectRandom(self):
        rand = random.randint(0, len(self.ReadJSON()) - 1)
        for index, value in enumerate(self.ReadJSON()[rand]):
            return value

    def DeleteData(self, address):
        with open(address, "w", encoding='utf-8') as file:
            json.dump([], file, indent=4)

        with open(self.address, "w", encoding='utf-8') as file:
            json.dump([], file, indent=4)


