import tkinter as tk
import random

root = tk.Tk()
root.title("Cuestionarios")
root.geometry("900x650")



def mostrar(pagina):
    pagina.tkraise()

contenedor = tk.Frame(root)
contenedor.pack(fill="both", expand=True)

paginas = {}
for nombre in ["python","mate","historia","ambiental"]:
    frame = tk.Frame(contenedor)
    frame.pack(fill="both", expand=True)
    paginas[nombre] = frame

for frame in paginas.values():
    frame.place(relwidth=1,relheight=1)



menu = tk.Frame(root)
menu.pack()

tk.Button(menu,text="Python",command=lambda:mostrar(paginas["python"])).pack(side="left",padx=5)
tk.Button(menu,text="Matematicas",command=lambda:mostrar(paginas["mate"])).pack(side="left",padx=5)
tk.Button(menu,text="Historia",command=lambda:mostrar(paginas["historia"])).pack(side="left",padx=5)
tk.Button(menu,text="Ambiental",command=lambda:mostrar(paginas["ambiental"])).pack(side="left",padx=5)



def crear_cuestionario(frame,titulo,preguntas):

    tk.Label(frame,text=titulo,font=("Arial",20,"bold")).pack(pady=10)

    spinboxes=[]

    for p,opciones,correcta in preguntas:

        tk.Label(frame,text=p).pack()

        opciones=list(opciones)
        random.shuffle(opciones)

        spin=tk.Spinbox(frame,values=opciones,state="readonly")
        spin.pack(pady=3)

        spinboxes.append((spin,correcta))

    resultado=tk.Label(frame,text="")
    resultado.pack(pady=10)

    def revisar():
        puntos=0
        for spin,correcta in spinboxes:
            if spin.get()==correcta:
                puntos+=1

        resultado.config(text=f"Puntaje: {puntos}/10")

    tk.Button(frame,text="Enviar",command=revisar).pack(pady=10)



preg_python=[
("Funcion para imprimir:",("print()","echo()","log()"),"print()"),
("Lista en python:",("[]","{}","()"),"[]"),
("Crear funcion:",("def","func","create"),"def"),
("Tipo entero:",("int","str","bool"),"int"),
("Bucle infinito:",("while True","for True","loop"),"while True"),
("Potencia:",("**","//","^"),"**"),
("Extension python:",(".py",".pt",".java"),".py"),
("Terminar bucle:",("break","stop","exit"),"break"),
("Comentario:",("#","//","--"),"#"),
("Entrada usuario:",("input()","scan()","read()"),"input()")
]



preg_mate=[
("Derivada de 3x^2:",("6x","3x","6x^2"),"6x"),
("Numero primo:",("7","9","12"),"7"),
("Integral de senx:",("-cosx+c","cosx+c","-senx"),"-cosx+c"),
("2x=10 x vale:",("5","10","2"),"5"),
("Media 2,4,6,8:",("5","4","6"),"5"),
("Integral e^x:",("e^x+c","-e^x+c","e^x^2"),"e^x+c"),
("Derivada 3x^5:",("15x^4","8x^5","5x^3"),"15x^4"),
("5^2:",("25","10","15"),"25"),
("Constante integracion:",("Solo indefinidas","Siempre","Nunca"),"Solo indefinidas"),
("Tiempo se calcula con:",("velocidad y distancia","masa y fuerza","volumen y area"),"velocidad y distancia")
]



preg_historia=[
("En que año llego Cristobal Colon a america:",("1492","1500","1480"),"1492"),
("Quien fue el libertador de Colombia:",("Simon Bolivar","Napoleon","Hidalgo"),"Simon Bolivar"),
("¿Qué civilización construyó las pirámides de Giza?Piramides:",("Egipcios","Romanos","Griegos"),"Egipcios"),
("¿En qué año terminó la Segunda Guerra Mundial?:",("1945","1939","1950"),"1945"),
("¿Qué imperio gobernaba gran parte de Sudamérica antes de la llegada de los españoles?:",("Inca","Maya","Azteca"),"Inca"),
("El Muro de Berlin cayo:",("1989","1991","1975"),"1989"),
("En que año fue la Primera guerra mundial:",("1914","1939","1890"),"1914"),
("En que año fue la revolucion francesa:",("1789","1804","1700"),"1789"),
("El Imperio romano cayo en el año:",("476","600","350"),"476"),
("En que siglo Descubrimiento America:",("XV","XVI","XIV"),"XV")
]


preg_ambiental=[
("Gas principal calentamiento:",("CO2","Oxigeno","Helio"),"CO2"),
("Capa que protege UV:",("Ozono","Nitrogeno","CO2"),"Ozono"),
("Energia renovable:",("Solar","Carbon","Petroleo"),"Solar"),
("Deforestacion afecta:",("Biodiversidad","Internet","Electricidad"),"Biodiversidad"),
("Reciclaje reduce:",("Basura","Agua","Aire"),"Basura"),
("Gas respiramos:",("Oxigeno","CO2","Metano"),"Oxigeno"),
("Contaminacion agua afecta:",("Vida marina","Lunas","Sol"),"Vida marina"),
("Planeta con vida:",("Tierra","Marte","Venus"),"Tierra"),
("Recurso renovable:",("Viento","Gas","Carbon"),"Viento"),
("Calentamiento global causa:",("Cambio climatico","Mas hielo","Menos sol"),"Cambio climatico")
]


crear_cuestionario(paginas["python"],"Cuestionario Python",preg_python)
crear_cuestionario(paginas["mate"],"Cuestionario Matematicas",preg_mate)
crear_cuestionario(paginas["historia"],"Cuestionario Historia",preg_historia)
crear_cuestionario(paginas["ambiental"],"Cuestionario Ambiental",preg_ambiental)

mostrar(paginas["ambiental"])

root.mainloop()