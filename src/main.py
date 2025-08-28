import flet as ft
from pages.albums import AlbumsPage
from pages.artists import ArtistsPage
from pages.home import HomePage
from pages.settings import SettingsPage
from pages.test import Test

from components.playbar import PlayBar
from components.sidebar import SideBar

PAGES = {
    "home": HomePage,
    "albums": AlbumsPage,
    "artists": ArtistsPage,
    "settings": SettingsPage,
    "test": Test
}

def main(page: ft.Page):
    page.window.maximized=True
    page.title = "Jam"

    content_container = ft.Container(expand=True)

    def navigate(route):
        if route in PAGES:
            content_container.content=PAGES[route]()
        page.update()

    sidebar = SideBar(navigate)
    bottom_bar = PlayBar()

    main_layout = ft.Row(
        controls=[
            sidebar,
            
            ft.Column(
                controls=[
                    content_container,
                    bottom_bar
                ],
                expand=True
            )
        ],
        expand=True
    )

    content_container.content=HomePage()
    page.add(main_layout)

ft.app(main)
