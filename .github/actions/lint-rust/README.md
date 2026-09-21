# lint-rust

Installs a Rust toolchain with Clippy and runs `cargo clippy --all-targets -- -D warnings` in a Cargo project. Warnings are treated as errors.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/lint-rust@main
  with:
    path: crates/app
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `toolchain` | `stable` | Rust toolchain passed to `dtolnay/rust-toolchain` |
| `path` | `.` | Directory containing `Cargo.toml` |
