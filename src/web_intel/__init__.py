"""Web Intel - Intelligent web crawling and AI-powered querying."""

__version__ = "0.1.0"

# Expose main components at package level
from web_intel.core.config import Config
from web_intel.agents.factory import AgentFactory
from web_intel.crawlers.factory import CrawlerFactory
from web_intel.storage.factory import StorageFactory
from web_intel.core.orchestrator import AgentOrchestrator

__all__ = [
    "Config",
    "AgentFactory",
    "CrawlerFactory",
    "StorageFactory",
    "AgentOrchestrator",
]


# src/web_intel/models/__init__.py
"""Data models for web_intel."""

from web_intel.models.query import QueryContext, QueryResult
from web_intel.models.session import Session, Message
from web_intel.models.crawl_result import CrawlResult, PageResult

__all__ = [
    "QueryContext",
    "QueryResult",
    "Session",
    "Message",
    "CrawlResult",
    "PageResult",
]


# src/web_intel/agents/__init__.py
"""AI agent implementations."""

from web_intel.agents.base import BaseAgent
from web_intel.agents.ollama import OllamaAgent
from web_intel.agents.factory import AgentFactory

__all__ = [
    "BaseAgent",
    "OllamaAgent",
    "AgentFactory",
]


# src/web_intel/crawlers/__init__.py
"""Web crawler implementations."""

from web_intel.crawlers.base import BaseCrawler
from web_intel.crawlers.crawl4ai import Crawl4AICrawler
from web_intel.crawlers.factory import CrawlerFactory

__all__ = [
    "BaseCrawler",
    "Crawl4AICrawler",
    "CrawlerFactory",
]


# src/web_intel/storage/__init__.py
"""Storage implementations."""

from web_intel.storage.base import BaseStorage
from web_intel.storage.file_storage import FileStorage
from web_intel.storage.factory import StorageFactory

__all__ = [
    "BaseStorage",
    "FileStorage",
    "StorageFactory",
]


# src/web_intel/utils/__init__.py
"""Utility functions and exceptions."""

from web_intel.utils.exceptions import (
    WebIntelError,
    CrawlerError,
    AgentError,
    StorageError,
    ValidationError,
)

__all__ = [
    "WebIntelError",
    "CrawlerError",
    "AgentError",
    "StorageError",
    "ValidationError",
]


# src/web_intel/core/__init__.py
"""Core components."""

from web_intel.core.config import Config
from web_intel.core.orchestrator import AgentOrchestrator

__all__ = [
    "Config",
    "AgentOrchestrator",
]


# src/web_intel/cli/__init__.py
"""CLI components."""

from web_intel.cli.app import app

__all__ = [
    "app",
]


# src/web_intel/cli/commands/__init__.py
"""CLI commands."""

# This file can be empty or import commands
# The commands are registered in app.py


# src/web_intel/cli/ui/__init__.py
"""CLI UI components."""

from web_intel.cli.ui.console import console
from web_intel.cli.ui.progress import show_progress

__all__ = [
    "console",
    "show_progress",
]
