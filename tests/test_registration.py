"""Tests for centralized command registration."""

import unittest
from unittest.mock import MagicMock

from telegram_study_tracker.handlers.registration import register_command_handlers


class CommandRegistrationTests(unittest.TestCase):
    """Verify the current public commands are registered together."""

    def test_registers_all_supported_commands(self) -> None:
        application = MagicMock()

        register_command_handlers(application)

        registered_commands = {
            next(iter(call.args[0].commands)) for call in application.add_handler.call_args_list
        }
        self.assertEqual(registered_commands, {"start", "help", "about", "ping", "log"})
