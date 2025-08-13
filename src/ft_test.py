import flet as ft
import FleetingViews

def main(page:ft.Page):
    appbar = ft.AppBar(
        ft.IconButton(icon=ft.Icons.HOME),
        ft.IconButton()
    )

    view_definitions={}

    fv=FleetingViews.create_views(view_definitions=view_definitions,page=page)
    
    fv.on_view_change=my_callback_hook