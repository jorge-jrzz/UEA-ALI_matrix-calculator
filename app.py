# Autores: Jorge Juarez, Iván Garrido Velázquez, Casandra Zetina Rodríguez
import flet as ft
from determinantes_cifrado.cifradohill import *
from funcionalidades_terminal.operaciones_matrices import *
import numpy as np
from sympy import Matrix
from fractions import Fraction # Para que los resultados salgan en fracciones

# Tamaño para las matrices
DOS_X_DOS = 160
DOS_X_TRES = 240
TRES_X_TRES = 200
TRES_X_DOS = 160
CUATRO_X_DOS = 120
CUATRO_X_TRES = 200
CUATRO_X_CUATRO = 280
TRES_X_CUATRO = 280
DOS_X_CUATRO = 280
CINCO_X_CINCO = 320

#Matriz clave
clave = np.array([[3, 3], [2, 5]])

#Inversa de la matriz clave
clave_inversa = np.array(Matrix(clave).inv_mod(28))

# Lista de inputs para la matriz
# coos = []
coos_a = []
coos_b = []
rows = 1
colums = 0
textfields = []

#resultado = ("1  2  3  4  5\n6  7  8  9  10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25")

# Mapeo de letras con numeros
tabla = "\nTABLA DE EQUIVALENCIAS: \nA = 0 B = 1 C = 2 D = 3 E = 4 \nF = 5 G = 6 H = 7 I = 8 \nJ = 9 K = 10 L = 11 M = 12 \nN = 13 O = 14 P = 15 Q = 16 \nR = 17 S = 18 T = 19 U = 20 \nV = 21 W = 22 X = 23 Y = 24 \nZ = 25 ' '(espacio) = 26 Ñ = 27"

