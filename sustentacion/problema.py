import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("Cuestionarios")
root.geometry("900x650")

def mostrar(pagina):
    pagina.tkraise()

contenedor = tk.Frame(root)
contenedor.pack(fill="both", expand=True)

paginas = {}
for nombre in ["Spinbox","Radiobutton","Checkbutton","Select"]:
    frame = tk.Frame(contenedor)
    frame.pack(fill="both", expand=True)
    paginas[nombre] = frame

for frame in paginas.values():
    frame.place(relwidth=1,relheight=1)

menu = tk.Frame(root)
menu.pack()

tk.Button(menu,text="Spinbox",command=lambda:mostrar(paginas["Spinbox"])).pack(side="left",padx=5)
tk.Button(menu,text="Radiobutton",command=lambda:mostrar(paginas["Radiobutton"])).pack(side="left",padx=5)
tk.Button(menu,text="Checkbutton",command=lambda:mostrar(paginas["Checkbutton"])).pack(side="left",padx=5)
tk.Button(menu,text="Select",command=lambda:mostrar(paginas["Select"])).pack(side="left",padx=5)



def verificar_respuesta1():
    valor1 = spin1.get()

    if valor1 == "While True":
        etiqueta_resultado1.config(text="Correcto")
    else:
        etiqueta_resultado1.config(text="Incorrecto")

def verificar_respuesta2():
    valor2 = spin2.get()
    
    if valor2 == "-cosx+c":
        etiqueta_resultado2.config(text="Correcto")
    else:
        etiqueta_resultado2.config(text="Incorrecto")

def verificar_respuesta3():
    valor3 = spin3.get()

    if valor3 == "1914":
        etiqueta_resultado3.config(text="Correcto")
    else:
        etiqueta_resultado3.config(text="Incorrecto")

def verificar_respuesta4():
    valor4 = spin4.get()

    if valor4 == "2020":
        etiqueta_resultado11.config(text="Correcto")
    else:
        etiqueta_resultado11.config(text="Incorrecto")
        

lbl_texto1 = tk.Label(paginas["Spinbox"], text="¿Que siclo se utiliza para hacer un bucle infinito? ").pack(pady=1)

spin1 = tk.Spinbox(paginas["Spinbox"], values=("For True", "While True", "loop"))
spin1.pack(pady=3)

boton1 = tk.Button(paginas["Spinbox"], text="Respodner", command=verificar_respuesta1)
boton1.pack()

etiqueta_resultado1 = tk.Label(paginas["Spinbox"], text="")
etiqueta_resultado1.pack(pady=1)

#///

lbl_texto2 = tk.Label(paginas["Spinbox"], text="¿Integral de senx? ").pack(pady=1)

spin2 = tk.Spinbox(paginas["Spinbox"], values=("cosx+c", "-cosx+c", "-senx"))
spin2.pack(pady=3)

boton2 = tk.Button(paginas["Spinbox"], text="Responder", command=verificar_respuesta2)
boton2.pack()

etiqueta_resultado2 = tk.Label(paginas["Spinbox"], text="")
etiqueta_resultado2.pack(pady=1)

#///

lbl_texto3 = tk.Label(paginas["Spinbox"], text="¿En que año fue la Primera guerra mundial? ").pack(pady=1)

spin3 = tk.Spinbox(paginas["Spinbox"], values=("1939" ,"1914" ,"1920"))
spin3.pack(pady=3)

boton3 = tk.Button(paginas["Spinbox"], text="Responder", command=verificar_respuesta3)
boton3.pack()

etiqueta_resultado3 = tk.Label(paginas["Spinbox"], text="")
etiqueta_resultado3.pack(pady=1)


lbl_texto4 = tk.Label(paginas["Spinbox"], text="¿Que año es? ").pack(pady=1)

spin11 = tk.Spinbox(paginas["Spinbox"], values=("2000", "2020", "2026"))
spin11.pack(pady=3)

boton11 = tk.Button(paginas["Spinbox"], text="Responder", command=verificar_respuesta4)
boton11.pack()

etiqueta_resultado11 = tk.Label(paginas["Spinbox"], text="")
etiqueta_resultado11.pack(pady=1)

var1 = StringVar()

tk.Label(paginas["Radiobutton"], text="¿Que lenguaje usa Android Studio?").pack()
Radiobutton(paginas["Radiobutton"], text="Kotlin", variable=var1, value="Kotlin").pack()
Radiobutton(paginas["Radiobutton"], text="Python", variable=var1, value="Python").pack()
Radiobutton(paginas["Radiobutton"], text="C#", variable=var1, value="C#").pack()

resultado4 = tk.Label(paginas["Radiobutton"], text="")
resultado4.pack()

def revisar_radio1():
    if var1.get() == "Kotlin":
        resultado4.config(text="Correcto")
    else:
        resultado4.config(text="Incorrecto")

