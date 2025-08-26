import flet as ft

def Test():
    return ft.Card(
        content=ft.Container(
            content=ft.Image(src="../examples/Cover.jpg"),
            margin=10,
            padding=10,
            #alignment=ft.alignment.center,
            width=150,
            height=150,
            border_radius=10,
            ink=True,
            on_click=lambda e: print("Clickable transparent with Ink clicked!"),
        ),
            
    )