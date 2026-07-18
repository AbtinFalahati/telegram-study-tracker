"""Tests for the /log minutes validation rule."""

import unittest

from telegram_study_tracker.services.minutes_validation import validate_minutes


class ValidateMinutesTests(unittest.TestCase):
    """Verify the /log validation rule in isolation from Telegram."""

    def test_accepts_a_positive_integer(self) -> None:
        self.assertEqual(validate_minutes("45"), 45)

    def test_rejects_non_numeric_input(self) -> None:
        with self.assertRaises(ValueError):
            validate_minutes("abc")

    def test_rejects_empty_input(self) -> None:
        with self.assertRaises(ValueError):
            validate_minutes("")

    def test_rejects_zero(self) -> None:
        with self.assertRaises(ValueError):
            validate_minutes("0")

    def test_rejects_negative_numbers(self) -> None:
        with self.assertRaises(ValueError):
            validate_minutes("-10")
