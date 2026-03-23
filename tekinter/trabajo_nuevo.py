import tkinter as tk



def respuesta():
    try:
        num1 = float(ent_num1.get())
        num2 = float(ent_num2.get())
        suma = num1 + num2
        lbl_respuesta.config(text=f"El resultado: {suma:g}")
    except ValueError:
        lbl_respuesta.config(text="¡Solo se puede ingresar numeros!")
        

root = tk.Tk()
root.geometry("400x400")
etiqueta = tk.Label(root, text="SUMATORIA").pack()


lbl_num1 = tk.Label(root, text="Ingresa el primer numero").pack()
ent_num1 = tk.Entry(root)
ent_num1.pack()

lbl_num2 = tk.Label(root, text="Ingrese el segundo numero").pack()
ent_num2 = tk.Entry(root)
ent_num2.pack()


btn_respuesta = tk.Button(root, text="SUMAR", command=respuesta).pack()

lbl_respuesta = tk.Label(root)
lbl_respuesta.pack()

root.mainloop()