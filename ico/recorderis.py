import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("350x350")
root.title("Amix")
root.iconbitmap(r"C:\Users\Edwin Santiago\OneDrive\Documentos\programacion 2\pdf\IMG\perico.ico")

def verificar_respues1():
    valor1 = spin1.get()

    if valor1 == "2026":
        etiqueta_resultado1.config(text="Correcto")
    else:
        etiqueta_resultado1.config(text="Incorreto")



texto1 = tk.Label(root, text="En que año estamos").pack(pady=1.5)

spin1 = tk.Spinbox(root, values=("2020","2030","2026"))
spin1.pack(pady=1.5)

boto1 = tk.Button(root, text="Responder", command=verificar_respues1)
boto1.pack(pady=1.5)

etiqueta_resultado1 = tk.Label(root, text="")
etiqueta_resultado1.pack()
root.mainloop()
