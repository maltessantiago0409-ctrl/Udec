import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("350x100")

titulo1 = Label(root, text="Este es el primer texto").pack(anchor=NW)
titulo2 = Label(root, text="Segundo").pack(anchor=NW)
titulo3 = Label(root, text="Tercer Texto").pack(anchor=NW)
titulo4 = Label(root, text="Este es el cuarto, ultimo texto y el mas largo de todos").pack(anchor=NW)

root.mainloop()