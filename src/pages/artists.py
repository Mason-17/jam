import flet as ft

def ArtistsPage():

    grid = ft.GridView(
        spacing=5
    )

    for _ in range(25):
        grid.controls.append(
            ft.Container(
                content=ft.Image(
                    src="https://picsum.photos/200",
                ),
                ink=True
            )
        )

    return grid