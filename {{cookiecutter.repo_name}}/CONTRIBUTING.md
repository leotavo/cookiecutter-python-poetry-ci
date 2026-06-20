# Contributing

Trunk-based flow with `{type}/{slug}` branch names and Conventional Commit messages.

## Branch naming

- Pattern: `{type}/{slug}`
- type ∈ {feat, fix, docs, chore, refactor, test}
- slug in kebab-case

## Pull requests

- Rebase or squash; keep PRs small (< 300 lines).
- Run pre-commit, lint, typecheck and tests before opening.

## Commit messages (Conventional Commits)

- Types: feat, fix, docs, refactor, test, chore
- Optional scope: `type(scope): description`
- Breaking change: `!` and a `BREAKING CHANGE:` footer
