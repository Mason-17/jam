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

    control_bar = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        #expand=True,
        controls=[
            ft.IconButton(icon=ft.Icons.PLAY_ARROW)
        ],
    )

    bar_card = ft.Container(
        content=ft.Card(
            content=control_bar,
            elevation=5
        ),
        padding=ft.padding.symmetric(vertical=20,horizontal=15,),
        width=None,
        margin=ft.Margin(0,0,0,20)
    )

    def navrail_helper(i):
        if i == 0:
            navigate("home")
        elif i == 1:
            navigate("albums")
        elif i ==2:
            navigate("")
        #page.update()

    sidebar_p = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOUSE_OUTLINED,
                selected_icon=ft.Icons.HOUSE,
                
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ALBUM_OUTLINED,
                selected_icon=ft.Icons.ALBUM,
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.MUSIC_NOTE_OUTLINED,
                selected_icon=ft.Icons.MUSIC_NOTE
            )
        ],
        on_change=lambda e: navrail_helper(e.control.selected_index)
    )
    

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

    combiner = ft.Column(
        controls=[
            content_container,
            #control_bar
            bar_card
        ],
        expand=True
    )

    main_layout = ft.Row(
        controls=[
            sidebar,
            #sidebar_p,
            combiner
        ],
        expand=True
    )

    content_container.content=HomePage()
    page.add(main_layout)

ft.app(main)
