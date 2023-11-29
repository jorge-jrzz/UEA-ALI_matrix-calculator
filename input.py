import flet as ft


def main(page: ft.Page):
    def button_clicked(e):  # Funcion para recolectar la informacion de los inputs
        # for i in items:
        #     t.value += f" i.value"

        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="1,1")
    tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
    tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
    tb4 = ft.TextField(label="With placeholder",
                       hint_text="Please enter text here")
    tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    page.add(tb1, tb2, tb3, tb4, tb5, b, t)  # La pagina es una lista


ft.app(target=main)
