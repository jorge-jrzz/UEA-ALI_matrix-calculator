import flet as ft

HEIGHT = 400


def main(page: ft.Page):
    def items(count):
        items = []
        rows = 1
        colums = 1
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    # Los valores de los recuadros (Estan en un for osea que son consecutivos)
                    # content=ft.Text(value=str(i)),
                    content=ft.TextField(label=f"{rows}, {colums}"),
                    alignment=ft.alignment.center,  # La posicion de los valores dentro de sus cuadros
                    width=50,    # El ancho de los cuadros
                    height=50,  # El alto de los cuadros
                    # bgcolor=ft.colors.AMBER,  # El color de los cuadros
                    # Las cuarvaturas de las esquinas de los cuadros
                    border_radius=ft.border_radius.all(5)
                )
            )
            rows += 1 if colums == 5 else rows
            colums += 1 if colums != 5 else colums
        return items

    # def slider_change(e):
    #     col.height = float(e.control.value)
    #     col.update()

    # width_slider = ft.Slider(
    #     min=0,
    #     max=HEIGHT,
    #     divisions=20,
    #     value=HEIGHT,
    #     label="{value}",
    #     width=500,
    #     on_change=slider_change,
    # )

    col = ft.Column(
        wrap=True,
        spacing=10,  # EL espacio entre los cuadros
        run_spacing=10,
        controls=items(25),  # Cantidad de items (25 -> matriz de 5x5)
        height=220,
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Change the column height to see how child items wrap onto multiple columns:"
                )
                # width_slider,
            ]
        ),
        ft.Container(content=col, bgcolor=ft.colors.BLACK26),
    )


ft.app(target=main)
