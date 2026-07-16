# Architecture Decision Log

This file records decisions that influence the project so future contributors understand the reasoning, not just the result.

## ADR-001: Use a `src/` layout when application code begins

**Status:** Accepted  
**Date:** 2026-07-16

### Context

Python can place packages at the repository root or under `src/`. We want imports and tests to behave like they will after the project is installed.

### Decision

Application code will live in `src/telegram_study_tracker/`.

### Consequences

This prevents tests from accidentally importing code only because the repository root is on the Python path. It requires a little more packaging setup in Sprint 1, which is worthwhile for a portfolio project.

## ADR-002: Start with SQLite for persistence

**Status:** Accepted  
**Date:** 2026-07-16

### Context

The early product needs reliable local storage without operational overhead.

### Decision

Use SQLite when persistence is introduced.

### Consequences

SQLite is bundled with Python, easy to inspect, and appropriate for a small bot. A future move to a server database would require a deliberate migration, not a hidden change.

## ADR-003: Defer dependencies until needed

**Status:** Accepted  
**Date:** 2026-07-16

### Decision

`requirements.txt` remains empty in Sprint 0. Each dependency must be justified by the sprint that introduces it.

### Consequences

The repository starts simple and avoids unused packages. Sprint 3 selects and pins the Telegram library now that the project has a clear integration boundary.

## ADR-004: Use `python-telegram-bot` as the Telegram integration library

**Status:** Accepted  
**Date:** 2026-07-16

### Context

The project needs a Python interface to the Telegram Bot API but should avoid implementing HTTP requests and update parsing itself.

### Decision

Use `python-telegram-bot==22.8`, pinned in `requirements.txt`.

### Consequences

The project gains a maintained, high-level interface for future Telegram integration and reproducible dependency installation. The dependency does not create or contact a bot by itself.
