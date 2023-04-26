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

def update_panel(panel_text: str, add_text: str = "", remove_text: str = "") -> Panel:
    """
    Updates the text of a Rich panel by adding or removing specified text.
    
    Args:
        panel_text (str): The current text of the panel.
        add_text (str, optional): The text to add to the panel. Defaults to "".
        remove_text (str, optional): The text to remove from the panel. Defaults to "".
        
    Returns:
        Panel: The updated panel with the modified text.
    """
    # Remove specified text from panel
    if remove_text:
        panel_text = panel_text.replace(remove_text, "")

    # Add specified text to panel
    if add_text:
        panel_text += add_text

    # Return updated panel
    return Panel(panel_text)

def update_panel_text(panel: Panel, text: str):
    """Updates a Rich panel's text and renders it to the console."""
    panel.text += f"\n{text}"
    print(panel)
    
    # Remove the added text after 5 seconds
    sleep(5)
    panel.text = panel.text.replace(f"\n{text}", "")
    print(panel)

# Example usage
panel = Panel("Original panel text")
update_panel_text(panel, "New text added to panel")