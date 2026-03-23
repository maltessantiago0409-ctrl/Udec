import tkinter as tk

truco = False
texto_truco = ""
MSJ_DEFAULT = "Pedro, por favor responder a esta pregunta: ¿Cuál es tu pregunta?"

def respuesta():
    lbl_respuesta.config(text=texto_truco)

def enmascarar(event):
    global truco, texto_truco
    texto = ent_solicitud.get()

    # Reiniciar truco
    if(texto == ""):
        print("Truco desactivado")
        truco = False
        return

    # Activar truco
    if(not truco and texto[0] == "."):
        print("Truco activado")
        truco = True
    
    # Desactivar truco
    if(len(texto) > 1 and truco and event.char == "."):
        print("Truco desactivado")
        truco = False
    
    if truco:
        texto_truco += event.char
        tamanio = min(len(texto), len(MSJ_DEFAULT))
        ent_solicitud.delete(0,tk.END)
        ent_solicitud.insert(0,MSJ_DEFAULT[:tamanio])

# Ventana
root = tk.Tk()
root.geometry("400x400")

# Sección solicitud
lbl_solicitud = tk.Label(root, text="Ingrese una pregunta").pack()
ent_solicitud = tk.Entry(root)
ent_solicitud.pack()
ent_solicitud.bind("<KeyRelease>",enmascarar)

# Sección pregunta
lbl_pregunta = tk.Label(root, text="Ingrese una pregunta").pack()
ent_pregunta = tk.Entry(root).pack()

# Sección botón
btn_respuesta = tk.Button(root, text="Preguntar", command=respuesta).pack()

# Sección respuesta
lbl_respuesta = tk.Label(root)
lbl_respuesta.pack()

root.mainloop()
