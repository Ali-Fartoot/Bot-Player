from typing import Dict
import json
class Movies:
    def __init__(self,address : str):
        self.address = address


    def ReadJSON(self,):
        with open(self.address, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def WriteToJSON(self,data: Dict[int, list]):

        with open(self.address, "r",encoding='utf-8') as file:
            jsonFile = self.ReadJSON()
            for keys, values in data.items():
                for obj in jsonFile:
                    if keys in obj:
                        return
                output = {self.FileNameCleaning(keys): [x for x in values]}
            jsonFile.append(output)

        with open(self.address, "w",encoding='utf-8') as file:
            json.dump(jsonFile, file, indent=4)



    def FileNameCleaning(self,fileName : str):
        sections = fileName.split('/')
        return sections[-1].split('.')[0]
    
    def ReturnIndex(self,key):
        index = 0
        data = self.ReadJSON()
        for obj in data:
            if key in obj:
                return index
            else:
                index = index + 1

    def DeleteMovie(self,key):
        data = self.ReadJSON()
        output=[]
        for obj in data:
            if key not in obj:
                output.append(obj)

        with open(self.address, 'w',encoding='utf-8') as file:
            json.dump(output, file)


    def ReturnLength(self,):
        data = self.ReadJSON()
        return len(data)


movies = Movies("Movies.json")
fileName = movies.FileNameCleaning("Rec 2022-02-26 0010")
movies.WriteToJSON(dict({fileName: ["Rec 2022-02-26 0007", fileName+'temp']}))
