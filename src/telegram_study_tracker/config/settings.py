"""Environment-based configuration loading and validation."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


class ConfigurationError(ValueError):
    """Raised when required application configuration is invalid."""


@dataclass(frozen=True, slots=True)
class Settings:
    """Validated application settings."""

    telegram_bot_token: str


def load_settings() -> Settings:
    """Load settings from the environment and a local .env file when present."""
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

    if not token:
        raise ConfigurationError("TELEGRAM_BOT_TOKEN is missing or empty.")
    if any(character.isspace() for character in token) or ":" not in token:
        raise ConfigurationError("TELEGRAM_BOT_TOKEN has an invalid format.")

    return Settings(telegram_bot_token=token)
