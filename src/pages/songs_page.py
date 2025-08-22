import flet as ft
    
def SongsPage():
    song_list = []
    for i in range(0,120):
        song_list.append(ft.FilledTonalButton(text=f"Song {i}"))

    return ft.ListView(
        #alignment=ft.MainAxisAlignment.START,
        spacing = 5,
        width=50,
        controls=song_list
    )