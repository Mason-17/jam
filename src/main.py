import flet as ft
from pages.albums_page import AlbumsPage
from pages.songs_page import SongsPage
from pages.artists_page import ArtistsPage
from globals import Globals
from controls import Controls


def main(page: ft.Page):
    page.title = "Jam Music Player"
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 900
    page.window_height = 600
    page.window.maximized = True
    page.theme = Globals.dark_default
    print(Globals.music_dir)

    def close_di_open_picker():
        page.close(music_dir_dialog)
        file_dialog = ft.FilePicker()
        page.add(file_dialog)
        file_dialog.get_directory_path()

    music_dir_dialog = ft.AlertDialog(
        modal=True,
        title="No music folder",
        content=ft.Text("Pick a foler?"),
        actions=[
            ft.TextButton(text="Yes", on_click=lambda e: close_di_open_picker()),
            ft.TextButton(text="No", on_click=lambda e: page.close(music_dir_dialog))
        ]
    )
    page.add(music_dir_dialog)

    if Globals.music_dir == "":
        print("lets fix that")
        page.open(music_dir_dialog)

    active_page = "albums"
    sidebar_collapsed = False

    # Containers
    content_container = ft.Container(expand=True)

    nav_bar = ft.Container(
        #bgcolor=ft.Colors.GREY_200,
        padding=10,
        #content=nav_column
    )

    


    # Navigation handler
    def navigate(route):
        nonlocal active_page
        active_page = route
        if route == "albums":
            content_container.content = AlbumsPage()
        elif route == "songs":
            content_container.content = SongsPage()
        elif route == "artists":
            content_container.content = ArtistsPage()
        page.update()


    sidebar = ft.Column(
        controls=[
            ft.IconButton(icon=ft.Icons.ALBUM, on_click=lambda e: navigate("albums")),
            ft.IconButton(icon=ft.Icons.MUSIC_NOTE, on_click=lambda e: navigate("songs"))
        ]
    )

    # Layout structure
    main_layout = ft.Row(
        controls=[
            #nav_bar,
            sidebar,
            content_container
        ],
        expand=True
    )

    # Set default page content
    content_container.content = AlbumsPage()

    page.add(main_layout)


ft.app(target=main)
