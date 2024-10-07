import pandas as pd
import arff

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('ejercicio_3.csv')

# Convertir el DataFrame a un formato que la biblioteca arff pueda entender
data = df.to_numpy().tolist()
attributes = [(col, 'REAL' if df[col].dtype in ['float64', 'int64'] else 'STRING') for col in df.columns]

# Crear el objeto ARFF
arff_data = {
    'description': 'Dataset de Análisis Táctico en Fútbol',
    'relation': 'futbol_tactico',
    'attributes': attributes,
    'data': data
}

# Guardar el dataset en formato ARFF
with open('ejercicio_3.arff', 'w') as f:
    arff.dump(arff_data, f)

print("Archivo ARFF creado exitosamente.")
