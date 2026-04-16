# Secure Development Controls — DevSecOps Pipeline and Build Security

**Source:** NIST SP 800-218 v1.1; SLSA Framework v1.0; OWASP CI/CD Security Top 10; OpenSSF Scorecard; EO 14028; OMB M-22-18; OMB M-23-16

This reference documents the technical controls for securing the software development pipeline, build environment, and software supply chain, aligned to SSDF practice groups PO and PS.

---

## DevSecOps Pipeline Architecture

A DevSecOps pipeline integrates security tooling and policy gates directly into the CI/CD workflow. The pipeline must not be optional — security gates enforce that releases cannot proceed without passing security checks.

### Required Pipeline Security Stages

```
[Developer Workstation]
  pre-commit hooks:
    - secrets detection (gitleaks / detect-secrets)
    - code formatting / linting compliance
    - SAST lite check (Semgrep, fast rules)

[Version Control — Pull Request Opened]
  automated status checks (required to pass before merge):
    - SAST full scan (SonarQube / Semgrep / CodeQL)
    - SCA scan (OWASP Dependency-Check / Snyk / Black Duck)
    - IaC scan (checkov / tfsec / terrascan) if IaC modified
    - Secrets scan (trufflehog / gitleaks on diff + history)
    - Licence compliance check (FOSSA / Licensee)
  human checks (required to pass before merge):
    - Minimum 2 reviewers approved
    - CODEOWNERS approval for security-critical modules
    - Security review for changes to auth, crypto, admin modules

[CI Build — On Merge to Main]
  build stage:
    - Dependency install from private proxy/cache
    - Compile with security hardening flags (PW.6)
    - Unit tests + security unit tests
  security scan stage:
    - Container image build + image vulnerability scan (Trivy / Snyk Container)
    - SBOM generation (Syft / CycloneDX CLI)
    - SLSA provenance generation
  artifact publishing:
    - Sign artifact (cosign / GPG)
    - Publish to controlled artifact registry with metadata

[Pre-Release Test Environment Deployment]
  DAST:
    - OWASP ZAP baseline scan (automated)
    - API security scan
  security integration tests:
    - Security regression test suite
    - Authentication and authorisation test cases
  penetration test:
    - Full application penetration test for major releases
    - Limited scope spot-check for minor releases

[Release Approval Gate]
  automated checks:
    - All previous gates passed
    - No open critical/high vulnerabilities without risk acceptance
    - SBOM generated and signed
    - Artifact signature verified
  human approval:
    - Release manager approval
    - Security sign-off for major releases

[Production Deployment]
  deployment controls:
    - Signed artifact verified before deployment
    - SBOM published to consumers or stored in repository
    - Deployment recorded in change management system

[Production Monitoring]
  runtime security monitoring:
    - CVE alert feed monitoring against deployed SBOM components
    - WAF and runtime anomaly detection
    - Dependabot / Renovate continuous dependency update PRs
```

---

## SAST Configuration

### Semgrep Recommended Rulesets for SSDF

| Ruleset | Focus | SSDF Practice |
|---------|-------|--------------|
| p/security-audit | Broad security patterns | PW.5, PW.7 |
| p/owasp-top-ten | OWASP Top 10 vulnerabilities | PW.5, PW.7 |
| p/cwe-top-25 | CWE Top 25 dangerous weaknesses | PW.5, PW.7 |
| p/secrets | Hardcoded credentials and API keys | PS.1 |
| p/supply-chain | Supply chain risk patterns | PW.4 |
| p/jwt | JSON Web Token misuse | PW.5 |
| p/xss | Cross-site scripting | PW.5 |
| p/sql-injection | SQL injection patterns | PW.5 |
| p/insecure-transport | HTTP usage, weak TLS | PW.5 |

### SARIF Output and Integration

Static Analysis Results Interchange Format (SARIF) v2.1.0 is the standard format for SAST tool outputs. SARIF enables:
- Unified finding display in GitHub Code Scanning or Azure DevOps
- Finding deduplication across multiple scanners
- Historical trending of finding count by severity
- PR annotations showing findings inline on changed lines

SARIF severity mapping:
- `error` → SAST finding blocks PR merge (Critical/High threshold)
- `warning` → SAST finding displayed but does not block
- `note` → Informational finding

### CodeQL Queries for SSDF-Critical CWEs

