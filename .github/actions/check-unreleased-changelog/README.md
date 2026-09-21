# check-unreleased-changelog

Fails if the `[Unreleased]` section of a `CHANGELOG.md` has entries in it. Point it at the target branch of a PR to make sure everything already on that branch has been released before more changes land.

## Usage

```yaml
- uses: actions/checkout@v7
  with:
    fetch-depth: 0

- uses: k-3679/reusable-workflows/.github/actions/check-unreleased-changelog@main
  with:
    ref: ${{ github.event.pull_request.base.sha }}
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `changelog-file` | `CHANGELOG.md` | Path to the changelog |
| `ref` | `HEAD` | Commit or ref to read the changelog from |

## What it checks

Reads the file as it exists at `ref`, takes everything between `## [Unreleased]` and the next `## [` heading, and fails if any non-blank line is left. Also fails if the file does not exist at `ref`.
