# SSP Writing Guide

The System Security Plan (SSP) is the centerpiece of the FedRAMP authorization package.
It tells the complete security story of the Cloud Service Offering (CSO): architecture,
data flows, control implementations, roles, and boundary. Many SSPs exceed 500 pages.

> Always use the official FedRAMP SSP template. One template covers all baselines
> (LI-SaaS, Low, Moderate, High). Templates at: https://www.fedramp.gov/rev5/documents-templates/

---

## SSP Section-by-Section Guide

### Section 1: Information System Name and Title
- Formal name of the CSO
- Unique identifier (assigned during FedRAMP process)
- Service model (IaaS / PaaS / SaaS)
- Deployment model (Public / Private / Community / Hybrid cloud)

### Section 2: System Categorization
- FIPS 199 impact determination: Confidentiality / Integrity / Availability
- Overall impact level = high-water mark of the three values
- Justify each categorization with the types of federal information processed

### Section 3: System Owner / Authorizing Official
- List CSP system owner, ISSO, and agency AO contacts
- For agency authorization, include the sponsoring agency AO

### Section 4: Assignment of Security Responsibility
- Identify the ISSO (Information System Security Officer)
- Document CSP security team contacts

### Section 5: System Mission / Purpose
- Brief description of what the system does
- What federal agencies/programs it supports
- What types of federal data it handles

### Section 6: System Description
- Narrative description of the system
- Technology stack overview
- Key system components

### Section 7: General System Description / System Environment
**This is one of the most scrutinized sections.**
- Detailed architecture description
- Authorization boundary narrative — clearly define what is IN and OUT of scope
- Network architecture diagram (embedded)
- Data flow diagrams (embedded)
- Ports, protocols, and services table
- External connections table (all services connecting to/from the boundary)

**Common mistakes:**
- Vague boundary descriptions ("the cloud environment") — be specific
- Missing data flows for admin/management traffic
- Not documenting external services (DNS, NTP, update servers, SaaS tools used by admins)

### Section 8: System Environment / Interconnections
- Interconnection Security Agreements (ISAs) for each external system
- Leveraged FedRAMP services (IaaS/PaaS) and their authorization status
- Inherited controls from leveraged services must be documented in CIS/CRM workbook

### Section 9: Laws, Regulations, Standards (Appendix B)
- Required attachment: SSP Appendix B (Laws & Regulations) — use the FedRAMP template
- Lists applicable federal laws (FISMA, Privacy Act, etc.)
- May include agency-specific requirements (HIPAA, CJIS if applicable)

### Section 10: Minimum Security Controls
**The largest section — one narrative per control.**

For each control in the applicable baseline:

```
[Control ID] [Control Name]
Implementation Status: Implemented | Partially Implemented | Planned | Not Applicable | Alternative Implementation

[Control Implementation Statement]
Describe HOW the control is implemented. Be specific:
- What tool, policy, or process implements this control?
- Who is responsible?
- Where is the evidence?
- For shared controls: what is the CSP responsibility vs. customer responsibility?

Customer Responsibility (if applicable):
[Describe what the customer/agency must do]
```

**Writing tips:**
- Address every verb in the control requirement — if the control says "monitor and record," describe both monitoring AND recording
- Reference specific policy document names, tool names, configuration settings
- For inherited controls from FedRAMP IaaS/PaaS: state "This control is fully/partially inherited from [Provider]. See CIS/CRM workbook."
- Mark unimplemented controls as "Planned" and ensure they appear in POA&M

### SSP Appendices (A through Q)

| Appendix | Content | Required? |
|---|---|---|
| A | Acronyms & Glossary | Yes |
| B | Related Laws & Regulations (Attachment 12) | Yes |
| C | Security Policies & Procedures | Yes (CSP-authored) |
| D | User Guide | Yes |
| E | Rules of Behavior | Yes (FedRAMP template) |
| F | IT Contingency Plan | Yes (FedRAMP ISCP template, updated Dec 2024) |
| G | Configuration Management Plan | Yes (CSP-authored) |
| H | Incident Response Plan | Yes (CSP-authored) |
| I | Control Implementation Summary (CIS) / CRM Workbook | Yes (FedRAMP template) |
| J | FIPS 199 Categorization | Yes |
| K | Integrated Inventory Workbook (IIW) | Yes (FedRAMP template, updated Dec 2024) |
| L | Cryptographic Modules Table | Yes |
| M | Continuous Monitoring Plan | Yes |
| N | Separation of Duties Matrix | Conditional |
| O | POA&M | Yes (FedRAMP template) |
| P | Supply Chain Risk Management Plan | Yes (Rev 5) |
| Q | Privacy Impact Assessment (PIA) | If PII in scope |

---

## SSP Quality Checklist

Before submitting, verify:
- [ ] All controls for the applicable baseline have implementation statements
- [ ] No controls describe future/planned state as currently implemented
- [ ] All "Planned" controls appear in POA&M
- [ ] Architecture diagrams and control narratives are consistent
- [ ] External connections table matches the data flow diagrams
- [ ] CIS/CRM workbook is complete for all shared/inherited controls
- [ ] IIW lists every asset in the boundary
- [ ] Cryptographic modules table lists all FIPS 140-2/3 validated modules in use
- [ ] All required appendices (C through Q as applicable) are attached
- [ ] SSP Appendix A-12 is the current FedRAMP Laws & Regulations template
