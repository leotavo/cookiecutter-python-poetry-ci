import subprocess
import sys


def _run(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    try:
        return subprocess.call(cmd)
    except FileNotFoundError as exc:
        print(f"Command not found: {exc}", file=sys.stderr)
        return 127


def lint() -> None:
    rc = _run([sys.executable, "-m", "ruff", "check", "."])
    sys.exit(rc)


def format() -> None:
    rc = _run([sys.executable, "-m", "ruff", "format", "."])
    sys.exit(rc)


def typecheck() -> None:
    rc = _run([sys.executable, "-m", "mypy", "."])
    sys.exit(rc)


def test() -> None:
    rc = _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-q",
            "--cov=src",
            "--cov-report=term-missing",
            "--cov-report=xml",
        ]
    )
    if rc == 5:
        rc = 0
    sys.exit(rc)
