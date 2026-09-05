# California Consumer Privacy Act (CCPA/CPRA) Skill for Claude

> **Disclaimer:** This skill provides informational guidance based on the text of the California Consumer Privacy Act (Cal. Civ. Code §1798.100 et seq.) and the California Privacy Rights Act (Proposition 24), together with CPPA regulations and published enforcement guidance. It does not constitute legal advice. For matters involving significant compliance risk, CPPA investigation response, class action exposure, or complex data-sharing arrangements, consult a qualified privacy attorney licensed in California.

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert advisor on California's comprehensive privacy law framework — covering both the **California Consumer Privacy Act (CCPA)**, effective January 1, 2020, and the **California Privacy Rights Act (CPRA)**, effective January 1, 2023. The CPRA substantially amended and expanded CCPA, created the independent California Privacy Protection Agency (CPPA), and introduced new rights and obligations that this skill fully covers.

The skill handles the full breadth of CCPA/CPRA compliance work: determining whether a business meets the statutory thresholds, guiding the design of consumer rights workflows, drafting privacy notices and opt-out mechanisms, classifying data recipients (service providers, contractors, and third parties), advising on Sensitive Personal Information (SPI) handling, and assessing penalty exposure under the CPPA enforcement regime.

A key strength of the skill is its coverage of the **CPRA additions** — the right to correct, the right to limit SPI use, data minimization and purpose limitation obligations, retention disclosure requirements, contractor classification, and mandatory cybersecurity audit and risk assessment obligations. These CPRA-era changes are where many businesses still have significant gaps, particularly those that completed their initial CCPA compliance work before 2023.

**As of January 1, 2026**, two major CPRA regulatory programs went live:

- **Cybersecurity Audits**: Businesses processing PI presenting significant consumer security risk must conduct annual cybersecurity audits. Regulations finalized in 2025 are now in effect.
- **Risk Assessments**: Businesses must conduct and document risk assessments before processing high-risk PI. The CPPA may request submission of these assessments at any time.

**Also effective January 1, 2026**: The CPPA finalized its **Automated Decision-Making Technology (ADMT)** regulations. Consumers now have the right to opt out of ADMT producing significant decisions, access information about automated processing, and request human review. Businesses must implement ADMT opt-out mechanisms **by January 1, 2027**.

The skill also incorporates **2026 CPPA enforcement precedents** — including the record-breaking $2.75M Disney fine, the $1.1M PlayOn Sports action, and the $375K Ford Motor settlement — to help users understand the current enforcement posture and calibrate their own penalty exposure.

The skill also provides a **CCPA/GDPR comparative analysis**, enabling global privacy teams to map existing EU compliance controls to California requirements and identify US-specific gaps — avoiding duplicate work while catching the material differences (such as the opt-out model vs. the opt-in model for consent, or the private right of action for data breaches).

---

## 2. What's New in Version 1.4.0 (July 2026)

| Update | Detail |
|--------|--------|
| **ADMT rules now live** | CPPA finalized ADMT regulations; effective January 1, 2026 (previously listed as "pending rulemaking") |
| **ADMT compliance deadline** | Businesses must implement ADMT opt-out mechanisms by **January 1, 2027** |
| **Cybersecurity audits now live** | Annual cybersecurity audit requirement is in effect as of January 1, 2026 (previously "pending final rulemaking") |
| **Risk assessments now live** | Risk assessment submission requirement is live as of January 1, 2026 |
| **Disney $2.75M fine** | Largest CCPA enforcement action ever — children's data, opt-out failures, ad tech data sharing |
| **PlayOn Sports $1.1M fine** | Unauthorized sharing of consumer PI with third parties |
| **Ford Motor $375K fine** | Failure to process deletion and access requests within required timeframes |

---

## 3. Intended Audiences

| Audience | How They Use the Skill |
|----------|----------------------|
| **Privacy counsel and DPOs** | Threshold analysis, rights workflow design, vendor contract review, enforcement risk assessment |
| **Compliance managers** | Gap assessments against CCPA/CPRA requirements, remediation roadmaps, audit preparation |
| **In-house legal teams** | Drafting privacy notices, service provider agreements, and opt-out mechanisms |
| **Product and engineering teams** | Implementing Global Privacy Control (GPC) signal handling, consent management, data deletion pipelines, ADMT opt-out flows |
| **Marketing and data teams** | Understanding what constitutes a "sale" or "sharing" for cross-context behavioral advertising; SPI use limits |
| **Startups and SMBs** | Determining whether the thresholds apply; understanding first-priority obligations |
| **Global privacy teams** | Mapping GDPR controls to CCPA/CPRA; identifying US-specific gaps and requirements |
| **Data brokers and ad-tech companies** | Understanding the broad definition of "sale" and "sharing"; opt-out mechanism requirements |
| **AI/ML teams** | Understanding ADMT opt-out obligations, human review requirements, and the January 1, 2027 compliance deadline |

