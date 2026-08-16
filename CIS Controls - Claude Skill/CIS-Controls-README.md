# CIS Controls v8 Skill for Claude

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert cybersecurity advisor grounded in the **CIS Controls v8** (formerly CIS Top 20, now CIS Top 18), published by the Center for Internet Security in May 2021. CIS Controls v8 is the most widely adopted prioritized cybersecurity framework globally — built from real-world attack data drawn from the MITRE ATT&CK framework and the Verizon Data Breach Investigations Report — and this skill provides deep, actionable guidance across every one of its 18 controls and all 153 safeguards.

The skill's defining feature is its handling of **Implementation Groups (IGs)** — the scoping mechanism that makes CIS Controls practical for any organization size. It can profile an organization, determine the correct IG (IG1 for small businesses with limited IT staff, IG2 for mid-size organizations with dedicated IT, IG3 for large enterprises with sensitive regulated data), and scope all subsequent guidance to the applicable safeguards. This means a 12-person startup and a Fortune 500 enterprise both get advice calibrated to their actual obligations, not a generic list of 153 controls.

For each of the 18 controls, the skill provides safeguard-level guidance: what the control requires, why it matters in terms of real attack scenarios, how to implement it with practical tooling examples, and what evidence to collect for assessments. It handles gap assessments, policy and procedure drafting, security awareness training program design, incident response planning (Control 17), and penetration testing program development (Control 18).

The skill also provides **cross-framework mapping** — translating CIS Controls v8 safeguards to their equivalents in NIST CSF 2.0, ISO 27001:2022 Annex A, CMMC 2.0, and SOC 2 Trust Services Criteria. This makes it particularly valuable for organizations that need to satisfy multiple frameworks simultaneously, or that want to use CIS Controls as the implementation backbone for a formal certification program.

---

## 2. Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **CISOs and security managers** | IG scoping, gap assessment leadership, risk-based remediation prioritization |
| **IT security engineers** | Safeguard-level implementation guidance, tooling recommendations, configuration standards |
| **Compliance officers** | Mapping CIS Controls to regulatory requirements (CMMC, ISO 27001, SOC 2, NIST CSF) |
| **Small business IT teams** | IG1 essential cyber hygiene — practical guidance for resource-constrained environments |
| **Risk managers** | Connecting CIS Controls gaps to MITRE ATT&CK threat scenarios and business risk |
| **Auditors and assessors** | Gap assessment methodology, maturity scoring using CSAT or RAG scoring |
| **DevOps and platform engineers** | Controls 1–4, 7, 8, 16 — asset inventory, secure configuration, patching, logging |
| **Security awareness managers** | Control 14 — training program design and content planning |
| **Penetration testers and red teams** | Control 18 — pen test program scoping, methodology, and remediation tracking |
| **vCISOs and security consultants** | Client assessments, IG determination, multi-framework mapping for compliance projects |

---

## 3. Common Use Cases

### Implementation Group Scoping
- *"We're a 50-person professional services firm with one IT person. Which Implementation Group applies to us?"*
- *"Our company stores health records for clients. Does that push us to IG2 or IG3?"*
- *"What's the difference between IG1 and IG2? Which safeguards get added?"*
- *"We just completed IG1. What's the priority order for tackling IG2 safeguards?"*

### Gap Assessment and Remediation Roadmap
- *"Conduct a CIS Controls v8 gap assessment for a mid-size financial services firm at IG2."*
- *"We have asset inventory (Control 1) and account management (Control 5) in place. Show me the highest-risk remaining gaps."*
- *"Build a 12-month remediation roadmap for a company that has completed IG1 and is working toward IG2."*
- *"Score our current controls maturity against CIS Controls v8 using RAG status."*

### Safeguard-Level Implementation Guidance
- *"How do we implement CIS Control 6, Safeguard 6.3 — MFA for externally exposed applications?"*
- *"What does CIS Control 8 (Audit Log Management) require at IG1 vs IG2?"*
- *"We need to implement Control 3 (Data Protection). Walk me through the safeguards and recommended tools."*
- *"What tooling do you recommend for CIS Control 7 continuous vulnerability management for an AWS environment?"*

### Policy and Procedure Drafting
- *"Draft a Vulnerability Management Policy aligned to CIS Control 7."*
- *"Write an Audit Log Management procedure covering CIS Control 8 safeguards for our IG2 environment."*
- *"Create an Incident Response Plan framework aligned to CIS Control 17."*
- *"Draft a Penetration Testing Policy that satisfies CIS Control 18."*

### Cross-Framework Mapping
- *"Map our CIS Controls v8 IG2 implementation to NIST CSF 2.0 subcategories."*
- *"Which CIS Controls v8 safeguards satisfy CMMC 2.0 Access Control and Identification & Authentication domains?"*
- *"Show me how CIS Controls map to ISO 27001:2022 Annex A controls so I can use our CIS gap assessment for our ISO audit."*
- *"We're doing SOC 2 and CIS Controls simultaneously. Where do the frameworks overlap?"*

### Incident Response and Penetration Testing
- *"Design our annual penetration testing program per CIS Control 18."*
- *"Build an incident response process that satisfies all CIS Control 17 safeguards."*
- *"What post-incident review elements does CIS Control 13 and Control 17 require?"*

---

## 4. How to Use the Skill

### Installation
1. Download the `cis-controls.skill` file from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `cis-controls.skill`
4. The skill is immediately active in your Claude sessions

### Triggering the Skill
The skill activates automatically when your message relates to CIS Controls, CIS Benchmarks, Implementation Groups, or cyber hygiene frameworks. Example phrases that trigger it:

