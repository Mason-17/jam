import flet as ft

def now_playing_view(page: ft.Page):
    return ft.View(
        "/now_playing",
        controls=[
            ft.Container(
                content=ft.Image(
                    src="assets/Cover.png",
                    width=600,
                    height=600,
                    fit=ft.ImageFit.FILL
                ),
                border=ft.border.all(4, ft.colors.BLUE),
                border_radius=10,
                padding=4,
                margin=10,
                alignment=ft.alignment.center
            )
        ]

    )