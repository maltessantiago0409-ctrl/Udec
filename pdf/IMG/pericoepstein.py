import tkinter as tk
from tkinter import *
import os
import sys

# Esto encuentra la carpeta donde está guardado este archivo .py
base_path = os.path.dirname(os.path.abspath(__file__))
# Une esa carpeta con el nombre del icono
ruta_icono = os.path.join(base_path, "perico.ico")

root = tk.Tk()
root.geometry("350x250")
root.title("Este es el codigo mas uribista de colombia")

# Ahora usa la ruta dinámica
try:
    root.iconbitmap(ruta_icono)
except:
    print("No se encontró el icono, pero el programa seguirá corriendo.")

root.mainloop()