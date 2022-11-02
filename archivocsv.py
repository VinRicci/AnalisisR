from csv import DictWriter
from data import Data


class Archivocsv:
    def __init__(self):
        self.documento = 'datos.csv'
        self.fieldnames = ['user_name', 'ia_name', 'result']

    def insert(self, data: Data):
        with open(self.documento, 'a', newline='') as f_object:
            writer = DictWriter(f_object, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerow({'user_name': data.usuario.name, 'ia_name': data.ia.name, 'result': data.result})
            f_object
