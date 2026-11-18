# Secure Dependencies in CI Pipelines

Course assignment: a GitHub Actions workflow that runs unit tests, then scans
Python dependencies (safety) and source code (bandit) for known security issues.

## Commit message pattern

Every commit uses `<type>(<scope>): <what changed>`.

| Type | Use for |
| --- | --- |
| `chore` | Repo setup, files added |
| `ci` | Workflow changes |
| `test` | Test changes |
| `fix(deps)` | Dependency version bumps that close vulnerabilities |
| `docs` | README and notes |
