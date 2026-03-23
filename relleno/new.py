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




Button(pagina1,text="Ir a Matemáticas",
command=lambda: mostrar_pagina(pagina2)).pack(pady=20)

    puntaje = 0

    respuestas_correctas = {
        1: "6x",
        2: "7",
        3: "-cosx+c",
        4: "5",
        5: "5",
        6: "e^x+c",
        7: "15x^4",
        8: "25",
        9: "Solo en indifinidas",
        10: "Velocidad y tiempo"
    }

    def verificar(numero, spin):
        nonlocal puntaje

        seleccion = spin.get()

        if seleccion == respuestas_correctas[numero]:
            resultado.config(text="Correcto", fg="green")
            puntaje += 1
        else:
            resultado.config(text="Incorrecto", fg="red")

        respuesta_puntaje.config(text="Puntaje: " + str(puntaje))

    pregunta_1 = Label(pagina2, text="Cual es la derivada de 3x^2:")
    pregunta_1.place(x=10, y=10)

    spin_1 = Spinbox(pagina2, values=("3x^3/3", "6x", "6x^2"))
    spin_1.place(x=10, y=30)

    boton_1 = Button(pagina2, text="Enviar", command=lambda: verificar(1, spin_1))
    boton_1.place(x=10, y=50)

    pregunta_2 = Label(pagina2, text="Cual de los siguientes es numero primo:")
    pregunta_2.place(x=10, y=70)

    spin_2 = Spinbox(pagina2, values=("6", "15", "7"))
    spin_2.place(x=10, y=90)

    boton_2 = Button(pagina2, text="Enviar", command=lambda: verificar(2, spin_2))
    boton_2.place(x=10, y=110)

    pregunta_3 = Label(pagina2, text="Cual es la integral de sen(x):")
    pregunta_3.place(x=10, y=130)

    spin_3 = Spinbox(pagina2, values=("-cosx+c", "cosx+c", "-senx+c"))
    spin_3.place(x=10, y=150)

    boton_3 = Button(pagina2, text="Enviar", command=lambda: verificar(3, spin_3))
    boton_3.place(x=10, y=170)

    pregunta_4 = Label(pagina2, text="Si 2x = 10 cuanto vale x:")
    pregunta_4.place(x=10, y=190)

    spin_4 = Spinbox(pagina2, values=("10", "5", "8"))
    spin_4.place(x=10, y=210)

    boton_4 = Button(pagina2, text="Enviar", command=lambda: verificar(4, spin_4))
    boton_4.place(x=10, y=230)

    pregunta_5 = Label(pagina2, text="Media de 2,4,6,8:")
    pregunta_5.place(x=10, y=250)

    spin_5 = Spinbox(pagina2, values=("4", "6", "5"))
    spin_5.place(x=10, y=270)

    boton_5 = Button(pagina2, text="Enviar", command=lambda: verificar(5, spin_5))
    boton_5.place(x=10, y=290)

    pregunta_6 = Label(pagina2, text="Integral de e^x:")
    pregunta_6.place(x=10, y=310)

    spin_6 = Spinbox(pagina2, values=("e^x+c", "-e^x+c", "e^x^2/2+c"))
    spin_6.place(x=10, y=330)

    boton_6 = Button(pagina2, text="Enviar", command=lambda: verificar(6, spin_6))
    boton_6.place(x=10, y=350)

    pregunta_7 = Label(pagina2, text="Derivada de 3x^5:")
    pregunta_7.place(x=10, y=370)

    spin_7 = Spinbox(pagina2, values=("4x^6/6", "8x^5", "15x^4"))
    spin_7.place(x=10, y=390)

    boton_7 = Button(pagina2, text="Enviar", command=lambda: verificar(7, spin_7))
    boton_7.place(x=10, y=410)

    pregunta_8 = Label(pagina2, text="Lado de patio de 625m²:")
    pregunta_8.place(x=10, y=430)

    spin_8 = Spinbox(pagina2, values=("125", "625", "25"))
    spin_8.place(x=10, y=450)

    boton_8 = Button(pagina2, text="Enviar", command=lambda: verificar(8, spin_8))
    boton_8.place(x=10, y=470)

    pregunta_9 = Label(pagina2, text="Todas las integrales llevan constante?")
    pregunta_9.place(x=10, y=490)

    spin_9 = Spinbox(pagina2, values=("Si", "Solo en indifinidas", "No"))
    spin_9.place(x=10, y=510)

    boton_9 = Button(pagina2, text="Enviar", command=lambda: verificar(9, spin_9))
    boton_9.place(x=10, y=530)

    pregunta_10 = Label(pagina2, text="Para calcular tiempo se necesita:")
    pregunta_10.place(x=10, y=550)

    spin_10 = Spinbox(pagina2, values=("Velocidad y tiempo", "Tiempo y gravedad", "Frecuencia y velocidad"))
    spin_10.place(x=10, y=570)

    boton_10 = Button(pagina2, text="Enviar", command=lambda: verificar(10, spin_10))
    boton_10.place(x=10, y=590)

    resultado = Label(pagina2, text="")
    resultado.place(x=400, y=10)

    respuesta_puntaje = Label(pagina2, text="Puntaje: 0")
    respuesta_puntaje.place(x=400, y=40)

Button(root, text="Siguiente página", command=abrir_pagina2).pack(pady=15)


def abrir_pagina3():

    pagina2 = Toplevel(root)
    pagina2.geometry("800x800")

from tkinter import messagebox

# Función para calcular el IMC
def abrir_pagina3():

    pagina3 = Toplevel(root)
    pagina3.geometry("350x300")

    Label(pagina3, text="Calculadora de IMC").pack(pady=10)

    Label(pagina3, text="Peso (kg)").pack()
    spin_peso = Spinbox(pagina3, from_=30, to=200)
    spin_peso.pack()

    Label(pagina3, text="Altura (m)").pack()
    spin_altura = Spinbox(pagina3, from_=1.0, to=2.5, increment=0.01)
    spin_altura.pack()

    resultado = Label(pagina3)
    resultado.pack(pady=10)

    def calcular_imc():

        try:
            peso = float(spin_peso.get())
            altura = float(spin_altura.get())

            imc = peso / (altura ** 2)

            if imc < 18.5:
                estado = "Bajo peso"
            elif imc < 25:
                estado = "Normal"
            elif imc < 30:
                estado = "Sobrepeso"
            else:
                estado = "Obesidad"

            resultado.config(text=f"IMC: {imc:.2f}\nEstado: {estado}")

        except:
            messagebox.showerror("Error", "Ingrese valores válidos")

    Button(pagina3, text="Calcular IMC", command=calcular_imc).pack()


# BOTON PARA IR A PAGINA 2
Button(root, text="Siguiente página", command=abrir_pagina2).pack(pady=20)

root.mainloop()