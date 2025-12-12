"""Data models for crawl results."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime


@dataclass
class PageResult:
    """Result from a single crawled page."""
    url: str
    content: str
    title: Optional[str] = None
    status_code: Optional[int] = None
    crawled_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CrawlResult:
    """Complete crawl operation result."""
    source_url: str
    pages: List[PageResult]
    success: bool
    total_pages: int
    failed_pages: int = 0
    crawl_depth: int = 1
    started_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def combined_content(self) -> str:
        """Get all page content combined."""
        return "\n\n".join([
            f"--- From: {page.url} ---\n{page.content}"
            for page in self.pages
        ])
    
    @property
    def all_urls(self) -> List[str]:
        """Get list of all crawled URLs."""
        return [page.url for page in self.pages]
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate."""
        if self.total_pages == 0:
            return 0.0
        return (self.total_pages - self.failed_pages) / self.total_pages
