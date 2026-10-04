# tools/registry.py
from typing import Dict, Callable, Any
from tools import calculator

class ToolSpec:
    def __init__(self, name: str, description: str, permission_level: int, func: Callable[..., Any]) -> None:
        self.name = name
        self.description = description
        self.permission_level = permission_level
        self.func = func

_registry: Dict[str, ToolSpec] = {}

def register_tool(spec: ToolSpec) -> None:
    _registry[spec.name] = spec

def get_tool(name: str) -> ToolSpec | None:
    return _registry.get(name)

# Register calculator at import time
register_tool(ToolSpec(
    name="calculator",
    description="Performs arithmetic calculations",
    permission_level=0,
    func=calculator.calculate_expression
))
