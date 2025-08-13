# nav_bar.py
import flet as ft

def bottom_nav_bar(page: ft.Page, selected_index: int = 0):
    def on_nav_change(e: ft.ControlEvent):
        index = e.control.selected_index
        route = ["/", "/albums", "/tracks"][index]
        # Instead of page.go(), we call switch manually
        page.session.set("nav_selected_index", index)
        page.session.set("nav_requested_route", route)
        page.pubsub.send_all("nav_switch")

    return ft.NavigationBar(
        selected_index=selected_index,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.Icons.ALBUM, label="Albums"),
            ft.NavigationDestination(icon=ft.Icons.MUSIC_NOTE, label="Tracks"),
        ],
    )
