# NIST SP 800-53 - Assessment, RMF, ConMon, and Framework Mapping Reference

## SP 800-53A Rev 5 - Assessment Procedures

### Purpose

SP 800-53A Rev 5 (January 2022) provides **assessment procedures** for every control in SP 800-53 Rev 5. Each procedure specifies:

1. **Objectives** - what the assessment must determine
2. **Methods** - Examine, Interview, or Test
3. **Objects** - what to examine/interview/test

### The Three Assessment Methods

| Method | Description | Examples |
|--------|-------------|---------|
| **Examine** | Review artifacts and documentation | Policy documents, SSP, configuration files, system logs, architecture diagrams, audit records, training records |
| **Interview** | Discuss implementation with personnel | ISSO, system owner, help desk, IT administrators, end users, senior leaders |
| **Test** | Exercise mechanisms directly | Vulnerability scans, penetration tests, configuration checks, firewall rule reviews, backup restoration tests |

### Assessment Depth

| Depth | Description | When Used |
|-------|-------------|----------|
| **Basic** | Check for existence of controls | Initial assessments; Low impact systems |
| **Focused** | Evaluate implementation | Most common approach |
| **Comprehensive** | Thorough, in-depth assessment | High impact systems; 3PAO assessments |

### Security Assessment Report (SAR) Structure

The SAR documents assessment results:

1. **Executive Summary** - High-level findings and authorization recommendation
2. **Assessment Scope** - Systems, components, controls assessed
3. **Assessment Methodology** - Methods used, depth, timeframe
4. **Findings** - Control-by-control results
5. **Weaknesses and Deficiencies** - OTS (Other Than Satisfied) findings
6. **Risk Exposure** - Risk ratings for identified weaknesses
7. **Recommendations** - Remediation actions

**Finding format:**
```
Control: AC-2(3)
Objective: Determine if inactive accounts are disabled within the defined period.
Status: Other Than Satisfied
Finding: Audit of Active Directory accounts identified 47 accounts inactive for >120 days; 
         ODV is 90 days. Automated account review process is not functioning correctly.
Risk: Moderate - dormant accounts represent attack surface for credential-based attacks.
Recommendation: Fix automated review process; immediately disable the 47 identified accounts.
```

---

## Plan of Action and Milestones (POA&M)

### POA&M Purpose

The POA&M (CA-5) is a living document tracking all security weaknesses found during assessments, continuous monitoring, and self-assessment. Required for all federal systems.

### POA&M Required Fields

| Field | Description |
|-------|-------------|
| POA&M ID | Unique identifier |
| Weakness/Deficiency | Description of the finding |
| Source | How discovered (scan, audit, assessment, pen test) |
| Control ID | Related SP 800-53 control |
| Risk Level | Critical / High / Moderate / Low |
| Scheduled Completion Date | When remediation will be complete |
| Milestone Description | Steps to remediate with dates |
| Resources Required | Staff, tools, budget |
| Status | Open / Completed / Delayed / Risk Accepted |

### POA&M Timelines (FedRAMP Guidance)

| Risk Level | Remediation Deadline |
|-----------|---------------------|
| Critical | 30 days |
| High | 90 days |
| Moderate | 180 days |
| Low | 1 year |
| Operational Requirement | Risk accepted; ISSO/SO signature required |

### Risk Acceptance

When a weakness cannot be remediated within the standard timeline:
- Document a **Risk Acceptance** with business justification
- ISSO and System Owner must sign off
- Authorizing Official (AO) may need to approve for High/Critical
- Review at each ConMon cycle
- Cannot be risk-accepted indefinitely for High/Critical findings

---

## Risk Management Framework (RMF) - SP 800-37 Rev 2

### Step 1 - Prepare

**Purpose:** Establish the organizational and system context for managing security and privacy risk.

**Key tasks:**
- Assign roles: Authorizing Official (AO), System Owner (SO), ISSO, Senior Agency IS Official (SAISO)
- Develop or update organizational risk management strategy (PM-9)
- Identify common controls (PM-10)
- Conduct mission/business process analysis (PM-11)
- Perform organization-level risk assessment (RA-3)
- Establish information life cycle for the system

**Output:** Risk management roles assigned; organization-level risk assessment completed; common control inventory established.

### Step 2 - Categorize

**Purpose:** Categorize the system and information processed, stored, and transmitted based on FIPS 199.

**Key tasks:**
- Describe the system (SSP Section 1 and 2)
- Identify information types using SP 800-60
- Determine impact levels for C, I, A
- Determine overall system impact level (high-water mark)
- Document in the Security Categorization document

**Output:** System Security Categorization document (signed by AO and SO).

### Step 3 - Select

**Purpose:** Select, tailor, and document the controls for the system.

**Key tasks:**
- Select starting baseline from SP 800-53B (Low/Moderate/High)
- Apply tailoring (common controls, scoping, ODVs, compensating controls)
- Document all tailoring decisions in the SSP
- Develop continuous monitoring strategy (CA-7)
- Review and approve control selection (AO concurrence)

**Output:** SSP with control selection; ConMon strategy.

