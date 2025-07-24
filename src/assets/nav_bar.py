import flet as ft

def nav_bar():
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.MUSIC_NOTE,label="TRACKS")
        ]
    )