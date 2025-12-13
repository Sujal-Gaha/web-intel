"""Rich console wrapper."""

from rich.console import Console
from rich.theme import Theme

# Custom theme
custom_theme = Theme(
    {
        "info": "cyan",
        "warning": "yellow",
        "error": "bold red",
        "success": "bold green",
    }
)

# Global console instance
console = Console(theme=custom_theme)
