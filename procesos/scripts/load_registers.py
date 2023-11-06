from models import Procesos
import pandas as pd

df = pd.read_excel('data/ReporteProcesosAperturaProxima.xlsx')

for _, row in df.iterrows():
    registro = Procesos(
        numero_proceso = ['numero_proceso'],
        nombre_proceso = ['nombre_proceso'],
        tipo_proceso = ['tipo_proceso'],
        fecha_apertura =['fecha_apertura'],
        unidad_ejecutora = ['unidad_ejecutora']
    )
    registro.save()