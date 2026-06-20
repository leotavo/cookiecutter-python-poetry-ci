# Contributing

Thanks for considering a contribution!

## Development

This repository is a [Cookiecutter](https://www.cookiecutter.io/) template. To work on it:

```bash
pip install -r requirements-dev.txt
pytest                      # run the pytest-cookies tests
cookiecutter . --no-input   # bake the template locally
```

## Pull requests

- Use [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `chore:`, …).
- Keep PRs focused and small; describe the change and how you tested it.
- CI must stay green: the template is baked and the generated project's full check
  suite runs on Python 3.11–3.13.

## Reporting issues

Please use the bug-report / feature-request templates.
