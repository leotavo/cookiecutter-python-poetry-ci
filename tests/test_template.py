"""Tests for the cookiecutter template itself, using pytest-cookies."""

from __future__ import annotations


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
