from lector import Lector
import pandas as pd

class LectorCSV(Lector):
    def leer_archivo(self):
        df = pd.read_csv(self.path)
        df.columns = df.columns.str.strip()  
        df['retraso'] = df['retraso'].replace('-', None)
        return df.to_dict(orient= 'records')