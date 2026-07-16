"""Central registration of Telegram command handlers."""

from telegram.ext import Application, CommandHandler

from telegram_study_tracker.handlers.commands import about, help_command, ping, start


def register_command_handlers(application: Application) -> None:
    """Register every command supported by the current application."""
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("ping", ping))
