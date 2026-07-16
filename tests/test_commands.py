"""Tests for public command responses."""

import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock

from telegram_study_tracker.handlers.commands import about, help_command, ping, start


class CommandResponseTests(unittest.IsolatedAsyncioTestCase):
    """Verify each command responds with its intended message."""

    async def test_start_replies_with_running_message(self) -> None:
        message = AsyncMock()
        update = SimpleNamespace(effective_message=message)

        await start(update, None)

        message.reply_text.assert_awaited_once_with(
            "Hello! Telegram Study Tracker is running."
        )

    async def test_help_replies_with_command_list(self) -> None:
        message = AsyncMock()
        update = SimpleNamespace(effective_message=message)

        await help_command(update, None)

        message.reply_text.assert_awaited_once()
        self.assertIn("/ping", message.reply_text.await_args.args[0])

    async def test_about_replies_with_project_purpose(self) -> None:
        message = AsyncMock()
        update = SimpleNamespace(effective_message=message)

        await about(update, None)

        self.assertIn("study habits", message.reply_text.await_args.args[0])

    async def test_ping_replies_with_pong(self) -> None:
        message = AsyncMock()
        update = SimpleNamespace(effective_message=message)

        await ping(update, None)

        message.reply_text.assert_awaited_once_with("Pong!")
