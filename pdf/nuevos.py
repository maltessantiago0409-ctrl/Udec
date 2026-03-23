import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x300")

def actualiza(value):
    opcion_set = Label(root, text=value).pack()

titulo =Label(root, text="Seleccione un opcion. ").pack()

opciones = [["color rojo", "rojo"],
           ["color azul", "azul"],
            ["color verde", "verde"],
             ["Color amarillo", "amarillo"]]

colores = StringVar()
colores.set("rojo")

for opcion, valor in opciones:
 Radiobutton(root, text=opcion, value=valor, variable=colores).pack()
boton_envia = Button(root, text="Enviar",
command=lambda:actualiza(colores.get())).pack()




root.mainloop()