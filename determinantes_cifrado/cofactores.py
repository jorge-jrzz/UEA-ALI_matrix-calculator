#Determinantes (método de cofactores(laplace))
# + - +
# - + -   ---> Ejemplo de una matriz 3*3
# + - +
import numpy as np

respuesta_final = ""

def cofactor(matriz, fila, columna):
    global respuesta_final
    submatriz = np.delete(np.delete(matriz, fila, axis=0), columna, axis=1)
    print(f"\nCalculando el cofactor para el elemento de la fila {fila + 1}, columna {columna + 1}:\n{submatriz}")
    respuesta_final += f"\nCalculando el cofactor para el elemento de la fila {fila + 1}, comna {columna + 1}:\n{submatriz}"

    # Obtener los elementos de la submatriz para la explicación
    elementos_submatriz = submatriz.flatten()

    # Mostrar la operación específica para calcular el cofactor
    operacion = f"{elementos_submatriz[0]} * {elementos_submatriz[3]} - {elementos_submatriz[1]} * {elementos_submatriz[2]}"
    print(f"Operación para el cofactor: {operacion}")
    respuesta_final += f"Operación para el cofactor: {operacion}"

    cof = ((-1) ** (fila + columna)) * determinante(submatriz)
    print(f"Resultado del cofactor: {cof}")
    respuesta_final += f"Resultado del cofactor: {cof}"
    return cof

def determinante(matriz):
    global respuesta_final
    size = len(matriz)

    if size == 1:
        return matriz[0, 0]
    elif size == 2:
        return matriz[0, 0] * matriz[1, 1] - matriz[0, 1] * matriz[1, 0]
    else:
        det = 0
        expresion_cofactores = ""
        for columna in range(size):
            cof = cofactor(matriz, 0, columna)
            print(f"\nMultiplicando el elemento en la fila 1, columna {columna + 1} por su cofactor:")
            print(f"{matriz[0, columna]} * {cof} = {matriz[0, columna] * cof}")
            if columna == 0:
                expresion_cofactores += f"{matriz[0, columna]} * {cof} "
            else:
                expresion_cofactores += f"+ {matriz[0, columna]} * {cof} "
            det += matriz[0, columna] * cof

        #expresion_cofactores = expresion_cofactores[:-2]  # Eliminar el último "+ "
        print(f"\nExpresión de la suma de los cofactores: {expresion_cofactores}")
        print(f"Suma: {det}")
        return det

def insertar_matriz():
    try:
        fila = int(input("Ingresa el número de filas de la matriz (máximo 5): "))
        columna = int(input("Ingresa el número de columnas (máximo 5): "))
        if fila > 5 or columna > 5:
            raise ValueError("Error, límite superado. Valores fuera del rango.")
        elif fila < 1 or columna < 1:
            raise ValueError("No puedes ingresar datos menores a 1.")
        elif fila != columna:
            raise ValueError("Error, la matriz debe ser cuadrada. Ingresa el mismo número de filas y columnas")
        matriz = np.zeros((fila, columna))

        for i in range(fila):
            for j in range(columna):
                matriz[i, j] = float(input(f"Ingrese el elemento en la posición ({i + 1}, {j + 1}): "))
        print("\nMatriz ingresada:")
        print(matriz)
        return matriz
    except ValueError as error:
        print(f"Error: {error}")
        return None

if __name__ == "__main__":
    matriz_usuario = insertar_matriz()

    if matriz_usuario is not None:
        print("\nCalculando el determinante usando el método de cofactores (laplace)...")
        resultado = determinante(matriz_usuario)
        print(f"\nDeterminante por cofactores: {resultado}")
        print(respuesta_final)
