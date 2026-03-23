import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x300")

x = IntVar()
x.set(value=1)

def actualiza(value):
    opcion_set = Label(root, text=x.get()).pack(pady=3)

titulo = Label(root, text="Seleccione la respuesta correcta").pack(pady=5)

opcion1 = Radiobutton(root, text="Esta es la primera opcion.", value=1, variable=x)
opcion1.pack(pady=5)

opcion2 = Radiobutton(root, text="Esta es la segunda opcion.", value=2, variable=x)
opcion2.pack(pady=5)


boton =  Button(root, text="Enviar", command=lambda: actualiza(x.get())).pack(pady=5)

root.mainloop()