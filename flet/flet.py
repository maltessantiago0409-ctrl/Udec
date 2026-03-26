import flet as ft

def main(page: ft.Page):
    page.title = "Mensaje"
    
    texto = ft.Text("No mano, el kawuañaki es el rey de los uribistas 😎")
    
    page.add(texto)

ft.app(target=main)