def main(page: ft.Page):
    
    global coos_a, coos_b, rows, colums
    # Configuracion de la pagina
    page.title = "Matrix Calculator"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 570
    page.window_width = 1170
    page.window_center()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def return_input(hint):
        user_input = ft.TextField(
            border=ft.InputBorder.NONE,
            max_length=3,
            counter_style=ft.TextStyle(size=0),
            text_size=12,
            text_align=ft.TextAlign.CENTER,
            hint_text=hint,
            hint_style=ft.TextStyle(
                size=10,
                color=ft.colors.GREY),
            filled=True,
            width=80,
            height=60,
            bgcolor=ft.colors.WHITE
        )
        return user_input
    
    # Input para las Aplicaciones de Hill de Hill 
    def return_input_ap(hint):
        user_input = ft.TextField(
            border=ft.InputBorder.NONE, 
            max_length=100,
            capitalization=ft.TextCapitalization.CHARACTERS,
            multiline=True,
            text_align=ft.TextAlign.CENTER,
            hint_text=hint,
            hint_style=ft.TextStyle(
                 size=16,
                 color=ft.colors.GREY
            ),
            filled=True,
            bgcolor=ft.colors.ORANGE_50
        )   
        return user_input #user_input.value 
    



    # Funcion para almacenar los inputs de hill
    def return_input_encrip(hint):
        user_input = ft.TextField(
            border=ft.InputBorder.NONE, 
            max_length=100,
            capitalization=ft.TextCapitalization.CHARACTERS,
            multiline=True,
            text_align=ft.TextAlign.CENTER,
            hint_text=hint,
            hint_style=ft.TextStyle(
                 size=16,
                 color=ft.colors.GREY
            ),
            filled=True,
            bgcolor=ft.colors.ORANGE_50,
            read_only=True
        )
        return user_input

    #resultado
    resultado = ft.TextField(
        border=ft.InputBorder.NONE, 
        max_length=1000,
        capitalization=ft.TextCapitalization.CHARACTERS,
        multiline=True,
        text_align=ft.TextAlign.CENTER,
        hint_text="",
        hint_style=ft.TextStyle(
            size=16,
            color=ft.colors.GREY
        ),
        filled=False, 
        bgcolor=ft.colors.ORANGE_50,
        read_only = True # impide que el simio del usuario escriba
       
    )

   
    # Creacion de inputs para la matriz
    # def create_inputs(colums, rows, count=26, limt=5):

    #     for i in range(1, count):
    #         colums += 1
    #         coo = return_input(f"({rows}, {colums})")
    #         coos.append(coo)
    #         if colums >= limt:
    #             rows += 1
    #             colums = 0

    #     return coos
    
    # inputs para la matriz a
    def create_inputs_a(colums, rows, count=26, limt=5):
        for i in range(1, count):
            colums += 1
            coo = return_input(f"A({rows}, {colums})")
            coos_a.append(coo)
            if colums >= limt:
                rows += 1
                colums = 0
        return coos_a

    # inputs matriz b
    def create_inputs_b(colums, rows, count=26, limt=5):
        for i in range(1, count):
            colums += 1
            coo = return_input(f"B({rows}, {colums})")
            coos_b.append(coo)
            if colums >= limt:
                rows += 1
                colums = 0
        return coos_b

    # Creacion de la matriz con los inputs y sus respectivas coordenadas
    # def items(count):

    #     in_size_op = input_size_matriz.value
    #     in_size_det = input_size_matriz_2.value

    #     if in_size_op is None and in_size_det is None:
    #         count = 26
    #         limt = 5
    #     elif in_size_det is None or in_size_det == "":
    #         count = convert_size(in_size_op) + 1
    #         limt = int(in_size_op[4])
    #         in_size_op = ""
    #     elif in_size_op is None or in_size_op == "":
    #         count = convert_size(in_size_det) + 1
    #         limt = int(in_size_det[4])
    #         in_size_det = ""

    #     items = []
    #     for i in range(1, count):
    #         items.append(
    #             ft.Container(
    #                 content=create_inputs(
    #                     colums, rows, count=count, limt=limt)[i-1],

    #                 alignment=ft.alignment.center,
    #                 width=55,
    #                 height=50,
    #                 bgcolor=ft.colors.WHITE,
    #                 border_radius=ft.border_radius.all(5),
    #             )
    #         )

    # coordenadas a
    def items_a(count):

        in_size_op = input_size_matriz.value
        in_size_det = input_size_matriz_2.value

        if in_size_op is None and in_size_det is None:
            count = 26
            limt = 5
        elif in_size_det is None or in_size_det == "":
            count = convert_size(in_size_op) + 1
            limt = int(in_size_op[4])
            in_size_op = ""
        elif in_size_op is None or in_size_op == "":
            count = convert_size(in_size_det) + 1
            limt = int(in_size_det[4])
            in_size_det = ""

        items = []
        for i in range(1, count):
            items.append(
                ft.Container(
                    content=create_inputs_a(
                        colums, rows, count=count, limt=limt)[i-1],

                    alignment=ft.alignment.center,
                    width=55,
                    height=50,
                    bgcolor=ft.colors.WHITE,
                    border_radius=ft.border_radius.all(5),
                )
            )

        return items
    # coordenadas b
    def items_b(count):

        in_size_op = input_size_matriz.value
        in_size_det = input_size_matriz_2.value

        if in_size_op is None and in_size_det is None:
            count = 26
            limt = 5
        elif in_size_det is None or in_size_det == "":
            count = convert_size(in_size_op) + 1
            limt = int(in_size_op[4])
            in_size_op = ""
        elif in_size_op is None or in_size_op == "":
            count = convert_size(in_size_det) + 1
            limt = int(in_size_det[4])
            in_size_det = ""

        items = []
        for i in range(1, count):
            items.append(
                ft.Container(
                    content=create_inputs_b(
                        colums, rows, count=count, limt=limt)[i-1],

                    alignment=ft.alignment.center,
                    width=55,
                    height=50,
                    bgcolor=ft.colors.WHITE,
                    border_radius=ft.border_radius.all(5),
                )
            )

        return items

    # Funcion para la eleccion del tema
    def subject_changed(e):
       
        subject = input_tema.value
        if subject == "Matrices":
            row_botones.controls.clear()
            row_botones.controls.append(main_subject)
            row_botones.controls.append(ops_matrices)
            operation.content.value = " "
            operation.update()
            matriz_a.content.controls.clear()
            matriz_a.content.controls.append(return_matrix_a())
            matriz_b.content.controls.clear()
            matriz_b.content.controls.append(return_matrix_b())
        elif subject == "Determinantes (A)":
            row_botones.controls.clear()
            row_botones.controls.append(main_subject)
            row_botones.controls.append(ops_det)
            operation.content.value = " "
            operation.update()
            matriz_a.content.controls.clear()
            matriz_a.content.controls.append(return_matrix_a())
            matriz_b.content.controls.clear()
            matriz_b.content.controls.append(return_matrix_b())
        elif subject == "Aplicaciones de Hill":
            row_botones.controls.clear()
            row_botones.controls.append(main_subject)
            row_botones.controls.append(ops_aplications)
            operation.content.value = " "
            operation.update()
            matriz_a.content.controls.clear()
            matriz_b.content.controls.clear()
            matriz_a.content.controls.append(return_input_ap("Ingreso letras"))
            matriz_b.content.controls.append(ft.Text("Matriz clave: \n[3, 3] \n[2, 5]", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, italic=True, text_align=ft.TextAlign.CENTER))
            matriz_b.content.controls.append(ft.Text(tabla, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, italic=True, text_align=ft.TextAlign.CENTER))

        page.update()

    entrada_mensaje = ft.TextField(
        border=ft.InputBorder.NONE, 
        max_length=100,
        capitalization=ft.TextCapitalization.CHARACTERS,
        multiline=True,
        text_align=ft.TextAlign.CENTER,
        hint_text="",
        hint_style=ft.TextStyle(
            size=16,
            color=ft.colors.GREY
        ),
        filled=True,
        bgcolor=ft.colors.ORANGE_50
    )
    # global entrada_mensaje
    # entrada_mensaje = return_input_encrip("")
    # def encriptar(e):
    #     global entrada_mensaje
    #     mensaje = entrada_mensaje.value
    #     resultado_encriptado = encriptar_mensaje(clave, mensaje)
    #     resultado.text = resultado_encriptado
    #     print("Si ejecuta la función")
    #     page.update()
    # Funcion para la eleccion del subtema
    def sub_subject_changed(e):
        subject = input_tema.value
        sub_subject = ""
        if subject == "Matrices":
            sub_subject = input_subtema_op.value
            if sub_subject == "Suma":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
                operation.content.value = " + "
                operation.update()
                matriz_a.content.controls.clear()
                matriz_a.content.controls.append(return_matrix_a())
                matriz_b.content.controls.clear()
                matriz_b.content.controls.append(return_matrix_b())
                # Botón
                resolver_botón.content = boton_sumar
            elif sub_subject == "Resta":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
                operation.content.value = " - "
                operation.update()
                matriz_a.content.controls.clear()
                matriz_a.content.controls.append(return_matrix_a())
                matriz_b.content.controls.clear()
                matriz_b.content.controls.append(return_matrix_b())
                # Botón 
                resolver_botón.content = boton_restar
            elif sub_subject == "Multiplicación por un escalar":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
                operation.content.value = " x "
                operation.update()
                matriz_a.content.controls.clear()
                matriz_a.content.controls.append(return_input("Escalar (k)"))
                # Botón 
                resolver_botón.content = ft.ElevatedButton("Multiplicar por un escalar", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK)
            elif sub_subject == "Multiplicacion de matrices":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices_2)
                operation.content.value = " x "
                operation.update()
                matriz_a.content.controls.clear()
                matriz_a.content.controls.append(return_matrix_a())
                matriz_b.content.controls.clear()
                matriz_b.content.controls.append(return_matrix_b())
                # Botón
                resolver_botón.content = boton_multiplicar
            elif sub_subject == "Inversión de matriz (A)":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices_2)
                operation.content.value = "A^-1"
                operation.update()
                matriz_b.content.controls.clear()
                resolver_botón.content = boton_inversa

            if sub_subject == "Inversión de matriz (A)" or sub_subject == "Multiplicacion de matrices":
                input_size_matriz.value = None
            else:
                input_size_matriz_2.value = None

        elif subject == "Determinantes (A)":
            sub_subject = input_subtema_det.value
            if sub_subject == "Método de cofactores":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_det)
                row_botones.controls.append(size_matrices_2)
                operation.content.value = "Det(A)"
                operation.update()
                matriz_b.content.controls.clear()
                resolver_botón.content = ft.ElevatedButton("Determinante por cofactores", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK)

            input_size_matriz.value = None

        elif subject == "Aplicaciones de Hill":
            sub_subject = input_subtema_ap.value
            if sub_subject == "Encriptación de Hill":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_aplications)
                operation.content.value = " "
                operation.update()
                matriz_a.content.controls.clear()
                entrada_mensaje.hint_text = "Ingresa la palabra o la oración a encriptar"
                matriz_a.content.controls.append(entrada_mensaje)
                # print (entrada_mensaje)
                matriz_b.content.controls.clear()
                matriz_b.content.controls.append(ft.Text("Matriz clave: \n[3, 3] \n[2, 5]", weight=ft.FontWeight.BOLD, italic=True, text_align=ft.TextAlign.CENTER))
                matriz_b.content.controls.append(ft.Text(tabla, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, italic=True, text_align=ft.TextAlign.CENTER))
                #botón 
                resolver_botón.content = boton_encriptar
            elif sub_subject == "Desencriptación de Hill": 
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_aplications)
                operation.content.value = " "
                operation.update()
                matriz_a.content.controls.clear()
                # matriz_a.content.controls.append(return_input_ap("Ingresa el código"))
                entrada_mensaje.hint_text = "Ingresa el código"
                matriz_a.content.controls.append(entrada_mensaje)
                matriz_b.content.controls.clear()
                matriz_b.content.controls.append(ft.Text("Matriz clave: \n[3, 3] \n[2, 5]", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, italic=True, text_align=ft.TextAlign.CENTER))
                matriz_b.content.controls.append(ft.Text(tabla, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, italic=True, text_align=ft.TextAlign.CENTER))
                # botón 
                # resolver_botón.content = ft.ElevatedButton("Desencriptar", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK)
                resolver_botón.content = boton_desencriptar

        page.update()

    # Suma
    def sumar(e):
        # Recoge las matrices del usuario.
        matriz_a_values = get_matrix_values_a()
        matriz_b_values = get_matrix_values_b()
        # print("Matriz a", matriz_a_values)
        # print("Matriz b: ", matriz_b_values)
        resultado_matriz = sumarMatrices(matriz_a_values, matriz_b_values)
        # Convierte el resultado a una cadena de texto y actualiza el contenedor 'resultado'.
        resultado.value = '\n'.join(' '.join(str(cell) for cell in row) for row in resultado_matriz)
        page.update()

    boton_sumar = ft.ElevatedButton("Sumar", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK, on_click=sumar)

    # Resta
    def restar(e):

        matriz_a_values = get_matrix_values_a()
        matriz_b_values = get_matrix_values_b()
        # print("Matriz a", matriz_a_values)
        # print("Matriz b: ", matriz_b_values)
        resultado_matriz = restarMatrices(matriz_a_values, matriz_b_values)
        # Convierte el resultado a una cadena de texto y actualiza el contenedor 'resultado'.
        resultado.value = '\n'.join(' '.join(str(cell) for cell in row) for row in resultado_matriz)
        page.update()
    boton_restar = ft.ElevatedButton("Restar", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK, on_click=restar)

    # Multiplicación
    def multiplicar(e):

        matriz_a_values = get_matrix_values_a()
        matriz_b_values = get_matrix_values_b()
        # print("Matriz a", matriz_a_values)
        # print("Matriz b: ", matriz_b_values)
        resultado_matriz = multiplicarMatrices(matriz_a_values, matriz_b_values)
        # Convierte el resultado a una cadena de texto y actualiza el contenedor 'resultado'.
        resultado.value = '\n'.join(' '.join(str(cell) for cell in row) for row in resultado_matriz)
        page.update()
    boton_multiplicar = ft.ElevatedButton("Multiplicar", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK, on_click=multiplicar)


    # Escalar


    # Cofactores

    # Hacer el resultado de las fracciones más estético
    def format_fraction(frac):
        # Convierte una fracción a formato Unicode
        if frac.denominator == 1:
            return str(frac.numerator)
        else:
            return f"{frac.numerator}⁄{frac.denominator}"
        
    # Inversa
    def inversa(e):
        matriz_a_values = get_matrix_values_a()
        print ("Matriz a", matriz_a_values)
        resultado_inversa = calcular_inversa(matriz_a_values)
        resultado_inversa = [[Fraction(cell).limit_denominator() for cell in row] for row in resultado_inversa]
        resultado.value = '\n'.join('(' + ', '.join(format_fraction(Fraction(cell)) for cell in row) + ')' for row in resultado_inversa)
        resultado.text_size = 20
        page.update()
    boton_inversa = ft.ElevatedButton("Inversa", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK, on_click=inversa)

    # Funciones para el cifrado de hill

    def encriptar(e):
        mensaje = entrada_mensaje.value
        # print (mensaje)
        resultado.value = encriptar_mensaje(clave, mensaje)
        # print("Si ejecuta la función")
        resultado.text = resultado.value
        # print(resultado)
        page.update()

    def desencriptar(e):
        codigo = entrada_mensaje.value
        resultado.value = desencriptar_mensaje(clave, clave_inversa, codigo)
        # print("Si ejecuta la función DESENCRIPTAR")
        resultado.text = resultado.value
        # print(resultado)
        page.update()
    boton_encriptar = ft.ElevatedButton("Encriptar", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK, on_click=encriptar)
    boton_desencriptar = ft.ElevatedButton("Desencriptar", bgcolor=ft.colors.ORANGE, color=ft.colors.BLACK, on_click=desencriptar)
    
   
    # Funcion para convertir el tamaño de la matriz en un numero
    def convert_size(matriz_size):
        size = matriz_size.split("x")
        return int(size[0]) * int(size[1])

    # Funcion para el cambio de tamaño de la matriz
    def size_changed(e):
        subject = input_tema.value
        sub_subject_2 = ""
        size_it = ""
        itemss = 0
        if subject == "Matrices":
            sub_subject_2 = input_subtema_op.value
            if sub_subject_2 == "Inversión de matriz (A)" or sub_subject_2 == "Multiplicacion de matrices":
                size_it = input_size_matriz_2.value
                itemss = convert_size(size_it)
            else:
                size_it = input_size_matriz.value
                itemss = convert_size(size_it)

        elif subject == "Determinantes (A)":
            sub_subject_2 = input_subtema_det.value
            size_it = input_size_matriz_2.value
            itemss = convert_size(size_it)            

        matriz_a.content.controls.clear()
        matriz_b.content.controls.clear()
        coos_a.clear()
        coos_b.clear()
        if sub_subject_2 == "Multiplicación por un escalar":
            matriz_a.content.controls.append(return_input("Escalar (k)"))
            matriz_b.content.controls.append(return_matrix_b(itemss))
        elif sub_subject_2 == "Inversión de matriz (A)":
            matriz_a.content.controls.append(return_matrix_a(itemss))
            matriz_b.content.controls.clear()
        elif sub_subject_2 == "Método de cofactores":
            matriz_a.content.controls.append(return_matrix_a(itemss))
            matriz_b.content.controls.clear()
        else: 
            matriz_a.content.controls.append(return_matrix_a(itemss))
            matriz_b.content.controls.append(return_matrix_b(itemss))


        page.update()

    # Funcion para obtener el tamaño de la matriz
    def get_size(size_in) -> int:
        if size_in == "2 x 2":
            return DOS_X_DOS
        elif size_in == "2 x 3":
            return DOS_X_TRES
        elif size_in == "3 x 3":
            return TRES_X_TRES
        elif size_in == "3 x 2":
            return TRES_X_DOS
        elif size_in == "4 x 2":
            return CUATRO_X_DOS
        elif size_in == "4 x 3":
            return CUATRO_X_TRES
        elif size_in == "4 x 4":
            return CUATRO_X_CUATRO
        elif size_in == "3 x 4":
            return TRES_X_CUATRO
        elif size_in == "2 x 4":
            return DOS_X_CUATRO
        elif size_in == "5 x 5":
            return CINCO_X_CINCO
        else:
            return None
                 
    # Boton para la eleccion de tema
    input_tema = ft.Dropdown(
        on_change=subject_changed,
        text_size=13,
        width=220,
        height=50,
        bgcolor="#FFA132",
        label="Tema",
        hint_text="Elige un tema",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        options=[
            ft.dropdown.Option("Matrices"),
            ft.dropdown.Option("Determinantes (A)"),
            ft.dropdown.Option("Aplicaciones de Hill")
        ],
        autofocus=True
    )

    # Boton para la eleccion del subtema
    input_subtema_op = ft.Dropdown(
        on_change=sub_subject_changed,
        text_size=13,
        width=220,
        height=50,
        label="subtema",
        hint_text="Elige un subtema",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        options=[
            ft.dropdown.Option("Suma"),
            ft.dropdown.Option("Resta"),
            ft.dropdown.Option("Multiplicación por un escalar"),
            ft.dropdown.Option("Multiplicacion de matrices"),
            ft.dropdown.Option("Inversión de matriz (A)")
        ],
        autofocus=True
    )

    # Boton para la eleccion del subtema DE DETERMINANTES
    input_subtema_det = ft.Dropdown(
        on_change=sub_subject_changed,
        text_size=11.5,
        width=230,
        height=50,
        label="subtema",
        hint_text="Elige un subtema",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        options=[
            ft.dropdown.Option("Método de cofactores")
        ],
        autofocus=True
    )

    # Boton selecionado para la aplicacion de criptografia de hill
    input_subtema_ap = ft.Dropdown(
        on_change=sub_subject_changed,
        text_size=13,
        width=220,
        height=50,
        label="subtema",
        hint_text="Elige un subtema",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        options=[
            ft.dropdown.Option("Encriptación de Hill"),
            ft.dropdown.Option("Desencriptación de Hill")
        ],
        autofocus=True
    )

    # Boton para la eleccion de tamaño de matrices
    input_size_matriz = ft.Dropdown(
        on_change=size_changed,
        text_size=13,
        width=220,
        height=50,
        bgcolor="#FFDEA5",
        label="Tamaño de matrices",
        hint_text="Elige el tamaño de matrices",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        options=[
            ft.dropdown.Option("2 x 2"),
            ft.dropdown.Option("2 x 3"),
            ft.dropdown.Option("3 x 3"),
            ft.dropdown.Option("3 x 2"),
            ft.dropdown.Option("4 x 2"),
            ft.dropdown.Option("4 x 3"),
            ft.dropdown.Option("4 x 4"),
            ft.dropdown.Option("3 x 4"),
            ft.dropdown.Option("2 x 4"),
            ft.dropdown.Option("5 x 5")
        ],
        autofocus=True
    )

    # Boton para la eleccion de tamaño de matrices cuadradas
    input_size_matriz_2 = ft.Dropdown(
        on_change=size_changed,
        text_size=13,
        width=220,
        height=50,
        bgcolor="#FFDEA5",
        label="Tamaño de matrices",
        hint_text="Elige el tamaño de matrices",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        options=[
            ft.dropdown.Option("2 x 2"),
            ft.dropdown.Option("3 x 3"),
            ft.dropdown.Option("4 x 4"),
            ft.dropdown.Option("5 x 5")
        ],
        autofocus=True
    )

     
    # Contenedor del boton para la seleccion del tema
    main_subject = ft.Container(
        input_tema,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FFA132",
        padding=5,
        border_radius=ft.border_radius.all(5)
    )

    # Contenedor del boton para la seleccion del subtema de operaciones con matrices
    ops_matrices = ft.Container(
        input_subtema_op,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FFA132",
        padding=5,
        border_radius=ft.border_radius.all(5)
    )

    # Contenedor del boton para la seleccion del subtema de determinantes
    ops_det = ft.Container(
        input_subtema_det,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FFA132",
        padding=5,
        border_radius=ft.border_radius.all(5)
    )

    # Contenedor del boton para la seleccion de la aplicacion
    ops_aplications = ft.Container(
        input_subtema_ap,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FBC364",
        padding=5,
        border_radius=ft.border_radius.all(5)
    )

    # Contenedor del boton para la seleccion del tamaño de matrices
    size_matrices = ft.Container(
        input_size_matriz,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FBC364",
        padding=5,
    )

    # Contenedor del boton para la seleccion del tamaño de matrices cuadradas
    size_matrices_2 = ft.Container(
        input_size_matriz_2,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FBC364",
        padding=5,
    )
    
    # Fila de botones (tema, subtema, tamaño de matrices)
    row_botones = ft.Row(
        [main_subject]
    )

    # Contenedor de los botones (tema, subtema, tamaño de matrices)
    botones = ft.Container(row_botones)

    def return_tabla(hint):
        user_input = ft.TextField(
            border=ft.InputBorder.NONE,
            capitalization=ft.TextCapitalization.CHARACTERS,
            multiline=True,
            text_align=ft.TextAlign.CENTER,
            hint_text=hint,
            hint_style=ft.TextStyle(
                 size=16,
                 color=ft.colors.BLACK87
            ),
            disabled=True,
        )   
        return user_input
    
    # Funcion para el acomodo de los inputs en una matriz de 5 x 5

    def return_matrix_a(itemss=25):

        in_op = input_size_matriz.value
        in_det = input_size_matriz_2.value
        in_size_op = get_size(in_op)
        in_size_det = get_size(in_det)

        if in_size_op is None and in_size_det is None:
            size = CINCO_X_CINCO
        elif in_size_det is None:
            size = in_size_op
        elif in_size_op is None:
            size = in_size_det

        row = ft.Row(
            wrap=True,
            spacing=10,
            run_spacing=10,
            controls=items_a(itemss),
            width=size
        )

        return row
    
    def return_matrix_b(itemss=25):

        in_op = input_size_matriz.value
        in_det = input_size_matriz_2.value
        in_size_op = get_size(in_op)
        in_size_det = get_size(in_det)

        if in_size_op is None and in_size_det is None:
            size = CINCO_X_CINCO
        elif in_size_det is None:
            size = in_size_op
        elif in_size_op is None:
            size = in_size_det

        row = ft.Row(
            wrap=True,
            spacing=10,
            run_spacing=10,
            controls=items_b(itemss),
            width=size
        )

        return row

    def get_matrix_values_a():  
        # Recupera los valores de los campos de entrada y los almacena en una lista.
        in_size_op = input_size_matriz.value
        in_size_det = input_size_matriz_2.value
        if in_size_op is None and in_size_det is None:
            count = 26
            limt = 5
        elif in_size_det is None or in_size_det == "":
            count = convert_size(in_size_op) + 1
            limt = int(in_size_op[0])
            in_size_op = ""
        elif in_size_op is None or in_size_op == "":
            count = convert_size(in_size_det) + 1
            limt = int(in_size_det[0])
            in_size_det = ""
        coos = create_inputs_a(colums, rows, count=count, limt=limt)
        matriz_values = [float(coo.value) for coo in coos if coo.value.strip() != '']
        #Da forma a 'matriz_values' para que tenga la forma de la matriz original.
        num_rows = count // limt
        num_columns = limt
        matriz_values = np.reshape(matriz_values, (num_rows, num_columns))
        return matriz_values
    
    def get_matrix_values_b():  
        # Recupera los valores de los campos de entrada y los almacena en una lista.
        in_size_op = input_size_matriz.value
        in_size_det = input_size_matriz_2.value
        if in_size_op is None and in_size_det is None:
            count = 26
            limt = 5
        elif in_size_det is None or in_size_det == "":
            count = convert_size(in_size_op) + 1
            limt = int(in_size_op[0])
            in_size_op = ""
        elif in_size_op is None or in_size_op == "":
            count = convert_size(in_size_det) + 1
            limt = int(in_size_det[0])
            in_size_det = ""
        coos = create_inputs_b(colums, rows, count=count, limt=limt)
        matriz_values = [float(coo.value) for coo in coos if coo.value.strip() != '']
        #Da forma a 'matriz_values' para que tenga la forma de la matriz original.
        num_rows = count // limt
        num_columns = limt
        matriz_values = np.reshape(matriz_values, (num_rows, num_columns))
        return matriz_values




    # Matriz A
    matriz_a = ft.Container(
        content=return_matrix_a(),
        bgcolor="#FFDEA5",
        padding=10,
        border_radius=ft.border_radius.all(5),
    )

    # Matriz B
    matriz_b = ft.Container(
        content=return_matrix_b(),
        bgcolor="#FFDEA5",
        padding=10,
        border_radius=ft.border_radius.all(5),
    )

    # Operacion
    operation = ft.Container(
        content=ft.Text("  ", color=ft.colors.BLACK, size=30)
    )

    def on_column_scroll(e: ft.OnScrollEvent):
        pass 
    
    # Contenedor de botón calcular 
    resolver_botón = ft.Container(
        bgcolor="#FFFFFF",
        padding=10,
        border_radius=ft.border_radius.all(5),
    )
    # Contenedor de las matrices
    # Contenedor de las matrices
    matrices = ft.Container(
        ft.Row(
            [
                matriz_a,  # Matriz A
                operation,
                matriz_b,  # Matriz B
                ft.Text(" = "),
                    ft.Container(
                    content=ft.Column(
                       [
                            resultado,
                            #color=ft.colors.WHITE
                            ft.Text(
                                "\n" * 50,  # Agrega líneas en blanco al final
                                color=ft.colors.WHITE
                            )
                       ], 
                        spacing=10,
                        height=200,
                        width=200,
                        scroll=ft.ScrollMode.ALWAYS,
                        on_scroll=on_column_scroll
                    ),
                    bgcolor="#F7C56F",
                    width=310,
                    height=310,
                    border_radius=ft.border_radius.all(5)
                )                      
            ] 
        )
    )
    
    #Función para almacenar y devolver los outputs del usuario
#    def outputsUser():
#         global resultado
#         resultado.text = desencriptar_mensaje(clave, clave_inversa, entrada_mensaje.value)
#         page.update()
    # Contenedor principal de la aplicacion
    main_conteiner = ft.Container(
        ft.Column([
        botones, 
        matrices, 
        ft.Row([
            ft.Text("A", color=ft.colors.ORANGE, size=20), 
            ft.Text("B", color=ft.colors.ORANGE, size=20),
            ft.Text("Result", color=ft.colors.ORANGE, size=20)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([resolver_botón],  alignment=ft.MainAxisAlignment.CENTER)
    ]))

    page.add(main_conteiner)

    # Funcion para el saber el tamaño de la aplicacion en tiempo real
    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


# Ejecucion en aplicacion de escritorio
ft.app(target=main)
# Ejecucion en local host ( navegador web )
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)