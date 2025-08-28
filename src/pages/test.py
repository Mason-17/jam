import flet as ft

def Test():
    return ft.GridView(
        controls=[
            ft.Container(
                content=ft.Image(src="https://picsum.photos/200",border_radius=10),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=200,
                height=200,
                border_radius=10,
                ink=True,
                on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                expand=False,
            ),
        ],
        runs_count=6
            
    )