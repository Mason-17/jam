import flet as ft

def home_view(page: ft.Page):
    def go_to_settings(e):
        page.go("/settings")

    def go_to_albums(e):
        page.go("/albums")

    return ft.View(
        "/",
        controls=[
            ft.Text("Home Page", size=30),
            ft.ElevatedButton("Go to Settings", on_click=go_to_settings),
            ft.ElevatedButton("Go to Albums", on_click=go_to_albums)
        ],
    )
