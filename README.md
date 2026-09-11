# reusable-workflows

[![Release](https://img.shields.io/github/v/release/k-3679/reusable-workflows)](https://github.com/k-3679/reusable-workflows/releases)
[![Changelog](https://img.shields.io/badge/changelog-CHANGELOG.md-blue)](CHANGELOG.md)

Shared, reusable GitHub Actions workflows and composite actions, extracted out of individual project repos so they can be maintained and versioned in one place.

## Structure

- `.github/workflows/`: reusable workflows (`workflow_call`), invoked from other repos via `uses: <org>/reusable-workflows/.github/workflows/<file>.yml@<ref>`.
- `.github/actions/`: composite actions, invoked via `uses: <org>/reusable-workflows/.github/actions/<name>@<ref>`.
