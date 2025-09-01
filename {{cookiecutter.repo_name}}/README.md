# {{ cookiecutter.project_name }}

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg)
[![CI](https://github.com/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.gh_owner }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml)

{{ cookiecutter.description }}

## Ambiente de desenvolvimento

- Pré-requisitos: Python {{ cookiecutter.python_version }}+ e Poetry 2.x
- Venv local: configurada via `poetry.toml` (`[virtualenvs] in-project = true`)

### Instalação

```bash
poetry install
```

### Executar

```bash
poetry run python -m {{ cookiecutter.package_name }}
```

### Scripts

```bash
poetry run lint
poetry run format
poetry run typecheck
poetry run test
```
