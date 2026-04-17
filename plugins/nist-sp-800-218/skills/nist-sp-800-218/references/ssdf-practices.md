# SSDF Practices Reference — All Practice Groups

**Source:** NIST SP 800-218 v1.1, February 2022
**CSRC:** https://csrc.nist.gov/publications/detail/sp/800-218/final

This reference provides the complete SSDF practice inventory with all tasks and representative implementation examples, serving as a detailed lookup for each of the 19 active practices across four practice groups.

---

## PO: Prepare the Organisation

**Purpose:** Establish the organisational conditions, processes, and resources necessary to ensure that software development is performed securely throughout the SDLC.

### PO.1 — Define Security Requirements for Software Development

**Practice description:** Ensure that security requirements that apply to software that the organisation produces are identified, prioritised, and integrated into the SDLC.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PO.1.1 | Identify and communicate the organisation-wide security and privacy requirements to which software must adhere | Map applicable laws (FISMA, HIPAA, PCI DSS, state privacy laws), contractual obligations, and organisational policies to a software security requirement baseline; publish as internal standard |
| PO.1.2 | Identify and communicate the security and privacy requirements for each software project | Conduct application risk classification at project initiation; derive requirements from threat model, data classification, and applicable compliance scope; document in the project security requirements specification |
| PO.1.3 | Periodically review and revise the security requirements to address changes in the threat landscape and regulatory environment | Annual review cycle; ad-hoc review triggered by new CVE patterns, regulatory changes, or significant architectural changes |

**Key frameworks linked:**
- OWASP Application Security Verification Standard (ASVS): requirement levels 1/2/3 corresponding to application risk tier
- CWE Top 25 Most Dangerous Software Weaknesses: use as a minimum requirements reference
- NIST SP 800-53 SA-8 (Security and Privacy Engineering Principles), SA-15 (Development Process, Standards, and Tools)

---

### PO.2 — Implement Roles and Responsibilities

**Practice description:** Ensure that everyone participating in the SDLC is prepared to perform their security-related activities.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PO.2.1 | Create new roles or add security duties to existing roles to ensure security activities are owned and performed | Define security responsibilities in job descriptions for: developers (secure coding), architects (threat modelling, secure design), DevOps (pipeline security), product owners (security requirements prioritisation), QA (security test case development) |
| PO.2.2 | Provide role-appropriate training for all SDLC participants on their security responsibilities | Annual role-based security training; new hire security onboarding; training currency tracked in LMS |
| PO.2.3 | Conduct security awareness training for all individuals performing software development | OWASP Top 10 coding awareness; language-specific secure coding examples; phishing and social engineering awareness for developers |

**Security champion programme:**

A security champion is a developer or engineer who serves as the primary security point of contact within their development team. The programme:

