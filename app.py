# import flet as ft


# def main(page: ft.Page):
#     def button_clicked(e):
#         t.value = f"Dropdown value is:  {dd.value}"
#         page.update()

#     t = ft.Text()
#     b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
#     dd = ft.Dropdown(
#         width=100,
#         options=[
#             ft.dropdown.Option("Red"),
#             ft.dropdown.Option("Green"),
#             ft.dropdown.Option("Blue"),
#         ],
#     )
#     page.add(dd, b, t)


# ft.app(target=main)

import flet as ft


def main(page: ft.Page):

    def button_clicked(e):  # Funcion para recolectar la informacion de los inputs
        t.value = f"Textboxe value of (1, 1) are: {coos[0].value}."
        page.update()

        values = []
        for i in coos:
            values.append(i.value)

        print(values)

    def button_clicked_tema(e):
        t.value = f"Dropdown value is:  {dd.value}"
        page.update()

    t = ft.Text()

    coos = []
    rows = 1
    colums = 0
    for i in range(1, 26):
        colums += 1
        coo = ft.TextField(  # label=f"({rows}, {colums})",
            # label_style=ft.TextStyle(size=10),
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

    row = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(25),
        width=320,

    )

    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    resultado = """
    1  2  3  4  5
    6  7  8  9  10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25"""

    page.window_center()
    page.title = "Matrix Calculator"
    page.window_height = 600
    page.window_width = 1060

    def page_resize(e):
        print("New page size:", page.window_width, page.window_height)

    page.on_resize = page_resize

    dd = ft.Dropdown(
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

    b = ft.ElevatedButton(text="Submit", on_click=button_clicked_tema)

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Matriz de 5 x 5"
                ),
                b, t
            ]
        ),
        ft.Row(
            [
                ft.Container(
                    dd,
                    ft.TextStyle(color=ft.colors.BLACK),
                    bgcolor="#FFA132",
                    padding=5,
                    border_radius=ft.border_radius.all(5)
                ),
                ft.Container(
                    ft.Dropdown(
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
                            ft.dropdown.Option("Inversión de matrices"),
                        ]
                    ),
                    ft.TextStyle(color=ft.colors.BLACK),
                    bgcolor="#FFA132",
                    padding=5,
                    border_radius=ft.border_radius.all(5)
                ),
                ft.Container(
                    ft.Dropdown(
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
                    ),
                    ft.TextStyle(color=ft.colors.BLACK),
                    bgcolor="#FFDEA5",
                    padding=5,
                    border_radius=ft.border_radius.all(5)
                )
            ]
        ),
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
                    alignment=ft.alignment.center,
                ),
            ]
        ),
        b, t

    )


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
