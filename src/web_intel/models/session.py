from dataclasses import dataclass
from typing import Any, Dict, List, Optional

@dataclass
class Message:
    role: str
    content: str

class Session:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.messages: List[Message] = []
        self.context: Optional[str] = None
        self.metadata: Dict[str, Any] = {}
    
    def add_message(self, role: str, content: str):
        self.messages.append(Message(role=role, content=content))
    
    def get_context_window(self, max_tokens: int) -> List[Message]:
        # Return messages that fit within token limit
        return []