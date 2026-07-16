"""Tests for configuration validation."""

import os
import unittest
from unittest.mock import patch

from telegram_study_tracker.config.settings import ConfigurationError, load_settings


class LoadSettingsTests(unittest.TestCase):
    """Validate required environment configuration."""

    @patch("telegram_study_tracker.config.settings.load_dotenv")
    def test_missing_token_raises_configuration_error(self, mock_load_dotenv: object) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ConfigurationError):
                load_settings()

    @patch("telegram_study_tracker.config.settings.load_dotenv")
    def test_valid_token_returns_settings(self, mock_load_dotenv: object) -> None:
        token = "123456:abcdefghijklmnopqrstuvwxyz"

        with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": token}, clear=True):
            settings = load_settings()

        self.assertEqual(settings.telegram_bot_token, token)
