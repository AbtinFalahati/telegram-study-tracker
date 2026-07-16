"""Global error handling for Telegram updates."""

import logging

from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def handle_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log unexpected handler failures without exposing details to users."""
    logger.error(
        "event=unhandled_update_error update_type=%s",
        type(update).__name__,
        exc_info=context.error,
    )