---

## 4. Common Use Cases

### Business Applicability and Threshold Analysis
- *"Does our company need to comply with CCPA? We're a SaaS startup with $18M ARR and 80,000 users."*
- *"We're a non-profit. Does CCPA apply to us?"*
- *"We sell user data to advertisers for 45% of our revenue — which CCPA threshold do we trigger?"*
- *"Does CPRA apply to our company differently from CCPA?"*

### Consumer Rights Workflows
- *"Walk me through the step-by-step process for handling a Right to Delete request under CCPA."*
- *"What identity verification is required before responding to a Right to Know request?"*
- *"What are the exceptions to the Right to Delete? Can we retain data for fraud prevention?"*
- *"How do we handle a Right to Correct request for data we received from a third party?"*
- *"What's the timeline for responding to a Right to Limit SPI Use request?"*

### Privacy Notice and Policy Drafting
- *"Draft a CCPA-compliant privacy notice for collection on our mobile app sign-up screen."*
- *"What must our privacy policy include under CPRA to be compliant?"*
- *"Write a 'Do Not Sell or Share My Personal Information' link notice for our homepage."*
- *"Draft a 'Limit the Use of My Sensitive Personal Information' disclosure."*

### Vendor and Data Recipient Classification
- *"Is our analytics vendor a service provider or a third party under CCPA?"*
- *"What must a service provider contract include to prevent the disclosure from being treated as a sale?"*
- *"What's the difference between a service provider and a contractor under CPRA?"*
- *"We share data with ad exchanges — does that constitute a sale or sharing?"*

### SPI and Opt-Out Mechanism Design
- *"We collect precise geolocation data. How does SPI treatment change our obligations?"*
- *"What signals must we accept as a valid opt-out? Does Global Privacy Control count?"*
- *"Design our opt-out of sale and sharing workflow including GPC signal handling."*
- *"When do we need the 'Limit Use of SPI' link vs. the 'Do Not Sell or Share' link?"*

### ADMT Compliance (Deadline: January 1, 2027)
- *"We use an ML model to make credit decisions. Does ADMT apply? What do we need to do by January 2027?"*
- *"What must our ADMT opt-out mechanism look like under the CPPA regulations?"*
- *"Our hiring process uses automated screening tools. How do ADMT rules affect us?"*
- *"What human review rights must we offer for automated decisions?"*

### Enforcement, Penalties, and GDPR Alignment
- *"What is our penalty exposure if we're found to have missed opt-out signals for 10,000 consumers?"*
- *"We have an existing GDPR compliance program. What additional steps do we need for CCPA?"*
- *"Produce a side-by-side comparison of CCPA/CPRA and GDPR obligations for our privacy team."*
- *"The Disney fine was $2.75M — could we face a similar action for our ad tech data sharing?"*
- *"We missed the 45-day deadline for 500 access requests. What is our exposure?"*

---

## 5. How to Use the Skill

### Installation
1. Download the `ccpa.skill` file from this folder
2. In Claude, go to **Settings → Skills**
3. Click **Upload Skill** and select `ccpa.skill`
4. The skill is immediately active in your Claude sessions

### Triggering the Skill
The skill activates automatically whenever your message touches CCPA or CPRA topics. No special commands are needed. Example phrases that will trigger it:

- *"Is this CCPA compliant?"*
- *"We need to add a Do Not Sell link — what does it need to say?"*
- *"Help me design our consumer rights request process."*
- *"Does sharing data with our ad network count as a sale under California law?"*
- *"What SPI categories does CPRA add?"*
- *"Run a CCPA gap assessment on our current privacy practices."*
- *"Draft a service provider agreement clause for our data processor."*
- *"Compare CCPA and GDPR for our compliance team."*
- *"Do we need an ADMT opt-out mechanism?"*
- *"What do the 2026 CPPA enforcement actions mean for us?"*

### Example Prompts

```
"We're a B2C e-commerce company with $30M revenue and 120,000 California 
customers. Run a CCPA/CPRA gap assessment against our current practices: 
we have a privacy policy, no 'Do Not Sell' link, and we use Google Analytics 
and Facebook Pixel."
```

```
"Draft a CCPA-compliant at-collection privacy notice for our mobile app 
sign-up screen. We collect: name, email, phone, precise location, and 
browsing history within the app. We share data with advertising partners."
```

```
"A California consumer submitted a Right to Delete request through our 
website 30 days ago and we haven't responded. Walk me through what we 
must do now, what exceptions might apply, and what our penalty exposure is."
```

```
"We're a European company with GDPR compliance already in place. Produce 
a side-by-side gap analysis showing what additional steps we need to take 
for CCPA/CPRA compliance."
```

