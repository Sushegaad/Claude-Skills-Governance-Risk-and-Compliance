---
name: nist-sp-800-218
description: >
  Apply this skill for any question about secure software development practices,
  the NIST Secure Software Development Framework (SSDF), NIST SP 800-218, SSDF
  practice groups PO PS PW RV, software security requirements, DevSecOps pipeline
  security, secure coding standards, software vulnerability management, software
  supply chain security, EO 14028 software security requirements, SBOM for software
  producers, software composition analysis, dependency scanning, static analysis
  SAST dynamic analysis DAST, threat modelling for software, secure design
  principles, security testing of software, software security assessment,
  penetration testing of applications, open source software security, software
  integrity verification, code signing, reproducible builds, build pipeline
  security, software attestation, software bill of materials, NIST mapping to
  SP 800-53 secure development controls, ISO 27001 software development controls,
  NIST CSF software security, OpenSSF Scorecard, CycloneDX SPDX for software
  security, software vulnerability disclosure, coordinated vulnerability disclosure,
  CVD programme, CVSS scoring for software, software patch management, software
  security metrics, software security training for developers, security champions
  programme, application security programme, OWASP integration with SSDF.
---

# NIST SP 800-218: Secure Software Development Framework (SSDF)

**Publication:** NIST Special Publication 800-218, Version 1.1, February 2022
**CSRC:** https://csrc.nist.gov/publications/detail/sp/800-218/final

---

## Purpose and Scope

NIST SP 800-218 defines the Secure Software Development Framework (SSDF): a set of fundamental, sound, and secure software development practices. The SSDF is not a development process or lifecycle model — it is a reference framework of practices that organisations should incorporate into their existing software development lifecycles (SDLCs) regardless of technology, platform, or programming language.

Primary objectives:
- Reduce the number of vulnerabilities in released software
- Reduce the potential impact of undetected or unaddressed vulnerabilities
- Address the root causes of vulnerabilities to prevent future recurrences
- Establish repeatable, documented, and measurable secure development practices
- Support attestation and compliance with EO 14028 software security requirements

The SSDF applies to all types of software: commercial off-the-shelf (COTS), open-source, custom-developed, and software as a service (SaaS). It applies to software producers and to organisations that define software security requirements for their suppliers.

---

## SSDF Structure

The SSDF is organised into four practice groups, 19 practices, and a set of tasks and implementation examples per practice. Each practice entry contains:

- **Practice ID:** Group prefix + number (e.g., PO.1, PS.2)
- **Practice title:** Short label
- **Practice description:** What should be accomplished
- **Tasks:** Specific actions to implement the practice
- **Notional implementation examples:** Non-prescriptive examples of tools, techniques, and approaches

### Practice Groups

| Group | Name | Practice Count |
|-------|------|---------------|
| PO | Prepare the Organisation | 5 practices (PO.1–PO.5) |
| PS | Protect the Software | 3 practices (PS.1–PS.3) |
| PW | Produce Well-Secured Software | 8 practices (PW.1–PW.9, except PW.3 and PW.8) |
| RV | Respond to Vulnerabilities | 3 practices (RV.1–RV.3) |

Note: PW.3 and PW.8 were removed in SSDF v1.1. Active PW practices are PW.1, PW.2, PW.4, PW.5, PW.6, PW.7, PW.9.

---

## PO: Prepare the Organisation

Establish and maintain the organisation-wide conditions needed to support secure software development throughout the software development lifecycle.

### PO.1 — Define Security Requirements for Software Development

**Description:** Ensure that security requirements are identified, prioritised, and integrated into the SDLC from the beginning.

**Tasks:**
- PO.1.1: Identify and document security requirements at the organisational level (regulatory, contractual, policy)
- PO.1.2: Identify and document security and privacy requirements for each software project
- PO.1.3: Review and revise software requirements periodically and when significant changes occur

**Key implementation examples:**
- Maintain a catalogue of applicable security requirements by software category (web, mobile, embedded, cloud)
- Use threat modelling to derive security requirements from system design (STRIDE, PASTA, attack trees)
- Map software security requirements to SP 800-53, OWASP ASVS, or CWE Top 25 as reference

### PO.2 — Implement Roles and Responsibilities

