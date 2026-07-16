# Telegram Study Tracker

A Telegram bot that helps learners record study sessions, review progress, and build consistent study habits.

This is an open-source learning project. Its goal is twofold: deliver a useful application and demonstrate professional Python, Git, documentation, testing, and architecture practices.

## Project status

**Sprint 0 — project foundation.** No Telegram functionality has been implemented yet.

## Planned structure

```text
telegram-study-tracker/
├── docs/                         # Architecture, decisions, and learning notes
├── src/telegram_study_tracker/   # Application code (introduced in Sprint 1)
├── tests/                        # Automated tests, mirroring src/ (introduced in Sprint 1)
├── README.md                     # Project overview and contributor entry point
├── ROADMAP.md                    # High-level delivery plan
├── CHANGELOG.md                  # User-visible project changes
├── requirements.txt              # Runtime dependencies
├── .gitignore                    # Files Git must not track
└── LICENSE                       # MIT license
```

`src/` keeps importable application code separate from repository tooling and documentation. The package name uses underscores because Python identifiers cannot use hyphens. `tests/` is separate so quality checks never become production code. These folders will be created when Sprint 1 introduces the first executable feature; creating empty directories now would add no value because Git does not track them.

## Getting started

There is nothing to run during Sprint 0. The first setup and run instructions will be added with the first bot feature.

## Development principles

- Deliver one small, testable feature per sprint.
- Prefer simple, explicit code over clever abstractions.
- Record meaningful technical decisions in [`docs/decisions.md`](docs/decisions.md).
- Keep user-facing changes in [`CHANGELOG.md`](CHANGELOG.md).
- Make focused Git commits with clear messages.

## License

Licensed under the [MIT License](LICENSE).
