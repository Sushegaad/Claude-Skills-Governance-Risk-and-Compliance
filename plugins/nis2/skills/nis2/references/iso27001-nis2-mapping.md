# ISO 27001:2022 to NIS2 Art. 21 Cross-Reference

ISO/IEC 27001:2022 certification provides strong evidence of NIS2 compliance for many Art. 21 measures. However, ISO 27001 certification does NOT substitute NIS2 obligations - entities remain responsible for meeting Art. 21, Art. 20, and Art. 23 requirements directly.

Key gaps where NIS2 goes beyond ISO 27001:
- **Art. 21(2)(d)**: NIS2 explicitly mandates supply chain security obligations tied to ENISA coordinated risk assessments (Art. 22)
- **Art. 21(2)(j)**: NIS2 explicitly mandates MFA - ISO 27001 Annex A.8.5 covers authentication but MFA is not universally required
- **Art. 20**: Management body personal liability has no ISO 27001 equivalent
- **Art. 23**: Incident reporting timelines (24h/72h/1 month) are more prescriptive than ISO 27001's general incident management controls

---

## Mapping Table

| NIS2 Art. 21 Measure | NIS2 Requirement | ISO 27001:2022 Annex A Controls |
|---|---|---|
| **M1** Risk Analysis & Policies | Risk analysis methodology, IS policies | A.5.1 Policies; A.5.2 (Information security roles and responsibilities); A.8.8 Vuln mgmt; Clause 6.1 Risk assessment; Clause 8.2 IS risk assessment |
| **M2** Incident Handling | Detection, response, recovery procedures | A.5.24 IS incident planning; A.5.25 Assessment of IS events; A.5.26 Response; A.5.27 Post-incident review; A.5.28 Evidence collection |
| **M3** BCP / DR / Crisis | Backup, DR, crisis management | A.5.29 IS during disruption; A.5.30 ICT readiness; A.8.13 Backup; A.8.14 Redundancy |
| **M4** Supply Chain Security | Supplier/service-provider risk | A.5.19 IS in supplier relationships; A.5.20 Supplier agreements; A.5.21 ICT supply chain; A.5.22 Supplier monitoring; A.5.23 Cloud services |
| **M5** Secure Acquisition & Dev | SDLC security, vulnerability disclosure | A.8.25 Secure dev lifecycle; A.8.26 App security; A.8.27 Secure architecture; A.8.28 Secure coding; A.8.29 Testing; A.8.30 Outsourced dev; A.5.8 IS in PM |
| **M6** Effectiveness Assessment | KPIs, audits, management review | A.5.35 Independent IS review; A.5.36 Policy compliance; Clause 9.1 Monitoring; Clause 9.2 Internal audit; Clause 9.3 Management review |
| **M7** Cyber Hygiene & Training | Awareness and training | A.6.3 IS awareness/training; A.5.7 Threat intelligence; A.6.8 IS event reporting |
| **M8** Cryptography | Crypto policies, key management | A.8.24 Use of cryptography |
| **M9** HR, Access Control, Asset Mgmt | Least privilege, RBAC, asset inventory | A.5.9 Asset inventory; A.5.10 Asset use; A.5.11 Asset return; A.8.2 Privileged access; A.8.3 Access restriction; A.8.4 Source code; A.6.1 Screening; A.6.5 Responsibilities on termination |
| **M10** MFA & Secure Comms | MFA, phishing-resistant auth, encrypted comms | A.8.5 Secure authentication; A.8.20 Network security; A.8.26 App security; A.8.24 Cryptography |

---

## ISO 27001 Controls With No Direct NIS2 Measure Equivalent

The following ISO 27001:2022 Annex A controls are important for overall security posture but do not map to a specific Art. 21 measure. They may still be relevant for NIS2 governance and compliance evidence:

- **A.5.31** Legal, statutory, regulatory, contractual requirements  
- **A.5.32** Intellectual property rights
- **A.5.33** Protection of records
- **A.5.34** Privacy and PII protection (→ see also GDPR)
- **A.6.4** Disciplinary process
- **A.8.1** User endpoint devices
- **A.8.9** Configuration management
- **A.8.10** Information deletion

---

## NIS2 Requirements With Limited ISO 27001 Coverage

| NIS2 Requirement | Gap vs ISO 27001 | Recommended Action |
|---|---|---|
| Art. 20 - Management body approval and personal liability | No ISO 27001 equivalent | Board cybersecurity policy; training records; documented approval minutes |
| Art. 23 - 24h early warning | ISO 27001 A.5.24–5.26 cover incident management but not specific timelines | Pre-drafted CSIRT notification templates; automated alerting workflows |
| Art. 23 - 72h notification | Same as above | Incident triage runbooks with timeline checkpoints |
| Art. 23 - 1-month final report | Same as above | Post-incident review template with all Art. 23(4) required fields |
| Art. 22 - ENISA supply chain risk assessments | ISO 27001 A.5.19–5.23 cover supplier security generally | Monitor ENISA and national authority supply chain advisories; integrate into supplier risk register |
| Art. 21(2)(j) - MFA mandate | ISO 27001 A.8.5 covers authentication; MFA not universal | Deploy MFA for remote access, privileged accounts, cloud consoles as minimum |

---

## Practical Guidance for ISO 27001-Certified Entities

If your organisation holds ISO 27001:2022 certification, you are well-positioned for NIS2 but should:

1. **Confirm entity classification** - verify whether you are an EE or IE under Art. 3 and your Member State's transposition law
2. **Address Art. 20 governance** - document board-level approval of cybersecurity measures and ensure training records are maintained
3. **Implement the Art. 23 reporting workflow** - your IRP likely needs an explicit NIS2 notification track with pre-drafted CSIRT templates and 24h/72h/1-month checkpoints
4. **Review supply chain coverage** - map your supplier security controls to Art. 21(2)(d) and integrate ENISA coordinated risk assessment outputs
5. **Mandate MFA** - if not already universal, deploy MFA for remote access and privileged accounts
6. **Register with your national competent authority** - most Member States require in-scope entities to self-register
