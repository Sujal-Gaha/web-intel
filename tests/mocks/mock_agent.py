"""Mock agent for testing."""

from typing import AsyncIterator

from web_intel.agents.base import BaseAgent
from web_intel.models.query import QueryContext, QueryResult


class MockAgent(BaseAgent):
    """Mock agent that returns predictable responses."""

    def __init__(self, config=None):
        self.config = config
        self.query_count = 0

    async def query(self, prompt: str, context: QueryContext, **kwargs) -> QueryResult:
        """Return a mock response."""
        self.query_count += 1

        return QueryResult(
            response=f"Mock response to: {prompt}",
            model_used="mock-model",
            tokens_used=len(prompt.split()),
            finish_reason="stop",
            metadata={"mock": True},
        )

    async def stream_query(
        self, prompt: str, context: QueryContext, **kwargs
    ) -> AsyncIterator[str]:
        """Stream a mock response."""
        words = f"Mock response to: {prompt}".split()
        for word in words:
            yield word + " "

    def prepare_context(self, content: str, max_tokens: int) -> str:
        """Return truncated content."""
        return content[: max_tokens * 4]

    async def validate_connection(self) -> bool:
        """Always return True for mock."""
        return True