1. Selects champions from volunteer developers with security interest
2. Provides champions with advanced training (CISSP, CSSLP, OWASP ASVS, threat modelling)
3. Gives champions a defined responsibility set: security requirement review, threat model facilitation, code review of security-sensitive changes, SAST finding triage
4. Reserves time in sprints for security activities (typically 10–20% of champion's sprint allocation)
5. Connects champions to a security community of practice for knowledge sharing

**Training curriculum mapping:**

| Role | Minimum Training | Recommended Additional |
|------|-----------------|----------------------|
| Developer | OWASP Top 10, CWE Top 25, language-specific secure coding | Threat modelling, OWASP ASVS, OWASP WebGoat/Juice Shop practical |
| Security Champion | All developer training + threat modelling workshop | CSSLP, OWASP Testing Guide |
| Architect | Threat modelling (STRIDE/PASTA), secure design principles, OWASP ASVS L3 | Security architecture review facilitation |
| DevOps/Platform | Pipeline security, secrets management, container security, IaC security | SLSA framework, supply chain security |
| QA | Security test case development, DAST tool operation, OWASP Testing Guide | Penetration testing fundamentals |

---

### PO.3 — Implement Supporting Toolchains

**Practice description:** Use toolchains and their security features to reduce human error and increase repeatability of security activities throughout the SDLC.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PO.3.1 | Specify which toolchain components address which security tasks | Publish the approved toolchain for each SDLC phase; document what security function each tool serves |
| PO.3.2 | Implement and integrate toolchain components; configure to support security tasks | Integrate tools into CI/CD pipeline with required pass/fail gates; configure rulesets and severity thresholds |
| PO.3.3 | Continuously test, maintain, and update toolchain components | Annual toolchain review; alert on tool vendor advisories; retire deprecated tools |

**Recommended toolchain by SDLC phase:**

| SDLC Phase | Security Tool Category | Tool Examples |
|-----------|----------------------|--------------|
| IDE / Pre-commit | SAST lite, secret detection, linting | Semgrep, detect-secrets, trufflehog, gitleaks, git-secrets |
| Pull Request / Code Review | SAST, IaC scanning | SonarQube, Checkmarx, Snyk Code, Semgrep, tfsec, checkov |
| CI Build | SCA, container scanning, SBOM generation | OWASP Dependency-Check, Snyk Open Source, Black Duck, Trivy, Syft, CycloneDX CLI |
| Pre-release Testing | DAST, API scanning, fuzz testing | OWASP ZAP, Burp Suite, Nuclei, OSS-Fuzz, AFL++, OWASP Amass |
| Release | Artifact signing, SBOM publishing | cosign, Sigstore, GPG, SLSA provenance generator (slsa-github-generator) |
| Production Monitoring | RASP, WAF, runtime CVE alerting | OpenTelemetry + security dashboards, Dependabot/Renovate alerts |

**Pipeline gate configuration example:**

```
Stage: Security-SAST
  Tool: Semgrep (rulesets: p/security-audit, p/owasp-top-ten)
  Threshold: FAIL if:
    - Any finding with severity=CRITICAL
    - Any finding with severity=HIGH AND confidence=HIGH
  Action on failure: Block merge to main branch
  Notification: Alert security-team@org.example + developer

Stage: Security-SCA
  Tool: OWASP Dependency-Check
  Threshold: FAIL if:
    - Any CVE with CVSS >= 9.0 in direct dependencies
    - Any CVE with CVSS >= 7.0 with known exploit
  Action on failure: Block release pipeline; create security defect ticket

Stage: Security-Container
  Tool: Trivy
  Threshold: FAIL if:
    - Any OS package CVE with severity=CRITICAL
    - Container running as root (unless explicit exception)
  Action on failure: Block deployment
```

---

### PO.4 — Define and Use Criteria for Software Security Checks

**Practice description:** Define and use criteria for checking the security of the software at important decision points in the SDLC.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PO.4.1 | Define criteria for checking software security at phase transitions and at release | Create phase-gate security checklists; define what evidence is required to proceed (test results, review sign-offs, scan artifacts) |
| PO.4.2 | Define severity thresholds for findings that block progression | Document finding severity to gate impact mapping; publish as policy |
| PO.4.3 | Evaluate software against the defined criteria at the appropriate checkpoints | Execute checklists at each gate; document any exceptions with compensating controls and risk acceptance |

**SDLC security phase-gate checklist:**

| Gate | Required Evidence | Blocking Criteria |
|------|-----------------|------------------|
| Requirements → Design | Completed threat model, security requirements documented | No threat model, missing security requirements for data classification tier |
| Design → Code | Design review sign-off from architect and security reviewer | Open high/critical design-level risks without accepted mitigation |
| Code → Test | SAST scan complete, no critical/high unmitigated findings, peer code review complete for all changes | Any unreviewed security-critical code, critical SAST findings open |
| Test → Release Candidate | DAST scan complete, penetration test complete (for significant releases), no critical/high findings open without accepted exception | Open critical/high pen test findings without risk acceptance; missing SBOM |
| Release Candidate → Production | Release approval from designated approver; security checklist signed; SBOM archived; artifacts signed | Missing signatures, unsigned artifacts, open critical vulnerabilities |

---

### PO.5 — Implement and Maintain Secure Environments for Software Development

**Practice description:** Ensure that all components of the environments used for software development are strongly protected from internal and external threats.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PO.5.1 | Separate development, staging, and production environments | Separate cloud accounts or subscriptions per environment; no shared credentials between environments; production access requires MFA + JIT |
| PO.5.2 | Secure the developer environment | Enforce endpoint security (EDR, disk encryption, MFA); require MFA for all code repository access; monitor for credential exposure |
| PO.5.3 | Secure the build environment | Use ephemeral build agents; use OIDC/workload identity for pipeline authentication (no static long-lived secrets stored in pipeline); sign all build outputs |

**Build environment security requirements:**

1. Build agents: ephemeral containers or VMs spun up per build job, destroyed after completion — no persistent build workers with accumulated state
2. Secrets management: all build-time secrets retrieved from secrets manager (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault) using temporary credentials via OIDC federation; no secrets in environment variables committed to pipeline definitions
3. Dependency caching: private artifact proxy/cache (Nexus, Artifactory, GitHub Packages) with allow-listing; no direct pull from public registries in production builds
4. Build provenance: generate SLSA provenance attestation for each build; attest build environment, source commit, build steps
5. Artifact signing: sign all release artifacts before publishing; reject unsigned artifacts in deployment pipelines

**Developer workstation security baseline:**

| Control | Requirement |
|---------|------------|
| Endpoint protection | EDR agent installed and reporting to security operations |
| Disk encryption | Full disk encryption (BitLocker/FileVault) enabled |
| Screen lock | 5-minute screen lock timeout |
| MFA for repositories | Phishing-resistant MFA required for GitHub/GitLab/Bitbucket access |
| SSH key management | Ed25519 keys minimum; keys protected with strong passphrase; hardware security key recommended |
| Credentials | No hardcoded credentials; use credential manager or OS keychain |
| OS patching | Critical patches applied within 7 days; all patches within 30 days |

---

## PS: Protect the Software

**Purpose:** Protect all components of the software from tampering and unauthorised access throughout the SDLC and after release.

### PS.1 — Protect All Forms of Code from Unauthorised Access and Tampering

**Practice description:** Protect all components of software from being tampered or treated in an unsafe manner, whether they are stored internally or externally.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PS.1.1 | Store all forms of code in version control with access controls | Centralised Git platform with enforced authentication; individual developer accounts (no shared credentials); separate repositories per component |
| PS.1.2 | Limit access to code repositories to authorised individuals; log all access | RBAC on repositories: read/write for developers, read-only for CI/CD service accounts; quarterly access review; audit logging of all access events |
| PS.1.3 | Use two-party review for all code merged to production branches | Branch protection rules requiring minimum 2 reviewer approvals; CODEOWNERS file for security-critical modules requiring security team approval; dismiss stale reviews on push |

**Repository configuration security baseline:**

```
Protected branches: main, release/*
  - Require pull request reviews: minimum 2 approvals
  - Require review from CODEOWNERS for: auth/, crypto/, admin/, api/security/
  - Dismiss stale reviews when new commits are pushed
  - Require status checks to pass: security-sast, security-sca, security-secrets
  - Require signed commits
  - Require linear history
  - Restrict who can push to matching branches: restrict to release engineers
  - Block force pushes
  - Block branch deletion
```

**Secrets in code repository:**

- Pre-commit hook using gitleaks or detect-secrets to block commits containing patterns matching: API keys, passwords, private keys, tokens, AWS access keys, database connection strings
- Automated scanning of existing repository history: trufflehog --verified on repository + all branches; findings reported to security team for key rotation
- Response to confirmed secret committed: immediately rotate the exposed credential; purge from git history using BFG Repo Cleaner or git-filter-repo; force-push branches; notify affected service owners

---

### PS.2 — Provide a Mechanism for Verifying the Integrity of the Software Release

**Practice description:** Make software integrity verification information available to software acquirers.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PS.2.1 | Digitally sign software using a code signing certificate or key pair | Authenticode (Windows PE/MSI), Apple Developer ID (macOS, iOS), GPG detached signatures (packages, archives), cosign (container images, generic artifacts) |
| PS.2.2 | Provide hash values for software artifacts using SHA-256 or stronger | Publish SHA-256, SHA-384, or SHA-512 checksums alongside all release artifacts; use sha256sum or CertUtil to generate; publish on secure HTTPS distribution channel |
| PS.2.3 | Protect signing keys securely | Sign using key stored in HSM or cloud KMS (AWS KMS, Azure Key Vault, GCP KMS); never export private key; key access restricted to release pipeline service account; key rotation schedule defined and practiced |

**SLSA (Supply chain Levels for Software Artifacts) framework levels:**

| SLSA Level | Requirements | Protections |
|-----------|-------------|------------|
| SLSA 1 | Documented build process | Establishes basic provenance trail |
| SLSA 2 | Version-controlled build process; hosted build platform that generates signed provenance | Guards against build tampering |
| SLSA 3 | Hardened build platform; auditable build platform; builds isolated from other builds | Guards against compromised build platform |
| SLSA 4 (Level 4, now Build L3 in SLSA v1.0) | Hermetic builds; reproducible builds; signed provenance by build platform | Highest assurance of build integrity |

**Provenance attestation content:**

```json
{
  "subject": [{"name": "artifact-name", "digest": {"sha256": "<hash>"}}],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "https://slsa-framework.github.io/github-actions-buildtypes/workflow/v1",
      "externalParameters": {"workflow": {"ref": "refs/tags/v1.0.0", "repository": "https://github.com/org/repo", "path": ".github/workflows/release.yml"}},
      "resolvedDependencies": [{"uri": "git+https://github.com/org/repo", "digest": {"gitCommit": "<commit-sha>"}}]
    },
    "runDetails": {"builder": {"id": "https://github.com/slsa-framework/slsa-github-generator"}, "metadata": {"invocationId": "<run-url>", "startedOn": "<timestamp>", "finishedOn": "<timestamp>"}}
  }
}
```

---

### PS.3 — Archive and Protect Each Software Release

**Practice description:** Preserve the integrity of each software release by protecting it from any changes.

| Task ID | Task Description | Example Implementations |
|---------|-----------------|------------------------|
| PS.3.1 | Store each release version as an immutable, integrity-verified archive | Immutable object storage (S3 Object Lock, Azure Blob immutable storage, Google Cloud Storage Object Hold); compute and record SHA-256 hash of archive at ingest |
| PS.3.2 | Keep records of all release artifacts, and all relevant observations about the software's security | Per-release security package contents (see below) |
| PS.3.3 | Restrict and audit access to archived releases and their associated records | IAM-controlled access to artifact archive; only release engineers and auditors may access; all access logged |

**Per-release security package contents:**

```
release-v<X.Y.Z>/
  artifacts/
    software-<version>.<ext>           (signed release binary/package)
    software-<version>.<ext>.sha256    (cryptographic hash)
    software-<version>.<ext>.sig       (detached GPG or cosign signature)
  sbom/
    software-<version>.spdx.json       (SPDX format SBOM, signed)
    software-<version>.cdx.json        (CycloneDX format SBOM)
  security/
    sast-results-<date>.sarif          (SAST tool output in SARIF format)
    sca-results-<date>.json            (SCA dependency scan output)
    dast-results-<date>.json           (DAST scan summary)
    pentest-report-<date>.pdf          (penetration test report — CONFIDENTIAL)
    vulnerability-exceptions.json      (risk-accepted findings with approver and expiry)
  provenance/
    slsa-provenance.intoto.jsonl       (SLSA provenance attestation)
  approvals/
    release-approval-<date>.md         (signed release approval record)
```

---

## PW: Produce Well-Secured Software — Extended Detail

### PW.1 — Design Software to Meet Security Requirements and Mitigate Security Risks

**Threat modelling process:**

Step 1 — Scope and decompose the system:
- Create a data flow diagram (DFD) at Level 0 (system context) and Level 1 (major components)
- Identify: processes, data stores, external entities, data flows
- Draw trust boundaries between different security domains

Step 2 — Identify threats:
- Apply STRIDE to each DFD element:
  - Spoofing: can an attacker impersonate a principal or component?
  - Tampering: can an attacker modify data in transit or at rest?
  - Repudiation: can a legitimate user deny performing an action?
  - Information Disclosure: can unauthorised parties access sensitive data?
  - Denial of Service: can availability of the system be disrupted?
  - Elevation of Privilege: can an attacker gain elevated permissions?

Step 3 — Evaluate threats:
- Assign DREAD scores (Damage, Reproducibility, Exploitability, Affected users, Discoverability) or CVSS pre-exploit base scores
- Prioritise by score

Step 4 — Determine mitigations:
- For each threat: accept / transfer / avoid / mitigate
- Document mitigation approach taken
- Map mitigations to SP 800-53 controls or OWASP ASVS requirements

Step 5 — Validate:
- Design review verifies all threats have a documented disposition
- Mitigations verified in code and test phases

---

### PW.4 — Reuse Existing, Well-Secured Software When Feasible

**Component health evaluation criteria:**

| Criterion | Acceptable | Warning | Reject |
|-----------|-----------|---------|--------|
| Last maintainer activity | < 6 months | 6–18 months | > 18 months (no response to issues) |
| Known CVEs | None or all patched | Any CVSS < 7.0 unpatched | Any CVSS >= 7.0 unpatched |
| Licence | Permissive (MIT, Apache-2.0, BSD) | Weak copyleft (LGPL) — legal review | Strong copyleft (GPL) in commercial product — legal review required |
| Download volume / community | Large active community | Small but active | Effectively abandoned |
| OpenSSF Scorecard | >= 7.0 | 4.0–6.9 | < 4.0 |
| Security policy | SECURITY.md present | No security policy but responsive | No security policy and unresponsive |

**OpenSSF Scorecard checks (key checks for SSDF alignment):**

- Branch-Protection: branch protection enabled (PO.5)
- Code-Review: code review required (PS.1)
- Dangerous-Workflow: no dangerous patterns in CI (PO.3, PO.5)
- Dependency-Update-Tool: automated dependency updates configured (PW.4)
- Fuzzing: fuzz testing active (PW.9)
- Maintained: recent commits — maintenance not abandoned (PW.4)
- Pinned-Dependencies: dependencies pinned to specific hashes (PW.4, PS.2)
- SAST: SAST tool runs in CI (PW.7)
- Security-Policy: SECURITY.md present with disclosure process (RV.1)
- Signed-Releases: release artifacts signed (PS.2)
- Token-Permissions: principle of least privilege in workflow tokens (PO.5)
- Vulnerabilities: no unpatched CVEs in default branch (RV.2)

---

### PW.5 — Create Source Code by Adhering to Secure Coding Practices

**Language-specific secure coding standards reference:**

| Language | Primary Standard | Key CWE Risks to Address |
|----------|----------------|--------------------------|
| C / C++ | CERT C Coding Standard, MISRA C (embedded) | CWE-119 (buffer overflow), CWE-416 (use-after-free), CWE-401 (memory leak), CWE-190 (integer overflow) |
| Java | CERT Java Coding Standard, Oracle Secure Coding Guidelines | CWE-502 (deserialization), CWE-611 (XXE), CWE-78 (OS command injection) |
| Python | OWASP Python Cheat Sheet, Bandit ruleset | CWE-89 (SQL injection), CWE-78 (command injection), CWE-22 (path traversal) |
| JavaScript / TypeScript | OWASP JavaScript Security Cheat Sheet | CWE-79 (XSS), CWE-1321 (prototype pollution), CWE-918 (SSRF) |
| Go | Google Go security guidelines | CWE-89 (database/sql without parameterisation), CWE-22 (filepath.Join bypass) |
| .NET / C# | Microsoft SDL secure coding, .NET security checklists | CWE-502 (BinaryFormatter deserialization), CWE-89 (ADO.NET without parameters) |
| Ruby | Brakeman ruleset, Rails security guide | CWE-89 (ActiveRecord raw SQL), CWE-77 (shell injection via backticks) |
| PHP | OWASP PHP Security Cheat Sheet | CWE-89, CWE-98 (file inclusion), CWE-79 if output not escaped |

**Universal secure coding principles (language-agnostic):**

1. Input validation: reject inputs that do not conform to an expected allowlist of characters, lengths, and formats; never construct queries, commands, or markup from untrusted input without neutralisation
2. Output encoding: use context-appropriate encoding before inserting untrusted data into HTML (HTML entity encoding), JavaScript (JS escape), URL (percent encoding), SQL (parameterised queries), OS command (avoid; use subprocess with array arguments)
3. Authentication: use established identity libraries; never implement custom authentication protocols; enforce MFA for privileged operations
4. Session management: use cryptographically random session identifiers; set Secure and HttpOnly flags on cookies; implement session expiry; revalidate session after privilege change
5. Cryptography: use current algorithms only (AES-256-GCM, ChaCha20-Poly1305, RSA-2048+, ECC P-256+, SHA-256+); use established cryptographic libraries; never implement custom cryptographic algorithms; never use MD5 or SHA-1 for security purposes
6. Error handling: return generic error messages to users; log detailed error information to secure log store; never expose stack traces, database errors, or internal paths in user-facing responses
7. Logging: log security events (authentication, authorisation failures, input validation failures, privilege changes) with sufficient context; exclude sensitive data (passwords, credentials, session tokens, PII) from logs

---

### PW.9 — Test Executable Code to Identify Vulnerabilities

**Security testing approach by test type:**

| Test Type | Purpose | When | Tools |
|-----------|---------|------|-------|
| SAST | Find vulnerabilities in source code | PR + CI build | Semgrep, CodeQL, SonarQube, Checkmarx |
| SCA | Identify vulnerable dependencies | PR + CI build | OWASP DC, Snyk, Black Duck, Trivy |
| Secrets scanning | Detect committed credentials | Pre-commit + CI | gitleaks, detect-secrets, trufflehog |
| DAST (baseline) | Automated web vulnerability scan | CI on test environment | OWASP ZAP baseline scan |
| DAST (full active) | Full web vulnerability assessment | Release candidate | OWASP ZAP full scan, Burp Suite |
| API security testing | REST/GraphQL/gRPC vulnerability testing | Release candidate | OWASP ZAP, Burp Suite REST extension, Postman security tests |
| Container scanning | OS and layer vulnerability scanning | CI build | Trivy, Snyk Container, Clair |
| IaC scanning | Infrastructure-as-code misconfiguration | PR + CI | tfsec, checkov, terrascan, kics |
| Fuzz testing | Discover edge cases and memory corruption | Ongoing / nightly | libFuzzer, AFL++, boofuzz, ClusterFuzz |
| Penetration test | Adversarial exploitation attempt | Pre-production release and annually | PTES methodology; OWASP Testing Guide |
| Software composition analysis — licence | Identify licence compliance issues | PR + CI | FOSSA, Black Duck, Licensee |

**Penetration test scope document template:**

```
Software Penetration Test Scope — v<version>
Target application: <name and URL/binary>
Target version: <version under test>
Test environment: Dedicated test environment (not production); URL/endpoint: <test-url>
Test window: <start datetime> to <end datetime>
Testing methodology: OWASP Testing Guide v4.2 / PTES
In scope:
  - Web application: all endpoints and functionality accessible at <base URL>
  - API: REST API endpoints as documented in <API spec URL>
  - Mobile application: <platform> version <version number>
Out of scope:
  - Production environment and production data
  - Third-party services and integrations (no active testing against external providers)
  - Denial of service attacks
  - Social engineering
Rules of engagement:
  - Immediately notify <security contact> if critical finding discovered that affects production
  - No active exploitation of discovered vulnerabilities that could result in data loss
Deliverables:
  - Final report within 5 business days of test completion
  - Executive summary, technical findings (with CVSS scores, reproduction steps, remediation guidance), appendix with all test evidence
```

---

## RV: Respond to Vulnerabilities — Extended Detail

### RV.1 — Identify and Confirm Vulnerabilities

**Vulnerability disclosure policy (VDP) template:**

```
Vulnerability Disclosure Policy — <Organisation Name>

Security Contact: security@<org>.example
PGP Key Fingerprint: <fingerprint> (available at <URL>)

Scope:
  In scope: all software products listed at <URL>
  Out of scope: third-party services, infrastructure not managed by <org>

What to report:
  - Authentication or authorisation vulnerabilities
  - Remote code execution vulnerabilities
  - SQL injection, XSS, or other injection vulnerabilities
  - Memory corruption vulnerabilities
  - Sensitive data exposure
  - Cryptographic vulnerabilities

Process:
  1. Submit report to security@<org>.example
  2. Acknowledgement within 2 business days
  3. Initial severity assessment shared within 5 business days
  4. Remediation timeline communicated within 10 business days
  5. Coordinated disclosure: we request 90 days before public disclosure to allow remediation
  6. We do not take legal action against researchers following this policy

Recognition:
  We maintain a public Hall of Fame for reporters of valid security issues.
  We do not currently offer a monetary bug bounty.
```

**External vulnerability source monitoring:**

| Source | Frequency | Mechanism |
|--------|-----------|-----------|
| NVD (nvd.nist.gov) | Daily | NVD API query for products in SBOM/CPE inventory |
| CISA KEV (Known Exploited Vulnerabilities) | Daily | CISA KEV JSON feed subscription; alert on any KEV match to software inventory |
| Vendor security advisories | Per advisory | Advisory mailing list subscription per vendor |
| GitHub Security Advisories | Daily | Dependabot alerts or GitHub API |
| OSV.dev | Daily | OSV API query for package ecosystem |
| Bug bounty / responsible disclosure | Continuous | Monitored security email address |

---

### RV.2 — Assess, Prioritise, and Remediate Vulnerabilities

**Vulnerability severity and remediation SLA:**

| CVSS v3.1 Base Score | Severity | Remediation SLA | Risk Acceptance Authority |
|---------------------|----------|----------------|--------------------------|
| 9.0–10.0 | Critical | 15 calendar days | CISO; compensating control if patch unavailable |
| 7.0–8.9 | High | 30 calendar days | Security Manager |
| 4.0–6.9 | Medium | 90 calendar days | Engineering Lead |
| 0.1–3.9 | Low | 180 calendar days or next planned release | Development Team |
| 0.0 (Informational) | Informational | Best effort; no SLA | Development Team |

**CVSS environmental scoring adjustments:**

Environmental metrics allow the base CVSS score to be adjusted for the specific context:

- Modified Attack Vector: if the vulnerability requires network access but the service is internal-only network-accessible, this may reduce the effective score
- Modified Confidentiality/Integrity/Availability Impact: if the affected system processes public data only (no PII, no financial), Confidentiality Impact may be reduced
- Compensating Controls (CR/IR/AR): if a WAF, network restriction, or other compensating control is in place that meaningfully reduces exploitability, this reduces temporal and environmental scores

Always document:
1. Base CVSS score (from NVD or vendor)
2. Environmental adjustments applied and rationale
3. Final effective score used for prioritisation
4. Approver name and date

**Patch delivery options decision tree:**

```
Vulnerability confirmed → Assign CVSS score
→ Is a patch available from vendor/maintainer?
  YES → Apply patch per SLA; regression test; release patch version
  NO → Is a workaround available (WAF rule, configuration change, feature disable)?
    YES → Apply compensating control; document; set review date (30 days or when patch appears)
    NO → Is the risk acceptable given asset context?
      YES → Risk accept with ISSO/CISO approval; document with expiry date
      NO → Remove or replace the vulnerable component
```

---

### RV.3 — Analyse Vulnerabilities to Identify Root Causes

**Root cause taxonomy:**

| Root Cause Category | CWE Class | SDLC Phase | Preventive Action |
|--------------------|-----------|-----------|-------------------|
| Input validation omission | CWE-20 | Coding | Add input validation training; SAST rule for untrusted input usage |
| SQL injection via string concatenation | CWE-89 | Coding | Enforce ORM usage or parameterised queries via SAST |
| Reflected/stored XSS | CWE-79 | Coding | Enforce output encoding library; template auto-escaping; CSP policy |
| Insecure direct object reference | CWE-639 | Design/Coding | Add design review checklist item for authorisation on resource access |
| Hardcoded credential | CWE-798 | Coding | Pre-commit secret detection; secrets management training |
| Dependency vulnerability | CWE-1035 | Build/Maintenance | SCA alerts; dependency update automation (Dependabot/Renovate) |
| Missing authentication | CWE-306 | Design | Add authentication requirement to all endpoints in design review |
| Insecure deserialization | CWE-502 | Coding | Prohibit native deserialization of untrusted data; use JSON/XML with schema validation |
| Security misconfiguration | CWE-16 | Operations | IaC scanning; security baseline configuration standards |
| Insufficient logging | CWE-778 | Design/Coding | Security logging requirements in design checklist |

**Root cause reporting template (per vulnerability):**

```
Vulnerability Root Cause Analysis

CVE/Ticket ID: <identifier>
Affected component: <component name and version>
CVSS Score: <base score> (environmental: <adjusted score>)
Date introduced: <approximate date or commit>
Date detected: <date>
Detection source: <SAST / SCA / DAST / pen test / external researcher / monitoring>

Root cause description:
  [Describe the specific code pattern, design decision, or process failure that caused the vulnerability]

CWE classification: CWE-<number> — <name>
SDLC phase where introduced: <requirements / design / coding / testing / deployment / maintenance>
Type of failure: <knowledge gap / process failure / tooling gap / resource constraint>

Why was it not caught earlier?
  [Describe why existing controls did not detect it]

Corrective action for this vulnerability:
  [Describe the specific code change or configuration fix applied]

Systemic preventive actions:
  1. [Training update / SAST rule / checklist addition / policy change — whichever applies]
  2. [Additional action if warranted]

Owner for preventive actions: <name>
Target completion date: <date>
```
