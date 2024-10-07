import numpy as np

# Generar un conjunto de datos simulado
np.random.seed(42)
X = np.random.rand(100, 5)  # 100 muestras, 5 características
y = np.random.rand(100)      # 100 valores objetivo

# Normalización (Min-Max Scaling)
X_normalized = (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))

# Función para calcular la penalización L1
def l1_penalty(w, lambda_):
    return lambda_ * np.sum(np.abs(w))

# Función para calcular la penalización L2
def l2_penalty(w, lambda_):
    return lambda_ * np.sum(w ** 2)

# Inicializar pesos aleatorios
w = np.random.rand(X_normalized.shape[1])

# Definir un valor de lambda
lambda_value = 0.1

# Calcular las penalizaciones
l1_cost = l1_penalty(w, lambda_value)
l2_cost = l2_penalty(w, lambda_value)

# Imprimir resultados
print(f"Pesos iniciales: {w}")
print(f"Penalización L1: {l1_cost}")
print(f"Penalización L2: {l2_cost}")