**Description:** Ensure that everyone participating in the SDLC has an appropriate level of security skills and knowledge for their role.

**Tasks:**
- PO.2.1: Create new roles or add duties to existing roles as needed for security
- PO.2.2: Provide role-appropriate training and awareness to all personnel involved in software development
- PO.2.3: Conduct security awareness training for all individuals performing software development

**Key implementation examples:**
- Define security responsibilities in job descriptions for developers, architects, DevOps engineers, and product owners
- Deliver role-specific training: secure coding for developers, threat modelling for architects, security testing for QA
- Establish a security champions programme to embed security expertise in development teams
- Track training completion and currency (annual refresh minimum)

### PO.3 — Implement Supporting Toolchains

**Description:** Use automation to reduce human error and increase repeatability of security activities throughout the SDLC.

**Tasks:**
- PO.3.1: Specify which tools are required or recommended for each SDLC process stage
- PO.3.2: Integrate security-focused tooling into the SDLC toolchain (IDE plugins, CI/CD pipeline stages)
- PO.3.3: Configure and maintain tools to support security practices; retire or replace inadequate tools

**Key implementation examples:**
- Pre-commit hooks: secret detection (detect-secrets, trufflehog), linting, SAST lite checks
- CI/CD pipeline security stages: SAST, SCA/dependency scanning, container image scanning, IaC scanning
- IDE security plugins: security linters, real-time vulnerability detection (Semgrep, Snyk, Checkmarx IDE)
- Artifact repository: enforce signed artifacts, vulnerability scanning of stored images

### PO.4 — Define and Use Criteria for Software Security Checks

**Description:** Define clear criteria for evaluating the security of software before it advances to the next SDLC phase and before release.

**Tasks:**
- PO.4.1: Define criteria for security checks at SDLC phase gates and for release approval
- PO.4.2: Define severity thresholds for findings that block advancement (critical/high findings block release)
- PO.4.3: Evaluate software against defined criteria at appropriate phase-gate checkpoints

**Key implementation examples:**
- Security requirement traceability matrix (SRTM) mapping requirements to test evidence
- Release criteria: zero unmitigated critical/high CVEs in direct dependencies, SAST findings below defined threshold, penetration test findings remediated or risk-accepted by authorised reviewer
- Phase-gate checklists for design, pre-code, pre-test, pre-release, and post-release phases

### PO.5 — Implement and Maintain Secure Environments for Software Development

**Description:** Ensure that development, build, and testing environments are protected to prevent tampering, contamination, or exfiltration of source code, build artifacts, and developer credentials.

**Tasks:**
- PO.5.1: Separate development, staging, and production environments and control access to each
- PO.5.2: Secure the developer environment: endpoints, credentials, access to source code repositories
- PO.5.3: Secure the build environment: build systems, build pipelines, build toolchains, build credentials

**Key implementation examples:**
- Dedicated build accounts with least privilege; build service accounts cannot modify production environments
- Source code repository access controls: branch protection rules, required reviews, signed commits
- Build system hardening: ephemeral build agents, no persistent secrets in build environment, artifact signing
- Separate testing environments using anonymised or synthetic data (no production data in test)
- Developer workstation management: EDR, full disk encryption, MFA for code repository access

---

## PS: Protect the Software

Protect all components of the software from tampering and unauthorised access throughout the SDLC.

### PS.1 — Protect All Forms of Code from Unauthorised Access and Tampering

**Description:** Protect code in all forms: source code, build scripts, infrastructure-as-code, configuration, and any other software components.

**Tasks:**
- PS.1.1: Store all code in a version control system with access controls
- PS.1.2: Limit and monitor write access to source code repositories
- PS.1.3: Use code review (minimum two-person integrity) before merging to protected branches

**Key implementation examples:**
- Branch protection: require pull request reviews, status checks passing, signed commits
- CODEOWNERS files to enforce security-team review of security-sensitive modules
- Audit logging of all code repository access, clone operations, and administrative changes
- Repository scanning for secrets and credentials committed to version control history

### PS.2 — Provide a Mechanism for Verifying the Integrity of the Software Release

**Description:** Provide a way for software consumers to verify the integrity and authenticity of released software.

