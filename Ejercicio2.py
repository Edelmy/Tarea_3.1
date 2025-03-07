#   Codigo que implementa el esquema numerico 
#   del metodo de eliminacion Gaussiana para
#   resolver sistemas de ecuaciones
# Chay Dzul Edelmy

import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        # En este bloque, realizamos el pivoteo parcial.
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        # Aquí comenzamos la eliminación hacia adelante.
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    
    # Sustitución regresiva
    #Inicializamos un vector x con ceros y luego, comenzando desde la última fila, calculamos los valores de las incógnitas. 
    # Utilizamos el producto punto para restar las contribuciones de las incógnitas ya calculadas.
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x #la función devuelve el vector x

# Definición del sistema de ecuaciones
# La matriz A se incluye por renglones
# El vector b se incluye por columnas
A = np.array([[6, -2, 3, -1, 2], [-3, 5, -2, 4, -1], [4, 3, 7, -5, 3], [-2, 6, -3, 1, -4], [1, -3, 2, -5, 6]], dtype=float)
b = np.array([15, -6, 20, -4, 7], dtype=float)

# Resolución del sistema
sol = gauss_elimination(A, b)

# Imprimir la solución
print("Solución del sistema:")
print(sol)