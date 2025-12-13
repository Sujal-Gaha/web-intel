# Example: core/agent.py
from web_intel.core.config import Config
from web_intel.storage.base import BaseStorage


class Agent:
    def __init__(self, llm_client: BaseLLMClient, storage: BaseStorage, config: Config):
        self.llm = llm_client
        self.storage = storage
        self.config = config