**Tasks:**
- PS.2.1: Digitally sign software release artifacts using a controlled signing key
- PS.2.2: Provide cryptographic hash values (SHA-256 minimum) alongside release artifacts
- PS.2.3: Maintain the signing key infrastructure securely; use HSM or key management service

**Key implementation examples:**
- Code signing: Authenticode (Windows), Apple notarisation (macOS), GPG signatures (Linux packages, container images)
- Container image signing: Sigstore/cosign, Docker Content Trust, Notary
- Provide SPDX or CycloneDX SBOM signed alongside release artifact
- Publish signing key fingerprints and verification instructions in software documentation
- Implement SLSA (Supply chain Levels for Software Artifacts) framework to document build provenance

### PS.3 — Archive and Protect Each Software Release

**Description:** Preserve all evidence that is needed to confirm the integrity of each software release for as long as that software is supported.

**Tasks:**
- PS.3.1: Store archives of all released software versions with evidence of integrity (hash, signature)
- PS.3.2: Retain build records, dependencies snapshot, SBOM, and test results for each release
- PS.3.3: Control and audit access to the release archive

**Key implementation examples:**
- Immutable artifact storage: write-once object storage for release artifacts
- Retain per-release: source code snapshot, compiled artifacts, dependencies lock file, SBOM, SAST/DAST results, penetration test report, release approval record, signing certificate chain
- Archive retention period aligned with software supported lifetime plus regulatory requirements

---

## PW: Produce Well-Secured Software

Produce well-secured software with minimal security vulnerabilities in its releases.

### PW.1 — Design Software to Meet Security Requirements and Mitigate Security Risks

**Description:** Design software to meet security requirements and to reduce security vulnerabilities before coding begins.

**Tasks:**
- PW.1.1: Define and document threat model for each software component; update on significant design changes
- PW.1.2: Design software to implement security controls that address identified threats and satisfy security requirements
- PW.1.3: Review and evaluate software designs to validate security properties before coding begins

**Key implementation examples:**
- Threat modelling methodologies: STRIDE (Microsoft), PASTA, LINDDUN (privacy), attack trees
- Threat modelling output: data flow diagram, trust boundary identification, threat enumeration, mitigation decisions (DREAD ratings or CVSS pre-exploitation scores)
- Secure design principles: least privilege, defence in depth, fail securely, minimise attack surface, separation of duties, do not trust input, secure defaults
- Design review checklist aligned to OWASP ASVS architecture requirements

### PW.2 — Review the Software Design to Verify Compliance with Security Requirements

**Description:** Have a qualified reviewer independently verify that the software design satisfies security requirements and adequately addresses identified threats.

**Tasks:**
- PW.2.1: Have individuals with sufficient security expertise conduct software design review
- PW.2.2: Document design review findings and confirm disposition of all security-relevant findings

**Key implementation examples:**
- Architecture review board (ARB) or security architecture review gate for new systems and significant changes
- Design review checklist mapped to security requirements and threat model threats
- Track open design-level risks in the project risk register

### PW.4 — Reuse Existing, Well-Secured Software When Feasible

**Description:** Use existing software that is well-secured, actively maintained, and appropriate for the intended use to reduce the risk of introducing new vulnerabilities through reuse.

**Tasks:**
- PW.4.1: Identify and evaluate applicable well-secured software components for reuse
- PW.4.2: Determine and document security risks from reusing a component; accept or mitigate before use
- PW.4.3: Maintain a list of approved third-party software components and versions in use

**Key implementation examples:**
- Approved component catalogue with security evaluation status and approved version ranges
- Software Composition Analysis (SCA): automated scanning of direct and transitive dependencies against CVE database (OWASP Dependency-Check, Snyk, Black Duck, FOSSA)
- Pin dependency versions; use lock files (package-lock.json, Pipfile.lock, go.sum)
- Evaluate component health: maintenance status, disclosed vulnerability history, community response time
- Prohibition on end-of-life (EOL) components in production software without an approved exception

### PW.5 — Create Source Code by Adhering to Secure Coding Practices

**Description:** Reduce the number of security vulnerabilities by following well-established conventions for secure coding.

**Tasks:**
- PW.5.1: Follow secure coding standards appropriate to the programming language and platform
- PW.5.2: Use security-focused static analysis tools on source code throughout development
- PW.5.3: Train developers on secure coding practices relevant to their language and domain

