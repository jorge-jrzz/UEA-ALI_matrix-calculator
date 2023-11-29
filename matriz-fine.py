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
        coo = ft.TextField(label=f"{rows}, {colums}")
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
                    # content=ft.TextField(label=f"{rows}, {colums}"),
                    alignment=ft.alignment.center,
                    width=55,
                    height=50,
                    bgcolor=ft.colors.GREY,
                    border_radius=ft.border_radius.all(5)
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

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Matriz de 5 x 5"
                )
            ]
        ),
        ft.Container(content=row, bgcolor=ft.colors.WHITE24),
        # row,
        b, t
    )

    # values = []
    # for i in coos:
    #     values.append(i.value)

    # print(values)


ft.app(target=main)
