"""Main CLI application using Typer."""
import typer
from typing import Optional
from pathlib import Path

from web_intel.cli.commands import crawl, query
from web_intel.cli.ui.console import console
from web_intel.core.config import Config

app = typer.Typer(
    name="wi",
    help="🕷️ Intelligent web crawling and AI-powered querying",
    add_completion=False,
)

# Register command groups
app.add_typer(crawl.app, name="crawl")
app.add_typer(query.app, name="query")


@app.command()
def version():
    """Show version information."""
    console.print("web-intel version 0.1.0", style="bold green")


@app.callback()
def callback():
    """
    Web Intel Agent - Crawl websites and query content with AI.
    """
    pass
