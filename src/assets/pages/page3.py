import flet as ft

class Page3:
    def __init__(self, page, Globals):
        self.page = page
        self.Globals = Globals

    def gen_nav_bar(self):
        home = ft.ElevatedButton(text="Home",on_click=lambda _: self.page.go("/"))
        b2 = ft.ElevatedButton(
            text="page2",
            on_click=lambda _: self.page.go("/2")
        )
        b3 = ft.ElevatedButton(
            text="3",
            on_click=lambda _: self.page.go("/3")
        )
        nav_row = ft.Row(
            controls=[
                home,
                b2,
                b3
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        return nav_row