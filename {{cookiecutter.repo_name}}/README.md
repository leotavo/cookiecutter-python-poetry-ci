# {{ cookiecutter.project_name }}

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg)
[![CI](https://github.com/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }})

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
poetry run poe lint        # ruff check
poetry run poe format      # ruff format
poetry run poe typecheck   # mypy
poetry run poe test        # pytest with coverage
```
