# Vulnerability Triage Workflow

Use this folder as the evidence area for validated findings. Do not store real secrets here.

## Finding lifecycle

1. **Detected** — scanner reports a finding.
2. **Validated** — security owner confirms it is exploitable/relevant.
3. **Classified** — record severity, affected component, CVE/CWE when available, and evidence.
4. **Decision** — remediate, accept risk, or mark false positive with justification.
5. **Remediated** — record the code/dependency/configuration change.
6. **Rescanned** — rerun the relevant scanner and record the result.
7. **Closed** — close only after the finding is fixed or formally risk-accepted.

## Severity gate

| Severity | Pipeline behavior | Target action |
|---|---|---|
| CRITICAL | Fail | Immediate remediation |
| HIGH | Fail | Remediate before merge/release |
| MEDIUM | Tool-dependent / report | Prioritize in backlog |
| LOW | Report | Track and fix as practical |
| INFO | Report | Informational only |

The current GitHub Actions workflow uses hard gates for Semgrep `ERROR`, pip-audit findings, Gitleaks findings, and Trivy `HIGH,CRITICAL` findings.

## Triage record

Copy `template.md` for each validated finding and name it with an internal identifier, e.g. `SEC-001.md`.
