import flet as ft

def settings_view(page: ft.Page):
    def go_home(e):
        page.go("/")

    return ft.View(
        "/settings",
        controls=[
            ft.Text("Settings Page", size=30),
            ft.ElevatedButton("Back to Home", on_click=go_home),
        ],
    )
