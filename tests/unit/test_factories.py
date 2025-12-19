"""Unit tests for factory classes."""

import pytest

from web_intel.agents.factory import AgentFactory
from web_intel.crawlers.factory import CrawlerFactory
from web_intel.storage.factory import StorageFactory
from web_intel.core.config import Config


class TestAgentFactory:
    """Tests for AgentFactory."""

    def test_create_ollama_agent(self, test_config):
        """Test creating Ollama agent."""
        agent = AgentFactory.create("ollama", test_config)

        assert agent is not None
        assert agent.model == test_config.ollama_model

    def test_create_unknown_agent(self, test_config):
        """Test creating unknown agent type."""
        with pytest.raises(ValueError, match="Unknown agent type"):
            AgentFactory.create("nonexistent", test_config)

    def test_list_available_agents(self):
        """Test listing available agents."""
        available = AgentFactory.list_available()

        assert "ollama" in available
        assert isinstance(available, list)


class TestCrawlerFactory:
    """Tests for CrawlerFactory."""

    def test_create_crawl4ai_crawler(self, test_config):
        """Test creating Crawl4AI crawler."""
        crawler = CrawlerFactory.create("crawl4ai", test_config)

        assert crawler is not None
        assert crawler.timeout == test_config.crawler_timeout

    def test_create_with_callback(self, test_config):
        """Test creating crawler with progress callback."""

        def callback(msg, current, total):
            pass

        crawler = CrawlerFactory.create(
            "crawl4ai", test_config, progress_callback=callback
        )

        assert crawler.progress_callback == callback

    def test_list_available_crawlers(self):
        """Test listing available crawlers."""
        available = CrawlerFactory.list_available()

        assert "crawl4ai" in available


class TestStorageFactory:
    """Tests for StorageFactory."""

    def test_create_file_storage(self, test_config):
        """Test creating file storage."""
        storage = StorageFactory.create("file", test_config)

        assert storage is not None

    def test_list_available_storage(self):
        """Test listing available storage types."""
        available = StorageFactory.list_available()

        assert "file" in available
