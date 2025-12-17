from typing import Optional
import typer
from typer import Typer
from pathlib import Path
import asyncio

from web_intel.cli.ui.console import console
from web_intel.core.config import Config
from web_intel.crawlers.base import BaseCrawler
from web_intel.crawlers.factory import CrawlerFactory
from web_intel.models.crawl_result import CrawlResult
from web_intel.storage.base import BaseStorage
from web_intel.storage.factory import StorageFactory
from web_intel.utils.exceptions import CrawlerError, StorageError

app: Typer = typer.Typer(help="Crawl websites")


@app.command("url")
def crawl_url(
    url: str = typer.Argument(..., help="URL to crawl"),
    output: Optional[Path] = typer.Option(None, "--output", "-o"),
    depth: int = typer.Option(1, "--depth", "-d"),
) -> None:
    """Crawl a single URL"""
    asyncio.run(_crawl_url(url, output, depth))


async def _crawl_url(
    url: str = typer.Argument(..., help="URL to crawl"),
    output: Optional[Path] = typer.Option(None, "--output", "-o"),
    depth: int = typer.Option(1, "--depth", "-d"),
) -> None:
    try:
        """Async implementatl of crawl_url"""
        config: Config = Config()

        crawler: BaseCrawler = CrawlerFactory.create("crawl4ai", config)
        storage: BaseStorage = StorageFactory.create(config.storage_type, config)

        crawl_res: CrawlResult = await crawler.crawl(url)

        print(f"Crawl Result {crawl_res}")

    except StorageError as e:
        console.print(f"[red]Storage error: [/red] {e}")
        raise typer.Exit(1)
    except CrawlerError as e:
        console.print(f"[red]Crawler error:[/red] {e}")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")
        console.print_exception()
        raise typer.Exit(1)
