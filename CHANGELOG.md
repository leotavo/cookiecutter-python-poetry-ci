# Changelog

All notable changes to this template are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- The template failed to generate at all: GitHub Actions `${{ ... }}` expressions in
  the generated workflow collided with cookiecutter's Jinja `{{ ... }}` delimiters.
  They are now escaped with `{% raw %}`.
- Standardized on Ruff as the single linter **and** formatter. Black and ruff-format
  were both configured in pre-commit while CI only checked Black, so a generated
  project could pass pre-commit and fail CI.

### Added

- Root CI workflow that bakes the template and runs the generated project's full
  check suite (`ruff check`, `ruff format --check`, `mypy`, `pytest`) across
  Python 3.11, 3.12 and 3.13.
- Functional `use_ci` / `use_precommit` flags via a post-generation hook.
- Portfolio README, root `LICENSE` (MIT), `.gitignore`, a `CHANGELOG`, and
  English documentation for the generated project.
