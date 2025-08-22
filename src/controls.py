import userpaths
from globals import Globals
import flet as ft
from music_state import Music_State

class Controls:
    def play_pause(e):
        print("pressed")
        if Globals.playing == True:
            Music_State.pause()
        else: Music_State.play()

    music_folder_selector = ft.FilePicker()

    player_bar = ft.BottomAppBar(
        #shape=None,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS),
                ft.IconButton(icon=ft.Icons.PLAY_ARROW,on_click=play_pause),
                ft.IconButton(icon=ft.Icons.SKIP_NEXT),
            ]
        )
    )

    
    