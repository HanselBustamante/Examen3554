import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('ejercicio_2.csv')

# Seleccionar las columnas de interés
columnas_seleccionadas = df[['velocidad', 'frecuencia_cardiaca', 'distancia_al_balon']]

# Calcular la media, mediana y moda
resultados = {}
for column in columnas_seleccionadas.columns:
    media = columnas_seleccionadas[column].mean()
    mediana = columnas_seleccionadas[column].median()
    moda = columnas_seleccionadas[column].mode()[0]  # Tomamos el primer valor de la moda
    
    resultados[column] = {
        'Media': media,
        'Mediana': mediana,
        'Moda': moda
    }

# Imprimir resultados
print("Resultados de Media, Mediana y Moda:")
for col, stats in resultados.items():
    print(f'\nColumna: {col}')
    for stat, value in stats.items():
        print(f'  {stat}: {value:.2f}')

# Graficar el diagrama de cajas-bigote
plt.figure(figsize=(12, 6))
sns.boxplot(data=columnas_seleccionadas)
plt.title('Diagrama de Cajas-Bigote de Velocidad, Frecuencia Cardíaca y Distancia al Balón')
plt.ylabel('Valores')
plt.xticks(ticks=range(len(columnas_seleccionadas.columns)), labels=columnas_seleccionadas.columns)
plt.grid(axis='y', alpha=0.75)
plt.show()
