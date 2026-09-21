# update-changelog

Turns the `[Unreleased]` section of a `CHANGELOG.md` into a versioned release section and updates the compare links at the bottom of the file. Meant to run in a release workflow, right before the changelog is committed and tagged.

## Usage

```yaml
- uses: k-3679/reusable-workflows/.github/actions/update-changelog@main
  id: changelog
  with:
    new-version: 1.4.0
    new-tag: v1.4.0
    release-date: 2026-09-21
    repo-url: ${{ github.server_url }}/${{ github.repository }}
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `changelog-file` | `CHANGELOG.md` | Path to the changelog. If the file is missing the step is skipped |
| `new-version` | required | Version for the new section heading, e.g. `1.4.0` |
| `new-tag` | required | Git tag for the release, e.g. `v1.4.0` |
| `release-date` | required | Date for the heading, `YYYY-MM-DD` |
| `repo-url` | required | Repository URL, used to build the compare links |
| `fail-on-empty` | `false` | Fail instead of releasing an empty version section when `[Unreleased]` has no entries |

## Outputs

| Output | Description |
| --- | --- |
| `updated` | `true` if the file was rewritten, `false` if it was missing or had no `[Unreleased]` section |

## What it does

Given this:

```markdown
## [Unreleased]

### Fixed

- Config loader no longer crashes on an empty file.

[unreleased]: https://github.com/org/repo/compare/v1.3.0...HEAD
```

it writes this:

```markdown
## [Unreleased]

## [1.4.0] - 2026-09-21

### Fixed

- Config loader no longer crashes on an empty file.

[unreleased]: https://github.com/org/repo/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/org/repo/compare/v1.3.0...v1.4.0
```

If there is no previous `[unreleased]` link, the new version links to its release page instead of a compare view.
