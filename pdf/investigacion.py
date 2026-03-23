from tkinter import *
root = Tk()
root.geometry("250x250")
texto1 = Label(root, text="Introduzca su nombre de usuario y contraseña. ").grid(row=0, column=0)

entrada1 = Entry(root, width=25)
entrada1.grid(row=1 ,column=0)

entrada2 = Entry(root, width=25, show="*")
entrada2.grid(row=2, column=0)

def clic_boton():
    texto = Label(root, text=f"Hola'{entrada1.get()}',inicio sesion correctamente").grid(row=1, column=0)

boton1 =  Button(root, text="Enviar", bg="red", padx=100, pady=15, command=clic_boton).grid(row=3, column=0)
root.mainloop()
