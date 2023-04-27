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

def remove_tasks(panelname, removed_task):
    remove_task_panel = Panel(title = panelname, subititle = "✅", box = box.SQUARE, border_style = "bold white")
    
    return remove_task_panel