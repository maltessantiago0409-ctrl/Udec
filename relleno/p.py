import tkinter as tk
from tkinter import*

root = tk.Tk()
root.title("Ejemplo spinbox")
root.geometry("300x250")

# -------- CAMBIAR PAGINA --------
def mostrar_pagina(pagina):
    pagina.tkraise()

# -------- CONTENEDOR --------
contenedor = Frame(root)
contenedor.pack(fill="both", expand=True)

pagina1 = Frame(contenedor)
pagina2 = Frame(contenedor)
pagina3 = Frame(contenedor)

for pagina in (pagina1, pagina2, pagina3):
    pagina.grid(row=0, column=0, sticky="nsew")

# =========================
# PAGINA 1 (HISTORIA)
# =========================

def verificar_respuesta1():
    valor1 = spin1.get()

    if valor1 == "1492":
        etiqueta_resultado1.config(text="¡Correto!")
    else:
        etiqueta_resultado1.config(text="¡Incorrecto!")

def verificar_respuesta2():
    valor2 = spin2.get()

    if valor2 == "Agusto Cesar":
        etiqueta_resultado2.config(text="¡Correcto!")
    else:
        etiqueta_resultado2.config(text="Incorrecto :(")

def verificar_respuesta3():
    valor3 = spin3.get()

    if valor3 == "Egipcios":
        etiqueta_resultado3.config(text="¡Correcto!")
    else:
        etiqueta_resultado3.config(text="¡Incorrecto!")

def verificar_respuesta4():
    valor4 = spin4.get()

    if valor4 == "1945":
        etiqueta_resultado4.config(text="¡Correcto!")
    else:
        etiqueta_resultado4.config(text="¡Incorrecto!")

def verificar_respuesta5():
    valor5 = spin5.get()

    if valor5 == "Imperio Inca":
        etiqueta_resultado5.config(text="¡Correcto!")
    else:
        etiqueta_resultado5.config(text="¡Incorrecto!")

def verificar_respuesta6():
    valor6 = spin6.get()

    if valor6 == "Simon Bolivar":
        etiqueta_resultado6.config(text="¡Correcto!")
    else:
        etiqueta_resultado6.config(text="¡Incorrecto!")
def verificar_respuest7():
    valor7 = spin7.get()

    if valor7 == "Europa":
        etiqueta_resultado7.config(text="¡Correcto!")
    else:
        etiqueta_resultado7.config(text="¡Incorrecto!")


lbl_texto1 = tk.Label(root, text="¿En qué año llegó Cristóbal Colón a América?").pack(pady=3)

spin1 = tk.Spinbox(root, values = ("1498", "1492", "1502"))
spin1.pack(pady=2.5)

boton1 = tk.Button(root, text="Respodenr", command=verificar_respuesta1)
boton1.pack()

etiqueta_resultado1 = tk.Label(root, text="")
etiqueta_resultado1.pack(pady=6)

#///

lbl_texto2 = tk.Label(root, text="¿Quién fue el primer emperador de Roma?").pack(pady=3)

spin2 = tk.Spinbox(root, values = ("Carlos Mario " ,"Agusto Cesar", "Julio Cesar"))
spin2.pack(pady=2.5)

boton2 = tk.Button(root,text="Responder", command=verificar_respuesta2)
boton2.pack()

etiqueta_resultado2 = tk.Label(root, text="")
etiqueta_resultado2.pack(pady=6)

#///

lbl_texto3 = tk.Label(root, text="¿Qué civilización construyó las pirámides de Giza?").pack(pady=3)

spin3 = tk.Spinbox(root, values =("Romanos", "Egipcios", "Griegos"))
spin3.pack(pady=2.5)

boton3 = tk.Button(root, text="Responder", command=verificar_respuesta3)
boton3.pack()

etiqueta_resultado3 = tk.Label(root, text="")
etiqueta_resultado3.pack(pady=6)

#///

lbl_texto4 = tk.Label(root, text="¿En qué año terminó la Segunda Guerra Mundial?").pack(pady=3)

spin4 = tk.Spinbox(root, values = ("1945", "1939", "1950"))
spin4.pack(pady=2.5)

boton4 = tk.Button(root, text="Responder", command=verificar_respuesta4)
boton4.pack()

etiqueta_resultado4 = tk.Label(root, text="")
etiqueta_resultado4.pack(pady=6)

#///

lbl_texto5 = tk.Label(root, text="¿Qué imperio gobernaba gran parte de Sudamérica antes de la llegada de los españoles?").pack(pady=3)

spin5 = tk.Spinbox(root, values=("Imperio Maya", "Imperio Azteca", "Imperio Inca"))
spin5.pack(pady=2.5)

boton5 = tk.Button(root, text="Responder", command=verificar_respuesta5)
boton5.pack()

etiqueta_resultado5 = tk.Label(root, text="")
etiqueta_resultado5.pack(pady=6)

#///

lbl_texto6 = tk.Label(root, text="¿Quién lideró la independencia de Colombia?").pack(pady=3)

spin6 = tk.Spinbox(root, values=("Napoleón Bonaparte", "Simon Bolivar", "Miguel Hidalgo"))
spin6.pack(pady=2.5)

boton6 = tk.Button(root, text="Responder", command=verificar_respuesta6)
boton6.pack()

etiqueta_resultado6 = tk.Label(root, text="")
etiqueta_resultado6.pack(pady=6)

#///

lbl_texto7 = tk.Label(root, text="¿En qué continente se originó la civilización griega?").pack(pady=3)

spin7 = tk.Spinbox(root, values=("Asia", "Europa", "Africa"))
spin7.pack(pady=2.5)

boton7 = tk.Button(root, text="Responder", command=verificar_respuest7)
boton7.pack()

etiqueta_resultado7 = tk.Label(root, text="")
etiqueta_resultado7.pack(pady=6)

root.mainloop()