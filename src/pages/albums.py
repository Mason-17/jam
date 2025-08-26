import flet as ft

def AlbumsPage():
    grid = ft.GridView(
        runs_count=5,
        run_spacing=5,
        spacing=5,
        child_aspect_ratio=.9
    )

    for _ in range(30):
        grid.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Image(
                            src="../examples/Cover.jpg",
                            border_radius=10,
                            #width=200,
                            #height=200
                        ),
                        ft.Text(
                            "albumfaljdlkjaajfjfj928982j9j2f982j98j29jf92jf",
                            text_align="center",
                            overflow=ft.TextOverflow.ELLIPSIS,
                            no_wrap=True
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=3
                ),
                ink=True,
                padding=4,
                margin=4,
                border_radius=10,
                on_click=lambda e: print("clicked1"),
            )
        )

    return grid