import flet as ft

def nav_bar(page: ft.Page):
    def on_nav_change(e):
        selected_index=e.control.selected_index
        if selected_index==0:
            page.go("/")
        elif selected_index==1:
            page.go("/tracks")
        elif selected_index==2:
            page.go("/albums")

    route_to_index={"/":0,"/albums":1,}
    current_index=route_to_index.get(page.route,0)
    return ft.NavigationBar(
        selected_index=current_index,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.PLAY_ARROW,label="HOME"),
            ft.NavigationBarDestination(icon=ft.Icons.MUSIC_NOTE,label="TRACKS"),
            ft.NavigationBarDestination(icon=ft.Icons.ALBUM,label="ALBUMS")
        ]
    )