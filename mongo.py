from pymongo import MongoClient
from data import Data


class Mongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.base = self.client['analisisr']
        self.coleccion = self.base['jugadas']

    def ingresarDatos(self, data:Data):
        documento = {
            "user": {
                "name": data.usuario.name,
                "beats": data.usuario.beats
            },
            "ia": {
                "name": data.ia.name,
                "beats": data.ia.beats
            },
            "result": data.result
        }
        self.coleccion.insert_one(documento)
        print("Exito")
