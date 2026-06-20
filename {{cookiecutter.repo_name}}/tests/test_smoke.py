import importlib


def test_import_pkg():
    mod = importlib.import_module("{{ cookiecutter.package_name }}")
    assert mod is not None


def test_version_available():
    import {{ cookiecutter.package_name }} as pkg

    assert isinstance(pkg.__version__, str)
    assert pkg.__version__


def test_main_returns_zero():
    from {{ cookiecutter.package_name }}.__main__ import main

    assert main() == 0


def test_main_prints_banner(capsys):
    from {{ cookiecutter.package_name }} import __version__
    from {{ cookiecutter.package_name }}.__main__ import main

    assert main() == 0
    out = capsys.readouterr().out
    assert "{{ cookiecutter.repo_name }}" in out
    assert __version__ in out
