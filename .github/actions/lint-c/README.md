# lint-c

Runs `cppcheck` over a directory with the `warning`, `style`, `performance` and `portability` checks enabled. Any finding fails the step.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/lint-c@main
  with:
    path: src
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `path` | `.` | Directory to lint |

`cppcheck` is installed with `apt-get`, so this only works on Ubuntu runners.
