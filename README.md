# reusable-workflows

Shared, reusable GitHub Actions workflows and composite actions, extracted out of individual project repos so they can be maintained and versioned in one place.

## Structure

- `.github/workflows/`: reusable workflows (`workflow_call`), invoked from other repos via `uses: <org>/reusable-workflows/.github/workflows/<file>.yml@<ref>`.
- `.github/actions/`: composite actions, invoked via `uses: <org>/reusable-workflows/.github/actions/<name>@<ref>`.
