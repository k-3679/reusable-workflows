# reusable-workflows

[![CodeQL](https://github.com/k-3679/reusable-workflows/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/k-3679/reusable-workflows/actions/workflows/github-code-scanning/codeql)
[![Release](https://img.shields.io/github/v/release/k-3679/reusable-workflows)](https://github.com/k-3679/reusable-workflows/releases)
[![Changelog](https://img.shields.io/badge/changelog-CHANGELOG.md-blue)](CHANGELOG.md)

Shared, reusable GitHub Actions workflows and composite actions, extracted out of individual project repos so they can be maintained and versioned in one place.

## Structure

```bash
reusable-workflows/
├── CHANGELOG.md                      # release history (Keep a Changelog format)
├── README.md
└── .github/                          # GH workflows
    ├── workflows/                    # reusable workflows (workflow_call)
    └── actions/                      # composite actions
```

## Actions

Each action has a README in its folder with usage, inputs and what it checks.

| Action | What it does |
| --- | --- |
| [`validate-changelog`](.github/actions/validate-changelog) | Fails unless the PR added a well-formed entry to `[Unreleased]` |
| [`check-unreleased-changelog`](.github/actions/check-unreleased-changelog) | Fails if `[Unreleased]` still has entries at a given ref |
| [`update-changelog`](.github/actions/update-changelog) | Moves `[Unreleased]` into a new version section at release time |
| [`validate-launcher-metadata`](.github/actions/validate-launcher-metadata) | Checks a launcher JSON file has a semantic `version` |
| [`codeql-analyze`](.github/actions/codeql-analyze) | Runs CodeQL for one language and uploads the results |
| [`trivy-security-scan`](.github/actions/trivy-security-scan) | Trivy scan for vulnerabilities, secrets and misconfigs, with a high/critical threshold |
| [`lint-c`](.github/actions/lint-c) | `cppcheck` |
| [`lint-go`](.github/actions/lint-go) | `golangci-lint` |
| [`lint-node`](.github/actions/lint-node) | ESLint 8 |
| [`lint-php`](.github/actions/lint-php) | `php -l` |
| [`lint-python`](.github/actions/lint-python) | `ruff check` |
| [`lint-rust`](.github/actions/lint-rust) | `cargo clippy` |

See [CHANGELOG.md](CHANGELOG.md) for release history.