**Key implementation examples:**
- Secure coding standards by language: CERT C/C++, OWASP Java Secure Coding, Apple iOS security guidelines, Android security best practices
- Common vulnerability prevention: input validation (allowlist), output encoding, prepared statements for SQL, context-appropriate escaping for XSS prevention, safe API usage for memory-safe operations
- SAST tools: SonarQube, Semgrep, Checkmarx, Coverity, CodeQL; configure to enforce security rulesets
- SAST finding triage: security engineers review false positives; track true positives as defects
- CWE Top 25 Most Dangerous Software Weaknesses as a training reference

### PW.6 — Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security

**Description:** Improve the security of the software's build output by using available security features in the build toolchain.

**Tasks:**
- PW.6.1: Use compiler and linker options that improve the security of the executable (where applicable)
- PW.6.2: Determine the security-relevant configuration for runtime interpreters and execution environments

**Key implementation examples:**
- C/C++ compiler hardening flags: -fstack-protector-all, -D_FORTIFY_SOURCE=2, -pie -fPIE, -Wl,-z,relro,-z,now, -O2
- Enable Address Space Layout Randomisation (ASLR) at OS level; use PIE executables
- Enable Control Flow Integrity (CFI) where compiler support is available
- Java/JVM: enable SecurityManager (deprecated Java 17+), address deserialization risks
- Python: disable -O optimisations that strip assert statements in security-relevant code
- Container images: run as non-root user, use read-only root filesystem, drop all capabilities

### PW.7 — Review and/or Analyse Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements

**Description:** Identify vulnerabilities in the code through manual review, automated analysis, or a combination, and ensure that security requirements are implemented.

**Tasks:**
- PW.7.1: Perform code reviews on security-sensitive code areas; use peer review for all production code
- PW.7.2: Use automated SAST tools to supplement manual review
- PW.7.3: Track and remediate all code review findings according to severity and release criteria

**Key implementation examples:**
- Mandatory security-focused code review for: authentication/authorisation code, cryptography usage, session management, input handling, direct memory manipulation, privilege elevation, network communication
- SAST finding severity mapping to defect priority: critical → P0 (block release), high → P1 (fix in current sprint), medium → P2 (fix in next sprint), low → P3 (backlog)
- Automated code review tooling integrated into pull request workflow with required status checks

### PW.9 — Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements

**Description:** Test the compiled or interpreted code to identify vulnerabilities and verify that security controls are implemented correctly.

**Tasks:**
- PW.9.1: Use DAST tools against running software in a test environment
- PW.9.2: Perform penetration testing on software prior to first production deployment and after major changes
- PW.9.3: Review test results and remediate confirmed vulnerabilities per release criteria

**Key implementation examples:**
- DAST tools: OWASP ZAP (automated scan), Burp Suite Professional (manual-assisted), Nikto (web server configuration)
- DAST integration into CI/CD: baseline scan on every build; full active scan on release candidate
- Penetration testing: internal team or third-party; scope to define in-scope assets and test boundaries; methodology aligned to PTES, OWASP Testing Guide, or NIST SP 800-115
- Fuzz testing: use fuzzing frameworks (libFuzzer, AFL, boofuzz) for parsers, protocol handlers, and API endpoints
- Security regression testing: maintain a suite of tests derived from previously discovered vulnerabilities

---

## RV: Respond to Vulnerabilities

Identify residual vulnerabilities in software releases and respond appropriately to address them.

### RV.1 — Identify and Confirm Vulnerabilities on an Ongoing Basis

**Description:** Establish a process to identify vulnerabilities in released software from both internal and external sources on a continuous basis.

**Tasks:**
- RV.1.1: Gather information about potential vulnerabilities in the software from internal and external sources
- RV.1.2: Review and confirm each reported potential vulnerability; assign a severity rating using CVSS
- RV.1.3: Analyse confirmed vulnerabilities to determine root cause to enable broader remediation