```
"Our website uses cookies for cross-context behavioral advertising via 
a third-party DSP. Does this constitute 'sharing' under CPRA? Do we 
need a 'Do Not Sell or Share' link? Must we honor GPC signals?"
```

```
"We use automated scoring to approve or deny insurance applications. 
The CPPA's ADMT rules are now live. What must we implement, and what 
is our deadline for the consumer opt-out mechanism?"
```

---

## 6. Skill Implementation Details

### Architecture

```
ccpa/
├── SKILL.md                              # Core skill — thresholds, rights, obligations,
│                                         #   penalties, opt-out requirements, SPI rules,
│                                         #   ADMT rules, cybersecurity audit/risk
│                                         #   assessment obligations, 2026 enforcement cases
└── references/
    ├── consumer-rights-workflows.md      # Step-by-step workflows for each consumer right:
    │                                     #   verification, response, exceptions, timelines
    └── ccpa-gdpr-comparison.md           # Side-by-side CCPA/CPRA vs. GDPR comparison
                                          #   for global compliance teams
```

**Total:** ~450 lines across 3 files (SKILL.md + 2 reference files)

### What's in SKILL.md

- **Who Must Comply** — the three statutory thresholds (revenue, data volume, revenue from sale/sharing) with worked examples
- **Key Definitions** — Personal Information, Sensitive Personal Information, Sale, Sharing, Service Provider, Contractor, Third Party
- **Consumer Rights table** — all 9 rights with statutory citation and response deadlines, including ADMT opt-out (effective Jan 1, 2026; compliance deadline Jan 1, 2027)
- **Key Obligations** — privacy notice at collection, privacy policy requirements, opt-out mechanisms (including ADMT opt-out), data minimization, retention limits, service provider contract requirements, cybersecurity audit obligations (live Jan 1, 2026), risk assessment obligations (live Jan 1, 2026), ADMT compliance framework
- **Penalties and Enforcement** — CPPA civil penalties ($2,500/$7,500 per violation), private right of action ($100–$750 per consumer per data breach incident)
- **2026 Enforcement Precedents** — Disney $2.75M (record), PlayOn Sports $1.1M, Ford Motor $375K; analysis of enforcement posture
- **Nine workflow categories** — how to help with applicability, rights fulfillment, notices, vendor classification, SPI, opt-outs (including ADMT), GDPR alignment, gap assessment, and enforcement/penalty analysis

### What's in the reference files

| File | Contents |
|------|----------|
| `consumer-rights-workflows.md` | Step-by-step workflows for all consumer rights; identity verification standards; exception handling (fraud prevention, legal obligation, free speech); response letter templates; escalation paths for denied requests |
| `ccpa-gdpr-comparison.md` | Side-by-side table covering lawful basis vs. opt-out model, consent requirements, data subject/consumer rights, data retention, DPO vs. no DPO requirement, enforcement mechanisms, private right of action, SPI vs. special category data |

### Inputs used to build the skill

| Input | Description |
|-------|-------------|
| **Cal. Civ. Code §1798.100 et seq.** | Full CCPA statutory text with all CPRA amendments |
| **CPRA (Proposition 24, 2020)** | Amendment text creating CPPA and adding CPRA rights/obligations |
| **CPPA regulations (2025–2026)** | Final CPPA rulemaking including ADMT regulations, cybersecurity audit rules, and risk assessment requirements (all effective January 1, 2026) |
| **CPPA enforcement actions (2026)** | Disney $2.75M, PlayOn Sports $1.1M, Ford Motor $375K enforcement orders |
| **GDPR (Regulation (EU) 2016/679)** | Used for the comparative analysis reference file |
| **IAPP and privacy bar guidance** | Practitioner interpretation of key definitions (sale, sharing, service provider) |

### Skill trigger phrases

`CCPA`, `CPRA`, `California Consumer Privacy Act`, `California Privacy Rights Act`, `Do Not Sell`, `Do Not Share`, `consumer rights California`, `right to delete California`, `right to know California`, `right to correct California`, `sensitive personal information`, `SPI`, `CPPA`, `California privacy`, `opt-out of sale`, `GPC signal`, `Global Privacy Control`, `service provider agreement CCPA`, `CCPA gap assessment`, `CCPA compliance`, `California data privacy`, `CCPA vs GDPR`, `cross-context behavioral advertising`, `automated decision-making California`, `ADMT`, `CPPA enforcement`, `cybersecurity audit CCPA`, `risk assessment CPRA`

---

## 7. Author

**Hemant Naik**
[LinkedIn](https://www.linkedin.com/in/tanaji-naik/) · [hemant.naik@gmail.com](mailto:hemant.naik@gmail.com)

Skill version: 1.9.0 — September 2026
