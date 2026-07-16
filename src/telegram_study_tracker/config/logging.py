"""Logging configuration for the application."""

import logging


def configure_logging() -> None:
    """Configure consistent, field-oriented application logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s level=%(levelname)s logger=%(name)s message=%(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
