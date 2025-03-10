import pandas as pd
from datetime import timedelta
from slot import Slot  # Importa la clase Slot

class Aeropuerto:
    def __init__(self, vuelos: pd.DataFrame, slots: int, t_embarque_nat: int, t_embarque_internat: int):
        self.df_vuelos = vuelos
        self.n_slots = slots
        self.slots = {}
        self.tiempo_embarque_nat = t_embarque_nat
        self.tiempo_embarque_internat = t_embarque_internat
        
        # Inicializar los slots
        for i in range(1, self.n_slots + 1):
            self.slots[i] = Slot()  # Crea un objeto Slot por cada ID
        
        # Añadir columnas de fecha de despegue y slot
        self.df_vuelos['fecha_despegue'] = pd.NaT
        self.df_vuelos['slot'] = 0
    
    def calcula_fecha_despegue(self, row) -> pd.Series:
        """
        Calcula la fecha de despegue sumando la fecha de llegada, el tiempo de embarque y el retraso.
        """
        # Convertimos la fecha de llegada a datetime
        try: 
            fecha_llegada = pd.to_datetime(row['fecha_llegada'])
        except ValueError:
            print(f"Valor de fecha_llegada incorrecto: {row['fecha_llegada']}")
            return pd.NaT 
        
        # Obtener el retraso (si existe)
        retraso = pd.to_timedelta(0)
        if row['retraso'] not in [None, '-', '']:
            try:
                retraso = pd.to_timedelta(row['retraso'])  # Convierte el retraso en un timedelta
            except ValueError:
                print(f"Valor de retraso incorrecto: {row['retraso']}")
                retraso = pd.to_timedelta(0)

        # Tiempo de embarque dependiendo si es vuelo nacional o internacional
        if row['tipo_vuelo'] == 'NAT':
            tiempo_embarque = timedelta(minutes=self.tiempo_embarque_nat)
        else:
            tiempo_embarque = timedelta(minutes=self.tiempo_embarque_internat)
        
        # Calculamos la fecha de despegue
        fecha_despegue = fecha_llegada - tiempo_embarque - retraso
        
        return fecha_despegue
    
    def encuentra_slot(self, fecha_vuelo) -> int:
        for id in self.slots:
            estaLibre = self.slots[id].slot_esta_libre_fecha_determinada(fecha_vuelo)
            if estaLibre:
                return id
        return None
       
    def asigna_slot(self, vuelo) -> pd.Series:
        """
        Asigna un slot al vuelo después de calcular su fecha de despegue.
        Si no se encuentra un slot libre, incrementa la fecha de despegue.
        """
        fecha_despegue = self.calcula_fecha_despegue(vuelo)
        # Intentar encontrar un slot libre
        slot_id = self.encuentra_slot(fecha_despegue)
        
        while slot_id is None:
            # Si no hay slot libre, incrementar la fecha de despegue en 10 minutos
            fecha_despegue += timedelta(minutes=10)
            slot_id = self.encuentra_slot(fecha_despegue)
     
        self.slots[slot_id].asigna_vuelo(vuelo['id'], fecha_despegue, vuelo['fecha_llegada'])
        
        # Asignar los valores calculados en el DataFrame
        vuelo['fecha_despegue'] = fecha_despegue
        vuelo['slot'] = slot_id
        
        # Imprimir el resultado
        print(f" El Vuelo {vuelo['id']} con fecha de despegue {fecha_despegue} y fecha de llegada {vuelo['fecha_llegada']}, ha sido asignado al slot {slot_id}")
        return vuelo
    
    def asigna_slots(self):
        """
        Ordena los vuelos por fecha de llegada y asigna un slot a cada uno.
        """
        self.df_vuelos = self.df_vuelos.sort_values(by='fecha_llegada')
        
        for index, vuelo in self.df_vuelos.iterrows():
            self.asigna_slot(vuelo)
    
    @staticmethod
    def preprocess_data(dates_dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Recibe un DataFrame de fechas, lo concatena y asegura que las fechas son correctas.
        """
        # Concatenar los DataFrames y asegurarse de que las fechas están en formato datetime
        fecha = dates_dataframe['fecha_llegada']
        if fecha is not None:
            dates_dataframe['fecha_llegada'] = pd.to_datetime(dates_dataframe['fecha_llegada'])
            
        return dates_dataframe