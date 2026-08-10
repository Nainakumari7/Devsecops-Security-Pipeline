name: Security Finding
description: Track a validated security finding through remediation and rescan.
title: "[SEC] "
labels: [security]
body:
  - type: input
    id: scanner
    attributes:
      label: Scanner
      placeholder: Semgrep / pip-audit / Gitleaks / Trivy
    validations:
      required: true
  - type: dropdown
    id: severity
    attributes:
      label: Severity
      options:
        - Critical
        - High
        - Medium
        - Low
        - Info
    validations:
      required: true
  - type: textarea
    id: evidence
    attributes:
      label: Evidence and validation
    validations:
      required: true
  - type: textarea
    id: remediation
    attributes:
      label: Remediation plan
    validations:
      required: true
