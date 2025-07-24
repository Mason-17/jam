import flet as ft

class Home:
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

    def gen_gallery(self):
        gallery = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )
        for i in range(0,60):
            gallery.controls.append(
                ft.Image(
                    src=f"https://picsum.photos/150/150?{i}",
                    fit=ft.ImageFit.NONE,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                )
        )