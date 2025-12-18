"""Storage factory."""

from typing import Dict, Callable

from web_intel.models.crawl_result import CrawlResult
from web_intel.storage.base import BaseStorage
from web_intel.storage.file_storage import FileStorage
from web_intel.core.config import Config


# Define the storage constructor type
StorageConstructor = Callable[[Config], BaseStorage]


class StorageFactory:
    """Factory for creating storage instances."""

    _storage_types: Dict[str, StorageConstructor] = {
        "file": FileStorage,
    }

    @classmethod
    def create(
        cls,
        storage_type: str,
        config: Config,
    ) -> BaseStorage:
        """Create a storage instance."""
        storage_class: StorageConstructor | None = cls._storage_types.get(storage_type)

        if not storage_class:
            available: str = ", ".join(cls._storage_types.keys())
            raise ValueError(
                f"Unknown storage type: {storage_type}. " f"Available: {available}"
            )

        return storage_class(config)

    @classmethod
    def register(cls, name: str, storage_class: StorageConstructor) -> None:
        """Register a new storage implementation."""
        cls._storage_types[name] = storage_class

    @classmethod
    def list_available(cls) -> list[str]:
        """List all available storage types."""
        return list(cls._storage_types.keys())
