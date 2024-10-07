import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ejercicio_2.csv')

columnas_seleccionadas = df[['velocidad', 'frecuencia_cardiaca', 'distancia_al_balon']]

plt.figure(figsize=(10, 6))
correlation_matrix = columnas_seleccionadas.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Mapa de Calor de Correlaciones entre Variables Seleccionadas')
plt.show()
