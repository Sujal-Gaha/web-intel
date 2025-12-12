class WebIntelError(Exception):
    """Base exception"""
    pass

class CrawlerError(WebIntelError):
    """Crawler-related errors"""
    pass

class AgentError(WebIntelError):
    """Agent-related errors"""
    pass

class StorageError(WebIntelError):
    """Storage-related errors"""
    pass