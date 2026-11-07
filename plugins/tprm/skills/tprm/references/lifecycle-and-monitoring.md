# TPRM Lifecycle, Monitoring Signals, and Offboarding

## Lifecycle (Interagency Guidance on Third-Party Relationships, June 2023 — OCC Bulletin 2023-17)
1. **Planning** — define the need, inherent risk of the activity, whether it's critical; plan the relationship's risk profile before vendor selection.
2. **Due diligence and third-party selection** — depth proportional to risk/criticality: capabilities, financial condition, security programme, reliance on fourth parties, legal/regulatory standing.
3. **Contract negotiation** — bake in the addendum clause bank; rights you don't contract for, you won't get during an incident.
4. **Ongoing monitoring** — see signals below; rigor proportional to tier; periodic independent review of the TPRM programme itself, documentation and board reporting.
5. **Termination** — planned exits (expiry, insourcing, replacement) and hostile exits (breach, insolvency); execute the offboarding checklist.

**Status note (November 2026):** the June 2023 interagency guidance remains operative. A proposed replacement, "Proposed Third-Party Risk Management Guidance" (OCC, Federal Reserve, FDIC and NCUA; 91 FR 58536, September 15, 2026; comments due November 16, 2026), would rescind and replace it, with NCUA joining for the first time, and would also rescind the OCC foreign-based third-party bulletin, the 2024 bank-fintech joint statement, and the 2024 community bank TPRM guide. Flag the proposal; do not apply it until finalized.

## Tiering model (practitioner standard)
| Tier | Profile | Due diligence | Reassessment |
|---|---|---|---|
| 1 Critical | Sensitive-data access at scale, business-critical, hard to substitute (DORA critical/important) | Full questionnaire + SOC 2/ISO review + contract addendum + exit plan | Annual + continuous signals |
| 2 High | Moderate data access or important service | Standard questionnaire + report review | Annual light / biennial full |
| 3 Moderate | Limited data, replaceable | Screening questionnaire | At renewal |
| 4 Low | No data access, commodity | Terms review only | On change |
Re-tier on: new data categories, new integrations/OAuth scopes, M&A on either side, incident history.

## Monitoring signals (continuous, between assessments)
- Vendor breach disclosures and incident notifications (and NON-notification when public reporting exists — a trust signal in itself)
- Sub-processor list changes; new fourth-party concentrations
- Assurance report renewals: new SOC 2 period gaps, scope shrinkage, fresh exceptions
- Security posture drift: exposed services, leaked credentials (external attack-surface tooling)
- Financial/viability: funding events, layoffs affecting security teams, going-concern language
- Integration blast radius reviews: quarterly OAuth/API token scope audit for connected SaaS — lesson of the Salesloft Drift breach (Aug 2025): stolen Drift OAuth tokens exposed Salesforce data at 700+ downstream organisations; software supply chain lesson: Shai-Hulud npm worm (Sept 2025) harvesting CI/CD secrets
- SLA and support-quality trend

## Offboarding checklist
1. Access: disable SSO/IdP assignments, VPN, revoke API keys and OAUTH GRANTS, remove IP allow-list entries, collect badges/hardware
2. Data: inventory vendor-held data; return in agreed format; certified deletion incl. backup-cycle expiry date; confirm sub-processor deletion flow-down
3. Technical debris: DNS records, webhooks, integrations, scheduled jobs, shared repos/buckets, service accounts
4. Contractual: termination assistance obligations, final invoices, records retention per regulatory schedule, survival clauses (confidentiality, audit rights)
5. Organisational: notify internal stakeholders, update the vendor register/Register of Information (DORA), knowledge transfer, lessons learned fed back into tiering
6. Verification: 30-day post-exit check that access is truly dead (log review) — the most-skipped, most-valuable step
