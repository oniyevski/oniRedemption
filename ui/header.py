from flet import *
from ui.colors import *

class Functions:
    @staticmethod
    def minimazePage(element):
        element.page.window_minimized = True
        element.page.update()

    @staticmethod
    def closePage(element):
        element.page.window_destroy()

class Header:
    def __init__(self, config):
        self.config = config
        self.functions = Functions()

        self.logoText = Row(
            controls=[
                Text(
                    "oniRedemption",
                    color=REDEMPTION,
                    size=20,
                    weight=FontWeight.BOLD
                ),
                Text(
                    "v1.0",
                    color=WHITE,
                    size=20,
                    weight=FontWeight.BOLD
                )
            ]
        )
        self.menu = Row(
            controls=[
                IconButton(
                    icons.MINIMIZE_ROUNDED,
                    icon_color=WHITE,
                    on_click=self.functions.minimazePage
                ),
                IconButton(
                    icons.CLOSE,
                    icon_color=WHITE,
                    on_click=self.functions.closePage
                )
            ]
        )
        self.header = Container(
            alignment=alignment.center,
            content=Row(
                alignment="spaceBetween",
                controls=[
                    self.logoText,
                    self.menu
                ]
            )
        )
