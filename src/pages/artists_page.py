import flet as ft

def ArtistsPage():
    return ft.Container(
        content=ft.Column([
            ft.Text("Artists", size=32, weight="bold"),
            ft.Text("List of artists will appear here...")
        ], spacing=20, expand=True),
        padding=20
    )
