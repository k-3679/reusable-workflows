# codeql-analyze

Runs CodeQL for one language and uploads the results to the repository's Security tab. The `codeql.yml` reusable workflow calls this once per language from a matrix; you can also call it directly.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/codeql-analyze@main
  with:
    language: python
    build-mode: none
```

For compiled languages that CodeQL cannot build on its own, use `build-mode: manual` and pass the build steps:

```yaml
- uses: k-3679/reusable-workflows/.github/actions/codeql-analyze@main
  with:
    language: c-cpp
    build-mode: manual
    build-command: |
      cmake -B build
      cmake --build build
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `language` | required | CodeQL language: `actions`, `c-cpp`, `csharp`, `go`, `java-kotlin`, `javascript-typescript`, `python`, `ruby`, `rust`, `swift` |
| `build-mode` | required | `none`, `autobuild` or `manual` |
| `queries` | `""` | Extra query packs, comma-separated: `security-extended`, `security-and-quality` |
| `build-command` | `""` | Shell commands to build the project. Required when `build-mode` is `manual` |

Results are uploaded under the category `/language:<language>`, so several languages in one workflow do not overwrite each other.
