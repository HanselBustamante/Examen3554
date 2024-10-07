import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import KBinsDiscretizer, MinMaxScaler

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('ejercicio_4.csv')

# **1. One-Hot Encoding**
# Aplicar One-Hot Encoding a 'formacion' y 'zona_controlada'
one_hot_encoder = OneHotEncoder(sparse_output=False)  # Cambié 'sparse' a 'sparse_output'

# Transformar 'formacion'
formacion_encoded = one_hot_encoder.fit_transform(df[['formacion']])
formacion_encoded_df = pd.DataFrame(formacion_encoded, columns=one_hot_encoder.get_feature_names_out(['formacion']))

# Transformar 'zona_controlada' usando la misma instancia de OneHotEncoder
zona_encoded = one_hot_encoder.fit_transform(df[['zona_controlada']])
zona_encoded_df = pd.DataFrame(zona_encoded, columns=one_hot_encoder.get_feature_names_out(['zona_controlada']))

# Concatenar los DataFrames y eliminar las columnas originales
df = pd.concat([df, formacion_encoded_df, zona_encoded_df], axis=1)
df.drop(['formacion', 'zona_controlada'], axis=1, inplace=True)

# **2. Label Encoding**
# Aplicar Label Encoding a la columna 'equipo'
label_encoder = LabelEncoder()
df['equipo_encoded'] = label_encoder.fit_transform(df['equipo'])

# **3. Discretización**
# Discretizar la columna 'velocidad' en 3 intervalos (bins)
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
df['velocidad_discretizada'] = discretizer.fit_transform(df[['velocidad']])

# **4. Normalización**
# Normalizar la columna 'frecuencia_cardiaca'
scaler = MinMaxScaler()
df['frecuencia_cardiaca_normalizada'] = scaler.fit_transform(df[['frecuencia_cardiaca']])

# Imprimir el dataframe final para verificar cambios
print(df.head())

# Guardar el nuevo DataFrame en un archivo Excel
excel_file_path = 'ejercicio_4_preprocesado.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Archivo Excel guardado como {excel_file_path}")
