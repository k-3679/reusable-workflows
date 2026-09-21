# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added CodeQL badge in `README.md`.
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

- Every composite action now has a `README.md` with usage, inputs and what it checks; the root `README.md` lists them.
- `validate-changelog` now enforces Keep a Changelog structure in `[Unreleased]`: entries must be `- ` bullets of at least three words, grouped under a known category (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`) that is neither empty nor duplicated. Errors are reported as file/line annotations.
- `trivy.yml` now accepts `json-file` and `sarif-file` inputs and uploads the Trivy scan results as a workflow artifact.
- `trivy-security-scan` now enables the `misconfig` scanner by default via a new `scanners` input.
- Extracted the inline Python in `validate-changelog` and `update-changelog` composite actions into standalone `.py` scripts.
- `release-vita-launcher.yml` rebases onto the latest `$RELEASE_BRANCH` (with autostash) before committing and pushing.
- `README.md` Structure section now shows a file tree instead of a bullet list.

### Removed

- `release-vita-launcher.yml` no longer runs a security scan job (not needed for this workflow).

### Fixed

- `codeql-analyze`: typo in the `queries` input description.
- `validate-changelog`: the `[Unreleased]` body was only terminated by a bracketed `## [` heading, so any following non-bracketed `## ` heading was treated as part of the section.
- Replaced placeholder `OWNER/reusable-workflows` action references with `k-3679/reusable-workflows` in `lint.yml` and `trivy.yml` (originally named `security-scan.yml`).
- `release-vita-launcher.yml` now calls `restrict-branch.yml` and `lint.yml` via `k-3679/reusable-workflows@main` instead of local relative paths.
- `trivy-security-scan`: bumped `aquasecurity/trivy-action` from `0.28.0` (tag no longer exists upstream, broke every workflow run) to `v0.36.0`.
- `trivy-security-scan`: bumped `github/codeql-action/upload-sarif` from `v3` to `v4` (v3 deprecated December 2026).
- `security-scan.yml` and `release-vita-launcher.yml`: added missing `actions: read` permission, required by `codeql-action/upload-sarif` (was failing with "Resource not accessible by integration").
- `trivy-security-scan`: authenticate Trivy DB downloads with `GITHUB_TOKEN` to avoid GHCR anonymous pull rate limits.
- Renamed `security-scan.yml` to `trivy.yml` and updated the `release-vita-launcher.yml` reference to match.
- `codeql.yml`: `matrix` was assigned directly from `fromJSON(inputs.languages)`, which required callers to pass a full `{"include": [...]}` matrix object; a plain JSON array failed with "A sequence was not expected". `languages` is now wrapped under `matrix.include` internally.
- `trivy-security-scan`: `trivy convert` has no knowledge of the original scan directory, so it set the SARIF's `originalUriBaseIds.ROOTPATH.uri` to the JSON report file's own path instead of the repo root, which would break file/line links for any real findings. A `jq` step now patches `ROOTPATH` to `$GITHUB_WORKSPACE` after conversion.
