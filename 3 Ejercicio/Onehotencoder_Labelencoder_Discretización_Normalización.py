import pandas as pd
import arff
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import KBinsDiscretizer, MinMaxScaler

# **1. Cargar el dataset desde un archivo ARFF**
with open('ejercicio_3.arff', 'r') as f:
    dataset = arff.load(f)

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(dataset['data'], columns=[attr[0] for attr in dataset['attributes']])

# **2. One-Hot Encoding**
# Aplicar One-Hot Encoding a 'formacion' y 'zona_controlada'
one_hot_encoder = OneHotEncoder(sparse_output=False)
encoded_features = one_hot_encoder.fit_transform(df[['formacion', 'zona_controlada']])

# Obtener los nombres de las columnas después de la codificación
feature_names = one_hot_encoder.get_feature_names_out(['formacion', 'zona_controlada'])

# Convertir los resultados a DataFrame y añadirlos al original
encoded_df = pd.DataFrame(encoded_features, columns=feature_names)
df = pd.concat([df, encoded_df], axis=1)
df.drop(['formacion', 'zona_controlada'], axis=1, inplace=True)  # Eliminar las columnas originales

# **3. Label Encoding**
# Supongamos que tienes una columna categórica llamada 'equipo'
label_encoder = LabelEncoder()
df['equipo_encoded'] = label_encoder.fit_transform(df['equipo'])

# **4. Discretización**
# Discretizar la columna 'velocidad' en 3 intervalos (bins)
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
df['velocidad_discretizada'] = discretizer.fit_transform(df[['velocidad']])

# **5. Normalización**
# Normalizar la columna 'frecuencia_cardiaca'
scaler = MinMaxScaler()
df['frecuencia_cardiaca_normalizada'] = scaler.fit_transform(df[['frecuencia_cardiaca']])

# Guardar el DataFrame en un archivo Excel
excel_file_path = 'ejercicio_3_preprocesado.xlsx'
df.to_excel(excel_file_path, index=False)

excel_file_path
