import json

class JsonExample:

    def __init__(self) -> None:
        pass

    def createJson(self, nombre, apellido, edad):
        data = {}
        data['nombre'] = nombre
        data['apellido'] = apellido
        data['edad'] = edad
        with open('data.json', 'w') as file:
            json.dump(data, file)
        return data
    
    def readJson(self):
        with open('data.json') as file:
            data = json.load(file)
            print(data)
            return data

e = JsonExample()
e.createJson("Juan", "Perez", 30)
e.readJson()
