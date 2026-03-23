from tkinter import *
root = Tk()

entrada = Entry(root, width=100, show="*")
entrada.grid(row=0, column=0)
entrada.insert(0, "Escriba aqui....")

def clik_boton():
    texto = Label(root, text="¡Se envio corretamente!").grid(row=1, column=0)

boton1 = Button(root, text="Enviar", bg="red",padx=100,pady=25, 
command = clik_boton).grid(row=2, column=0)

root.mainloop()
