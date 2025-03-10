from claseAeropuerto import Aeropuerto
from lectorCSV import LectorCSV
from lectorJson import LectorJSON as LectorJson
from lectorTXT import LectorTxt
import pandas as pd

if __name__ == "__main__":
    # Leer los archivos usando los lectores
    lector_csv = LectorCSV("data_proyecto/vuelos_2.csv")
    lector_txt = LectorTxt("data_proyecto/vuelos_1.txt")
    lector_json = LectorJson("data_proyecto/vuelos_3.json")

    # Convertir los datos de cada archivo en DataFrames
    vuelos_csv = lector_csv.leer_archivo()
    vuelos_txt = lector_txt.leer_archivo()
    vuelos_json = lector_json.leer_archivo()
    
    # Unir todos los DataFrames en uno solo
    vuelos_completos = vuelos_csv+vuelos_json+vuelos_txt

    # Procesar los datos (asegurar que las fechas sean correctas)
    vuelos_completos = Aeropuerto.preprocess_data(pd.DataFrame(vuelos_completos))

    # Crear un objeto de Aeropuerto
    aeropuerto = Aeropuerto(vuelos_completos, slots=5, t_embarque_nat=20, t_embarque_internat=30)

    # Asignar slots a cada vuelo
    aeropuerto.asigna_slots()