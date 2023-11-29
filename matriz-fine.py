import flet as ft


def main(page: ft.Page):

    def button_clicked(e):  # Funcion para recolectar la informacion de los inputs
        t.value = f"Textboxe value of (1, 1) are: {coos[0].value}."
        page.update()

        values = []
        for i in coos:
            values.append(i.value)

        print(values)

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

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Matriz de 5 x 5"
                )
            ]
        ),
        ft.Row(
            [
                ft.Container(content=row, bgcolor=ft.colors.WHITE24),
                ft.Text(" + "),
                ft.Container(content=row, bgcolor=ft.colors.WHITE24),
                ft.Text(" = "),
                ft.Container(
                    content=ft.Text(
                        resultado,
                        color=ft.colors.WHITE
                    ),
                    bgcolor="#FFDEA5",
                    width=300,
                    height=300,
                    border_radius=ft.border_radius.all(5),
                    alignment=ft.alignment.center,
                ),

            ]
        ),
        b, t

    )


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
