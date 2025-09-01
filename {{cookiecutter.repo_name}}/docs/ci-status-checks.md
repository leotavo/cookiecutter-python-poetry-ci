# Status Checks obrigatórios (CI)

Workflow "CI" com job `ci ({{ cookiecutter.python_version }})`.

1) Settings → Branches → Add rule (`main`)
2) Require status checks to pass; selecionar `ci ({{ cookiecutter.python_version }})`
3) Require branches to be up to date before merging
