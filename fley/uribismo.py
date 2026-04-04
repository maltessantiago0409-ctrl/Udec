import flet as ft

def main(page: ft.Page):
    page.title = "Mensaje"
    
    texto = ft.Text("No mundo")
    
    page.add(texto)

ft.app(target=main)