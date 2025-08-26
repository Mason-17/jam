import flet as ft
from pages.albums import AlbumsPage
from pages.home import HomePage
from pages.settings import SettingsPage
from pages.test import Test


def main(page: ft.Page):
    #content = ft.View()

    content_container = ft.Container(expand=True)
    active_page = "albums"
    page.window.maximized=True
    

    def navigate(route):
        nonlocal active_page
        active_page = route

        if route == "home":
            content_container.content=HomePage()
        elif route == "albums":
            content_container.content=AlbumsPage()
        elif route == "settings":
            content_container.content=SettingsPage()
        elif route == "test":
            content_container.content=Test()

        page.update()

    sidebar = ft.Column(
        controls=[
            ft.IconButton(icon=ft.Icons.HOUSE,on_click=lambda e: navigate("home")),
            ft.IconButton(icon=ft.Icons.ALBUM,on_click=lambda e: navigate("albums")),
            ft.IconButton(icon=ft.Icons.MIC),
            ft.IconButton(icon=ft.Icons.MUSIC_NOTE),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.Icons.WARNING,on_click=lambda e: navigate("test")),
            ft.IconButton(icon=ft.Icons.SETTINGS,on_click=lambda e: navigate("settings"))
        ]
    )

    main_layout = ft.Row(
        controls=[
            sidebar,
            content_container
        ],
        expand=True
    )

    content_container.content=AlbumsPage()
    page.add(main_layout)

ft.app(main)
