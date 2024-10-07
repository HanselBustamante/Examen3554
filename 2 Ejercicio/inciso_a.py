import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('ejercicio_2.csv')

# Función para calcular percentiles y cuartiles
def calcular_percentiles_y_cuartiles(data):
    percentiles = {
        '25% (Cuartil 1)': np.percentile(data, 25),
        '50% (Mediana)': np.percentile(data, 50),
        '75% (Cuartil 3)': np.percentile(data, 75),
        '100% (Máximo)': np.max(data),
        '0% (Mínimo)': np.min(data)
    }
    return percentiles

# Calcular percentiles y cuartiles para cada columna
resultados = {}
for column in df.columns:
    if df[column].dtype in [np.int64, np.float64]:  # Solo columnas numéricas
        resultados[column] = calcular_percentiles_y_cuartiles(df[column])

# Imprimir resultados de manera más clara
print("Resultados de Percentiles y Cuartiles:")
for col, percentiles in resultados.items():
    print(f'\nColumna: {col}')
    for key, value in percentiles.items():
        print(f'  {key}: {value:.2f}')

# Graficar la distribución de la velocidad como ejemplo
plt.figure(figsize=(10, 6))
plt.hist(df['velocidad'], bins=30, color='blue', alpha=0.7)
plt.title('Distribución de la Velocidad de los Jugadores')
plt.xlabel('Velocidad (m/s)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
plt.axvline(np.mean(df['velocidad']), color='red', linestyle='dashed', linewidth=1)
plt.text(np.mean(df['velocidad']), 50, f'Media: {np.mean(df["velocidad"]):.2f}', color='red')
plt.show()
