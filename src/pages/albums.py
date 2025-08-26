import flet as ft

def AlbumsPage():
    grid = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=160,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5
    )
    for _ in range (0,60):
        grid.controls.append(
            ft.IconButton(
                content=ft.Column(
                    controls=[
                        ft.Image(
                            "../examples/Cover.jpg",
                            fit=ft.ImageFit.COVER,
                            border_radius=8,
                            width=120,
                            height=120
                        ),
                        ft.Text("album ig",size=12,text_align="center",no_wrap=True)
                    ]
                ),
                #icon_size=160,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                padding=10,
                width=120,
                height=200
            )
        )
    return grid