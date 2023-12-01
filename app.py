# Autor: Jorge Jusrez

import flet as ft


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

    page.window_center()
    page.title = "Matrix Calculator"
    page.window_height = 600
    page.window_width = 1060
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Creacion de inputs para la matriz
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

    # Creacion de la matriz con los inputs
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=coos[i-1],
                    alignment=ft.alignment.center,
                    width=55,
                    height=50,
                    bgcolor=ft.colors.WHITE,
                    border_radius=ft.border_radius.all(5),
                )
            )

        return items

    # Acomodo de los inputs en una matriz de 5 x 5
    row = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(25),
        width=320
    )

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
        ]
    )

    # Boton para la eleccion del subtema DE DETERMINANTES
    input_subtema_det = ft.Dropdown(
        text_size=13,
        width=220,
        height=50,
        label="subtema",
        hint_text="Elige un subtema",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        options=[
            ft.dropdown.Option("Método de cofactores"),
            ft.dropdown.Option("Método de expansión de Laplace.")
        ]
    )

    # Boton selecionado para la aplicacion
    input_subtema_ap = ft.Dropdown(
        text_size=13,
        width=220,
        height=50,
        label="Criptografía de Hill",
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        disabled=True
    )

    # Boton para la eleccion de tamaño de matrices
    input_tamaño_matriz = ft.Dropdown(
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
        ]
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
        input_tamaño_matriz,
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

    # Contenedor de las matrices
    matrices = ft.Container(
        ft.Row(
            [
                ft.Container(content=row, bgcolor="#FFDEA5",
                             padding=10, border_radius=ft.border_radius.all(5)),
                ft.Text(" + "),
                ft.Container(content=row, bgcolor="#FFDEA5",
                             padding=10, border_radius=ft.border_radius.all(5)),
                ft.Text(" = "),
                ft.Container(
                    content=ft.Text(
                        resultado,
                        color=ft.colors.WHITE
                    ),
                    bgcolor="#FFDEA5",
                    width=310,
                    height=310,
                    border_radius=ft.border_radius.all(5),
                    alignment=ft.alignment.center
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

# Ejecucion en local host
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
