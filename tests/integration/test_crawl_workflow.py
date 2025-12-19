"""Integration tests for crawl workflow."""

import pytest
from pathlib import Path

from web_intel.core.config import Config
from web_intel.crawlers.factory import CrawlerFactory
from web_intel.storage.factory import StorageFactory


@pytest.mark.asyncio
class TestCrawlWorkflow:
    """Integration tests for complete crawl workflow."""

    async def test_complete_crawl_and_save(self, test_config, tmp_path):
        """Test complete crawl and save workflow."""
        # Setup
        test_config.storage_path = str(tmp_path)

        crawler = CrawlerFactory.create("crawl4ai", test_config)
        storage = StorageFactory.create("file", test_config)

        # Crawl (using a real simple page)
        result = await crawler.crawl("https://example.com", depth=1)

        # Verify crawl result
        assert result.success is True
        assert result.total_pages > 0
        assert len(result.pages) > 0

        # Save
        result_id = await storage.save_crawl_result(result, format="markdown")

        # Verify file exists
        expected_file = tmp_path / "crawls" / f"{result_id}.md"
        assert expected_file.exists()

        # Verify content
        content = expected_file.read_text()
        assert "example.com" in content.lower()
