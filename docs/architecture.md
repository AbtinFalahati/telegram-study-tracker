# Architecture

## Current state

Sprint 0 contains no executable application code. This document defines the direction for the smallest useful architecture rather than prematurely committing to implementation details.

## Guiding design

The bot will begin as a small Python application with clear boundaries:

```text
Telegram update
    → interface layer (commands and replies)
    → application layer (study-tracking use cases)
    → data layer (SQLite persistence)
```

The interface layer translates Telegram-specific updates into application calls. The application layer owns business rules, such as validating a study session. The data layer owns database access. Keeping these responsibilities separate makes the core rules easier to test and avoids spreading Telegram or SQL details throughout the project.

## Planned package layout

```text
src/telegram_study_tracker/
├── __init__.py
├── main.py              # Application startup and dependency wiring
├── bot/                 # Telegram command handlers and response formatting
├── application/         # Use cases and business rules
└── infrastructure/      # SQLite and other external integrations
```

We will add a folder only when a real feature needs it. For example, there is no database package until we persist study sessions.

## Dependencies

- The Telegram integration will depend on a maintained Python Telegram library, selected in Sprint 1.
- SQLite is included with Python, so no separate database server is required for the initial product.
- Secrets such as a bot token must come from environment variables, never source control.
