# SSDF Implementation Guidance — Programme Establishment and Maturity

**Source:** NIST SP 800-218 v1.1; NIST IR 8397 (Guidelines on Minimum Standards for Developer Verification); NIST SP 800-218A (AI/ML application supplement, draft); OMB M-22-18; OMB M-23-16

This reference provides practical guidance for organisations implementing the SSDF: how to assess current-state maturity, prioritise implementation, build an SSDF programme, and demonstrate compliance through attestation and measurable outcomes.

---

## SSDF Implementation Approach

The SSDF is not prescriptive about implementation order or required tools. It defines outcomes (practices and tasks) rather than mechanisms. Organisations should:

1. Assess current-state: identify which practices are already implemented, partially implemented, or absent
2. Prioritise gaps: based on risk, regulatory requirements, and resources available
3. Integrate into existing processes: the SSDF supplements existing SDLC methodologies (Agile, DevOps, waterfall); it does not replace them
4. Iterate: implement the highest-priority practices first; expand coverage over time
5. Document and measure: maintain evidence of practice implementation

---

## SSDF Maturity Assessment

### Current-State Assessment Template

For each practice, assess the current state using this scale:

| Maturity Level | Description |
|---------------|-------------|
| 0 — Not Implemented | Practice is not performed; no documentation or tooling |
| 1 — Initial | Practice is performed ad-hoc or informally; results are not consistent |
| 2 — Documented | Practice is defined; documentation exists; performed consistently in most projects |
| 3 — Managed | Practice is performed consistently; metrics collected; management reviews results |
| 4 — Optimised | Practice is continuously improved based on metrics and feedback |

### Practice Maturity Assessment Grid

| Practice | Current Level | Target Level | Gap | Priority | Owner |
|---------|--------------|-------------|-----|----------|-------|
| PO.1 Security Requirements | — | — | — | — | — |
| PO.2 Roles/Responsibilities | — | — | — | — | — |
| PO.3 Toolchains | — | — | — | — | — |
| PO.4 Security Check Criteria | — | — | — | — | — |
| PO.5 Secure Environments | — | — | — | — | — |
| PS.1 Protect Code | — | — | — | — | — |
| PS.2 Integrity Verification | — | — | — | — | — |
| PS.3 Archive Releases | — | — | — | — | — |
| PW.1 Secure Design | — | — | — | — | — |
| PW.2 Design Review | — | — | — | — | — |
| PW.4 Reuse Components | — | — | — | — | — |
| PW.5 Secure Coding | — | — | — | — | — |
| PW.6 Build Hardening | — | — | — | — | — |
| PW.7 Code Review | — | — | — | — | — |
| PW.9 Security Testing | — | — | — | — | — |
| RV.1 Identify Vulnerabilities | — | — | — | — | — |
| RV.2 Remediate Vulnerabilities | — | — | — | — | — |
| RV.3 Root Cause Analysis | — | — | — | — | — |

---

## SSDF Implementation Roadmap

### Phase 1 — Foundation (Months 1–3)

**Focus:** Essential controls that have broad risk reduction impact and low implementation complexity.

| Practice | Milestone | Activities |
|---------|-----------|-----------|
| PO.2 | Security training programme initiated | Define training curriculum per role; assign to all developers; track completion |
| PO.5 | Secure environment baseline | Enable MFA for all developer accounts and code repositories; enable branch protection on protected branches; enforce required reviewers |
| PS.1 | Code protection baseline | Enable audit logging on code repositories; configure CODEOWNERS; enforce signed commits |
| PW.5 | SAST integrated | Deploy SAST tool (e.g., Semgrep) to CI pipeline; configure security rulesets; establish finding review process |
| PW.4 | SCA integrated | Deploy SCA tool (e.g., OWASP Dependency-Check) to CI pipeline; configure CVE threshold; alert on new highs |
| RV.1 | Vulnerability intake | Establish security@org monitoring; define internal CVE monitoring frequency; subscribe to CISA KEV feed |
| RV.2 | Remediation SLA defined | Publish and communicate vulnerability remediation SLA by severity |

**Phase 1 success criteria:**
- 100% of production code repositories have branch protection enabled
- 100% of developers with repository write access have MFA enabled
- SAST and SCA running on every PR for all active development repositories
- Security training completion > 80%
- Documented vulnerability remediation SLA published

