import random
import pandas as pd
from deap import base, creator
from prettytable import PrettyTable

# Definir la función f(x) = x^(2x) - 1
def f(x):
    return x ** (2 * x) - 1

# Crear tipos de problema (maximización)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Función principal para ejecutar el algoritmo genético
def algoritmo_genetico(poblacion_original, num_generaciones):
    data = {
        'Población Original': [],
        'x1': [],
        'f(x)=x^(2x)-1': [],
        'Fenotipo': [],
        'Izquierda': [],
        'Derecha': [],
        'Combinación': [],
        'Mutación': [],
        'Población Final': []
    }
    
    # Crear la población inicial
    poblacion = [creator.Individual([x]) for x in poblacion_original]
    
    for gen in range(num_generaciones):  # Generar el número de generaciones
        print(f"\nGeneración {gen + 1}:")
        
        # Recolectar datos para cada individuo en la población
        for ind in poblacion:
            x1 = ind[0]
            data['Población Original'].append(x1)
            data['x1'].append(x1)
            data['f(x)=x^(2x)-1'].append(f(x1))
            
            # Convertir a binario
            fenotipo = format(x1, '08b')
            data['Fenotipo'].append(fenotipo)
            
            # Dividir el fenotipo
            izquierda = fenotipo[:4]
            derecha = fenotipo[4:]
            data['Izquierda'].append(izquierda)
            data['Derecha'].append(derecha)
            
            # Combinación
            combinacion = izquierda + derecha
            data['Combinación'].append(combinacion)
            
            # Mutación
            mutacion = combinacion[:-2] + {
                '00': '10',
                '01': '11',
                '10': '00',
                '11': '01'
            }[combinacion[-2:]]  # Aplicar mutación
            
            data['Mutación'].append(mutacion)
            data['Población Final'].append(int(mutacion, 2))

        # Crear un DataFrame y ordenarlo
        df_resultados = pd.DataFrame(data)
        df_resultados = df_resultados.sort_values(by='x1', ascending=False)

        # Crear una tabla bonita
        tabla = PrettyTable()
        tabla.field_names = df_resultados.columns.tolist()

        for index, row in df_resultados.iterrows():
            tabla.add_row(row)

        # Imprimir la tabla
        print(tabla)

        # Preparar la población para la siguiente generación
        poblacion_original = df_resultados['Población Final'].tolist()
        poblacion = [creator.Individual([x]) for x in poblacion_original]

        # Limpiar datos para la próxima generación
        data = {key: [] for key in data.keys()}

# Definir la población original
poblacion_original = [10, 13, 3, 4, 8, 1, 12, 5, 7, 6, 9, 11]

# Pedir al usuario el número de generaciones
try:
    num_generaciones = int(input("Ingrese el número de generaciones: "))
    # Ejecutar el algoritmo genético
    algoritmo_genetico(poblacion_original, num_generaciones)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
