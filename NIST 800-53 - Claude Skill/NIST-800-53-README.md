# NIST SP 800-53 Revision 5 Skill for Claude

> ⚠️ **Disclaimer:** This skill provides informational guidance based on NIST SP 800-53 Rev 5, SP 800-53B, SP 800-53A Rev 5, and SP 800-37 Rev 2. It does not constitute authoritative NIST guidance or legal advice. For formal FISMA authorization decisions, FedRAMP assessments, and ATO packages, consult your Authorizing Official, ISSO, and accredited 3PAO.

---

## 1. What Does the Skill Do?

The NIST SP 800-53 Rev 5 Compliance Skill transforms Claude into an expert federal information security controls advisor with comprehensive knowledge of Special Publication 800-53 Revision 5 — *Security and Privacy Controls for Information Systems and Organizations* — published by NIST in September 2020. The skill guides federal agencies, contractors, cloud service providers, and system owners through the complete Risk Management Framework (RMF) lifecycle from system categorization through authorization and continuous monitoring.

The skill covers all 20 control families (AC through SR) across the Low, Moderate, and High impact baselines as defined in SP 800-53B. It supports FIPS 199 system categorization using the three confidentiality, integrity, and availability impact levels; baseline selection and tailoring including organization-defined value (ODV) assignment, scoping considerations, and overlay application; and SSP narrative writing with the three required components of implementation description, responsible roles, and evidence artifacts.

The skill incorporates the key Rev 5 enhancements: the new Privacy (PT) family with 8 controls addressing PII consent, minimization, and transparency; the new Supply Chain Risk Management (SR) family with 12 controls; outcome-based control statements; and the separation of baselines into SP 800-53B. It also covers SP 800-53A Rev 5 assessment procedures using Examine, Interview, and Test methods, POA&M management, and continuous monitoring strategy.

Cross-framework mapping is a core capability: the skill maps SP 800-53 controls to FedRAMP parameters, FISMA requirements, CMMC 2.0 Level 2 (derived from SP 800-171), ISO 27001:2022, NIST CSF 2.0, HIPAA Security Rule, and PCI DSS v4.0. This makes the skill equally useful for federal agencies pursuing ATO, cloud providers seeking FedRAMP authorization, and private sector organizations benchmarking against federal security standards.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|------------------------|
| **ISSOs (Information System Security Officers)** | Write SSP narratives, manage POA&Ms, prepare assessment packages, advise on control implementation |
| **System Owners** | Understand control obligations for their systems, make tailoring decisions, respond to assessment findings |
| **Authorizing Officials** | Understand risk posture from assessment findings, evaluate ATO recommendations |
| **3PAOs and Independent Assessors** | Reference assessment procedures (SP 800-53A), evaluate control sufficiency, write SAR findings |
| **FedRAMP Cloud Service Providers** | Navigate the Moderate/High baseline, apply FedRAMP overlay parameters, prepare authorization packages |
| **Federal Agency IT Teams** | Implement FISMA-required controls, build continuous monitoring programmes, categorize systems |
| **CMMC Practitioners** | Map CMMC 2.0 Level 2 requirements to SP 800-53 controls via SP 800-171 derivation |
| **Security Architects** | Design systems with control inheritance, apply overlays (OT/SCADA, healthcare, cloud) |

---

## 3. Common Use Cases

### System Categorization and Baseline Selection
- "Help me categorize our HR system under FIPS 199"
- "What is the high-water mark rule for system categorization?"
- "Which baseline applies to a system processing PII and financial data?"
- "How do I use SP 800-60 to determine information type impact levels?"

### Control Family Deep-Dives
- "Explain all the AC (Access Control) family controls and their baseline assignments"
- "What does SI-3 (Malware Protection) require at the Moderate baseline?"
- "Walk me through the IA family controls for a High impact system"
- "What enhancements does the SR (Supply Chain Risk Management) family include?"

### SSP Narrative Writing
- "Write an SSP narrative for AC-2 Account Management for our Azure-hosted system"
- "What are the three required components of every SSP control narrative?"
- "Draft an implementation statement for SC-28 Protection of Information at Rest"
- "What are common SSP pitfalls that assessors cite as findings?"

