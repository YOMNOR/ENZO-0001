# ai/model.py
from typing import Protocol, List, Dict, Any

class AIModelProvider(Protocol):
    def send_message(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        ...

    def generate_response(self, prompt: str, context: List[Dict[str, Any]] | None = None) -> str:
        ...

    def reset_context(self) -> None:
        ...

# A simple local stub for development/testing
class LocalStubModel:
    def __init__(self) -> None:
        self._history: list[dict] = []

    def send_message(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        self._history.extend(messages)
        return {"status": "ok", "reply": "Stub: I received your message."}

    def generate_response(self, prompt: str, context: List[Dict[str, Any]] | None = None) -> str:
        return f"Stub response to: {prompt}"

    def reset_context(self) -> None:
        self._history.clear()
