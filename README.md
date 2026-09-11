# reusable-workflows

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


See [CHANGELOG.md](CHANGELOG.md) for release history.