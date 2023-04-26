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


def update_panel_text(panel: Panel, text: str, add_text: bool = True):
    """
    Updates the text of a Rich panel by adding or removing some text.

    Args:
        panel (Panel): The Rich panel to update.
        text (str): The text to add or remove.
        add_text (bool, optional): Whether to add or remove the text. Defaults to True.

    Returns:
        Panel: The updated Rich panel.
    """
    if add_text:
        panel.update(f"{panel.renderable}\n{text}")
    else:
        panel_text = panel.renderable.split("\n")
        if text in panel_text:
            panel_text.remove(text)
        panel.update("\n".join(panel_text))
    return panel
