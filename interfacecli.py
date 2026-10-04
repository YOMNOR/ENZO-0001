# interface/cli.py
from core.context import ShortTermContext
from ai.model import LocalStubModel
from tools.registry import get_tool
from config.settings import settings

ctx = ShortTermContext()
model = LocalStubModel()

SPECIAL_COMMANDS = {"/help", "/status", "/reset", "/tools", "/memory", "/exit"}

def handle_special(cmd: str) -> bool:
    if cmd == "/help":
        print("Special commands:", ", ".join(sorted(SPECIAL_COMMANDS)))
    elif cmd == "/status":
        print("ENZO Beta-01")
        print("AI: Connected (stub)")
        print("Memory: Active")
        print("Tools: 1")
        print("Security: Active")
    elif cmd == "/reset":
        ctx.reset()
        model.reset_context()
        print("Context reset.")
    elif cmd == "/tools":
        print("Available tools: calculator")
    elif cmd == "/memory":
        msgs = ctx.get_messages()
        print(f"Short-term memory ({len(msgs)} messages).")
    elif cmd == "/exit":
        print("Shutting down. Goodbye.")
        return False
    return True

def run_cli() -> None:
    running = True
    while running:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nShutting down. Goodbye.")
            break
        if not user:
            continue
        if user.startswith("/"):
            running = handle_special(user)
            continue

        # Simple tool detection: if message starts with "calculate" or contains "×" or "*"
        if user.lower().startswith("calculate") or any(op in user for op in ("*", "/", "+", "-", "×")):
            # Extract expression after the word calculate if present
            expr = user
            if user.lower().startswith("calculate"):
                expr = user[len("calculate"):].strip()
            tool = get_tool("calculator")
            if tool:
                res = tool.func(expr)
                if res.get("ok"):
                    print(f"ENZO: {expr} = {res['result']}")
                else:
                    print("ENZO: The calculator tool could not complete the request.")
            else:
                print("ENZO: No calculator tool available.")
            ctx.add_message("user", user)
            continue

        # Otherwise forward to model stub
        ctx.add_message("user", user)
        reply = model.generate_response(user, ctx.get_messages())
        ctx.add_message("assistant", reply)
        print("ENZO:", reply)
