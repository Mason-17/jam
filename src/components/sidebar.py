import flet as ft

def SideBar(navigate_callback):
    return ft.Column(
        controls=[
            ft.IconButton(icon=ft.Icons.HOUSE,on_click=lambda e: navigate_callback("home")),
            ft.IconButton(icon=ft.Icons.ALBUM,on_click=lambda e: navigate_callback("albums")),
            ft.IconButton(icon=ft.Icons.MIC),
            ft.IconButton(icon=ft.Icons.MUSIC_NOTE),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.Icons.WARNING,on_click=lambda e: navigate_callback("test")),
            ft.IconButton(icon=ft.Icons.SETTINGS,on_click=lambda e: navigate_callback("settings"))
        ]
    )