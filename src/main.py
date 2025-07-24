import flet as ft
from assets import navi as navi
from assets import globals as Globals
from assets.pages.home import Home
from assets.pages.page2 import Page2
from assets.pages.page3 import Page3

#Globals = globals.Globals()
page_view_history = ["/","/2","/3"]
app_page_classes = []

def main(page: ft.Page):
    page.add(Home.gen_gallery)
    #page.update()


ft.app(target=main)