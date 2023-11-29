import tkinter as tk
from tkinter import ttk


class InterfazMatrices:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz de Matrices")

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label_matriz1 = ttk.Label(
            self.frame, text="Ingrese la primera matriz:")
        self.label_matriz1.grid(column=0, row=0, columnspan=2, pady=10)

        self.matriz1_entries = self.crear_matriz_entries(3, 3)
        self.mostrar_matriz_entries(self.matriz1_entries, row_start=1)

        self.label_matriz2 = ttk.Label(
            self.frame, text="Ingrese la segunda matriz:")
        self.label_matriz2.grid(column=0, row=4, columnspan=2, pady=10)

        self.matriz2_entries = self.crear_matriz_entries(3, 3)
        self.mostrar_matriz_entries(self.matriz2_entries, row_start=5)

        self.boton_calcular = ttk.Button(
            self.frame, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(column=0, row=8, columnspan=2, pady=10)

        # Crear un Text widget para mostrar las matrices
        self.text_resultado = tk.Text(
            self.frame, height=10, width=40, state=tk.DISABLED)
        self.text_resultado.grid(column=2, row=0, rowspan=9, padx=10)

    def crear_matriz_entries(self, filas, columnas):
        matriz_entries = []
        for i in range(filas):
            fila_entries = []
            for j in range(columnas):
                entry = ttk.Entry(self.frame, width=5)
                entry.grid(column=j, row=i)
                fila_entries.append(entry)
            matriz_entries.append(fila_entries)
        return matriz_entries

    def mostrar_matriz_entries(self, matriz_entries, row_start=0):
        for i, fila_entries in enumerate(matriz_entries):
            for j, entry in enumerate(fila_entries):
                entry.grid(column=j, row=i + row_start, padx=5, pady=5)

    def calcular(self):
        # Obtener las matrices ingresadas por el usuario
        matriz1 = [[int(entry.get()) for entry in fila]
                   for fila in self.matriz1_entries]
        matriz2 = [[int(entry.get()) for entry in fila]
                   for fila in self.matriz2_entries]

        # Mostrar las matrices en el Text widget
        resultado_text = "Matriz 1:\n"
        resultado_text += self.matriz_a_cadena(matriz1) + "\n\n"
        resultado_text += "Matriz 2:\n"
        resultado_text += self.matriz_a_cadena(matriz2) + "\n"

        self.text_resultado.config(state=tk.NORMAL)
        self.text_resultado.delete(1.0, tk.END)
        self.text_resultado.insert(tk.END, resultado_text)
        self.text_resultado.config(state=tk.DISABLED)

    def matriz_a_cadena(self, matriz):
        return "\n".join([" ".join(map(str, fila)) for fila in matriz])


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazMatrices(root)
    root.mainloop()
