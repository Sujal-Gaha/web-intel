from typing import Optional
import typer
from pathlib import Path

app = typer.Typer(help="Crawl websites")


@app.command("url")
async def crawl_url(
    url: str = typer.Argument(..., help="URL to crawl"),
    output: Optional[Path] = typer.Option(None, "--output", "-o"),
    depth: int = typer.Option(1, "--depth", "-d"),
):
    """Crawl a single URL"""
    pass
