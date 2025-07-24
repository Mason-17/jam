import flet as ft

def about_view(page: ft.Page):
    return ft.View(
        "/about",
        controls=[
            ft.Text("About Page", size=30),
        ],
    )