tk.Button(paginas["Radiobutton"], text="Responder", command=revisar_radio1).pack()

var2 = StringVar()

tk.Label(paginas["Radiobutton"], text="¿Cuanto es 5x5?").pack()
Radiobutton(paginas["Radiobutton"], text="10", variable=var2, value="10").pack()
Radiobutton(paginas["Radiobutton"], text="25", variable=var2, value="25").pack()
Radiobutton(paginas["Radiobutton"], text="20", variable=var2, value="20").pack()

resultado5 = tk.Label(paginas["Radiobutton"], text="")
resultado5.pack()

def revisar_radio2():
    if var2.get() == "25":
        resultado5.config(text="Correcto")
    else:
        resultado5.config(text="Incorrecto")

tk.Button(paginas["Radiobutton"], text="Responder", command=revisar_radio2).pack()

var3 = StringVar()

tk.Label(paginas["Radiobutton"], text="¿Capital de Francia?").pack()
Radiobutton(paginas["Radiobutton"], text="Madrid", variable=var3, value="Madrid").pack()
Radiobutton(paginas["Radiobutton"], text="Paris", variable=var3, value="Paris").pack()
Radiobutton(paginas["Radiobutton"], text="Roma", variable=var3, value="Roma").pack()

resultado6 = tk.Label(paginas["Radiobutton"], text="")
resultado6.pack()

def revisar_radio3():
    if var3.get() == "Paris":
        resultado6.config(text="Correcto")
    else:
        resultado6.config(text="Incorrecto")

tk.Button(paginas["Radiobutton"], text="Responder", command=revisar_radio3).pack()

var4 = spin4 = StringVar()

tk.Label(paginas["Radiobutton"], text="Que año es").pack()
Radiobutton(paginas["Radiobutton"   ], text="2000", variable=var4, value="2000").pack()
Radiobutton(paginas["Radiobutton"], text="2026", variable=var4, value="2026").pack()
Radiobutton(paginas["Radiobutton"], text="2020", variable=var4, value="2020").pack()

resultado11 = tk.Label(paginas["Radiobutton"], text="")
resultado11.pack()

var_check1 = IntVar()
var_check2 = IntVar()

tk.Label(paginas["Checkbutton"], text="Selecciona un lenguaje de programacion").pack()

Checkbutton(paginas["Checkbutton"], text="Python", variable=var_check1).pack()
Checkbutton(paginas["Checkbutton"], text="HTML", variable=var_check2).pack()

resultado7 = tk.Label(paginas["Checkbutton"], text="")
resultado7.pack()

def revisar_check1():
    if var_check1.get() == 1 and var_check2.get() == 0:
        resultado7.config(text="Correcto")
    else:
        resultado7.config(text="Incorrecto")

tk.Button(paginas["Checkbutton"], text="Responder", command=revisar_check1).pack()

var_check3 = IntVar()
var_check4 = IntVar()

tk.Label(paginas["Checkbutton"], text="Selecciona un planeta").pack()

Checkbutton(paginas["Checkbutton"], text="Marte", variable=var_check3).pack()
Checkbutton(paginas["Checkbutton"], text="Google", variable=var_check4).pack()

resultado8 = tk.Label(paginas["Checkbutton"], text="")
resultado8.pack()

def revisar_check2():
    if var_check3.get() == 1 and var_check4.get() == 0:
        resultado8.config(text="Correcto")
    else:
        resultado8.config(text="Incorrecto")

tk.Button(paginas["Checkbutton"], text="Responder", command=revisar_check2).pack()



var_select1 = StringVar()

tk.Label(paginas["Select"], text="¿Animal que vuela?").pack()
opciones1 = ["Perro","Aguila","Gato"]

menu1 = OptionMenu(paginas["Select"], var_select1, *opciones1)
menu1.pack()

resultado9 = tk.Label(paginas["Select"], text="")
resultado9.pack()

def revisar_select1():
    if var_select1.get() == "Aguila":
        resultado9.config(text="Correcto")
    else:
        resultado9.config(text="Incorrecto")

tk.Button(paginas["Select"], text="Responder", command=revisar_select1).pack()

var_select2 = StringVar()

tk.Label(paginas["Select"], text="¿Color del cielo?").pack()
opciones2 = ["Azul","Rojo","Verde"]

menu2 = OptionMenu(paginas["Select"], var_select2, *opciones2)
menu2.pack()

resultado10 = tk.Label(paginas["Select"], text="")
resultado10.pack()

def revisar_select2():
    if var_select2.get() == "Azul":
        resultado10.config(text="Correcto")
    else:
        resultado10.config(text="Incorrecto")

tk.Button(paginas["Select"], text="Responder", command=revisar_select2).pack()

mostrar(paginas["Spinbox"])

root.mainloop()