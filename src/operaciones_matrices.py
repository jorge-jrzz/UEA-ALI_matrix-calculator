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


def matriz_vacia(matriz) -> list:
    matriz_vacia = list()

    for row in range(len(matriz)):
        matriz_vacia.append(list())
        for ccolumn in matriz[0]:
            matriz_vacia[row].append(0)

    return matriz_vacia


def calcular_inversa(matriz):
    m = sp.Matrix(matriz)
    if m.det() != 0:
        return np.linalg.inv(np.array(matriz))
    else:
        return "** La matriz es singular **"


def sumarMatrices(matriz_a, matriz_b):
    # return np.array(matriz1) + np.array(matriz2)
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        return "Las matrices no tienen las mismas dimensiones"
    else:
        matriz_suma = matriz_vacia(matriz_a)
        for row in range(len(matriz_a)):
            for column in range(len(matriz_a[row])):
                resultado = matriz_a[row][column] + matriz_b[row][column]
                matriz_suma[row][column] = resultado

        return np.array(matriz_suma)


def restarMatrices(matriz_a, matriz_b):
    # return np.array(matriz1) - np.array(matriz2)
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        return "Las matrices no tienen las mismas dimensiones"
    else:
        matriz_resta = matriz_vacia(matriz_a)
        for row in range(len(matriz_a)):
            for column in range(len(matriz_a[row])):
                resultado = matriz_a[row][column] - matriz_b[row][column]
                matriz_resta[row][column] = resultado

        return np.array(matriz_resta)


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
