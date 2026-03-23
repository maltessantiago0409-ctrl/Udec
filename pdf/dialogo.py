import tkinter as tk
from tkinter import *
from tkinter.messagebox import *

root = tk.Tk()
root.geometry("250x300")

root.title("Este es el titulo de la ventana principal")
root.iconbitmap(r'C:\Users\Edwin Santiago\OneDrive\Documentos\programacion 2\pdf\IMG\perico.ico')

def muestra_ventana():
    showwarning("Aqui va el titulo de cuadro de dialogo", "¡Un petrista entro en el sistema!")

boton1 = Button(root, text="Enviar", command=muestra_ventana,width=75).pack()

root.mainloop()