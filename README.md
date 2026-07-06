# factory-p1-loop

**Sacrificial P1 validation repo for the Mac mini AI factory.**

This repo exists to prove one thing end-to-end: **issue → `@codex` PR → required checks → merge, fully autonomous** (architecture v6.4.1, §10 P1). It contains a deliberately small Python library (`textstats`) with real tests so the loop exercises real work, not no-ops.

- Work arrives as GitHub Issues.
- Codex cloud picks up issues and opens PRs on `codex/*` branches.
- The `ci` check (ruff + pytest) is required on `main`.
- PRs from `codex/*` branches (or labeled `automerge`) get GitHub auto-merge enabled and land on green — no human in the loop.

Nothing here is production. The repo is disposable by design; delete it when P1 exits.

## Local dev

```sh
pip install pytest ruff
ruff check .
pytest -q
```
