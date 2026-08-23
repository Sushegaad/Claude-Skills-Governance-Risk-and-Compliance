# Vietnam PDPL — Claude Skill

A Claude skill for **Vietnam's Law on Personal Data Protection No. 91/2025/QH15** and its implementing **Decree 356/2025/ND-CP**, effective 1 January 2026.

---

## 1. What Does the Skill Do?

This skill turns Claude into an expert advisor on Vietnam's first comprehensive personal data protection law. It provides actionable guidance on compliance obligations for organisations operating in Vietnam or processing personal data of Vietnamese citizens, covering:

- Assessing compliance gaps against VN-PDPL and Decree 356
- Managing data subject rights requests within legally required timeframes
- Drafting and filing impact assessments (DPIA and cross-border transfer)
- Writing PDPL-compliant privacy notices, consent forms, and internal policies
- Responding to personal data breaches with a 72-hour notification workflow
- Sector-specific guidance for finance, AI, cloud computing, blockchain, and big data
- Evaluating Data Protection Officer (DPO) appointment requirements and qualifications
- Interpreting SME exemptions and transitional provisions

---

## 2. Intended Audiences

- **Legal and compliance teams** at Vietnamese companies or foreign companies with Vietnamese data subjects
- **Privacy officers and DPOs** building or managing a VN-PDPL compliance programme
- **Founders and executives** of startups and SMEs assessing their obligations and applicable exemptions
- **Technology teams** building products or services that process personal data in Vietnam
- **Consultants and law firms** advising clients on Vietnam data privacy
- **Multinational organisations** handling cross-border transfers of Vietnamese citizens' data

---

## 3. Common Use Cases

1. **Gap analysis** — "We're a Singapore SaaS company with Vietnamese users. What does VN-PDPL require from us?"
2. **Cross-border transfer** — "We store Vietnamese customer data on AWS in Singapore. Do we need to file an impact assessment?"
3. **Breach response** — "We discovered a data breach affecting Vietnamese users 48 hours ago. What do we need to do now?"
4. **Consent review** — "Is our current consent mechanism compliant with VN-PDPL? We use a pre-filled checkbox."
5. **DPIA** — "We're launching a new AI-based credit scoring product in Vietnam. What impact assessment do we need?"
6. **Data subject rights** — "A Vietnamese user is asking us to delete all their data. How do we handle this request?"
7. **SME exemptions** — "We're a small enterprise. Which VN-PDPL obligations can we defer for 5 years?"
8. **Privacy notice drafting** — "Draft a VN-PDPL-compliant privacy notice for our e-commerce platform."
9. **DPO appointment** — "Do we need a Data Protection Officer? What qualifications must they have?"
10. **Sensitive data handling** — "We collect health data and financial data. What extra obligations apply?"

---

## 4. How to Use

### Install the Skill

**Option A — Direct install (recommended):**
1. Open the Claude desktop app
2. Go to **Settings → Skills**
3. Click **Add Skill** and upload `vn-pdpl.skill`

**Option B — Via GRC Plugin Marketplace:**
1. Open Claude desktop app
2. Go to **Settings → Plugins**
3. Search for "GRC Skills" or "Vietnam PDPL"
4. Install the `vn-pdpl` skill

### Example Prompts

Once installed, try prompts like:

- *"Conduct a VN-PDPL gap analysis for our e-commerce business that collects names, emails, phone numbers, and purchase history from Vietnamese customers."*
- *"We process health data for Vietnamese patients in our telemedicine app. What sensitive data obligations apply?"*
- *"Draft a cross-border transfer impact assessment dossier for transferring Vietnamese employee HR data to our US-based Workday system."*
- *"A Vietnamese data subject has requested deletion of all their personal data. Walk me through the fulfilment process and required timelines."*
- *"We had a breach affecting 15,000 Vietnamese users' financial data. What do we need to notify, to whom, and by when?"*

---

## 5. Skill Implementation Details

| Property | Value |
|---|---|
| **Skill identifier** | `vn-pdpl` |
| **Law covered** | Law No. 91/2025/QH15 on Personal Data Protection |
| **Implementing decree** | Decree 356/2025/ND-CP (31 December 2025) |
| **Effective date** | 1 January 2026 |
| **Administering authority** | Ministry of Public Security of Vietnam |
| **Skill version** | 1.7.1 |
| **File** | `vn-pdpl.skill` |

**Reference files bundled in the skill:**

- `references/articles-overview.md` — Full breakdown of key articles: definitions, data categories (basic 11 items / sensitive 13 items), data subject rights, consent rules, processing bases, cross-border transfer, DPIA, breach notification, penalties, and transitional provisions

- `references/decree-356-implementation.md` — Implementation details from Decree 356: response timeframes, valid consent methods, sector-specific rules (finance/banking, big data, AI/automated processing, blockchain, cloud computing), and DPO qualifications

**Key law facts:**
- 6 data subject rights (informed, consent/withdraw, access/rectify, delete/restrict/object, complaints, protection)
- 72-hour breach notification to the Ministry of Public Security
- Cross-border transfer impact assessment due within 60 days of first transfer
- Domestic DPIA due within 60 days of first processing
- SME exemption: 5 years for Articles 21, 22, 33(2) unless processing sensitive or large-scale data
- Maximum penalties: VND 3 billion for organisations; 5% of Vietnam revenue for cross-border violations; 10× proceeds for data buying/selling

---

## 6. Author

**Hemant Naik**
Email: hemant.naik@gmail.com
GitHub: [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance)

---

*Skill version: 1.8.0 — August 2026*
