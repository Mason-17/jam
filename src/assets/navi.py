import flet as ft

def route_dict(page, Globals, app_page_classes):
    home_page = app_page_classes[0]
    page1 = app_page_classes[1]
    page2 = app_page_classes[2]

    route_view_dict = {
        "/": ft.View(
            route="/",
            controls=[
                home_page.gen_nav_bar()
            ],
            vertical_alignment=ft.MainAxisAlignment.START,
            spacing=0
        ),
        "/2": ft.View(
            route="/2",
            controls=[
                page1.gen_nav_bar()
            ],
            
        ),
        "/3": ft.View(
            route="/3",
            controls=[
                page2.gen_nav_bar()
            ],
        ),
        "/albums": ft.View(
            route="/albums",
            controls=[
                
            ]
        )
    }

    return route_view_dict