---

### Phase 2 — Depth (Months 3–9)

**Focus:** Processes and controls that require more organisational change and tool maturity.

| Practice | Milestone | Activities |
|---------|-----------|-----------|
| PO.1 | Security requirements process | Application risk classification in use; ASVS or equivalent requirements applied by risk tier; requirements in project backlogs |
| PO.3 | Toolchain formalised | Approved toolchain list published; all SDLC phases covered; tools integrated into pipeline |
| PO.4 | Phase-gate criteria | Phase-gate security checklists defined and in use; release criteria documented; exceptions process in place |
| PW.1 | Threat modelling adopted | Threat modelling process defined; architects and senior developers trained; threat model required for new systems and major changes |
| PW.5 | Secrets scanning | Pre-commit secrets detection deployed; CI pipeline secrets scan; existing repository history scanned |
| PS.2 | Artifact signing | Code signing process established for release artifacts; SHA-256 checksums published with all releases |
| RV.1 | VDP published | Vulnerability disclosure policy published; responsible disclosure process operational; security contact monitored |
| RV.3 | Root cause analysis | RCA process defined for critical/high vulnerabilities; RCA outcomes fed back into training updates |

**Phase 2 success criteria:**
- Threat models exist for all tier-1 and tier-2 applications
- Release artifacts are signed for all production releases
- Vulnerability disclosure policy publicly accessible
- Phase-gate checklists in use for at least 75% of active development projects
- SAST true-positive finding density decreasing from phase 1 baseline

---

### Phase 3 — Optimise (Months 9–18)

**Focus:** Advanced controls, supply chain security hardening, and programme maturity.

| Practice | Milestone | Activities |
|---------|-----------|-----------|
| PO.3 | DAST integrated | DAST (OWASP ZAP) running in CI against test environments; API security scanning implemented |
| PW.9 | Penetration testing programme | Annual penetration test cadence established; scope defined; findings tracked to closure |
| PW.6 | Build hardening | Compiler hardening flags enabled for compiled languages; container images run non-root; IaC scanning in CI |
| PS.2 | SBOM programme | SBOM generated for all releases; SBOM published to consumers or stored in artifact archive; SBOM signed |
| PS.3 | Release archive | Per-release security package archived with all required artifacts (SBOM, scan results, approval records) |
| PW.4 | Component governance | Approved component catalogue in use; EOL component tracking; automated dependency updates (Dependabot/Renovate) |
| PO.5 | Build environment hardening | Ephemeral build agents; OIDC-based pipeline authentication; no static secrets in CI/CD |
| RV.3 | Trend reporting | Quarterly vulnerability trend reports to management; training updated based on recurring CWEs |

**Phase 3 success criteria:**
- DAST running on all web-facing applications prior to production release
- SBOM generated and archived for 100% of production releases
- Ephemeral build agents in use; no static long-lived credentials in CI/CD pipelines
- Penetration testing completed for all tier-1 applications within the past 12 months
- Approved component catalogue covering all production software

---

## Application Risk Classification

Risk classification determines which SSDF practices apply at what rigour level. Classify applications at project inception.

### Classification Tiers

| Tier | Characteristics | SSDF Rigour |
|------|----------------|------------|
| Tier 1 — Critical | Processes highly sensitive data (PII, payment, health, government classified); internet-facing; failure causes significant harm; regulated | All SSDF practices at full rigour; penetration test annually (minimum); SBOM required; third-party security review for major releases |
| Tier 2 — High | Processes sensitive data; internal-facing; failure causes significant operational disruption | All SSDF practices; penetration test every 2 years; SBOM required |
| Tier 3 — Medium | Processes internal non-sensitive data; limited external access | Core SSDF practices (PO.1–PO.4, PS.1–PS.2, PW.5, PW.7, PW.9, RV.1–RV.2); DAST scan before major releases |
| Tier 4 — Low | Internal tools; no sensitive data; limited user base | Minimum practices (PS.1, PW.5, RV.1–RV.2); SAST in CI; SCA in CI |

### Risk Classification Criteria

Score each characteristic (0–2) to determine tier:

