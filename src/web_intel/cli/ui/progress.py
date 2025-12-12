from contextlib import contextmanager
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

@contextmanager
def show_progress():
    """Context manager for showing progress."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
    ) as progress:
        yield progress