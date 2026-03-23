import tkinter as tk

truco = False
truco_texto = ""

def responder():
    texto = entry_solicitud.get()
    lbl_respuesta.config(text=f"Respuesta a: {texto}")

def enmascarar(event):
    global truco
    solicitud = entry_solicitud.get()

    if solicitud == "":
        truco = False
        print("Truco desactivado")
        return

    if not truco and solicitud.startswith("."):
        print("Truco activado")
        truco = True

    if truco and event.char == "." and len(solicitud) > 1:
        truco = False
        print("Truco desactivado")

    if truco:
        mensaje = "Pedro porfavor responde"
        truco_texto = truco_texto
        entry_solicitud.delete(0, tk.END)
        entry_solicitud.insert(0, mensaje[:len(solicitud)])


root = tk.Tk()

tk.Label(root, text="Ingrese Su Solicitud:").pack()

entry_solicitud = tk.Entry(root, width=50)
entry_solicitud.pack()
entry_solicitud.bind("<KeyPress>", enmascarar)

tk.Label(root, text="Cual es tu pregunta?").pack()

entry_pregunta = tk.Entry(root, width=50)
entry_pregunta.pack()

tk.Button(root, text="Enviar Pregunta", command=responder).pack()

lbl_respuesta = tk.Label(root, text="Respuesta:")
lbl_respuesta.pack()

root.mainloop()