| Characteristic | 0 | 1 | 2 |
|---------------|---|---|---|
| Data sensitivity | Public data only | Internal / limited PII | PII, payment, health, credentials, classified |
| Internet exposure | No internet access | Indirect (behind gateway) | Direct internet access |
| User base | < 50 internal users | > 50 internal or any external (non-privileged) | General public or high-privilege external |
| Business criticality | Low operational impact | Moderate operational impact | Critical business process or regulatory requirement |
| Regulatory scope | No regulatory requirement | Soft regulatory guidance | Hard regulatory requirement (HIPAA, PCI DSS, FISMA, GDPR) |

Total score: 0–3 = Tier 4; 4–5 = Tier 3; 6–7 = Tier 2; 8–10 = Tier 1

---

## SSDF Compliance Evidence Requirements

### Evidence Types by Practice

| Practice | Required Evidence |
|---------|-----------------|
| PO.1 | Security requirements specification document; requirements traceability matrix |
| PO.2 | Role description with security responsibilities; training completion records; training curriculum |
| PO.3 | Approved toolchain list; CI/CD pipeline configuration; tool scan reports |
| PO.4 | Phase-gate checklist templates; filled checklists for representative releases; exception log |
| PO.5 | Environment architecture diagram showing separation; MFA enforcement policy; build config showing ephemeral agents |
| PS.1 | Repository RBAC configuration; audit log samples; CODEOWNERS file; branch protection settings |
| PS.2 | Signing certificate or key details; signed artifact with verification instructions; hash files |
| PS.3 | Release archive inventory; access control configuration; retention schedule |
| PW.1 | Threat model documents (per application); threat modelling process documentation |
| PW.2 | Design review records; design review checklist; reviewer qualifications |
| PW.4 | Approved component catalogue; SCA scan reports; EOL tracking records |
| PW.5 | Secure coding standards; SAST scan reports; training completion records |
| PW.6 | Build script showing compiler flags; container image configuration; IaC scan results |
| PW.7 | Pull request reviews (sample); SAST scan findings and dispositions |
| PW.9 | DAST scan reports; penetration test report; security test results |
| RV.1 | CVE monitoring alerts; vulnerability disclosure policy; VDP submission log |
| RV.2 | Vulnerability management register; remediation records showing dates; exception log |
| RV.3 | RCA records for critical/high findings; training updates triggered by RCA; trend reports |

### attestation Package for Federal Software Producers

For software supplied to US federal agencies under EO 14028 / OMB M-22-18:

**Required attestation documents:**

1. Software Attestation Form (using CISA template): signed by an authorised individual (typically CISO or VP Engineering)
2. SBOM in SPDX or CycloneDX format for each software release
3. Supporting artefacts (on request from agency): scan reports, test results, architecture documentation

**Attestation form key declarations:**

```
I, [Authorised Individual], [Title], [Company], hereby attest that:

1. [Company] maintains and follows a secure software development lifecycle
   that incorporates SSDF practices as described in NIST SP 800-218.
   
2. [Company] employs automated security testing, including:
   - Static analysis (SAST) integrated into the development process
   - Software composition analysis (SCA) for third-party component vulnerabilities
   - Dynamic analysis (DAST) for web-accessible components
   
3. [Software Name, Version] has been reviewed for security vulnerabilities
   and all critical and high-severity vulnerabilities have been remediated
   or risk-accepted with documented compensating controls.
   
4. A Software Bill of Materials (SBOM) for [Software Name, Version] is
   available and provided herewith.
   
5. [Company] maintains a vulnerability disclosure policy and will notify
   the agency within [timeframe] of discovery of any vulnerability that
   could affect the agency's use of the software.

Signature: _____________  Date: ____________
```

---

## SSDF Framework Cross-Mapping

### SSDF to ISO/IEC 27001:2022 Mapping

