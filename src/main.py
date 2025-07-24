import flet as ft
from pages.home import home_view
from pages.settings import settings_view
from pages.about import about_view
from pages.albums import albums_view
from assets.nav_bar import nav_bar
from pages.tracks import tracks_view
from pages.now_playing import now_playing_view

def main(page: ft.Page):
    page.title = "Jam Music"
    page.window.maximized = True
    page.window.icon="/assets/icon.ico"
    
    page.go("/")

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(home_view(page))
        elif page.route == "/settings":
            page.views.append(settings_view(page))
        elif page.route == "/about":
            page.views.append(about_view(page))
        elif page.route == "/albums":
            page.views.append(albums_view(page))
        elif page.route == "/tracks":
            page.views.append(tracks_view(page))
        elif page.route == "/now_playing":
            page.views.append(now_playing_view(page))
        else:
            page.views.append(
                ft.View(
                    "/404",
                    controls=[
                        ft.Text("404 - Page not found"),
                        ft.ElevatedButton("Go Home", on_click=lambda e: page.go("/"))
                    ],
                )
            )

        page.update()
    page.on_route_change = route_change

ft.app(
    target=main,
    assets_dir="assets",
    #icon="icon.ico"
    )
