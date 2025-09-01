# Contribuição

Fluxo trunk‑based com convenção de branches `{type}/{slug}` e mensagens no padrão Conventional Commits.

## Convenção de branches

- Padrão: `{type}/{slug}`
- type ∈ {feat, fix, docs, chore, refactor, test}
- slug em kebab‑case

## Pull Requests

- Rebase ou squash; PRs pequenos (< 300 linhas).
- Rode pre-commit, lint, typecheck e testes antes de abrir.

## Mensagens de commit (Conventional Commits)

- Tipos: feat, fix, docs, refactor, test, chore
- Escopo opcional: `type(scope): descrição`
- Breaking change: `!` e `BREAKING CHANGE:` no corpo