| SSDF Practice | ISO 27001:2022 Controls |
|--------------|------------------------|
| PO.1 (Security Requirements) | 8.26 (Application security requirements), 5.8 (Information security in project management) |
| PO.2 (Roles/Responsibilities) | 6.3 (Information security awareness, education and training), 5.2 (Information security roles and responsibilities) |
| PO.3 (Toolchains) | 8.28 (Secure coding), 8.26 (Application security requirements) |
| PO.4 (Security Check Criteria) | 8.29 (Security testing in development and acceptance) |
| PO.5 (Secure Environments) | 8.31 (Separation of development, test and production environments), 8.4 (Access to source code) |
| PS.1 (Protect Code) | 8.4 (Access to source code), 5.15 (Access control) |
| PS.2 (Integrity Verification) | 8.16 (Monitoring activities), 8.20 (Networks security), 5.30 (ICT readiness for business continuity) |
| PS.3 (Archive Releases) | 8.12 (Data masking), 5.33 (Protection of records) |
| PW.1 (Secure Design) | 8.25 (Secure development life cycle), 8.27 (Secure system architecture and engineering principles) |
| PW.4 (Reuse Components) | 8.30 (Outsourced development), 5.19 (Information security in supplier relationships) |
| PW.5 (Secure Coding) | 8.28 (Secure coding) |
| PW.6 (Build Hardening) | 8.28 (Secure coding), 8.9 (Configuration management) |
| PW.7 (Code Review) | 8.28 (Secure coding), 8.29 (Security testing in development and acceptance) |
| PW.9 (Security Testing) | 8.29 (Security testing in development and acceptance), 8.8 (Management of technical vulnerabilities) |
| RV.1 (Identify Vulnerabilities) | 8.8 (Management of technical vulnerabilities), 5.7 (Threat intelligence) |
| RV.2 (Remediate Vulnerabilities) | 8.8 (Management of technical vulnerabilities) |
| RV.3 (Root Cause Analysis) | 5.27 (Learning from information security incidents), 5.28 (Collection of evidence) |

---

### SSDF to NIST SP 800-53 Rev 5 Control Families

| SSDF Practice Group | Primary SP 800-53 Control Families |
|--------------------|-----------------------------------|
| PO — Prepare the Organisation | SA (System and Services Acquisition), AT (Awareness and Training), PL (Planning), PM (Program Management) |
| PS — Protect the Software | SA (SA-10 Developer Configuration Management), CM (Configuration Management), SI (System and Information Integrity) |
| PW — Produce Well-Secured Software | SA (SA-11, SA-15, SA-17), RA (Risk Assessment), CM, SI |
| RV — Respond to Vulnerabilities | RA-5 (Vulnerability Monitoring and Scanning), SI-2 (Flaw Remediation), CA-7 (Continuous Monitoring), IR (Incident Response) |

---

### SSDF to NIST CSF 2.0 Function Mapping

| SSDF Practice Group | CSF 2.0 Function | CSF Categories |
|--------------------|-----------------|----------------|
| PO — Prepare the Organisation | Govern (GV) | GV.OC (Organisational Context), GV.RM (Risk Management Strategy), GV.RR (Roles, Responsibilities, Authorities) |
| PO — Prepare the Organisation | Identify (ID) | ID.AM (Asset Management), ID.RA (Risk Assessment) |
| PS — Protect the Software | Protect (PR) | PR.DS (Data Security), PR.IP (Information Protection Processes) |
| PW — Produce Well-Secured Software | Identify (ID) | ID.RA (Risk Assessment) |
| PW — Produce Well-Secured Software | Protect (PR) | PR.IP (Information Protection Processes and Procedures) |
| RV — Respond to Vulnerabilities | Detect (DE) | DE.CM (Continuous Monitoring) |
| RV — Respond to Vulnerabilities | Respond (RS) | RS.AN (Incident Analysis), RS.MI (Incident Mitigation) |
| RV — Respond to Vulnerabilities | Recover (RC) | RC.IM (Incident Recovery Plan Execution and Communication) |

---

## SSDF for AI/ML Software (NIST SP 800-218A Alignment)

NIST SP 800-218A (draft supplement) extends the SSDF for AI and machine learning software. Key additional considerations:

### Additional Considerations by Practice Group

**PO (Prepare):**
- PO.1: Security requirements must include AI-specific risks: data poisoning, model evasion, model inversion, membership inference, model theft
- PO.2: Additional roles required: ML engineer (training pipeline security), data scientist (training data integrity), AI red team
- PO.3: AI/ML toolchain additions: model versioning (MLflow, DVC), training pipeline security scanning, data pipeline integrity checks

**PS (Protect):**
- PS.1: Protect training data, model weights, and fine-tuning datasets in addition to source code
- PS.2: Sign and version model artifacts (model cards, weights checksum); register models in a model registry with access controls
- PS.3: Archive training dataset provenance (lineage), model training configurations, and evaluation results per model version