### Baseline Tailoring and Overlays
- "Which controls can we scope out for a system with no remote maintenance?"
- "How do we apply the FedRAMP overlay to a Moderate impact system?"
- "What ODV should we set for AU-11 audit log retention?"
- "We operate an OT/SCADA system — what overlay should we apply?"

### RMF Step Guidance
- "Walk me through all 7 RMF steps for a new federal information system"
- "What are the required outputs from the RMF Categorize step?"
- "How does continuous monitoring (Step 7) work in practice?"
- "What does the ATO package need to include for the Authorize step?"

### Gap Assessment and POA&M
- "Conduct a NIST 800-53 Moderate baseline gap assessment for our system"
- "What are the required fields in a POA&M under CA-5?"
- "How do I prioritize POA&M items — what are the remediation timelines?"
- "We have 15 OTS findings from our assessment — help me build our POA&M"

### Cross-Framework Mapping
- "Map our ISO 27001:2022 controls to NIST SP 800-53 control families"
- "How does FedRAMP relate to NIST SP 800-53?"
- "We're pursuing CMMC Level 2 — how does that map to SP 800-53?"
- "What SP 800-53 controls satisfy HIPAA Security Rule §164.312?"

---

## 4. How to Use the Skill

### Installation
1. Download `nist-800-53.skill` from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `nist-800-53.skill`
4. The skill is now active in all Claude sessions

### Triggering the Skill

The skill activates automatically when you raise NIST SP 800-53, RMF, FISMA, or federal security control topics. No special commands are needed. Example natural-language phrases that trigger the skill:

- *"What does NIST 800-53 require for...?"*
- *"I need to write an SSP narrative for..."*
- *"Help me categorize this system under FIPS 199"*
- *"We're going through FedRAMP authorization"*
- *"What baseline controls apply to a Moderate impact system?"*
- *"Walk me through the RMF steps"*
- *"We have a FISMA assessment coming up"*

### Example Prompts

```
We are categorizing a new federal HR system that processes employee PII including
names, SSNs, salary information, and performance reviews. Walk me through the
FIPS 199 categorization process and tell me which SP 800-53B baseline we should select.
```

```
Write SSP narratives for the following three controls for our AWS GovCloud-hosted
system: AC-2 (Account Management), IA-2(1) (MFA for Privileged Accounts), and
SC-28(1) (Encryption at Rest). Follow the standard three-component format.
```

```
We are a cloud service provider pursuing FedRAMP Moderate authorization. Our
assessors found 12 OTS findings. Help me build a POA&M with appropriate risk
levels, remediation timelines, and milestone descriptions for each finding.
```

```
Map the following SP 800-53 Rev 5 control families to their ISO 27001:2022 Annex A
equivalents and identify controls in each catalog that have no direct mapping counterpart:
AC, AU, IA, SC, and SI families.
```

```
We need to apply the Supply Chain Risk Management (SR) family controls for our
federal system. Explain each of the 12 SR controls, which baseline they apply to,
and provide implementation guidance for a Moderate impact system.
```

---

## 5. Skill Implementation Details

### Architecture

```
plugins/nist-800-53/
└── skills/
    └── nist-800-53/
        ├── SKILL.md                        # Core skill — framework overview, Rev 5 changes,
        │                                   #   8-step implementation guide (categorization through
        │                                   #   assessment/RMF), response format rules, cross-
        │                                   #   framework mapping table
        └── references/
            ├── control-families.md         # All 20 control families with key controls, L/M/H
            │                               #   baseline assignments, enhancement details,
            │                               #   implementation tips, common assessment findings
            ├── baselines-tailoring.md      # SP 800-53B baseline tables (Low/Moderate/High/Privacy),
            │                               #   tailoring actions, ODV examples, overlay guidance,
            │                               #   privacy and supply chain baseline specifics
            └── assessment-rmf.md           # SP 800-53A assessment procedures (Examine/Interview/Test),
                                            #   assessment depth levels, SAR structure, POA&M fields
                                            #   and timelines, RMF 7-step guidance, ConMon strategy,
                                            #   OSCAL, cross-framework mapping detail
```

### What's in SKILL.md