| CQL Query Name | CWE | SSDF Practice |
|----------------|-----|--------------|
| SqlInjection | CWE-89 | PW.5 |
| ReflectedXss | CWE-79 | PW.5 |
| StoredXss | CWE-79 | PW.5 |
| UnsafeDeserializationOfUserInput | CWE-502 | PW.5 |
| CommandInjection | CWE-78 | PW.5 |
| PathInjection | CWE-22 | PW.5 |
| SensitiveDataLogged | CWE-532 | PW.5, PO.2 |
| HardcodedCredentials | CWE-798 | PS.1 |
| InsecureRandomness | CWE-338 | PW.5 |
| UnusedCatchBlock | CWE-390 | PW.5 |
| RegexInjection | CWE-730 | PW.5 |

---

## SCA and Dependency Management

### Software Composition Analysis Scanning Coverage

SCA tools must analyse:
1. Direct dependencies declared in manifests (package.json, requirements.txt, pom.xml, go.mod, Gemfile, Cargo.toml)
2. Transitive (indirect) dependencies pulled in by direct dependencies
3. OS-level packages in container images (RPM, DEB packages)
4. Libraries statically compiled into executables (where detectable)
5. Development dependencies (may not require same urgency as production but should be monitored)

### Dependency Version Pinning Strategy

| Level | Description | Benefit | Risk |
|-------|-------------|---------|------|
| Dependency Range (e.g., ^1.2.0) | Allows minor/patch updates | Automatic security patches | Non-deterministic builds; may pull breaking changes |
| Version Lock (pin to e.g., 1.2.3) | Specific version only | Deterministic builds | Must manually update; risks missing security patches |
| Hash Pinning (pin to SHA-256 of package) | Specific content hash | Maximum integrity assurance | Requires manual update on any change |

**SSDF recommendation:** Use version pinning with a lock file (package-lock.json, poetry.lock, go.sum) for deterministic builds. Supplement with automated dependency update pull requests (Dependabot or Renovate) configured to create PRs for patch and minor updates with SCA scan on each. Hash pinning recommended for critical cryptographic or authentication libraries.

### OWASP Dependency-Check Integration

OWASP Dependency-Check (ODC) identifies project dependencies with known published CVEs.

```yaml
# ODC CI/CD integration example (GitHub Actions)
- name: Run OWASP Dependency-Check
  uses: dependency-check/dependency-check-action@main
  with:
    project: 'my-project'
    path: '.'
    format: 'SARIF'
    args: >
      --failOnCVSS 7
      --enableRetired
      --suppression suppression.xml
  env:
    JAVA_HOME: ${{ env.JAVA_HOME_17_X64 }}

- name: Upload ODC results to GitHub Security
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: reports/dependency-check-report.sarif
```

---

## Secrets Management Controls

### Secret Types and Detection Patterns

| Secret Type | Detection Pattern (regex class) | Rotation Action |
|------------|-------------------------------|-----------------|
| AWS Access Key | AKIA[0-9A-Z]{16} | Immediate key revocation in IAM |
| AWS Secret Key | 40-char base64 adjacent to AKIA key | Immediate key revocation |
| GitHub PAT (classic) | ghp_[a-zA-Z0-9]{36} | Revoke token at github.com/settings/tokens |
| GitHub App Installation Token | ghs_[a-zA-Z0-9]{36} | Token auto-expires but revoke immediately |
| Generic API Key | api_key|apikey|api-key followed by 20+ char value | Identify service → revoke in service console |
| Private Key (PEM) | -----BEGIN (RSA|EC|OPENSSH|PRIVATE) KEY----- | Generate new key pair; rotate all dependent certs |
| Database URL with password | (postgres|mysql|mongodb):\/\/[^:]+:[^@]+@ | Rotate database user password |
| JWT Secret | Common variable names: JWT_SECRET, SECRET_KEY + long string | Rotate secret; invalidate all existing JWTs |
| Slack Webhook URL | hooks.slack.com/services/[^ ]+ | Regenerate webhook in Slack app settings |
| NPM Auth Token | npm_[a-zA-Z0-9]{36} | Revoke token at npmjs.com |

### Secrets Management Platform Integration

Recommended secrets delivery pattern for build pipelines:

```
[Pipeline Job Starts]
  → CI/CD platform authenticates to secrets manager using OIDC workload identity
  → Secrets manager validates OIDC token claims (repository, workflow, branch)
  → Secrets manager returns time-limited secret value or temporary credentials
  → Secret injected as environment variable ONLY for the job scope
  → Secret NOT written to disk, NOT included in logs
  [Pipeline Job Ends]
  → Temporary credentials expire automatically
  → No secret persists in pipeline environment
```

