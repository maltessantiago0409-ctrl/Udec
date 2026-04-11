import flet as ft
import random

def main(page: ft.Page):
    page.title = "Ruleta de nombres"
    page.horizontal_alignment = "center"

    nombres = []

    input_nombre = ft.TextField(label="Agregar nombre")
    lista_texto = ft.Text("Nombres: []")

    resultado = ft.Text(value="🎯 Ganador: ?", size=20, weight="bold")

    # Campo para forzar ganador
    forzar_nombre = ft.TextField(label="Forzar ganador (opcional)")

    def agregar_nombre(e):
        if input_nombre.value:
            nombres.append(input_nombre.value)
            input_nombre.value = ""
            lista_texto.value = f"Nombres: {nombres}"
            page.update()

    def girar_ruleta(e):
        if not nombres:
            resultado.value = "⚠️ Agrega nombres primero"
            page.update()
            return

        # 👇 Si se escribe un nombre aquí, se fuerza el resultado
        if forzar_nombre.value and forzar_nombre.value in nombres:
            ganador = forzar_nombre.value
        else:
            ganador = random.choice(nombres)

        resultado.value = f"🎉 Ganador: {ganador}"
        page.update()

    page.add(
        ft.Text("🎡 Ruleta de nombres", size=30, weight="bold"),
        input_nombre,
        ft.ElevatedButton("Agregar", on_click=agregar_nombre),
        lista_texto,
        ft.Divider(),
        forzar_nombre,
        ft.ElevatedButton("Girar ruleta", on_click=girar_ruleta),
        resultado
    )

ft.app(target=main)