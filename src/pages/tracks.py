import flet as ft
from assets.nav_bar import nav_bar

def tracks_view(page: ft.Page):
    nb = nav_bar(page)

    return ft.View(
        "/tracks",
        controls=[
            ft.ProgressBar(
                width=400,
                color=ft.Colors.INDIGO,
            ),
            nb
        ]
    )