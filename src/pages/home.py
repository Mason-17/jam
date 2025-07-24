import flet as ft
from assets.nav_bar import nav_bar

def home_view(page: ft.Page):
    n = nav_bar(page)
    def go_to_settings(e):
        page.go("/settings")

    def go_to_albums(e):
        page.go("/albums")

    return ft.View(
        "/",
        controls=[
            ft.Text("Home Page", size=30),
            n,
        ],
    )
