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
    page.window_center()
    page.title = "Matrix Calculator"
    page.window_height = 600
    page.window_width = 1060
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Creacion de inputs para la matriz
    def create_inputs(colums, rows):
        for i in range(1, 26):
            colums += 1
            coo = ft.TextField(
                border=ft.InputBorder.NONE,
                max_length=3,
                counter_style=ft.TextStyle(size=0),
                text_size=12,
                text_align=ft.TextAlign.CENTER,
                hint_text=f"({rows}, {colums})",
                hint_style=ft.TextStyle(
                    size=10,
                    color=ft.colors.GREY),
                filled=True,
                width=55,
                height=50,
                bgcolor=ft.colors.WHITE,
            )
            coos.append(coo)
            if colums == 5:
                rows += 1
                colums = 0

        return coos

    # Creacion de la matriz con los inputs
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=create_inputs(colums, rows)[i-1],
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
        elif subject == "Determinantes":
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
            elif sub_subject == "Resta":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
            elif sub_subject == "Multiplicacion por un escalar":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
            elif sub_subject == "Multiplicacion de matrices":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
            elif sub_subject == "Inversión de matrices":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_matrices)
                row_botones.controls.append(size_matrices)
        elif subject == "Determinantes":
            sub_subject = input_subtema_det.value
            if sub_subject == "Método de cofactores" or sub_subject == "Método de expansión de Laplace.":
                row_botones.controls.clear()
                row_botones.controls.append(main_subject)
                row_botones.controls.append(ops_det)
                row_botones.controls.append(size_matrices_2)
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

        elif subject == "Determinantes":
            sub_subject_2 = input_subtema_det.value
            size_it = input_size_matriz_2.value
            itemss = convert_size(size_it)

        matriz_a.content.controls.clear()
        matriz_b.content.controls.clear()
        coos.clear()
        matriz_b.content.controls.append(return_matrix(itemss))
        matriz_a.content.controls.append(return_matrix(itemss))

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
            ft.dropdown.Option("Determinantes"),
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
                "Multiplicacion por un escalar"),
            ft.dropdown.Option("Multiplicacion de matrices"),
            ft.dropdown.Option("Inversión de matrices")
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
            ft.dropdown.Option("Método de expansión de Laplace.")
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
        border_radius=ft.border_radius.all(5)
    )

    # Fila de botones (tema, subtema, tamaño de matrices)
    row_botones = ft.Row(
        [main_subject]
    )

    # Contenedor de los botones (tema, subtema, tamaño de matrices)
    botones = ft.Container(row_botones)

    # Funcion para el acomodo de los inputs en una matriz de 5 x 5
    def return_matrix(itemss=25):
        in_size_op = get_size(input_size_matriz.value)
        in_size_det = get_size(input_size_matriz_2.value)
        if in_size_op == None and in_size_det == None:
            size = CINCO_X_CINCO
        elif in_size_op == None:
            size = in_size_det
        else:
            size = in_size_op
        # size = insize if insize != None else CINCO_X_CINCO
        row = ft.Row(
            wrap=True,
            spacing=10,
            run_spacing=10,
            controls=items(itemss),
            width=size,
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
        # bgcolor="#FFDEA4",
        bgcolor=ft.colors.BLACK,
        padding=10,
        border_radius=ft.border_radius.all(5),

        alignment=ft.Alignment(0, 0),
    )

    # Operacion
    operation = ft.Container(
        ft.Text(" + ")
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
    main_conteiner = ft.Container(ft.Column([botones, matrices]))

    page.add(main_conteiner)

    # Funcion para el saber el tamaño de la aplicacion en tiempo real
    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)

    # page.on_resize = page_resize


# Ejecucion en aplicacion de escritorio
ft.app(target=main)

# Ejecucion en local host ( navegador web )
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
