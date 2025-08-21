import flet as ft

def AlbumsPage():
    num_containers = 12
    containers = []

    for _ in range(num_containers):
        container = ft.Container(
            width=180,
            height=180,
            border_radius=8,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.SURFACE,
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
                top=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
                right=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
                bottom=ft.BorderSide(1, ft.Colors.ON_SURFACE_VARIANT),
            )
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
