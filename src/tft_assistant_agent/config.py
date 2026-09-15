"""Environment-backed application settings."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    model: str = "local"
    log_level: str = "INFO"
    max_steps: int = 8
    system_prompt: str = "You are a helpful TFT assistant."


def load_settings() -> Settings:
    """Load settings from environment variables with safe defaults."""

    return Settings(
        model=os.getenv("TFT_AGENT_MODEL", "local"),
        log_level=os.getenv("TFT_AGENT_LOG_LEVEL", "INFO").upper(),
        max_steps=int(os.getenv("TFT_AGENT_MAX_STEPS", "8")),
        system_prompt=os.getenv(
            "TFT_AGENT_SYSTEM_PROMPT",
            "You are a helpful TFT assistant.",
        ),
    )
