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


def modify_panel(panel_text, add_text=None, remove_text=None):
    """
    Modifies text in a Rich panel.

    Args:
        panel_text (str): Existing text in the panel.
        add_text (str, optional): Text to be added to the panel. Defaults to None.
        remove_text (str, optional): Text to be removed from the panel. Defaults to None.

    Returns:
        str: Updated text in the panel.
    """
    # Convert input panel_text to a list for easy modification
    panel_text_list = panel_text.split('\n')
    
    if add_text:
        panel_text_list.append(add_text)
        
    if remove_text:
        panel_text_list.remove(remove_text)
    
    # Convert the modified list back to a string and return it
    return '\n'.join(panel_text_list)

# Define initial panel text
panel_text = "This is some text in a Rich panel.\nHere is another line of text.\nAnd a third line!"

# Create the initial panel with the text
panel = Panel(panel_text, title="My Panel")

# Display the panel
print(panel)

# Modify the panel by adding a line of text
panel_text = modify_panel(panel_text, add_text="Here is a new line of text!")
panel.update(panel_text)

# Display the modified panel
print(panel)

# Modify the panel by removing a line of text
panel_text = modify_panel(panel_text, remove_text="And a third line!")
panel.update(panel_text)

# Display the modified panel
print(panel)