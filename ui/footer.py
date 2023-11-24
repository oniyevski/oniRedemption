from flet import *
from ui.colors import *


class Footer:
    def __init__(self, config):
        self.config = config
        self.logoText = Row(
            spacing=3,
            controls=[
                Container(
                    margin=margin.Margin(top=3, bottom=0, left=0, right=0),
                    content=Icon(
                        icons.HEART_BROKEN,
                        size=15,
                        color=REDEMPTION
                    )
                ),
                Text(
                    "developed by",
                    color=WHITE,
                    size=15,
                    weight=FontWeight.W_100),
                Text(
                    "oniyevski",
                    color=REDEMPTION,
                    size=15,
                    weight=FontWeight.BOLD
                )
            ]
        )
        self.footer = Container(
            alignment=alignment.center,
            content=Row(
                alignment="center",
                controls=[
                    self.logoText
                ]
            )
        )
