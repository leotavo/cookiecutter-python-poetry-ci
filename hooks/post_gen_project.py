"""Post-generation hook honoring the use_ci / use_precommit feature flags.

Cookiecutter renders this file with Jinja before running it, so the
cookiecutter placeholders below are substituted with the chosen values.
The hook runs inside the freshly generated project directory.
"""

from __future__ import annotations

import shutil
from pathlib import Path

_FALSEY = {"n", "no", "false", "0", "off"}


def _disabled(value: str) -> bool:
    return value.strip().lower() in _FALSEY


def main() -> None:
    if _disabled("{{ cookiecutter.use_ci }}"):
        shutil.rmtree(Path(".github"), ignore_errors=True)
    if _disabled("{{ cookiecutter.use_precommit }}"):
        Path(".pre-commit-config.yaml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
