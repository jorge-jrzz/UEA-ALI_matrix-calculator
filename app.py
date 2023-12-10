# Autor: Jorge Jusrez

import flet as ft


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

# Lista de inputs para la matriz
coos = []
rows = 1
colums = 0
resultado = """1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25"""


def main(page: ft.Page):

    global coos, rows, colums, resultado

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

    # Creacion de inputs para la matriz
    def create_inputs(colums, rows, count=26, limt=5):

        for i in range(1, count):
            colums += 1
            coo = return_input(f"({rows}, {colums})")
            coos.append(coo)
            if colums >= limt:
                rows += 1
                colums = 0

        return coos

    # Creacion de la matriz con los inputs y sus respectivas coordenadas
    def items(count):

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
                    content=create_inputs(
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
        elif subject == "Determinantes (A)":
            row_botones.controls.clear()
            row_botones.controls.append(main_subject)
            row_botones.controls.append(ops_det)
        elif subject == "Aplicaiones":
            row_botones.controls.clear()
            row_botones.controls.append(main_subject)
            row_botones.controls.append(aplications)

        page.update()

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
                matriz_a.content.controls.append(return_matrix())
            elif sub_subject == "Resta":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
                operation.content.value = " - "
                operation.update()
                matriz_a.content.controls.clear()
                matriz_a.content.controls.append(return_matrix())
            elif sub_subject == "Multiplicación por un escalar":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
                operation.content.value = " x "
                operation.update()
                matriz_a.content.controls.clear()
                matriz_a.content.controls.append(return_input("Escalar (k)"))
            elif sub_subject == "Multiplicacion de matrices":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
                operation.content.value = " x "
                operation.update()
                matriz_a.content.controls.clear()
                matriz_a.content.controls.append(return_matrix())
            elif sub_subject == "Inversión de matriz (A)":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
                operation.content.value = "A^-1"
                operation.update()
                matriz_b.content.controls.clear()

            input_size_matriz_2.value = None

        elif subject == "Determinantes (A)":
            sub_subject = input_subtema_det.value
            if sub_subject == "Método de cofactores" or sub_subject == "Método de expansión de Laplace":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_det)
                row_botones.controls.append(size_matrices_2)
                operation.content.value = "Det(A)"
                operation.update()
                matriz_b.content.controls.clear()

            input_size_matriz.value = None

        elif subject == "Aplicaiones":
            pass

        page.update()

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
            size_it = input_size_matriz.value
            itemss = convert_size(size_it)

        elif subject == "Determinantes (A)":
            sub_subject_2 = input_subtema_det.value
            size_it = input_size_matriz_2.value
            itemss = convert_size(size_it)

        matriz_a.content.controls.clear()
        matriz_b.content.controls.clear()
        coos.clear()
        if sub_subject_2 == "Multiplicación por un escalar":
            matriz_a.content.controls.append(return_input("Escalar (k)"))
            matriz_b.content.controls.append(return_matrix(itemss))
        elif sub_subject_2 == "Inversión de matriz (A)":
            matriz_a.content.controls.append(return_matrix(itemss))
            matriz_b.content.controls.clear()
        elif sub_subject_2 == "Método de cofactores" or sub_subject_2 == "Método de expansión de Laplace":
            matriz_a.content.controls.append(return_matrix(itemss))
            matriz_b.content.controls.clear()
        else: 
            matriz_a.content.controls.append(return_matrix(itemss))
            matriz_b.content.controls.append(return_matrix(itemss))


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
            ft.dropdown.Option("Aplicaiones")
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
            ft.dropdown.Option(
                "Multiplicación por un escalar"),
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
            ft.dropdown.Option("Método de cofactores"),
            ft.dropdown.Option("Método de expansión de Laplace")
        ],
        autofocus=True
    )

    # Boton selecionado para la aplicacion de criptografia de hill
    input_subtema_ap = ft.Dropdown(
        text_size=13,
        width=220,
        height=50,
        label="Criptografía de Hill",
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.NONE,
        disabled=True
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
    aplications = ft.Container(
        input_subtema_ap,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FFA132",
        padding=5,
        border_radius=ft.border_radius.all(5)
    )

    # Contenedor del boton para la seleccion del tamaño de matrices
    size_matrices = ft.Container(
        input_size_matriz,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FFDEA5",
        padding=5,
    )

    # Contenedor del boton para la seleccion del tamaño de matrices cuadradas
    size_matrices_2 = ft.Container(
        input_size_matriz_2,
        ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#FFDEA5",
        padding=5,
    )

    # Fila de botones (tema, subtema, tamaño de matrices)
    row_botones = ft.Row(
        [main_subject]
    )

    # Contenedor de los botones (tema, subtema, tamaño de matrices)
    botones = ft.Container(row_botones)

    # Funcion para el acomodo de los inputs en una matriz de 5 x 5
    def return_matrix(itemss=25):

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
            controls=items(itemss),
            width=size
        )

        return row

    # Matriz A
    matriz_a = ft.Container(
        content=return_matrix(),
        bgcolor="#FFDEA5",
        padding=10,
        border_radius=ft.border_radius.all(5),
    )

    # Matriz B
    matriz_b = ft.Container(
        content=return_matrix(),
        bgcolor="#FFDEA5",
        padding=10,
        border_radius=ft.border_radius.all(5),
    )

    # Operacion
    operation = ft.Container(
        content=ft.Text("  ", color=ft.colors.BLACK, size=30)
    )

    # Contenedor de las matrices
    matrices = ft.Container(
        ft.Row(
            [
                matriz_a,  # Matriz A
                operation,
                matriz_b,  # Matriz B
                ft.Text(" = "),
                ft.Container(
                    content=ft.Text(
                        resultado,
                        color=ft.colors.WHITE
                    ),
                    bgcolor="#FFDEA5",
                    width=310,
                    height=310,
                    border_radius=ft.border_radius.all(5)
                )
            ]
        )
    )

    # Contenedor principal de la aplicacion
    main_conteiner = ft.Container(ft.Column([
        botones, 
        matrices, 
        ft.Row([
            ft.Text("A", color=ft.colors.ORANGE, size=20), 
            ft.Text("B", color=ft.colors.ORANGE, size=20),
            ft.Text("Result", color=ft.colors.ORANGE, size=20)
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
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
