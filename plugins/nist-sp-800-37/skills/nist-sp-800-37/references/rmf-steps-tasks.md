# NIST SP 800-37 Rev 2 — RMF Steps and Tasks Reference

Source: NIST Special Publication 800-37 Rev 2, December 2018
https://doi.org/10.6028/NIST.SP.800-37r2

---

## Step 0 — Prepare

### Organisation-Level Tasks

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| P-1 | Risk Management Roles | Laws, EOs, directives, policies | Documented assignment of risk management roles | HO, SO, SAOP, CISO, AO |
| P-2 | Risk Management Strategy | Mission/business needs, risk tolerance | Risk management strategy; risk tolerance statements | HO, SAOP, CISO, AO |
| P-3 | Risk Assessment (Org) | Threat info, mission info, system inventory | Org-level risk assessment | CISO, Risk Executive |
| P-4 | Org-Wide Control Assignments | Risk assessment, enterprise architecture | Control allocation decisions | CISO, AO |
| P-5 | Mission/Business Functions | Stakeholder needs, mission statements | Mission/business function descriptions | SO, Mission/Business Owner |
| P-6 | Information Types | SP 800-60 Vol I & II | Information type taxonomy for the organisation | SO, SAOP |
| P-7 | Common Controls | Enterprise architecture, security plan templates | Common control register; CCP assignments | CISO, CCP |
| P-8 | Tailoring Guidance | SP 800-53, organisational policy | Org-specific tailoring policies | CISO, AO |
| P-9 | Enterprise Architecture | SP 800-160; security/privacy principles | Security and privacy architecture | SO, Enterprise Architect |
| P-10 | Requirements and Capabilities | Applicable laws, regulations, standards | Security and privacy requirements register | CISO, SAOP, Legal |

### System-Level Tasks

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| P-11 | Stakeholders | Mission analysis | Stakeholder register | SO |
| P-12 | System-Level Roles | Org-level assignments | Documented system-level role assignments | SO, AO, CISO |
| P-13 | Assets | System description | Asset inventory | SO, ISSO |
| P-14 | System-Level Risk Assess. | P-3 output, system information | System-level risk assessment | ISSO, SCA |
| P-15 | Auth. Boundary | Architecture, data flows | System boundary documentation | SO, ISSO |
| P-16 | System Registration | Boundary, categorisation | System registered in agency ISCM tool | SO, ISSO |
| P-17 | Laws and Regulations | Applicable legal framework | Legal requirements register | ISSO, Legal |
| P-18 | Common Control Providers | CCP register | Inheritance register; signed agreements | ISSO, CCP |

---

## Step 1 — Categorise

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| C-1 | System Description | SDLC documentation, contracts | Documented system description | SO |
| C-2 | Security Categorisation | FIPS 199, SP 800-60; system description | Security categorisation (SC = {C, I, A}) using FIPS 199; registered in ISCM | SO, ISSO, SAOP |

### FIPS 199 Categorisation Steps
1. Identify information types using SP 800-60 Vol II categories
2. Assign provisional C, I, A values for each type
3. Adjust based on mission criticality or aggregation (document all adjustments)
4. Apply the high-water mark: SC = {max(C values), max(I values), max(A values)}
5. Assign overall system impact level = max(SC.C, SC.I, SC.A)
6. Map to baseline: LOW = Low baseline; MODERATE = Moderate baseline; HIGH = High baseline

---

## Step 2 — Select

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| S-1 | Control Selection | SP 800-53 baselines; categorisation result | Initial control baseline selected | ISSO, SO |
| S-2 | Tailoring | Scoping guidance, risk assessment, overlays | Tailored control baseline; documented decisions | ISSO, SO, AO |
| S-3 | Control Assignment | Common control register | Control assignment (system/common/hybrid) per control | ISSO, CCP |
| S-4 | Monitoring Strategy | Org monitoring policy | Initial monitoring strategy integrated into SSP | ISSO |
| S-5 | SSP Approval | Completed SSP | Signed SSP | SO, AO |

