"""Responses for the bot's public commands."""

from telegram import Update
from telegram.ext import ContextTypes


async def _reply(update: Update, text: str) -> None:
    """Reply to the effective message when an update includes one."""
    if update.effective_message is not None:
        await update.effective_message.reply_text(text)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Confirm that the bot is running."""
    await _reply(update, "Hello! Telegram Study Tracker is running.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Describe the commands currently available."""
    await _reply(
        update,
        "Available commands:\n"
        "/start - Confirm the bot is running.\n"
        "/help - Show this help message.\n"
        "/about - Learn about this bot.\n"
        "/ping - Check whether the bot is responsive.",
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Explain the bot's purpose."""
    await _reply(
        update,
        "Telegram Study Tracker helps you build consistent study habits. "
        "Study-tracking features are coming soon.",
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Confirm that the bot can respond to updates."""
    await _reply(update, "Pong!")
