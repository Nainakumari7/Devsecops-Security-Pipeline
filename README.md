# DevSecOps Security Pipeline

A working CI security pipeline for a small Python/Flask application using GitHub Actions, Semgrep, pip-audit, Dependabot, Gitleaks, and Trivy.

## What this demonstrates

- **SAST:** Semgrep scans Python source and gates `ERROR` findings.
- **Dependency security:** pip-audit scans Python dependencies; Dependabot opens update PRs weekly.
- **Secret detection:** Gitleaks scans repository history/content.
- **Container security:** Trivy scans the Docker image and fails on `HIGH` or `CRITICAL` vulnerabilities.
- **Severity gates:** high-impact findings stop the CI pipeline.
- **Vulnerability triage:** validated findings can be documented from detection through remediation and repeat scan.

## Project structure

```text
.
├── app/main.py
├── tests/test_main.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── semgrep.yml
├── .gitleaks.toml
├── .github/
│   ├── dependabot.yml
│   ├── workflows/security.yml
│   └── ISSUE_TEMPLATE/security-finding.md
├── triage/
│   ├── README.md
│   └── template.md
├── SECURITY.md
└── README.md
```

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
python app/main.py
```

Then open `http://127.0.0.1:5000/health`.

## Run the security tools locally

Install the tools separately if they are not already available:

```bash
pip install pip-audit
pip-audit -r requirements.txt --strict --desc
semgrep scan --config semgrep.yml --error --severity ERROR
```

Gitleaks and Trivy are normally installed through their official releases/package managers. The GitHub Actions workflow runs them automatically in CI.

## GitHub setup

1. Create a GitHub repository and push this project to it.
2. Keep the default branch named `main` or update the workflow branch.
3. Enable Issues if you want to use the triage template.
4. Push a change or run **Actions → Security Pipeline → Run workflow**.
5. Review each gate in the workflow summary.

For a stronger production setup, protect `main` with required status checks for `Semgrep SAST gate`, `pip-audit dependency gate`, `Gitleaks secret gate`, and `Trivy container gate`.

## Demonstrating the triage workflow

Use a safe, intentionally non-secret test finding or a real scanner finding from this owned application. For each finding:

1. Copy `triage/template.md` to `triage/SEC-001.md`.
2. Record scanner, severity, evidence, and validation.
3. Decide: remediate, false positive, or risk acceptance.
4. Make the remediation.
5. Run the scanner again.
6. Record the rescan result and close the finding.

Do not add fake credentials merely to demonstrate Gitleaks. If you need to demonstrate the gate, use a disposable test repository/branch and remove the test secret immediately after the demonstration.

## Interview-ready summary

> Built a GitHub Actions DevSecOps pipeline for a Python application integrating Semgrep SAST, pip-audit and Dependabot for dependency security, Gitleaks for secret detection, and Trivy for container scanning. Added severity-based CI gates and a structured vulnerability-triage process covering validation, false positives, remediation, risk acceptance, and repeat scans.
