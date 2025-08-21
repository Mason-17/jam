import userpaths
import flet as ft

class Controls:
    music_folder_selector = ft.FilePicker(
        #initial_directory = userpaths.get_my_music()
    )

    player_bar = ft.BottomAppBar(
        #shape=None,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS),
                ft.IconButton(icon=ft.Icons.PLAY_ARROW,),
                ft.IconButton(icon=ft.Icons.SKIP_NEXT),
            ]
        )
    )

    