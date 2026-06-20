# {{ cookiecutter.project_name }}

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg)
[![CI](https://github.com/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml)

{{ cookiecutter.description }}

## Development

- Requirements: Python {{ cookiecutter.python_version }}+ and Poetry 2.x
- Local virtualenv: configured via `poetry.toml` (`[virtualenvs] in-project = true`)

### Install

```bash
poetry install
```

### Run

```bash
poetry run python -m {{ cookiecutter.package_name }}
```

### Tasks

```bash
poetry run lint        # ruff check
poetry run format      # ruff format
poetry run typecheck   # mypy
poetry run test        # pytest with coverage
```
