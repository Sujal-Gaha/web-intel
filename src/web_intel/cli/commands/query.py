from typing import Optional
import typer
from pathlib import Path

app = typer.Typer(help="Query crawled content")

@app.command("ask")
async def query_content(
    question: str = typer.Argument(...),
    source: Optional[Path] = typer.Option(None, "--source", "-s"),
    session: Optional[str] = typer.Option(None, "--session"),
):
    """Ask questions about crawled content"""
    pass

@app.command("interactive")
async def interactive_mode(source: Path):
    """Start interactive query session"""
    pass