# lint-python

Sets up Python and runs `ruff check` on a file or directory.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/lint-python@main
  with:
    path: src
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `python-version` | `3.12` | Python version passed to `actions/setup-python` |
| `path` | `.` | File or directory to lint |

Rules and exclusions come from the repository's `pyproject.toml` or `ruff.toml`, if there is one.
