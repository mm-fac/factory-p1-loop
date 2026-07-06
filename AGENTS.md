# Agent conventions for factory-p1-loop

## What this repo is

A small, dependency-free Python 3.12 library (`textstats`) used to validate an autonomous issue → PR → checks → merge loop. Treat every issue as a normal, small software task.

## Commands

- Test: `pytest -q`
- Lint: `ruff check .`
- Both must pass before you open or update a PR. CI runs exactly these two commands.

## Conventions

- Python 3.12, standard library only. Do not add dependencies.
- Every behavior change ships with tests in `tests/`. Bug fixes ship a regression test that fails without the fix.
- Keep diffs minimal and scoped to the issue. One issue = one PR.
- Follow existing code style: type hints on public functions, docstrings in the existing format.
- Reference the issue number in the PR description (`Fixes #N`).

## Hard rules

- Never modify `.github/**`, `AGENTS.md`, or `README.md` unless the issue explicitly asks for it.
- Never push to `main` directly. Work on a branch; open a PR.
- Never disable, skip, or weaken tests or lint rules to get green.
- Merging is automated: when required checks pass, the PR auto-merges. Do not merge manually.
