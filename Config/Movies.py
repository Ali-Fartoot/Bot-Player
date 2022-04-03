from typing import Dict
import json
class Movies:
    def __init__(self,address : str):
        self.address = address

    def WriteToJSON(self,data: Dict[str, list]):
        for keys,values in data.items():
            keys = self.FileNameCleaning(keys)
            data = {keys: [x for x in values]}
        with open(self.address, 'w', encoding='utf-8') as f:
            json.dump(data, f,separators=(',', ': '), ensure_ascii=False, indent=4)
    def ReadJSON(self,):
        with open(self.address, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            return data

    def FileNameCleaning(self,fileName : str):
        sections = fileName.split('/')
        return sections[-1].split('.')[0]
