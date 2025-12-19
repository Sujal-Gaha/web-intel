"""Unit tests for factory classes."""

import pytest

from web_intel.agents.base import BaseAgent
from web_intel.agents.factory import AgentFactory
from web_intel.crawlers.base import BaseCrawler
from web_intel.crawlers.factory import CrawlerFactory
from web_intel.storage.base import BaseStorage
from web_intel.storage.factory import StorageFactory


class TestAgentFactory:
    """Tests for AgentFactory."""

    def test_create_ollama_agent(self, test_config) -> None:
        """Test creating Ollama agent."""
        agent: BaseAgent = AgentFactory.create("ollama", test_config)

        assert agent is not None
        assert agent.model == test_config.ollama_model

    def test_create_unknown_agent(self, test_config) -> None:
        """Test creating unknown agent type."""
        with pytest.raises(ValueError, match="Unknown agent type"):
            AgentFactory.create("nonexistent", test_config)

    def test_list_available_agents(self) -> None:
        """Test listing available agents."""
        available: list[str] = AgentFactory.list_available()

        assert "ollama" in available
        assert isinstance(available, list)


class TestCrawlerFactory:
    """Tests for CrawlerFactory."""

    def test_create_crawl4ai_crawler(self, test_config) -> None:
        """Test creating Crawl4AI crawler."""
        crawler: BaseCrawler = CrawlerFactory.create("crawl4ai", test_config)

        assert crawler is not None
        assert crawler.timeout == test_config.crawler_timeout

    def test_create_with_callback(self, test_config) -> None:
        """Test creating crawler with progress callback."""

        def callback(msg, current, total) -> None:
            print(msg, current, total)
            pass

        crawler: BaseCrawler = CrawlerFactory.create(
            "crawl4ai", test_config, progress_callback=callback
        )

        assert crawler.progress_callback == callback

    def test_list_available_crawlers(self) -> None:
        """Test listing available crawlers."""
        available: list[str] = CrawlerFactory.list_available()

        assert "crawl4ai" in available


class TestStorageFactory:
    """Tests for StorageFactory."""

    def test_create_file_storage(self, test_config) -> None:
        """Test creating file storage."""
        storage: BaseStorage = StorageFactory.create("file", test_config)

        assert storage is not None

    def test_list_available_storage(self) -> None:
        """Test listing available storage types."""
        available: list[str] = StorageFactory.list_available()

        assert "file" in available
