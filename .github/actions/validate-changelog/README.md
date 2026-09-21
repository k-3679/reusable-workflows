# validate-changelog

Checks that a PR or push added a properly formed entry to the `[Unreleased]` section of a Keep a Changelog `CHANGELOG.md`.

## Usage

```yaml
- uses: actions/checkout@v7
  with:
    fetch-depth: 0

- uses: k-3679/reusable-workflows/.github/actions/validate-changelog@main
  with:
    base-sha: ${{ github.event.pull_request.base.sha || github.event.before }}
```

Needs full history (`fetch-depth: 0`) so it can read the changelog at `base-sha`.

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `changelog-file` | `CHANGELOG.md` | Path to the changelog |
| `base-sha` | `""` | Commit to compare against. Empty or unknown falls back to the merge-base with `default-branch` |
| `default-branch` | `main` | Branch used for the merge-base fallback |

## What it checks

The `[Unreleased]` section must:

- exist and not be empty
- differ from the one at `base-sha`
- group every entry under one of `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, `### Security`
- not repeat a category or leave one empty
- write each entry as a `- ` bullet of at least three words (indented lines continue the bullet above)

A valid section looks like this:

```markdown
## [Unreleased]

### Added

- New `--dry-run` flag for the sync command.

### Fixed

- Config loader no longer crashes on an empty file.
```

Every problem is reported as an annotation on the offending line, so you can fix them all in one go.
