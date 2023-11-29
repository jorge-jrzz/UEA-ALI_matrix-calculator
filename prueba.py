import numpy as np
import sympy as sp
from fractions import Fraction


def imprimir_matriz(mensaje1, matriz) -> None:
    """
    Imprime una matriz con un mensaje dado.

    Args:
        mensaje1 (str): El mensaje a imprimir antes de la matriz.
        matriz (list): La matriz a imprimir.
    """

    mensaje = mensaje1 + "\n"+"\t"
    for row in matriz:
        for element in row:
            frac = Fraction(str(element)).limit_denominator()
            mensaje += str(frac) + "\t"
        mensaje += "\n"+"\t"
    print(mensaje)


def calcular_inversa(matriz):
    m = sp.Matrix(matriz)
    if m.det() != 0:
        return np.linalg.inv(np.array(matriz))
    else:
        return "** La matriz es singular **"


# Inicializar las matrices
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 2, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

filas = len(matriz1)
columnas = len(matriz1[0])

# Crea la matriz
suma = np.empty([filas, columnas])
multi = np.empty([filas, columnas])
multi_es = np.empty([filas, columnas])

suma = np.array(matriz1) + np.array(matriz2)
resta = np.array(matriz1) - np.array(matriz2)
multi_es = np.dot(matriz1, 2)   # Multiplicacion por un escalar
multi = np.dot(matriz1, matriz2)
inversa = calcular_inversa(matriz1)

# Imprimir los resultados
print("Resultados")
imprimir_matriz("Matriz 1:", matriz1)
imprimir_matriz("Matriz 2:", matriz2)
imprimir_matriz("Suma 1- 2:", suma)
imprimir_matriz("Resta 1 - 2: ", resta)
imprimir_matriz("Multiplicación por un escalar matriz 1 x (2):", multi_es)
imprimir_matriz("Multiplicación 1 x 2:", multi)

try:
    imprimir_matriz("Inversa de la Matriz 1:", inversa)
except Exception as e:
    print(inversa)
