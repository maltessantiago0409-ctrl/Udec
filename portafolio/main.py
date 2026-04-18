import flet as ft

class PortafolioWeb:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.title = "Mi Portafolio Profesional"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        
        # Colores
        self.page.bgcolor = "#1e1e1e"
        self.color_primaria = "black"
        self.color_secundaria = "black"
        
        self.build_ui()

    def build_ui(self):
        self.cambiar_modo = ft.IconButton(
            icon="dark_mode",
            bgcolor=self.color_primaria,
            icon_color="white",
            on_click=self.cambiar_modo_oscuro,
        )

        # SECCIONES (FRAMES)
        self.frame_inicio = ft.Container(
            expand=True,
            padding=20,
            visible=True,
            content=self.build_inicio(),
        )

        self.frame_servicio = ft.Container(
            expand=True,
            padding=20,
            visible=False,
            content=self.build_servicio(),
        )

        self.frame_resumen = ft.Container(
            expand=True,
            padding=20,
            visible=False,
            content=self.build_resumen(),
        )

        # LAYOUT PRINCIPAL
        layout = ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    padding=15,
                    bgcolor=self.color_secundaria,
                    content=ft.Row([
                        ft.Text("PORTAFOLIO", color="white", weight="bold", size=20),
                        ft.Row([
                            ft.TextButton("Inicio", on_click=lambda _: self.cambiar_pagina(0), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Servicios", on_click=lambda _: self.cambiar_pagina(1), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Resumen", on_click=lambda _: self.cambiar_pagina(2), style=ft.ButtonStyle(color="white")),
                        ]),
                  
                    ], alignment="spaceBetween")
                ),
                ft.Container(
                    expand=True,
                    content=ft.Stack([
                        self.frame_inicio,
                        self.frame_servicio,
                        self.frame_resumen,
                    ])
                )
            ]
        )
        self.page.add(layout)

    def build_inicio(self):
        return ft.ResponsiveRow([
            ft.Column([
                ft.Text("Hola, soy Edwin Santiago Maltes", size=45, weight="bold", color="white"),
                ft.Text("Soy un estudiante de la Universidad Ucundinamarca en formacion, responsable y puntual .", size=20, color="white"),
                ft.Text("Numero: 3052981801 .", size=20, color="white"),
                ft.Text("Correo: maltessantiago0409@gmail.com .", size=20, color="white"),
                ft.ElevatedButton("Ver servicios", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(1)),
                ft.ElevatedButton("Ver resumen", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(2))
            ], col={"md": 8}, alignment="center"),
            ft.Container(
                content=ft.Image(src="universidad.jpeg", border_radius=20, fit="cover"),
                col={"md": 3},
                height=300
                
            )
        ], vertical_alignment="center")

    def build_servicio(self):
        return ft.Column([
            ft.Text("Mis Servicios", size=35, weight="bold"),
            ft.ResponsiveRow([
                self.crear_tarjeta("Diseño Web", "html5.svg"),
                self.crear_tarjeta("Python Dev", "python.svg"),
                self.crear_tarjeta("Github", "git.jpeg"),
            ]),
            ft.ElevatedButton("Ver inicio", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(0)),
            ft.ElevatedButton("Ver resumen", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(2))
            
        ], scroll="auto")

    def build_resumen(self):
        return ft.Column([
            ft.Text("Mi Resumen", size=35, weight="bold",color="white"),
            ft.Row([
                ft.Image(src="python.svg", width=40,color="white"),
                ft.Text("Programación en Python", size=18,color="white")
            ]),
            ft.Row([
                ft.Image(src="POO.svg", width=45,color="white"),
                ft.Text("Programación Orientada a Objetos (POO)", size=18,color="white")
            ]),
            ft.Row([
                ft.Image(src="TKINTER.svg", width=40,color="white"),
                ft.Text("Interfaces gráficas con TkinterS", size=18,color="white")
            ]),
            ft.Row([
                ft.Image(src="github.png", width=45,color="white"),
                ft.Text("Control de versiones con Git", size=18,color="white")
            ]),

            ft.ElevatedButton("Ver inicio", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(0)),
            ft.ElevatedButton("Ver servicios", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(1))
        ], spacing=20)

    def crear_tarjeta(self, titulo, img_src):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=img_src, width=50, height=50),
                ft.Text(titulo, weight="bold")
            ], horizontal_alignment="center"),
            bgcolor="bluegrey50",
            padding=20,
            border_radius=10,
            col={"sm": 4}
        )

    def cambiar_pagina(self, index):
        self.frame_inicio.visible = (index == 0)
        self.frame_servicio.visible = (index == 1)
        self.frame_resumen.visible = (index == 2)
        self.page.update()

    def cambiar_modo_oscuro(self, e):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.cambiar_modo.icon = "dark_mode"
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.cambiar_modo.icon = "light_mode"
        self.page.update()

def main(page: ft.Page):
    PortafolioWeb(page)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")