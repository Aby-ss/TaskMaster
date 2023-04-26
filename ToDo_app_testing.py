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


def modify_panel(panel: Panel, text: str, add_text: bool) -> Panel:
    if add_text:
        panel.body += text
    else:
        panel.body = panel.body.replace(text, '')
    return panel

my_panel = Panel("Hello, world!")
my_panel = modify_panel(my_panel, "world", False) # remove "world" from panel
my_panel = modify_panel(my_panel, "goodbye", True) # add "goodbye" to panel
