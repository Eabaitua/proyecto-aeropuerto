# Clase Lector y sus subclases (LectorCSV, LectorJSON, LectorTXT):
# Una vez que tengas una idea clara de cómo representar los datos de los vuelos en los slots,
# puedes pasar al desarrollo del módulo de lectura de archivos. Comienza con la clase base Lector,
# definiendo cómo leer archivos genéricos y luego desarrolla las subclases para leer archivos
# específicos en formatos como CSV, JSON y TXT. 

from abc import ABC, abstractmethod
import pandas as pd

class Lector(ABC):
    
    def __init__(self, path: str):
        self.path = path
        
    def comprueba_extension(self, extension: str):
        ext_archivo = self.path.split('.')[1]
        if ext_archivo == extension:
           return True 
        else:
           return False
               
    @abstractmethod
    def leer_archivo(self): 
        pass
    
    @staticmethod
    def convierte_dict_a_csv(data: dict, nombre_archivo: str = 'Lector.csv'):
        df = pd.DataFrame(data)
        df.to_csv('Lector.csv')
        
