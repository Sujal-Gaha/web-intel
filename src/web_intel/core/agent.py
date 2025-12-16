from web_intel.agents.llm_client import BaseLLMClient
from web_intel.core.config import Config
from web_intel.storage.base import BaseStorage


class Agent:
    def __init__(
        self, llm_client: BaseLLMClient, storage: BaseStorage, config: Config
    ) -> None:
        self.llm: BaseLLMClient = llm_client
        self.storage: BaseStorage = storage
        self.config: Config = config
