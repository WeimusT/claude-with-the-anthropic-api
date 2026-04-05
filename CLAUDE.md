# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Commands

```bash
pytest                        # run all tests
pytest tests/test_main.py     # run a single test file
ruff check .                  # lint
ruff format .                 # format
```

## Architecture

Source lives under `src/claude_with_the_anthropic_api/` (src layout). The entry point is `main.py:main()`, also registered as the `claude-with-the-anthropic-api` CLI script via `pyproject.toml`.

Tests are in `tests/` and import directly from the package (enabled by the editable install).
