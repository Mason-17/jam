import flet as ft

def PlayBar():
    control_bar = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.IconButton(icon=ft.Icons.PLAY_ARROW),
            ft.IconButton(icon=ft.Icons.SKIP_NEXT),
            ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS)
        ]
    )

    return ft.Container(
        content=ft.Card(
            content=control_bar,
            elevation=5,
        ),
        padding=ft.padding.symmetric(vertical=20, horizontal=15),
        margin=ft.Margin(0,0,0,20)
    )