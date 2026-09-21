# trivy-security-scan

Scans the checked-out tree with Trivy for vulnerabilities, leaked secrets and misconfigurations, uploads the findings to the Security tab, and fails the job when too many of them are high or critical.

## Usage

```yaml
- uses: actions/checkout@v7

- uses: k-3679/reusable-workflows/.github/actions/trivy-security-scan@main
  id: trivy
  with:
    fail-threshold-percent: 0
```

The job needs `security-events: write` and `actions: read` for the upload.

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `scan-ref` | `.` | Path to scan |
| `scanners` | `vuln,secret,misconfig` | Trivy scanners to run |
| `severity` | `CRITICAL,HIGH,MEDIUM,LOW` | Severities to include in the report |
| `fail-threshold-percent` | `0` | Fail when high/critical findings make up more than this percentage of all findings. `0` means any high or critical finding fails |
| `sarif-file` | `trivy-report.sarif` | Where to write the SARIF report |
| `json-file` | `trivy-report.json` | Where to write the JSON report |

## Outputs

| Output | Description |
| --- | --- |
| `total` | Number of findings |
| `highcrit` | Number of high and critical findings |
| `percentage` | `highcrit` as a percentage of `total`, two decimals |

## How it works

Trivy runs twice over the same path: once producing SARIF for the Security tab, once producing JSON for the threshold check. The threshold is a share, not a count, so `fail-threshold-percent: 20` allows one high finding among five lows but not two.
