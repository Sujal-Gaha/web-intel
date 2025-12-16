"""Query-related data models."""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
from datetime import datetime


@dataclass
class QueryContext:
    """
    Context for a query.

    Contains the content to analyze and metadata about the query.
    """

    content: str
    """The main content to analyze (crawled website, document, etc.)"""

    metadata: Dict[str, Any] = field(default_factory=dict)
    """Additional metadata about the query"""

    max_tokens: int = 4000
    """Maximum tokens to use for context"""

    conversation_history: List[Dict[str, str]] = field(default_factory=list)
    """Previous messages in the conversation (for multi-turn dialogs)"""

    def __post_init__(self) -> None:
        """Validate fields after initialization."""
        if not self.content:
            raise ValueError("Content cannot be empty")
        if self.max_tokens <= 0:
            raise ValueError("max_tokens must be positive")


@dataclass
class QueryResult:
    """
    Result from an agent query.

    Contains the response and metadata about the generation.
    """

    response: str
    """The agent's response text"""

    metadata: Dict[str, Any] = field(default_factory=dict)
    """Additional metadata about the response"""

    model_used: str = "unknown"
    """Name/identifier of the model that generated the response"""

    tokens_used: Optional[int] = None
    """Number of tokens used in generation (if available)"""

    finish_reason: Optional[str] = None
    """Reason why generation finished (e.g., 'stop', 'length', 'error')"""

    timestamp: datetime = field(default_factory=datetime.now)
    """When this response was generated"""

    def __post_init__(self) -> None:
        """Validate fields after initialization."""
        if not self.response:
            raise ValueError("Response cannot be empty")

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary for serialization.

        Returns:
            Dict representation of the result
        """
        return {
            "response": self.response,
            "model_used": self.model_used,
            "tokens_used": self.tokens_used,
            "finish_reason": self.finish_reason,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "QueryResult":
        """
        Create QueryResult from dictionary.

        Args:
            data: Dictionary with result data

        Returns:
            QueryResult instance
        """
        return cls(
            response=data["response"],
            model_used=data.get("model_used", "unknown"),
            tokens_used=data.get("tokens_used"),
            finish_reason=data.get("finish_reason"),
            timestamp=(
                datetime.fromisoformat(data["timestamp"])
                if "timestamp" in data
                else datetime.now()
            ),
            metadata=data.get("metadata", {}),
        )


# Example usage:
"""
# Creating a query context
context = QueryContext(
    content="This is the crawled website content...",
    max_tokens=4000,
    conversation_history=[
        {"role": "user", "content": "What is this about?"},
        {"role": "assistant", "content": "This is about..."}
    ],
    metadata={
        "source_url": "https://example.com",
        "crawl_date": "2024-01-01"
    }
)

# Creating a query result
result = QueryResult(
    response="The website is about...",
    model_used="llama2",
    tokens_used=150,
    finish_reason="stop",
    metadata={
        "total_duration": 1234567,
        "prompt_eval_count": 50
    }
)

# Serialize to dict
result_dict = result.to_dict()

# Deserialize from dict
result_loaded = QueryResult.from_dict(result_dict)
"""
