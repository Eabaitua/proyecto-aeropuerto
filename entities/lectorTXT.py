from lector import Lector

class LectorTxt(Lector):
    def leer_archivo(self):
        with open(self.path, 'r') as archivo:
            datos = archivo.readlines()
        datos_limpios = [linea.strip() for linea in datos]
        vuelos = []
        for vuelo in datos_limpios[1:]:
             info = [campo.strip() for campo in vuelo.split(',')]
             avion = {
                'id': info[0].strip(),  
                'fecha_llegada': info[1].strip().replace('T', ' '), 
                'retraso': info[2].strip() if info[2].strip() != '-' else None,  
                'tipo_vuelo': info[3].strip(),  
                'destino': info[4].strip()  
            }
             vuelos.append(avion)
        return vuelos