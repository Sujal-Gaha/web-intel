from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Dict


class BaseLLMClient(ABC):
    """Abstract base for all LLM providers."""

    @abstractmethod
    async def generate() -> Dict[str, Any]:
        """Non-streaming generation"""

    @abstractmethod
    async def stream_generate() -> AsyncIterator[str]:
        """Streaming generation"""

    @abstractmethod
    async def validate_connection() -> bool:
        """Check if service is accessible"""

    @abstractmethod
    def get_model_info() -> Dict[str, Any]:
        """Get model information"""
