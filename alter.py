import tkinter as tk
from tkinter import ttk


class InterfazTextoAlterado:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz de Texto Alterado")

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Etiqueta
        self.label = ttk.Label(self.frame, text="Seleccione una opción:")
        self.label.grid(column=0, row=0, columnspan=2, pady=10)

        # Campo de selección
        opciones = ["Mayúsculas", "Minúsculas", "Invertir"]
        self.seleccion_var = tk.StringVar()
        self.seleccion = ttk.Combobox(
            self.frame, textvariable=self.seleccion_var, values=opciones)
        self.seleccion.grid(column=0, row=1, columnspan=2, pady=5)
        self.seleccion.set(opciones[0])

        # Cuadro de entrada de texto
        self.entry_texto = ttk.Entry(self.frame, width=40)
        self.entry_texto.grid(column=0, row=2, columnspan=2, pady=5)

        # Botón para alterar el texto
        self.boton_alterar = ttk.Button(
            self.frame, text="Alterar Texto", command=self.alterar_texto)
        self.boton_alterar.grid(column=0, row=3, columnspan=2, pady=10)

        # Área de texto para mostrar el resultado
        self.text_resultado = tk.Text(
            self.frame, height=5, width=40, state=tk.DISABLED)
        self.text_resultado.grid(column=0, row=4, columnspan=2, pady=10)

    def alterar_texto(self):
        # Obtener la opción seleccionada y el texto ingresado por el usuario
        opcion = self.seleccion_var.get()
        texto = self.entry_texto.get()

        # Realizar la alteración según la opción seleccionada
        if opcion == "Mayúsculas":
            texto_alterado = texto.upper()
        elif opcion == "Minúsculas":
            texto_alterado = texto.lower()
        elif opcion == "Invertir":
            texto_alterado = texto[::-1]
        else:
            texto_alterado = "Opción no válida"

        # Mostrar el resultado en el área de texto
        self.text_resultado.config(state=tk.NORMAL)
        self.text_resultado.delete(1.0, tk.END)
        self.text_resultado.insert(tk.END, texto_alterado)
        self.text_resultado.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazTextoAlterado(root)
    root.mainloop()