**PW (Produce):**
- PW.1: Threat model must address ML-specific threats: adversarial examples (evasion), backdoor attacks (poisoning during training), model extraction
- PW.4: Evaluate pre-trained model trustworthiness: source, training data, known vulnerabilities (Hugging Face security advisories, CVEs in model infrastructure)
- PW.5: Data pipeline validation: schema enforcement, anomaly detection in training data, outlier rejection; input preprocessing validation at inference time

**RV (Respond):**
- RV.1: Monitor for ML-specific vulnerabilities: new attacks on model architecture type, exploits in inference framework (TensorFlow, PyTorch, ONNX Runtime)
- RV.2: Model update/rollback process equivalent to software patching; degraded model performance may indicate adversarial attack — include in incident criteria
- RV.3: Root cause analysis for AI incidents must distinguish: training data issue, model architecture issue, deployment configuration issue, adversarial attack

---

## Vendor / Third-Party SSDF Requirements

When an organisation procures software rather than developing it internally, SSDF practices apply to how the organisation defines and enforces software security requirements on suppliers.

### Procurement Checklist

| Item | SSDF Practice | Verification Method |
|------|--------------|---------------------|
| Does the supplier have a documented secure SDLC? | PO.1, PO.2 | Request SSDF attestation or equivalent policy documentation |
| Does the supplier perform SAST and SCA? | PW.5, PW.7, PW.4 | Request sample scan reports; verify tooling in attestation |
| Does the supplier perform penetration testing? | PW.9 | Request most recent penetration test executive summary or letter of attestation |
| Does the supplier publish SBOMs? | PS.2, PS.3 | Request SBOM for proposed software version; verify SPDX/CycloneDX format |
| Does the supplier sign release artifacts? | PS.2 | Verify artifact signatures; inspect signing certificate validity |
| Does the supplier have a vulnerability disclosure policy? | RV.1 | Review published VDP; verify security contact responsiveness |
| What is the supplier's vulnerability remediation SLA? | RV.2 | Contractually require: Critical <= 15 days, High <= 30 days |
| Does the supplier notify on significant vulnerabilities? | RV.2 | Require contractual notification obligation for Critical/High CVEs affecting supplied software |
| How does the supplier handle EOL components in the software? | PW.4 | Require SBOM review; require EOL component replacement obligations in contract |

### Contractual SSDF Requirements Clauses

**Clause 1 — Secure Development Attestation:**
Supplier shall, at execution and annually thereafter, provide a software security attestation confirming that the supplied software is developed in accordance with NIST SP 800-218 SSDF practices or equivalent. Supplier shall make supporting evidence available to Customer upon request with reasonable notice.

**Clause 2 — SBOM Delivery:**
Supplier shall deliver a machine-readable Software Bill of Materials (SBOM) in SPDX or CycloneDX format with each software release. The SBOM shall be signed by the Supplier and shall comply with NTIA minimum element requirements.

**Clause 3 — Vulnerability Notification:**
Supplier shall notify Customer within 5 business days of confirming a vulnerability with a CVSS base score >= 7.0 in any software component delivered under this agreement. Notification shall include CVSS score, CVE identifier (if available), affected versions, and Supplier's remediation plan and timeline.

**Clause 4 — Vulnerability Remediation SLA:**
Supplier shall release a patch or provide a verified compensating control for Critical vulnerabilities (CVSS >= 9.0) within 15 calendar days, High vulnerabilities (CVSS 7.0–8.9) within 30 calendar days, and Medium vulnerabilities (CVSS 4.0–6.9) within 90 calendar days of confirming the vulnerability.

**Clause 5 — EOL Component Restriction:**
Supplier shall not deliver software that incorporates components that have reached end-of-life without Customer's prior written approval. In the event a component reaches EOL during the contract term, Supplier shall notify Customer and provide a remediation plan within 30 days.

**Clause 6 — Source Code and Artifact Integrity:**
Supplier shall provide a cryptographic hash (SHA-256 minimum) and a digital signature for all software release artifacts. Customer may verify artifact integrity prior to installation. Supplier shall maintain signing key security in accordance with applicable industry standards.
