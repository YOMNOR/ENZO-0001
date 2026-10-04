core/context.py
from typing import List, Dict, Any

class ShortTermContext:
    def __init__(self, max_messages: int = 50) -> None:
        self._messages: List[Dict[str, Any]] = []
        self.max_messages = max_messages

    def add_message(self, role: str, content: str) -> None:
        self._messages.append({"role": role, "content": content})
        if len(self._messages) > self.max_messages:
            self._messages.pop(0)

    def get_messages(self) -> List[Dict[str, Any]]:
        return list(self._messages)

    def reset(self) -> None:
        self._messages.clear()
