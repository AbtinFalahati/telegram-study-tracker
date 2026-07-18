"""Validation for the /log command's minutes argument.

This module is the application layer for the /log use case. It has no
knowledge of Telegram or of the Persian replies sent to users; per ADR-005,
that translation happens only in the handler layer.
"""


def validate_minutes(raw_minutes: str) -> int:
    """Parse and validate a raw study-session length.

    A valid value is an integer greater than zero. Anything else raises
    ValueError with an English message describing the rule.
    """
    try:
        minutes = int(raw_minutes)
    except (TypeError, ValueError):
        raise ValueError("Study minutes must be a whole number.") from None

    if minutes <= 0:
        raise ValueError("Study minutes must be greater than zero.")

    return minutes
