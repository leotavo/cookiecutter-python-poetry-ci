# Required status checks (CI)

The "CI" workflow runs a `ci ({{ cookiecutter.python_version }})` job.

1. Settings → Branches → Add rule (`main`)
2. Require status checks to pass; select `ci ({{ cookiecutter.python_version }})`
3. Require branches to be up to date before merging
