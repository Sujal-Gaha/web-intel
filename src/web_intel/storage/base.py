# storage/base.py
from abc import ABC, abstractmethod

from web_intel.models.crawl_result import CrawlResult
from web_intel.models.session import Session


class BaseStorage(ABC):
    @abstractmethod
    async def save_crawl_result(self, result: CrawlResult) -> str:
        """Save crawl result and return ID"""
        pass
    
    @abstractmethod
    async def load_crawl_result(self, id: str) -> CrawlResult:
        """Load crawl result by ID"""
        pass
    
    @abstractmethod
    async def save_session(self, session: Session) -> None:
        pass
    
    @abstractmethod
    async def load_session(self, session_id: str) -> Session:
        pass