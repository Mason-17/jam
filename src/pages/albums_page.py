import flet as ft
#from ..controls import Controls

def generate_card():
    return ft.Card(content=[
        ft.Text("CarD")
    ])

def AlbumsPage():
    num_containers = 12
    containers = []

    for _ in range(num_containers):
        container = ft.Container(
            ink=True,
            width=200,
            height=200,
            border_radius=8,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.SURFACE,
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
                top=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
                right=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
                bottom=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
            ),
            on_click=lambda e: print("clicked!!"),
            
            #content=ft.Image(src="../example_imgs/Cover.jpg",fit=ft.ImageFit.CONTAIN,border_radius=8,)
        )
        containers.append(container)

    return ft.GridView(
        expand=True,
        max_extent=200,
        child_aspect_ratio=1,
        spacing=15,
        run_spacing=15,
        controls=containers
    )