### Step 4 - Implement

**Purpose:** Implement the controls and document how they are deployed in the operational environment.

**Key tasks:**
- Implement the selected controls
- Document implementation in SSP (one narrative per control)
- Document design and implementation information for developer controls (SA-4)
- Identify and address supply chain risks (SR family)

**Output:** Implemented controls; completed SSP implementation narratives.

### Step 5 - Assess

**Purpose:** Determine if the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting security and privacy requirements.

**Key tasks:**
- Develop Security Assessment Plan (SAP) using SP 800-53A
- Select qualified assessors (independent for Moderate/High; 3PAO for FedRAMP)
- Conduct assessments (examine, interview, test)
- Document findings in SAR
- Develop initial POA&M from SAR findings

**Output:** SAP, SAR, initial POA&M.

**Independence requirements:**
- **Low systems:** Self-assessment permitted
- **Moderate systems:** Independent assessor (different team from implementers)
- **High systems / FedRAMP:** 3PAO required; must be accredited by A2LA/FedRAMP PMO

### Step 6 - Authorize

**Purpose:** Provide organizational accountability by requiring a senior official to determine if the security and privacy risk to organizational operations/assets is acceptable.

**Authorization package contents:**
1. System Security Plan (SSP)
2. Security Assessment Report (SAR)
3. Plan of Action and Milestones (POA&M)
4. Executive Summary (for AO review)

**Authorization decisions:**
- **Authorization to Operate (ATO)** - risk is acceptable; typically granted for 3 years
- **Common Control Authorization (CCA)** - for common control providers
- **Denial of Authorization to Operate (DATO)** - risk is not acceptable; system must be shut down or remediated
- **Authorization to Use (ATU)** - for external systems/services

**Ongoing authorization:** Continuous authorization (preferred for Moderate/High) replaces periodic re-authorization with real-time risk management.

### Step 7 - Monitor

**Purpose:** Maintain ongoing situational awareness about the security and privacy posture of the system.

**Key tasks:**
- Implement ConMon strategy (CA-7)
- Conduct ongoing assessments of selected controls
- Respond to changes in system and threat environment
- Report security status to AO
- Update SSP, SAR, POA&M as changes occur
- Conduct ongoing risk determination and acceptance

**FedRAMP ConMon requirements:**
- Monthly vulnerability scans (OS, databases, web apps)
- Annual penetration test (conducted by 3PAO)
- Monthly POA&M updates
- Significant change request before major system changes
- Annual security reviews

---

## Continuous Monitoring (ConMon) Strategy

### ConMon Frequencies (SP 800-137 / CA-7)

| Activity | Recommended Frequency | FedRAMP Frequency |
|----------|----------------------|------------------|
| Vulnerability scans (OS) | Monthly | Monthly |
| Vulnerability scans (Web app) | Monthly | Monthly |
| Vulnerability scans (Database) | Monthly | Weekly |
| Control assessments (selected) | Ongoing/quarterly | Annually |
| Security awareness training | Annual | Annual |
| Contingency plan testing | Annual | Annual |
| Full control assessment | Every 3 years / at reauthorization | Annual (3PAO) |
| Penetration testing | Annual (Moderate+) | Annual (3PAO) |

### ConMon Automation

Support tools for ConMon implementation:
- **SCAP (Security Content Automation Protocol)** - standardized vulnerability scanning
- **CVE/CVSS** - common vulnerability scoring
- **OVAL/XCCDF** - configuration checking
- **NVD (National Vulnerability Database)** - NIST vulnerability repository
- **CDM (Continuous Diagnostics and Mitigation)** - DHS/CISA program for federal agencies
- **OSCAL** - machine-readable security control documentation

---

## OSCAL - Open Security Controls Assessment Language

OSCAL (developed by NIST) provides machine-readable representations of SP 800-53 content:

### OSCAL Layers

| Layer | Purpose | Formats |
|-------|---------|---------|
| **Catalog** | Control definitions (SP 800-53 catalog) | JSON, XML, YAML |
| **Profile** | Baseline selection and tailoring | JSON, XML, YAML |
| **Component Definition** | Reusable component implementations | JSON, XML, YAML |
| **System Security Plan** | SSP in machine-readable format | JSON, XML, YAML |
| **Assessment Plan** | SAP in machine-readable format | JSON, XML, YAML |
| **Assessment Results** | SAR findings in machine-readable format | JSON, XML, YAML |
| **POA&M** | Plan of action in machine-readable format | JSON, XML, YAML |

**FedRAMP OSCAL adoption:** FedRAMP has been moving toward OSCAL-based SSP submissions. Tools supporting OSCAL: Trestle (IBM), Xacta 360, Atlasity, Empower.

---

## Cross-Framework Mapping

### SP 800-53 Rev 5 → ISO 27001:2022

