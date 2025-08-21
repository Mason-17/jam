import flet as ft

def SongsPage(navigate_to_song=None):
    songs = [
        {"track": 1, "title": "Time", "artist": "Pink Floyd", "album": "The Dark Side of the Moon", "duration": "6:53"},
        {"track": 2, "title": "Come Together", "artist": "The Beatles", "album": "Abbey Road", "duration": "4:20"},
        {"track": 3, "title": "Billie Jean", "artist": "Michael Jackson", "album": "Thriller", "duration": "4:54"},
        {"track": 4, "title": "Back in Black", "artist": "AC/DC", "album": "Back in Black", "duration": "4:15"},
        {"track": 5, "title": "Dreams", "artist": "Fleetwood Mac", "album": "Rumours", "duration": "4:17"},
        {"track": 6, "title": "Hotel California", "artist": "Eagles", "album": "Hotel California", "duration": "6:30"},
    ]

    song_buttons = []

    for song in songs:
        btn = ft.OutlinedButton(
            content=ft.Row(
                [
                    ft.Text(str(song["track"]), width=30, text_align=ft.TextAlign.RIGHT),
                    ft.Text(song["title"], expand=True),
                    ft.Text(song["artist"], expand=True),
                    ft.Text(song["album"], expand=True),
                    ft.Text(song["duration"], width=50, text_align=ft.TextAlign.RIGHT),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10
            ),
            expand=True,
            on_click=lambda e, s=song: navigate_to_song(s) if navigate_to_song else print(f"Clicked: {s['title']} by {s['artist']}")
        )
        song_buttons.append(btn)

    return ft.ListView(
        expand=True,
        spacing=2,
        padding=5,
        auto_scroll=True,
        controls=song_buttons
    )
