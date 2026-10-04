# config/settings.py
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    enzo_ai_provider: str | None = os.getenv("ENZO_AI_PROVIDER")
    enzo_model: str | None = os.getenv("ENZO_MODEL")
    enzo_log_level: str = os.getenv("ENZO_LOG_LEVEL", "INFO")

settings = Settings()