OIDC-based authentication eliminates the need for long-lived static credentials in CI/CD pipelines — the most common source of supply chain CI/CD compromises.

Supported patterns:
- GitHub Actions → AWS (OIDC): `aws-actions/configure-aws-credentials`
- GitHub Actions → Vault (OIDC): `hashicorp/vault-action`
- GitLab CI → AWS (OIDC): `id_tokens` block with `sts:AssumeRoleWithWebIdentity`
- Azure DevOps → Azure Key Vault: Service connection with workload identity federation

---

## Container Security Controls

Container images are a common software delivery artifact. Container security requirements:

### Image Build Security

| Control | Implementation |
|---------|---------------|
| Base image selection | Use official minimal base images: distroless, alpine, ubi-minimal; avoid generic ubuntu/debian for production |
| Base image version pinning | Pin base image to digest: `FROM gcr.io/distroless/java17-debian12@sha256:<hash>` |
| CVE-free at build time | Run Trivy or Snyk Container scan; fail build if CRITICAL OS CVEs present |
| No secrets in image layers | SAST scan Dockerfiles for secret patterns; verify with docker history inspection |
| Run as non-root | Dockerfile must include `USER nonroot` or equivalent non-UID-0 user |
| Read-only root filesystem | Set `readOnlyRootFilesystem: true` in Kubernetes securityContext |
| Drop all capabilities | Set `capabilities: drop: ["ALL"]` in Kubernetes securityContext |
| No privileged containers | Prohibit `privileged: true` except for explicitly approved infrastructure workloads |

### Container Image Signing with cosign / Sigstore

```bash
# Sign an image using cosign with GitHub Actions OIDC (keyless signing)
cosign sign --yes "${IMAGE_NAME}@${IMAGE_DIGEST}"

# Verify image signature (consumer side)
cosign verify \
  --certificate-identity-regexp "https://github.com/org/repo/.github/workflows/release.yml" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  "${IMAGE_NAME}@${IMAGE_DIGEST}"
```

Sigstore keyless signing uses short-lived certificates issued by the Fulcio certificate authority, with signed timestamps recorded in the Rekor transparency log. This provides:
- No long-lived signing key to protect
- Verifiable link between the signed artifact and the GitHub Actions workflow that produced it
- Public audit trail of all signatures in Rekor

---

## SBOM Generation and Consumption

### Generating SBOMs with Syft

```bash
# Generate CycloneDX JSON SBOM from a container image
syft scan "${IMAGE_NAME}@${IMAGE_DIGEST}" \
  --output cyclonedx-json="sbom.cdx.json" \
  --output spdx-json="sbom.spdx.json"

# Generate SBOM from filesystem/source code
syft scan dir:./src --output cyclonedx-json="sbom-src.cdx.json"

# Attach SBOM to OCI image as attestation using cosign
cosign attest --yes \
  --predicate sbom.cdx.json \
  --type cyclonedx \
  "${IMAGE_NAME}@${IMAGE_DIGEST}"
```

### SBOM Quality Checks

A high-quality SBOM must meet these criteria:

| Quality Dimension | Minimum Requirement |
|------------------|---------------------|
| Completeness | All direct and transitive dependencies included |
| Identifiability | Each component has at least one of: PURL, CPE, or package name + version |
| Machine-readability | SPDX JSON or CycloneDX JSON format |
| Accuracy | Package versions match what is installed (not just what is declared in manifest) |
| Freshness | Generated from the specific build output, not from manifest alone |
| Integrity | SBOM itself is signed (producer signs the SBOM file) |

### SBOM Consumption for Vulnerability Monitoring

SBOM-based CVE monitoring workflow:

```
[SBOM File] → Extract package list (name, version, PURL/CPE)
  → Query OSV.dev API for each package:
     GET https://api.osv.dev/v1/query
     Body: {"package": {"name": "<pkg>", "ecosystem": "<npm|pypi|maven|...>"}, "version": "<version>"}
  → Query NVD API for each CPE:
     GET https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=<cpe>
  → Alert on any result with CVSS >= configured threshold
  → Create vulnerability management ticket for each new match
  → Re-query on scheduled interval (daily minimum)
```

---

## EO 14028 / OMB M-22-18 Software Attestation

### Self-Attestation Requirements

Software producers providing software to federal agencies must, under OMB M-22-18 and M-23-16, provide:

1. A software attestation form confirming adherence to SSDF practices
2. Supporting artifacts on request: SBOMs, test reports, vulnerability scan results