**Key implementation examples:**
- Internal sources: SAST/DAST results from production monitoring, runtime application self-protection (RASP), log analysis
- External sources: NVD/CVE database subscription, vendor security advisories, bug bounty programme submissions, responsible disclosure submissions, security researcher reports
- Vulnerability tracking: maintain a vulnerability management register with CVE/CWE ID, CVSS score, affected versions, status, and target remediation date
- SCA tools in production monitoring mode: alert when new CVEs published for components in use

### RV.2 — Assess, Prioritise, and Remediate Vulnerabilities

**Description:** Assess the severity of confirmed vulnerabilities, prioritise remediation based on risk, and remediate on a defined schedule.

**Tasks:**
- RV.2.1: Evaluate the severity of each confirmed vulnerability using a documented assessment process (CVSS, environmental scoring)
- RV.2.2: Prioritise vulnerabilities for remediation based on severity, exploitability, and business impact
- RV.2.3: Remediate vulnerabilities according to defined timelines; track exceptions with compensating controls

**Key implementation examples:**
- CVSS v3.1 environmental metrics: use asset criticality and compensating controls to adjust base scores
- Remediation SLA: Critical CVSS 9.0–10.0 → 15 days; High 7.0–8.9 → 30 days; Medium 4.0–6.9 → 90 days; Low 0.1–3.9 → 180 days or next planned release
- Patch delivery options: hotfix release, regular patch release, compensating control (WAF rule, network restriction), risk acceptance with ISSO/authorising official approval
- Coordinated Vulnerability Disclosure (CVD): define process for handling external researcher submissions (acknowledge within 5 business days, provide remediation timeline)
- EOL component replacement: trigger replacement project when a dependency reaches EOL or CVSS ≥ 7.0 with no patch available

### RV.3 — Analyse Vulnerabilities to Identify Their Root Causes

**Description:** Identify and address the root causes of vulnerabilities to prevent recurrence of similar vulnerabilities in both current and future software.

**Tasks:**
- RV.3.1: Analyse each confirmed vulnerability to identify its root cause (e.g., specific CWE, design flaw, missing control)
- RV.3.2: Use root cause data to update secure coding standards, training materials, and SDLC processes
- RV.3.3: Report vulnerability trends to management to drive investment in preventive measures

**Key implementation examples:**
- Root cause taxonomy: classify by CWE, SDLC phase where introduced (design/coding/configuration), and type of failure (knowledge gap, process failure, tooling gap)
- Retrospective review: for critical/high vulnerabilities, conduct a brief RCA meeting before closing the ticket
- Trend reporting: quarterly vulnerability trend report to engineering leadership covering: new vulnerabilities by severity, mean time to remediate (MTTR) by severity, top CWE categories, improvements over prior period
- Update training curriculum based on recurring CWE findings

---

## EO 14028 Software Security Requirements (May 2021)

Executive Order 14028 "Improving the Nation's Cybersecurity" established federal software security requirements that map directly to the SSDF. Key requirements for software producers selling to the federal government:

| EO 14028 Requirement | SSDF Mapping |
|---------------------|-------------|
| Use multi-factor authentication | PO.5.2 (developer environment security) |
| Maintain trusted source code supply chains | PS.1, PW.4 (code protection, component reuse) |
| Use automated tools to check for vulnerabilities | PW.5, PW.7, PW.9 (SAST/DAST/SCA) |
| Have documentation of code provenance | PS.1, PS.2 (code integrity, signing, SBOM) |
| Provide SBOM for software supplied to federal government | PS.2, PS.3 |
| Test for known or potential vulnerabilities in software | PW.7, PW.9, RV.1 |
| Maintain access control over proprietary code | PS.1, PO.5 |
| Provide vulnerability disclosure policy | RV.1, RV.2 |
| Attest to compliance with SSDF practices | All practice groups |

The Office of Management and Budget (OMB) memoranda M-22-18 and M-23-16 operationalise the EO 14028 software supply chain security requirements, requiring federal agencies to collect software attestation and SBOMs from software producers.

---

## SBOM Requirements (SP 800-218 + EO 14028)

A Software Bill of Materials (SBOM) is a machine-readable inventory of software components and dependencies.

### NTIA Minimum Elements (7 fields per component):

