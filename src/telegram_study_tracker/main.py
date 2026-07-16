"""Application startup for Telegram Study Tracker."""

import logging
import sys

from telegram_study_tracker.bot.application import create_application
from telegram_study_tracker.config.logging import configure_logging
from telegram_study_tracker.config.settings import ConfigurationError, load_settings

logger = logging.getLogger(__name__)


def main() -> None:
    """Load configuration, build the bot application, and start polling."""
    configure_logging()

    try:
        settings = load_settings()
    except ConfigurationError as error:
        print(f"Configuration error: {error}", file=sys.stderr)
        raise SystemExit(1) from None

    application = create_application(settings.telegram_bot_token)
    logger.info("event=application_started")
    application.run_polling()
