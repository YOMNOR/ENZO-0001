tools/calculator.py
from typing import Dict, Any
import re

def calculate_expression(expr: str) -> Dict[str, Any]:
    # Very small, safe parser: allow digits, whitespace, + - * / ( ) and decimals
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
        return {"ok": False, "error": "Invalid characters in expression."}
    try:
        # Evaluate in a restricted namespace
        result = eval(expr, {"__builtins__": None}, {})
        return {"ok": True, "result": result}
    except Exception as e:
        return {"ok": False, "error": str(e)}
