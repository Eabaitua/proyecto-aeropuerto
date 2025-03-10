from lector import Lector
import json

class LectorJSON(Lector):
    def leer_archivo(self):
        with open(self.path, 'r') as archivo:
            datos = json.load(archivo)
        for avion in datos:
            if avion['retraso'] == '-':
                avion['retraso'] = None
        return datos