| SP 800-53 Family | ISO 27001:2022 Annex A Controls |
|-----------------|-------------------------------|
| AC (Access Control) | 5.15–5.18 (Access, privilege), 8.2–8.5 |
| AT (Awareness & Training) | 6.3 (Security awareness) |
| AU (Audit) | 8.15 (Logging), 8.16 (Monitoring) |
| CA (Assessment) | 5.35 (IS review), 5.36 (Compliance) |
| CM (Config Mgmt) | 8.8–8.9 (Vulnerability, config), 8.32 |
| CP (Contingency) | 5.29 (BCP), 8.13 (Backup) |
| IA (Authentication) | 5.17 (Authentication), 8.5 (MFA) |
| IR (Incident Response) | 5.24–5.28 (Incident management) |
| PE (Physical) | 7.1–7.14 (Physical controls) |
| RA (Risk Assessment) | ISMS Clauses 6.1.2 (risk assessment) and 6.1.3 (risk treatment); note Annex A 5.1 is Policies for information security and 6.1 is Screening |
| SC (Comms Protection) | 5.14 (Transfer), 8.20–8.26 (Network) |
| SI (Integrity) | 8.7 (Malware), 8.8 (Vulnerability), 8.19 |
| SR (Supply Chain) | 5.19–5.22 (Supplier security) |

### SP 800-53 Rev 5 → NIST CSF 2.0

The CSF 2.0 (February 2024) maps to SP 800-53:

| CSF Function | Key SP 800-53 Families |
|-------------|----------------------|
| **GV (Govern)** | PM, PL, AT, RA |
| **ID (Identify)** | RA, CA, CM, PM |
| **PR (Protect)** | AC, AT, CM, IA, MA, MP, PE, SC, SI, SR |
| **DE (Detect)** | AU, CA, IR, RA, SI |
| **RS (Respond)** | IR, CA |
| **RC (Recover)** | CP, IR |

Full mapping: NIST publishes the CSF subcategory → SP 800-53 control mapping through the OLIR program and the Cybersecurity and Privacy Reference Tool (CPRT), not in SP 800-53B.

### SP 800-53 Rev 5 → CMMC 2.0

CMMC 2.0 is based on **NIST SP 800-171 Rev 2**, which derives from SP 800-53:

| CMMC Level | SP 800-53 Basis |
|-----------|----------------|
| Level 1 (Foundational) | Subset of 800-171 practices (17 practices from FAR clause) |
| Level 2 (Advanced) | Full SP 800-171 Rev 2 (110 practices = ~320 SP 800-53 controls) |
| Level 3 (Expert) | SP 800-171 + selected SP 800-172 controls |

SP 800-171 Appendix D provides the mapping from each 800-171 requirement to the SP 800-53 source controls.

### SP 800-53 Rev 5 → FedRAMP

FedRAMP uses the SP 800-53 Moderate or High baseline with overlay parameters:

| FedRAMP Difference | Detail |
|-------------------|--------|
| Specific ODV values | Defined in FedRAMP baseline documentation |
| Additional requirements | Incident reporting to US-CERT; 3PAO requirement |
| Cryptography | FIPS 140-2/140-3 validated modules explicitly required |
| ConMon | Specific monthly/annual frequencies required |
| SSP format | FedRAMP SSP template must be used |
| Authorization types | Agency ATO or JAB P-ATO |

---

## Key Roles in the RMF / SP 800-53 Context

| Role | Abbreviation | Responsibility |
|------|-------------|---------------|
| Authorizing Official | AO | Accepts risk; grants/denies ATO |
| Authorizing Official Designated Representative | AODR | Acts on behalf of AO |
| Chief Information Officer | CIO | Overall IT governance |
| Senior Agency Information Security Official | SAISO | Agency-wide IS oversight |
| Information System Security Officer | ISSO | Day-to-day security operations for system |
| Information System Security Manager | ISSM | Manages multiple ISSOs |
| System Owner | SO | Responsible for system operation |
| Common Control Provider | CCP | Implements shared/inherited controls |
| Security Control Assessor | SCA | Conducts independent assessment |
| Privacy Officer / CPO | CPO | Privacy program lead |

---

## Key NIST Publications Related to SP 800-53

| Publication | Title | Role |
|-------------|-------|------|
| SP 800-53 Rev 5 | Security and Privacy Controls | Main control catalog |
| SP 800-53A Rev 5 | Assessing Security and Privacy Controls | Assessment procedures |
| SP 800-53B | Control Baselines | Baseline definitions |
| SP 800-37 Rev 2 | Risk Management Framework | RMF steps |
| SP 800-60 Vol I/II | Information Types / Impact Levels | Categorization guidance |
| SP 800-30 Rev 1 | Risk Assessment | Risk assessment methodology |
| SP 800-137A | ConMon | Continuous monitoring |
| SP 800-63 Rev 4 | Digital Identity | Authentication assurance |
| SP 800-82 Rev 3 | OT Security | ICS/SCADA guide |
| SP 800-88 Rev 1 | Media Sanitization | Media disposal |
| SP 800-115 | Security Testing | Penetration testing methodology |
| FIPS 199 | Security Categorization | Impact level determination |
| FIPS 200 | Minimum Security Requirements | Baseline requirement |
| FIPS 140-3 | Cryptographic Modules | Cryptography standard |