| Field | Description |
|-------|-------------|
| Supplier name | Name of entity supplying the component |
| Component name | Name used to refer to the component |
| Component version | Version identifier used by supplier |
| Other unique identifiers | PURL, CPE, or supplier-specific identifier |
| Dependency relationship | Direct or transitive relationship to parent |
| Author of SBOM data | Entity generating the SBOM |
| Timestamp | Date and time SBOM was generated |

### SBOM Formats:

| Format | Governing Body | Use Case |
|--------|---------------|----------|
| SPDX (Software Package Data Exchange) | Linux Foundation / ISO 5962 | Open source licence compliance + security |
| CycloneDX | OWASP | Software security and risk management focus |
| SWID Tags | ISO/IEC 19770-2 | Endpoint asset management focus |

### SBOM Delivery Requirements:
- Delivered with each software release
- Machine-readable format (SPDX JSON, CycloneDX XML/JSON)
- Human-readable version provided in addition where required by contract
- Signed by software producer (integrity verification, PS.2)
- Updated when any component is added, updated, or removed

---

## SP 800-53 Rev 5 Control Mapping

| SSDF Practice | SP 800-53 Controls |
|--------------|-------------------|
| PO.1 (Security Requirements) | SA-8, SA-15, SA-17, PL-8 |
| PO.2 (Roles/Responsibilities) | AT-2, AT-3, PS-7, SA-3 |
| PO.3 (Toolchains) | SA-15, SA-11, CM-2, CM-3 |
| PO.4 (Security Check Criteria) | SA-11, SA-15, CA-2, CA-8 |
| PO.5 (Secure Environments) | CM-6, SC-28, AC-3, IA-5, SI-7 |
| PS.1 (Protect Code) | CM-3, SA-10, AC-3, AU-2 |
| PS.2 (Integrity Verification) | SA-10, SI-7, CM-14 |
| PS.3 (Archive Releases) | CP-9, CM-3, SA-10 |
| PW.1 (Secure Design) | SA-8, SA-17, RA-3, PL-8 |
| PW.2 (Design Review) | SA-11, CA-2, SA-4 |
| PW.4 (Reuse Components) | SA-4, SA-9, SA-12, CM-14 |
| PW.5 (Secure Coding) | SA-11, SA-15, CM-3 |
| PW.6 (Build Hardening) | CM-6, SA-15, SI-3 |
| PW.7 (Code Review) | SA-11, SA-15, CA-7 |
| PW.9 (Security Testing) | SA-11, CA-8, RA-5 |
| RV.1 (Identify Vulnerabilities) | RA-5, SI-5, CA-7 |
| RV.2 (Remediate Vulnerabilities) | RA-5, SI-2, CA-7 |
| RV.3 (Root Cause Analysis) | CA-2, IR-4, PM-4 |

---

## NIST CSF Mapping

| SSDF Practice Group | CSF Functions | CSF Categories |
|--------------------|--------------|----------------|
| PO (Prepare) | Govern, Identify | GV.OC, GV.RM, ID.AM, ID.RA |
| PS (Protect Software) | Protect | PR.DS, PR.IP, PR.AT |
| PW (Produce Well-Secured) | Identify, Protect | ID.RA, PR.IP, PR.DS |
| RV (Respond to Vulnerabilities) | Detect, Respond, Recover | DE.CM, RS.AN, RS.MI, RC.IM |

---

## Roles and Responsibilities

| Role | SSDF Responsibilities |
|------|-----------------------|
| Software Developer | Implement PW.5 (secure coding), PW.6 (build hardening), PW.7 (code review); complete security training (PO.2) |
| Security Architect | Lead PW.1 (secure design), PW.2 (design review), PO.1 (security requirements) |
| DevSecOps Engineer | Implement PO.3 (toolchains), PO.5 (secure environments), PW.6, PW.9 (DAST in CI/CD) |
| QA/Test Engineer | Execute PW.9 (security testing), maintain security regression tests |
| Security Engineer | Perform PW.7 (security code review), triage SAST/DAST findings, support PO.4 (release criteria) |
| Product Owner | Prioritise security requirements (PO.1), approve risk acceptance decisions (RV.2) |
| CISO/Security Lead | Define organisational security requirements (PO.1), approve SSDF programme (PO.2), review RV.3 trend reports |
| Software Procurement | Evaluate third-party components (PW.4), collect supplier attestations and SBOMs (PS.2, PS.3) |
