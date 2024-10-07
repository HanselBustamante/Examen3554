import pandas as pd
import numpy as np

# Crear un dataset
data = {
    'Altura (cm)': [150, 160, 170, 180, 190, 155, 165, 175, 185, 195],
    'Peso (kg)': [50, 60, 70, 80, 90, 55, 65, 75, 85, 95],
    'Talla (cm)': [40, 42, 44, 46, 48, 41, 43, 45, 47, 49],
    'Clase': ['Bajo', 'Bajo', 'Medio', 'Medio', 'Alto', 
              'Bajo', 'Medio', 'Medio', 'Alto', 'Alto']
}

df = pd.DataFrame(data)

def calcular_entropia(df, columna_clase):
    valores, conteos = np.unique(df[columna_clase], return_counts=True)
    probabilidades = conteos / len(df)
    entropia = -np.sum(probabilidades * np.log2(probabilidades))
    return entropia

def calcular_ganancia_informacion(df, columna_clase, columna_atributo):
    entropia_original = calcular_entropia(df, columna_clase)
    valores_unicos = df[columna_atributo].unique()
    
    entropia_ponderada = 0
    for valor in valores_unicos:
        subset = df[df[columna_atributo] == valor]
        probabilidad = len(subset) / len(df)
        entropia_subset = calcular_entropia(subset, columna_clase)
        entropia_ponderada += probabilidad * entropia_subset

    ganancia_informacion = entropia_original - entropia_ponderada
    return ganancia_informacion

# Calcular entropía
entropia_clase = calcular_entropia(df, 'Clase')
print(f'Entropía de la clase: {entropia_clase}')

# Calcular ganancia de información usando 'Altura (cm)'
ganancia_info_altura = calcular_ganancia_informacion(df, 'Clase', 'Altura (cm)')
print(f'Ganancia de información al dividir por altura: {ganancia_info_altura}')