### SP 800-53 Rev 5 Control Families
| ID | Family |
|----|--------|
| AC | Access Control |
| AT | Awareness and Training |
| AU | Audit and Accountability |
| CA | Assessment, Authorization, and Monitoring |
| CM | Configuration Management |
| CP | Contingency Planning |
| IA | Identification and Authentication |
| IR | Incident Response |
| MA | Maintenance |
| MP | Media Protection |
| PE | Physical and Environmental Protection |
| PL | Planning |
| PM | Program Management |
| PS | Personnel Security |
| PT | Personally Identifiable Information Processing and Transparency |
| RA | Risk Assessment |
| SA | System and Services Acquisition |
| SC | System and Communications Protection |
| SI | System and Information Integrity |
| SR | Supply Chain Risk Management |

---

## Step 3 — Implement

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| I-1 | Control Implementation | Approved SSP; design documentation | Implemented controls; updated SSP | SO, ISSO |
| I-2 | Update SSP | Implementation evidence | SSP implementation narratives completed | ISSO |

---

## Step 4 — Assess

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| A-1 | Assessment Preparation | SSP; SP 800-53A | Security Assessment Plan (SAP) | SCA, ISSO |
| A-2 | Control Assessment | SAP; SP 800-53A assessment procedures | SAR with findings | SCA |
| A-3 | Remediations | SAR findings | Remediated weaknesses (where feasible); updated SSP | ISSO, SO |
| A-4 | Assessment Report | Post-remediation assessment | Final SAR | SCA |
| A-5 | POA&M | SAR findings | Plan of Action and Milestones | ISSO, SO |

### Assessment Independence Requirements
- SCA must be **organisationally independent** of the ISSO/SO for HIGH-impact systems
- For MODERATE: independence is strongly encouraged
- For LOW: independence is preferred but an independent self-assessment may be acceptable with documented justification

---

## Step 5 — Authorise

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| R-1 | Authorization Package | SSP, SAR, POA&M | Complete authorization package | ISSO, SO |
| R-2 | Risk Determination | Authorization package; risk tolerance | Risk determination (residual risk assessment) | AO, AODR |
| R-3 | Risk Response | Risk determination | Risk response decision (accept/mitigate/transfer/avoid) | AO |
| R-4 | Authorization Decision | Risk response | Signed ATO (or DATO); authorization memo | AO |
| R-5 | Authorization Reporting | Authorization decision | OMB/FISMA reporting; agency dashboards updated | CISO, AO |

### ATO Decision Factors

The AO considers:
1. Completeness and quality of the authorization package
2. Overall residual risk level vs. organisational risk tolerance
3. Acceptability of POA&M timelines and milestones for open findings
4. Whether critical/high findings are resolved or have accepted risk with justification
5. Legal and regulatory compliance status
6. Prior ATO history and operational need

---

## Step 6 — Monitor

| Task # | Task Name | Primary Inputs | Key Outputs | Roles |
|--------|-----------|---------------|-------------|-------|
| M-1 | Monitoring Strategy | Org ISCM strategy | System monitoring strategy | ISSO |
| M-2 | Configuration Management | Baseline configuration | Configuration baselines; change management records | ISSO, SO |
| M-3 | Ongoing Assessments | Monitoring strategy | Ongoing assessment results | SCA, ISSO |
| M-4 | Ongoing Risk Response | Assessment results | Updated risk response decisions | AO, AODR |
| M-5 | Authorisation Updates | Significant change notification; ongoing assessments | Updated authorization decision; reauthorisation if required | AO |
| M-6 | Security Posture Reporting | Monitoring data | Security posture reports to AO and CISO | ISSO |
| M-7 | System Disposal | Decommission plans | Media sanitisation records; disposal documentation | SO, ISSO |

### Ongoing Authorisation Model
The **ongoing authorisation** model replaces fixed 3-year reauthorisation cycles with continuous monitoring. Requirements:
1. Real-time or near-real-time security posture data
2. Automated reporting dashboards accessible to AO
3. Defined triggers that escalate to AO review outside of normal reporting cycles
4. Monitoring program that provides sufficient coverage and confidence to support ongoing authorisation decisions

---

## RMF and SDLC Integration

| SDLC Phase | Relevant RMF Tasks |
|-----------|-------------------|
| Initiation | P-11 through P-18 (System-level Prepare) |
| Development/Acquisition | C-1, C-2, S-1 through S-5 |
| Implementation | I-1, I-2 |
| Operations/Maintenance | A-1 through A-5; R-1 through R-5; M-1 through M-6 |
| Disposal | M-7 |
