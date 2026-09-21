# lint-go

Sets up Go and runs `golangci-lint` in a directory.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/lint-go@main
  with:
    go-version: "1.23"
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `go-version` | `stable` | Go version passed to `actions/setup-go` |
| `path` | `.` | Directory containing the module to lint |

Linters and their settings come from the repository's own `.golangci.yml`, if there is one.
