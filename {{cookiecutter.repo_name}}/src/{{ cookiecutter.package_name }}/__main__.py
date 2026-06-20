from __future__ import annotations

from . import __version__


def main() -> int:
    print(f"{{ cookiecutter.repo_name }} {__version__} - CLI ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
