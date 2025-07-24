import flet as ft
from assets.nav_bar import nav_bar

def albums_view(page: ft.Page):
    nb = nav_bar(page)
    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    for i in range(0,60):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    return ft.View(
        "/albums",
        controls=[
            ft.Text("album page"),
            images,
            nb
        ]

    )