- Expert persona: NIST SP 800-53 compliance advisor with SP 800-53/53A/53B and SP 800-37 knowledge
- Response format table mapping 6 task types to structured outputs (family deep-dive, baseline selection, gap assessment, SSP narrative, RMF guidance, Q&A)
- Citation standard: control ID + enhancement (e.g., AC-2(3), SI-3(10)) with baseline designation
- Framework overview: authority (FISMA 2014), publication history, current Rev 5 version
- Key Rev 5 changes table (6 major changes from Rev 4)
- 8-step implementation guide: FIPS 199 categorization → baseline selection → 20 control families → tailoring → overlays → SSP narratives → SP 800-53A assessment → RMF integration
- FIPS 199 impact level table (Low/Moderate/High for C/I/A)
- SP 800-53B baseline comparison (Low ~156, Moderate ~323, High ~422 controls)
- All 20 control families with IDs, control ranges, and key focus areas
- Tailoring actions (5 types) and ODV examples table
- Overlay types and use cases
- SSP narrative structure with three components and common pitfalls
- SP 800-53A assessment methods and finding format
- RMF 7-step table with names, outputs, and roles
- Cross-framework mapping table (FedRAMP, FISMA, CMMC 2.0, ISO 27001, CSF 2.0, HIPAA, PCI DSS)

### What's in the reference files

| File | Contents |
|------|----------|
| `references/control-families.md` | All 20 families with control-by-control listings: AC (25 controls), AT (6), AU (16), CA (9), CM (14), CP (13), IA (13), IR (10), MA (6), MP (8), PE (23), PL (11), PM (32), PS (9), PT (8), RA (10), SA (23), SC (51), SI (23), SR (12) — each with L/M/H baseline checkmarks, enhancement details, and implementation notes |
| `references/baselines-tailoring.md` | SP 800-53B baseline descriptions for Low, Moderate, and High impact with key characteristics and critical additions at each tier; tailoring guidance covering all 5 tailoring action types; ODV examples for common controls; overlay application guidance for FedRAMP, DoD/CNSS, IC, Privacy, ICS, and Healthcare overlays; privacy and supply chain baseline specifics |
| `references/assessment-rmf.md` | SP 800-53A Rev 5 assessment procedures: 3 methods (Examine/Interview/Test) with examples; assessment depth levels (Basic/Focused/Comprehensive); SAR structure (7 sections); finding format with example; POA&M purpose, required fields (9 fields), and FedRAMP remediation timelines by risk level; RMF 7-step guidance; ConMon strategy; OSCAL guidance; cross-framework mapping detail |

### Inputs used to build the skill

| Input | Detail |
|-------|--------|
| Primary publication | NIST SP 800-53 Rev 5 (September 2020, updated December 2020) |
| Control baselines | NIST SP 800-53B (October 2020) |
| Assessment procedures | NIST SP 800-53A Rev 5 (January 2022) |
| RMF | NIST SP 800-37 Rev 2 |
| System categorization | FIPS 199, FIPS 200, NIST SP 800-60 Vol II |
| Legal authority | FISMA 2014 (44 U.S.C. § 3551 et seq.) |
| FedRAMP mapping | FedRAMP Moderate/High baselines + overlay parameters |
| CMMC mapping | CMMC 2.0 Level 2 via NIST SP 800-171 derivation |
| ISO 27001 mapping | ISO/IEC 27001:2022 Annex A cross-walk |
| CSF mapping | NIST CSF 2.0 (SP 800-53B Appendix C) |
| HIPAA mapping | HHS HIPAA Security Rule crosswalk |
| OT/SCADA guidance | NIST SP 800-82 |

### Skill trigger phrases

`NIST 800-53`, `SP 800-53`, `NIST SP 800-53 Rev 5`, `FISMA controls`, `federal information security controls`,
`RMF`, `Risk Management Framework`, `FIPS 199`, `FIPS 200`, `SSP narrative`,
`System Security Plan`, `ATO`, `Authority to Operate`, `POA&M`, `Plan of Action and Milestones`,
`Low baseline`, `Moderate baseline`, `High baseline`, `control tailoring`, `ODV`,
`organization-defined values`, `SP 800-53A`, `security assessment`, `SAR`,
`continuous monitoring`, `ConMon`, `FedRAMP authorization`, `3PAO`, `ISSO`,
`AC-2`, `IA-2`, `SC-28`, `SI-3`, `AU-12`, `control family`, `control enhancement`,
`supply chain risk management SR`, `privacy controls PT`, `OSCAL`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.8.0 — August 2026
