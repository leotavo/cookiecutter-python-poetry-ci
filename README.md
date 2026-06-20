# cookiecutter-python-poetry-ci

A [Cookiecutter](https://www.cookiecutter.io/) template for production-ready Python projects: **Poetry**, a `src/` layout, **Ruff** (lint **and** format), **mypy**, **pytest** with coverage, **pre-commit**, and a green **GitHub Actions** CI from the first commit.

[![CI](https://github.com/leotavo/cookiecutter-python-poetry-ci/actions/workflows/ci.yml/badge.svg)](https://github.com/leotavo/cookiecutter-python-poetry-ci/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/leotavo/cookiecutter-python-poetry-ci)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-blue)
[![Cookiecutter](https://img.shields.io/badge/cookiecutter-template-D4AA00?logo=cookiecutter&logoColor=white)](https://www.cookiecutter.io/)

## Why

Starting a Python project means re-wiring the same dozen tools every time. This template gives you a project that **lints, formats, type-checks, tests and passes CI from the first commit** — so you write code, not config.

The template itself is **CI-verified**: every change re-generates a project with `cookiecutter` and runs its full check suite on Python 3.11, 3.12 and 3.13.

## Quick start

```bash
pipx install cookiecutter           # or: pip install cookiecutter
cookiecutter gh:leotavo/cookiecutter-python-poetry-ci
cd <repo_name>
poetry install
poetry run pytest
```

## What you get

- **Poetry** for dependency & build management, with a `src/` layout
- **Ruff** as the single linter **and** formatter — no Black/isort overlap
- **mypy** with sensible strictness (`check_untyped_defs`, `warn_redundant_casts`, …)
- **pytest** + **coverage**, with smoke tests included
- **pre-commit** hooks kept in sync with CI
- **GitHub Actions** CI: `poetry install` → `ruff check` → `ruff format --check` → `mypy` → `pytest`
- A minimal CLI entry point and `docs/` (git-flow, CI status checks)

### Generated structure

```text
<repo_name>/
├── .github/workflows/ci.yml
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs/
│   ├── ci-status-checks.md
│   └── git-flow.md
├── poetry.toml
├── pyproject.toml
├── src/<package_name>/
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
└── tests/test_smoke.py
```

## Template options

| Prompt | Default | Description |
|---|---|---|
| `project_name` | `My Project` | Human-readable project name |
| `repo_name` | `my-project` | Repository / root directory name |
| `package_name` | `app` | Importable package under `src/` |
| `description` | … | Short project description |
| `author_name` / `author_email` | … | Package author |
| `license` | `MIT` | License identifier |
| `python_version` | `3.11` | Minimum Python version |
| `gh_owner` | `leotavo` | GitHub owner, used in the repository URL |
| `use_ci` | `y` | Include the GitHub Actions CI workflow (`n` to omit) |
| `use_precommit` | `y` | Include the pre-commit config (`n` to omit) |

## License

[MIT](LICENSE) © Leonardo Trindade
