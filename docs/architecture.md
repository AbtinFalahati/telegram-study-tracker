# Architecture

## Current state

Sprint 3 establishes the folder boundaries only. There is no executable application code, bot, handler, database, or Telegram API call yet.

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
├── bot/                 # Application startup and Telegram client wiring
├── handlers/            # Telegram-specific update and response adapters
├── services/            # Use cases and business rules
├── database/            # SQLite persistence boundary
└── config/              # Configuration loading and validation
```

Sprint 4 adds only the startup, configuration, and Telegram wiring modules. The `database` and `services` folders remain empty because no persistence or business behavior exists yet.

## Dependencies

- The Telegram integration will depend on a maintained Python Telegram library, selected in Sprint 1.
- SQLite is included with Python, so no separate database server is required for the initial product.
- Secrets such as a bot token must come from environment variables, never source control.

## Sprint 4 execution flow

```text
main()
  → load_settings() reads .env and validates TELEGRAM_BOT_TOKEN
  → create_application() builds python-telegram-bot Application
  → CommandHandler("start", start) is registered
  → run_polling() receives /start and calls start()
  → start() replies with the running confirmation
```

## Diagrams

Engineering diagrams are deliberately not produced yet. This project creates diagrams incrementally, only after the code they describe exists, so every diagram reflects the real implementation rather than a speculative future design.

The following diagrams will be added as the corresponding work lands, not before:

- **High-Level Architecture Diagram** — once more than one real layer is populated beyond the Sprint 4 skeleton.
- **Request Flow Diagram** — for each major Telegram command, once the command and its full path through the layers are implemented.
- **Database ER Diagram** — when SQLite persistence is introduced.
- **AI Pipeline Diagram** — when AI-powered coaching features are introduced.

No diagram is created ahead of the feature it documents.
