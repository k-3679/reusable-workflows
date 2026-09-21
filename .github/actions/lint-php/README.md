# lint-php

Sets up PHP and runs `php -l` on every `.php` file under a directory. This is a syntax check only; it does not enforce code style.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/lint-php@main
  with:
    php-version: "8.3"
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `php-version` | `8.2` | PHP version passed to `shivammathur/setup-php` |
| `path` | `.` | Directory searched for `.php` files |

All files are checked before the step fails, so one broken file does not hide the others.
