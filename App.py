from rich import box
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.console import Console
from rich.live import Live

from rich.traceback import install
install(show_locals=True)

from datetime import datetime
import numpy as np

layout = Layout()
layout.split_column(
        Layout(name = "Header"),
        Layout(name = "Body"),
        Layout(name = "Footer")
        )

layout["Header"].size = 3
layout["Footer"].size = 3

layout["Body"].split_row(Layout(name = "To Do"), Layout(name = "In Progress"), Layout(name = "Done"), Layout(name = "Daily"))

class Header:
    def __rich__(self) -> Panel:
        header_grid = Table.grid(expand = True)
        header_grid.add_column(justify="left")
        header_grid.add_column(justify="center", ratio = 1)
        header_grid.add_column(justify="right")

        header_grid.add_row(
                "📑", "[bold]TaskMaster", datetime.now().ctime().replace(":", "[blink]:")
                )

        return Panel(header_grid, style = "white on black", box = box.SQUARE)

class Footer:
    def __rich__(self) -> Panel:
        footer_grid = Table.grid(expand = True)
        footer_grid.add_column(justify="left")
        footer_grid.add_column(justify="center")
        footer_grid.add_column(justify="right")

        footer_grid.add_row(
                "📈", "[bold]Quote", "✅"
                )

        return Panel(footer_grid, style = "white on black", box = box.SQUARE)

layout["Header"].update(Header())
layout["Footer"].update(Footer())

print(layout)