- *"CIS Controls gap assessment"*
- *"Which Implementation Group are we?"*
- *"What safeguards cover MFA requirements in CIS?"*
- *"Map CIS Controls to NIST CSF"*
- *"CIS Control 6 implementation guidance"*
- *"CIS Benchmark for Windows Server"*
- *"IG1 essential cyber hygiene for small business"*
- *"CIS Controls v8 vs v7 — what changed?"*

### Example Prompts

```
"Profile our organization and determine our Implementation Group: we're 
a 200-person manufacturing company, we have a 3-person IT team (no 
dedicated security staff), we store customer PII and some proprietary 
manufacturing IP, and we have basic antivirus and firewall in place but 
no formal security program."
```

```
"Run a CIS Controls v8 IG2 gap assessment. We have: asset inventory 
(partial), no software allowlisting, basic firewall rules, password 
policy enforced, MFA on email only, monthly patching cycle, no SIEM, 
no formal incident response plan."
```

```
"Map the following CIS Controls v8 safeguards to their CMMC 2.0 
equivalents: 5.1, 5.2, 5.4, 6.1, 6.3, 6.5, 7.1, 7.3, 8.2."
```

```
"Draft a Data Protection Policy (CIS Control 3) for an IG2 organization 
that uses AWS S3 for storage and handles customer financial data."
```

```
"Build a prioritized 6-month CIS Controls v8 remediation roadmap for 
an IG1 organization that has zero formal security controls in place. 
Focus on quick wins that address the highest-frequency attack vectors."
```

---

## 5. Skill Implementation Details

### Architecture

```
cis-controls/
├── SKILL.md                          # Core skill — all 18 controls, IG determination,
│                                     #   gap assessment workflow, framework mappings
└── references/
    ├── safeguards-detail.md          # All 153 safeguards with IG assignment,
    │                                 #   implementation notes, and recommended tools
    ├── implementation-guidance.md    # Control-by-control implementation guidance,
    │                                 #   tooling examples, metrics, common pitfalls
    └── framework-mappings.md         # Detailed CIS v8 ↔ NIST CSF 2.0 / ISO 27001:2022
                                      #   / CMMC 2.0 / SOC 2 mapping tables
```

**Total:** ~875 lines across 4 files (SKILL.md + 3 reference files)

### What's in SKILL.md

- **Response format routing** — 7 task types mapped to specific output formats (gap assessment tables, safeguard narrative, mapping tables, policy structure)
- **CIS Controls v8 overview** — key changes from v7 to v8; why CIS Controls are prioritized and prescriptive
- **Implementation Groups** — IG1/IG2/IG3 profiles, safeguard counts (56/130/153), determination criteria
- **All 18 controls** — full descriptions with key safeguards called out for each IG level, from Control 1 (Asset Inventory) through Control 18 (Penetration Testing)
- **Framework mapping tables** — CIS Controls v8 → NIST CSF 2.0, CIS Controls v8 → ISO 27001:2022 Annex A, CIS Controls v8 → CMMC 2.0
- **Gap assessment workflow** — 6-step process from IG determination through remediation roadmap

### What's in the reference files

| File | Contents |
|------|----------|
| `safeguards-detail.md` | All 153 safeguards listed by control, with IG assignment (IG1/IG2/IG3), implementation notes, and recommended tools for each safeguard |
| `implementation-guidance.md` | Control-by-control deep-dive: what "implemented" looks like, metrics and KPIs, common pitfalls and misconceptions, tooling examples by control area |
| `framework-mappings.md` | Detailed bidirectional mapping tables: CIS v8 ↔ NIST CSF 2.0 subcategories; CIS v8 ↔ ISO 27001:2022 Annex A controls; CIS v8 ↔ CMMC 2.0 practices; CIS v8 ↔ SOC 2 TSC criteria |

### Inputs used to build the skill

| Input | Description |
|-------|-------------|
| **CIS Controls v8 (May 2021)** | Authoritative source for all 18 controls, 153 safeguards, IG assignments, and definitions |
| **CIS Controls v8 Implementation Guide** | CIS published implementation guidance and tooling recommendations |
| **MITRE ATT&CK Framework** | Used to ground IG prioritization in real-world attack scenarios |
| **Verizon DBIR** | Empirical attack data informing which controls address the most frequent breach causes |
| **NIST CSF 2.0** | Used for CIS → NIST mapping; Categories ID.AM, PR.AC, DE.CM, RS.RP, RC.RP |
| **ISO 27001:2022 Annex A** | Used for CIS → ISO mapping; all 93 Annex A controls |
| **CMMC 2.0 (32 CFR Part 170)** | Used for CIS → CMMC mapping across AC, IA, AU, SI, IR, RA, MP domains |
| **SOC 2 Trust Services Criteria** | Used for CIS → SOC 2 mapping across CC, A, C, PI criteria |
| **CIS CSAT Tool methodology** | Self-assessment scoring approach referenced in gap assessment workflow |

### Skill trigger phrases

`CIS Controls`, `CIS Top 18`, `CIS Top 20`, `CIS Controls v8`, `CIS Controls v7`, `Center for Internet Security`, `Implementation Group`, `IG1`, `IG2`, `IG3`, `CIS safeguards`, `CIS benchmark`, `cyber hygiene`, `CIS Controls gap assessment`, `CIS Controls mapping`, `essential cyber hygiene`, `CIS Controls NIST`, `CIS Controls ISO 27001`, `CIS Controls CMMC`, `CIS Controls SOC 2`, `CIS CSAT`

---

## 6. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.7.1 — August 2026
