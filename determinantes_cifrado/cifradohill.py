import numpy as np
from sympy import Matrix

#Matriz clave
clave = np.array([[3, 3], [2, 5]])

#Inversa de la matriz clave
clave_inversa = np.array(Matrix(clave).inv_mod(28))

def encriptar_mensaje(clave, mensaje):
    tabla = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26, 'Ñ': 27}

    numeros = [tabla[letra.upper()] for letra in mensaje]

    while len(numeros) % clave.shape[0] != 0:
        numeros.append(26)

    matriz = np.array(numeros).reshape(-1, clave.shape[0])
    resultado = np.dot(matriz, clave)
    resultado = resultado % 28
    letras = ''.join([list(tabla.keys())[list(tabla.values()).index(int(numero))] for numero in resultado.flatten()])

    return letras

def desencriptar_mensaje(clave, clave_inversa, mensaje_cifrado):
    tabla = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26, 'Ñ': 27}

    numeros = [tabla[letra.upper()] for letra in mensaje_cifrado]
    
    matriz = np.array(numeros).reshape(-1, clave.shape[0])
    resultado = np.dot(matriz, clave_inversa)
    resultado = resultado % 28
    letras = ''.join([list(tabla.keys())[list(tabla.values()).index(int(numero))] for numero in resultado.flatten()])

    return letras

# def imprimirEncriptacion(clave): 
#     mensaje_original = input("Ingresa la palabra o frase que deseas encriptar: ")
#     mensaje_encriptado = encriptar_mensaje(clave, mensaje_original)
#     print(f"La palabra o frase encriptada es: {mensaje_encriptado}")

# def imprimirDesencriptacion(clave, clave_inversa):
#     mensaje_cifrado = input("Ingresa el mensaje cifrado que deseas desencriptar: ")
#     mensaje_desencriptado = desencriptar_mensaje(clave, clave_inversa, mensaje_cifrado)
#     print(f"La palabra o frase desencriptada es: {mensaje_desencriptado}")

# imprimirEncriptacion(clave)

# imprimirDesencriptacion(clave, clave_inversa)}