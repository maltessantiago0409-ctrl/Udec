
from tkinter import *

window = Tk()

label = Label(window, text="Hola mundo", font=(("Aria",100,"bold")),fg="yellow")
label.pack()
label = Label(window, text="Hola mundo", font=(("Aria",100,"bold")),fg="blue")
label.pack()
label = Label(window, text="Hola mundo", font=(("Aria",100,"bold")),fg="red")
label.pack()
# label.place(x=60, y=100)

window.mainloop()
