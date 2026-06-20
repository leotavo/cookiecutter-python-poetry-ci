"""Tests for the cookiecutter template itself, using pytest-cookies."""

from __future__ import annotations

import re
from pathlib import Path

# Single source of truth for the files a default bake produces. If you add or
# remove a template file, update this set AND the "Generated structure" block in
# README.md — the two tests below fail otherwise, keeping docs and reality in sync.
EXPECTED_FILES = {
    ".gitattributes",
    ".github/dependabot.yml",
    ".github/workflows/ci.yml",
    ".gitignore",
    ".pre-commit-config.yaml",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "docs/ci-status-checks.md",
    "docs/git-flow.md",
    "poetry.toml",
    "pyproject.toml",
    "src/app/__init__.py",
    "src/app/__main__.py",
    "tests/test_smoke.py",
}


def test_bake_with_defaults(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert (result.project_path / "pyproject.toml").is_file()
    assert (result.project_path / ".github" / "workflows" / "ci.yml").is_file()
    assert (result.project_path / ".pre-commit-config.yaml").is_file()


def test_bake_without_ci_and_precommit(cookies):
    result = cookies.bake(extra_context={"use_ci": "n", "use_precommit": "n"})

    assert result.exit_code == 0
    assert not (result.project_path / ".github").exists()
    assert not (result.project_path / ".pre-commit-config.yaml").exists()


def test_bake_applies_custom_context(cookies):
    result = cookies.bake(extra_context={"repo_name": "acme-tool", "package_name": "acme"})

    assert result.exit_code == 0
    pyproject = (result.project_path / "pyproject.toml").read_text()
    assert 'name = "acme-tool"' in pyproject
    assert (result.project_path / "src" / "acme" / "__init__.py").is_file()


def test_generated_tree_matches_expected(cookies):
    """A default bake produces exactly EXPECTED_FILES — no more, no less.

    Guards against template drift: an accidentally added or removed file fails
    here with a clear diff, prompting an update to EXPECTED_FILES and the README.
    """
    result = cookies.bake()

    assert result.exit_code == 0
    actual = {
        path.relative_to(result.project_path).as_posix()
        for path in result.project_path.rglob("*")
        if path.is_file()
    }
    assert actual == EXPECTED_FILES


def test_readme_documents_generated_tree():
    """The README's "Generated structure" block must list exactly the generated
    files (by basename) — catching phantom entries and undocumented files."""
    readme = (Path(__file__).resolve().parent.parent / "README.md").read_text(encoding="utf-8")
    match = re.search(r"### Generated structure\s*```text\n(.*?)```", readme, re.S)
    assert match, "README is missing a '### Generated structure' code block"

    documented = set()
    for line in match.group(1).splitlines():
        if "── " not in line:  # skip non-entry lines (root, fences)
            continue
        name = line.split("── ", 1)[1].strip()
        if not name.endswith("/"):  # skip directories
            documented.add(name.split("/")[-1])

    expected_basenames = {path.split("/")[-1] for path in EXPECTED_FILES}
    assert documented == expected_basenames
