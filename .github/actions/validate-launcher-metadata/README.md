# validate-launcher-metadata

Fails unless the launcher metadata file is valid JSON with a semantic `version` field.

## Usage

```yaml
- uses: k-3679/reusable-workflows/.github/actions/validate-launcher-metadata@main
  with:
    metadata-file: launcher.json
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `metadata-file` | `launcher.json` | Path to the metadata file |

## What it checks

- the file exists
- it parses as JSON
- it has a `version` field
- the version matches `X.Y.Z` (digits only, no prefix or suffix)