**Attestation form required assertions (aligned to SSDF):**

| Assertion | SSDF Mapping |
|-----------|-------------|
| The software was developed and built in secure environments | PO.5 |
| Authorised access to developer environments is enforced | PO.5.2 |
| Software source code is protected from unauthorised access | PS.1 |
| The software is verified for integrity via signed artifacts or hashes | PS.2 |
| Software dependencies are inventoried (SBOM) | PS.2, PS.3 |
| Vulnerability scanning is performed during development | PW.7, PW.9 |
| Vulnerabilities are addressed on a risk-prioritised basis | RV.2 |
| Software code is reviewed for security vulnerabilities | PW.7 |

### Third-Party Assessment

For critical software (as defined by CISA criteria), self-attestation is not sufficient. A third-party assessment organisation (3PAO) or government-authorised assessor must:

1. Review the software producer's SSDF practices against a defined criteria
2. Inspect SDLC documentation, toolchain configuration, and policy records
3. Test the attestation claims against observable evidence
4. Issue a third-party assessment report

Critical software categories (CISA definition): software that operates with elevated privilege, performs critical system functions, or is directly integrated into operational technology or national security systems.

---

## Security Metrics for DevSecOps Programme

| Metric | Description | Target | Measurement Source |
|--------|-------------|--------|-------------------|
| SAST finding density | Number of SAST findings per 1,000 lines of code | Decreasing trend; below baseline threshold | SAST scan results per release |
| Mean time to remediate — Critical | Average days from critical CVE publication to patch release | <= 15 days | Vulnerability management system |
| Mean time to remediate — High | Average days from high CVE publication to patch release | <= 30 days | Vulnerability management system |
| Dependency freshness | Percentage of dependencies within one major version of latest | >= 90% | SCA scan results |
| EOL dependency count | Number of production dependencies past end-of-life | 0 (or approved exception) | SCA + vendor EOL calendar |
| SBOM completeness rate | Percentage of releases with complete, signed SBOM | 100% | Artifact registry metadata |
| Secrets in code incidents | Number of confirmed secrets committed to code repository | 0 per quarter | Repository scanning results |
| Security training completion | Percentage of developers with current security training | 100% of production code contributors | LMS completion records |
| Pipeline security gate bypass count | Number of approved exceptions to security pipeline gates | <= 2 per quarter with full documentation | Pipeline bypass log |
| Pen test finding closure rate | Percentage of pen test findings closed within SLA | >= 95% | Vulnerability management system |

---

## OWASP CI/CD Security Top 10 Mapping to SSDF

| OWASP CI/CD Risk | Description | SSDF Controls |
|-----------------|-------------|--------------|
| CICD-SEC-1: Insufficient Flow Control Mechanisms | Ability to push code without reviews and checks | PO.4, PS.1 (branch protection, required gates) |
| CICD-SEC-2: Inadequate Identity and Access Management | Excessive pipeline permissions; shared pipeline credentials | PO.5.3 (least privilege, OIDC-based auth) |
| CICD-SEC-3: Dependency Chain Abuse | Malicious packages; dependency confusion | PW.4 (component evaluation, private proxy, hash pinning) |
| CICD-SEC-4: Poisoned Pipeline Execution | Injecting code into pipeline via pull request triggers | PO.5.3 (pipeline isolation; no privileged access to untrusted code) |
| CICD-SEC-5: Insufficient Pipeline Based Access Controls | Secrets accessible to all pipeline jobs | PO.5.3 (secret scoping; OIDC; no long-lived secrets) |
| CICD-SEC-6: Insufficient Credential Hygiene | Hardcoded credentials in pipeline definitions or source code | PS.1.2 (secrets scanning), PO.5.3 (secrets manager integration) |
| CICD-SEC-7: Insecure System Configuration | Misconfigured version control, artifact registry, or pipeline platform | PO.5 (secure environment baseline) |
| CICD-SEC-8: Ungoverned Usage of 3rd Party Services | Unreviewed third-party actions or integrations with access to pipeline | PW.4 (third-party component evaluation), PO.3 (toolchain governance) |
| CICD-SEC-9: Improper Artifact Integrity Validation | Deploying artifacts without verifying integrity or provenance | PS.2 (signing and hash verification), PS.3 (immutable archive) |
| CICD-SEC-10: Insufficient Logging and Visibility | Lack of audit trail for pipeline activity | PO.5 (audit logging), PW.9 (test evidence retention) |
