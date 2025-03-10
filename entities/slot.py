
# Clase Slot:

# Comenzar con la clase Slot puede ser beneficioso, ya que es una parte fundamental de la 
# asignación de vuelos en el aeropuerto. Desarrollar esta clase te permitirá establecer
# cómo representar los slots de tiempo en el aeropuerto y cómo interactuar con ellos. 


# init: Inicializa un slot con un identificador y fechas inicial y final.
# asigna_vuelo: Puede implementarse para asignar un vuelo a este slot.
# slot_esta_libre_fecha_determinada: Verifica si el slot está libre en una fecha específica.
# Función preprocess_data:
# Esta función podría implementarse para realizar cualquier procesamiento previo necesario en los 
# datos antes de utilizarlos, como limpieza de datos, conversión de formatos, etc. (editado)
from datetime import datetime 
import pandas as pd

class Slot:
    def __init__(self):
        self.id = None   # no está inicializado
        self.fecha_despegue = pd.NaT
        self.fecha_aterrizaje = pd.NaT

    def asigna_vuelo(self, id, fecha_despegue, fecha_aterrizaje):  
        self.id = id 
        self.fecha_despegue = pd.to_datetime(fecha_despegue)
        self.fecha_aterrizaje = pd.to_datetime(fecha_aterrizaje)
     
    def slot_esta_libre_fecha_determinada(self, fecha):
        if pd.isna(self.fecha_despegue) or pd.isna(self.fecha_aterrizaje):
            # Si el slot no tiene asignada ninguna fecha, está libre
            return True
        # Convertimos la fecha proporcionada a un objeto datetime si es necesario
        if isinstance(fecha, str):
            fecha = pd.to_datetime(fecha)
        
        # Verificamos si la fecha está fuera del intervalo de [fecha_despegue, fecha_aterrizaje]
        if fecha <= self.fecha_despegue or fecha >= self.fecha_aterrizaje:
            return True  # El slot está libre
        
        return False
        
      
        
            