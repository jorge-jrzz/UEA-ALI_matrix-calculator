from fractions import Fraction
import numpy as np

matriz_a = [[2, 1, 1], [2, 1, 1], [2, 1, 1]]

print(type(np.array(matriz_a)))


def matriz_vacia(matriz) -> list:
    matriz_vacia = list()

    for row in range(len(matriz)):
        matriz_vacia.append(list())
        for ccolumn in matriz[0]:
            matriz_vacia[row].append(0)

    return matriz_vacia


def suma(matriz_a, matriz_b) -> list:
    matriz_suma = matriz_vacia(matriz_a)
    for row in range(len(matriz_a)):
        for column in range(len(matriz_a[row])):
            resultado = matriz_a[row][column] + matriz_b[row][column]
            matriz_suma[row][column] = resultado

    return matriz_suma


suma(matriz_a, matriz_a)


def imprimir_matriz(mensaje1, matriz) -> None:
    mensaje = mensaje1 + "\n"+"\t"
    for row in matriz:
        for element in row:
            frac = Fraction(str(element)).limit_denominator()
            mensaje += str(frac) + "\t"
        mensaje += "\n"+"\t"
    print(mensaje)


# matriz_vacia(matriz_a)
