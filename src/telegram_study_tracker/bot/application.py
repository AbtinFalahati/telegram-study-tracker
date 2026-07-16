"""Telegram application creation and component wiring."""

from telegram.ext import Application, ApplicationBuilder

from telegram_study_tracker.handlers.errors import handle_error
from telegram_study_tracker.handlers.registration import register_command_handlers


def create_application(token: str) -> Application:
    """Build the Telegram application and register its interface adapters."""
    application = ApplicationBuilder().token(token).build()
    register_command_handlers(application)
    application.add_error_handler(handle_error)
    return application
