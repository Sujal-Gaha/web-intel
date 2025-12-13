"""Agent factory."""

from typing import Dict, Callable

from web_intel.agents.base import BaseAgent
from web_intel.agents.ollama import OllamaAgent
from web_intel.core.config import Config


AgentConstructor = Callable[[Config], BaseAgent]


class AgentFactory:
    """Factory for creating agent instances."""

    _agents: Dict[str, AgentConstructor] = {
        "ollama": OllamaAgent,
    }

    @classmethod
    def create(
        cls,
        agent_type: str,
        config: Config,
    ) -> BaseAgent:
        """Create an agent instance."""
        agent_class = cls._agents.get(agent_type)

        if not agent_class:
            available = ", ".join(cls._agents.keys())
            raise ValueError(
                f"Unknown agent type: {agent_type}. " f"Available: {available}"
            )

        return agent_class(config)

    @classmethod
    def register(cls, name: str, agent_class: AgentConstructor) -> None:
        """Register a new agent implementation."""
        cls._agents[name] = agent_class

    @classmethod
    def list_available(cls) -> list[str]:
        """List all available agent types."""
        return list(cls._agents.keys())
