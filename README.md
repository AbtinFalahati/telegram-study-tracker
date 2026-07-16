# Telegram Study Tracker

A Telegram bot that helps learners record study sessions, review progress, and build consistent study habits.

This is an open-source learning project. Its goal is twofold: deliver a useful application and demonstrate professional Python, Git, documentation, testing, and architecture practices.

## Project status

**Sprint 4 — bot skeleton.** The bot runs and responds to `/start`, `/help`, `/about`, and `/ping`. Study-tracking features have not been implemented yet.

## Planned structure

```text
telegram-study-tracker/
├── docs/                         # Architecture, decisions, and learning notes
├── src/telegram_study_tracker/   # Application package, organized by responsibility
├── tests/                        # Automated tests, mirroring application behavior
├── assets/                       # Non-code project assets, such as diagrams
├── README.md                     # Project overview and contributor entry point
├── ROADMAP.md                    # High-level delivery plan
├── CHANGELOG.md                  # User-visible project changes
├── requirements.txt              # Runtime dependencies
├── .gitignore                    # Files Git must not track
└── LICENSE                       # MIT license
```

`src/` keeps importable application code separate from repository tooling and documentation. The package name uses underscores because Python identifiers cannot use hyphens. `tests/` is separate so quality checks never become production code. Empty folders include `.gitkeep` solely because Git tracks files, not directories; these placeholders will disappear as each area receives real files.

## Getting started

## Run locally

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Copy `.env.example` to `.env`, then replace its placeholder with a Telegram bot token. Never commit `.env`.
3. Install the package and its dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   python -m pip install -e .
   ```

4. Run the application:

   ```powershell
   python -m telegram_study_tracker
   ```

The bot currently supports `/start`, `/help`, `/about`, and `/ping`. Study-tracking commands are not implemented yet.

## Development principles

- Deliver one small, testable feature per sprint.
- Prefer simple, explicit code over clever abstractions.
- Record meaningful technical decisions in [`docs/decisions.md`](docs/decisions.md).
- Keep user-facing changes in [`CHANGELOG.md`](CHANGELOG.md).
- Make focused Git commits with clear messages.

## License

Licensed under the [MIT License](LICENSE).
