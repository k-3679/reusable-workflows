# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Reusable workflow `codeql.yml` (SAST via CodeQL, converted from the default "Advanced" setup so it can be shared across repos).
- Reusable workflow `lint.yml`.
- Reusable workflow `release-vita-launcher.yml`.
- Reusable workflow `restrict-branch.yml`.
- Reusable workflow `trivy.yml`.
- Composite action `check-unreleased-changelog`.
- Composite action `codeql-analyze`.
- Composite action `lint-c`.
- Composite action `lint-go`.
- Composite action `lint-node`.
- Composite action `lint-php`.
- Composite action `lint-python`.
- Composite action `lint-rust`.
- Composite action `trivy-security-scan`.
- Composite action `update-changelog`.
- Composite action `validate-changelog`.
- Composite action `validate-launcher-metadata`.
- Release and changelog badges in `README.md`.

### Changed

- `trivy.yml` now accepts `json-file` and `sarif-file` inputs and uploads the Trivy scan results as a workflow artifact.
- `trivy-security-scan` now enables the `misconfig` scanner by default via a new `scanners` input.
- `trivy-security-scan` now runs a single `trivy fs` scan (via `aquasecurity/setup-trivy`) and derives the SARIF report with `trivy convert`, instead of running `aquasecurity/trivy-action` twice.
- `trivy-security-scan`'s Security tab SARIF upload now sets `category: trivy-fs`.
- Extracted the inline Python in `validate-changelog` and `update-changelog` composite actions into standalone `.py` scripts.
- `release-vita-launcher.yml` rebases onto the latest `$RELEASE_BRANCH` (with autostash) before committing and pushing.
- `README.md` Structure section now shows a file tree instead of a bullet list.

### Removed

- `release-vita-launcher.yml` no longer runs a security scan job (not needed for this workflow).

### Fixed

- Replaced placeholder `OWNER/reusable-workflows` action references with `k-3679/reusable-workflows` in `lint.yml` and `trivy.yml` (originally named `security-scan.yml`).
- `release-vita-launcher.yml` now calls `restrict-branch.yml` and `lint.yml` via `k-3679/reusable-workflows@main` instead of local relative paths.
- `trivy-security-scan`: bumped `aquasecurity/trivy-action` from `0.28.0` (tag no longer exists upstream, broke every workflow run) to `v0.36.0`.
- `trivy-security-scan`: bumped `github/codeql-action/upload-sarif` from `v3` to `v4` (v3 deprecated December 2026).
- `security-scan.yml` and `release-vita-launcher.yml`: added missing `actions: read` permission, required by `codeql-action/upload-sarif` (was failing with "Resource not accessible by integration").
- `trivy-security-scan`: authenticate Trivy DB downloads with `GITHUB_TOKEN` to avoid GHCR anonymous pull rate limits.
- Renamed `security-scan.yml` to `trivy.yml` and updated the `release-vita-launcher.yml` reference to match.
- `codeql.yml`: `matrix` was assigned directly from `fromJSON(inputs.languages)`, which required callers to pass a full `{"include": [...]}` matrix object; a plain JSON array failed with "A sequence was not expected". `languages` is now wrapped under `matrix.include` internally.
