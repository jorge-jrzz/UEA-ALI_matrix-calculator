import flet as ft

HEIGHT = 400


def main(page: ft.Page):
    def items(count):
        items = []

        items.append(ft.Container(ft.TextField(label="1"),
                                  alignment=ft.alignment.center,  # La posicion de los valores dentro de sus cuadros
                                  width=50,    # El ancho de los cuadros
                                  height=50,  # El alto de los cuadros
                                  # Las cuarvaturas de las esquinas de los cuadros
                                  border_radius=ft.border_radius.all(5)))

        items.append(ft.Container(ft.TextField(label="2"),
                                  alignment=ft.alignment.center,  # La posicion de los valores dentro de sus cuadros
                                  width=50,    # El ancho de los cuadros
                                  height=50,  # El alto de los cuadros
                                  # Las cuarvaturas de las esquinas de los cuadros
                                  border_radius=ft.border_radius.all(5)))

        items.append(ft.Container(ft.TextField(label="3"),
                                  alignment=ft.alignment.center,  # La posicion de los valores dentro de sus cuadros
                                  width=50,    # El ancho de los cuadros
                                  height=50,  # El alto de los cuadros
                                  # Las cuarvaturas de las esquinas de los cuadros
                                  border_radius=ft.border_radius.all(5)))

        items.append(ft.TextField(label="4"))
        items.append(ft.TextField(label="5"))
        items.append(ft.TextField(label="6"))
        items.append(ft.TextField(label="7"))
        items.append(ft.TextField(label="8"))
        items.append(ft.TextField(label="9"))
        items.append(ft.TextField(label="10"))
        items.append(ft.TextField(label="11"))
        items.append(ft.TextField(label="12"))
        items.append(ft.TextField(label="13"))
        items.append(ft.TextField(label="14"))
        items.append(ft.TextField(label="15"))
        items.append(ft.TextField(label="16"))
        items.append(ft.TextField(label="17"))
        items.append(ft.TextField(label="18"))
        items.append(ft.TextField(label="19"))
        items.append(ft.TextField(label="20"))
        items.append(ft.TextField(label="21"))
        items.append(ft.TextField(label="22"))
        items.append(ft.TextField(label="23"))
        items.append(ft.TextField(label="24"))
        items.append(ft.TextField(label="25"))

        return items

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
            ]
        ),
        ft.Container(content=col, bgcolor=ft.colors.BLACK12),
    )


ft.app(target=main)
