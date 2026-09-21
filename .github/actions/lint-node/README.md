# lint-node

Sets up Node.js and runs ESLint 8 over a glob of files.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/lint-node@main
  with:
    glob: "src/**/*.js"
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `node-version` | `20` | Node.js version passed to `actions/setup-node` |
| `eslint-config` | `.eslintrc.json` | Path to the ESLint config |
| `glob` | `**/*.js` | Files to lint |

ESLint is installed at version 8, which reads the classic `.eslintrc.*` format. A flat `eslint.config.js` will not be picked up.
