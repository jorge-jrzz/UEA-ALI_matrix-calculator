import numpy as np
import sympy as sp
from fractions import Fraction

# def imprimir_matriz(mensaje1, matriz) -> None:
#     mensaje = mensaje1 + "\n"+"\t"
#     for row in matriz:
#         for element in row:
#             frac = Fraction(str(element)).limit_denominator()
#             mensaje += str(frac) + "\t"
#         mensaje += "\n"+"\t"
#     print(mensaje)

def calcular_inversa(matriz):
    m = sp.Matrix(matriz)
    if m.det() != 0:
        return np.linalg.inv(np.array(matriz))
    else:
        return "** La matriz es singular **"

def sumarMatrices(matriz1, matriz2):
    return np.array(matriz1) + np.array(matriz2)

def restarMatrices(matriz1, matriz2):
    return np.array(matriz1) - np.array(matriz2)

def multiplicarEscalar(matriz, escalar):
    return np.dot(matriz, escalar)

def multiplicarMatrices(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

# Imprimir los resultados
# print("Resultados")
# imprimir_matriz("Matriz 1:", matriz1)
# imprimir_matriz("Matriz 2:", matriz2)
# imprimir_matriz("Suma 1 + 2:", suma)
# imprimir_matriz("Resta 1 - 2: ", resta)
# imprimir_matriz("Multiplicación por un escalar matriz 1 x (2):", multi_es)
# imprimir_matriz("Multiplicación 1 x 2:", multi)

# try:
#     imprimir_matriz("Inversa de la Matriz 1:", inversa)
# except Exception as e:
#     print(inversa)

