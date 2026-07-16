# Learning Log

Use this log to turn implementation work into durable engineering knowledge. Add a short entry at the end of each sprint.

## Entry template

```markdown
## Sprint N — YYYY-MM-DD

### Learned
- What concept became clearer?

### Practiced
- What did I do myself?

### Questions
- What should I investigate next?

### Improvement for next sprint
- What would I do differently?
```

## Sprint 0 — 2026-07-16

### Learned

- A repository’s documentation can establish technical direction before code exists.
- A `src/` layout helps keep Python imports honest as a project grows.
- Architecture decisions should include their context and consequences.

### Practiced

- Defined a focused roadmap and initial repository conventions.

### Questions

- How does Python package installation make a `src/` layout work locally?
- Which Telegram library best fits the first bot feature?

### Improvement for next sprint

- Add only the minimum packaging, configuration, and test tooling required for the bot skeleton.

## Sprint 3 — 2026-07-16

### Learned

- A `src` layout separates installable application code from repository files.
- Folders should reflect responsibilities, not speculative features.
- A version-pinned dependency makes environments reproducible.

### Practiced

- Created a package-oriented architecture without prematurely implementing it.
- Prepared a safe environment-variable template for a future secret.

### Questions

- How does a virtual environment isolate package versions?
- How should configuration be validated when the application starts?

### Improvement for next sprint

- Add only the smallest executable package and configuration component needed to start safely.

## Sprint 4 — 2026-07-16

### Learned

- An entry point coordinates application startup without containing every responsibility.
- Configuration should be validated before connecting to an external service.
- An asynchronous command handler can reply to a Telegram update.

### Practiced

- Separated configuration loading, application wiring, and command response code.
- Wrote focused configuration tests with Python's built-in `unittest`.

### Questions

- How can application logging make startup and errors easier to diagnose?
- How should new command handlers be organized as the bot grows?
