# UK NIS — Incident Reporting Reference
## NIS Regulations 2018 — Regulations 11 and 13

---

## Overview

The NIS Regulations 2018 establish mandatory incident notification obligations for both Operators of Essential Services (OES) and Digital Service Providers (DSPs). This reference covers the legal thresholds, reporting requirements, notification procedures, and practical guidance for compliance.

---

## Part 1 — OES Incident Reporting (Regulation 11)

### 1.1 Legal Basis

**Regulation 11** of SI 2018/506 requires OES to notify the relevant Competent Authority of any incident that has a **significant impact on the continuity of the essential service** provided.

### 1.2 What Is a Significant Impact?

No fixed numeric threshold is prescribed. The Regulations list cross-cutting factors that Competent Authorities and the NCSC use to assess significance:

| Factor | Relevant Considerations |
|--------|------------------------|
| **Number of users affected** | The count of users relying on the essential service who are impacted |
| **Duration of the incident** | How long the service disruption has lasted or is expected to last |
| **Geographic spread** | The geographic area in which the service is disrupted (local, regional, national) |
| **Extent of disruption to the service** | Degree to which functioning of the essential service is impaired |
| **Extent of impact on economic and societal activities** | Downstream effects on other critical services, businesses, or public safety |

### 1.3 Notification Timeline

The NIS Regulations 2018 do not specify an explicit number of hours. The requirement is to notify **as soon as reasonably practicable** after becoming aware of a significant incident. In practice:

- Competent Authorities and the NCSC guidance consistently reference **72 hours** as the expected timeframe for initial notification
- Initial notifications may be partial; further details should be provided as they become available (updated notifications)
- Some Competent Authorities (e.g. Ofgem, CAA) publish sector-specific guidance specifying their preferred timelines and formats

**Key principle:** Do not delay reporting pending completion of a full investigation. Notify early with known information and supplement as the incident develops.

### 1.4 Who to Notify (OES)

| Sector | Primary Notification Recipient |
|--------|-------------------------------|
| Electricity | Ofgem |
| Oil | Department for Energy Security and Net Zero (DESNZ) |
| Gas | Ofgem |
| Air transport | Civil Aviation Authority (CAA) |
| Rail transport | Office of Rail and Road (ORR) |
| Road transport | Department for Transport (DfT) |
| Water transport / maritime | Department for Transport / Maritime and Coastguard Agency (MCA) |
| Health | Department of Health and Social Care (DHSC) / NHS England |
| Drinking water | Drinking Water Inspectorate (DWI) |
| Digital infrastructure (IXP, DNS, TLD) | Ofcom |

In addition to the Competent Authority, OES should notify the **NCSC** (National Cyber Security Centre) via report.ncsc.gov.uk for technical assistance and national-level coordination.

### 1.5 OES Notification Template

```
NIS INCIDENT NOTIFICATION — OPERATOR OF ESSENTIAL SERVICES

Submission Date/Time: [YYYY-MM-DD HH:MM UTC]
Notification Type: [ ] Initial  [ ] Updated  [ ] Final

-- ORGANISATION DETAILS --
Organisation Name:
NIS Sector:
Competent Authority:
Primary NIS Contact Name:
Primary NIS Contact Role:
Primary NIS Contact Email:
Primary NIS Contact Telephone:

-- INCIDENT DETAILS --
Date/Time Incident Detected (UTC): [YYYY-MM-DD HH:MM]
Date/Time Incident Started (if known, UTC): [YYYY-MM-DD HH:MM]
Systems/Services Affected: [Brief description of affected systems]
Nature of the Incident:
  [ ] Cyber attack (malware, ransomware, phishing, etc.)
  [ ] Denial of Service
  [ ] Unauthorised access / data breach
  [ ] System/software failure
  [ ] Third-party / supply chain compromise
  [ ] Physical attack on NIS
  [ ] Other (describe below)

-- IMPACT ASSESSMENT --
Current Status:
  [ ] Ongoing  [ ] Contained  [ ] Resolved
Description of impact on essential service continuity:
Estimated number of users affected:
Geographic area affected:
Duration of disruption (actual or estimated):
Cross-border impact considered?  [ ] No  [ ] Yes — describe:

-- RESPONSE ACTIONS --
Immediate actions taken:
Containment measures in place:
External assistance engaged (NCSC, law enforcement, etc.):

-- REGULATORY NOTES --
Has law enforcement been notified?  [ ] No  [ ] Yes — which force:
Has the NCSC been separately notified?  [ ] No  [ ] Yes
Are there personal data concerns (GDPR/UK GDPR)?  [ ] No  [ ] Yes — ICO notified?:

-- NEXT STEPS --
Planned remediation actions:
Estimated restoration timeframe:
Next update expected: [YYYY-MM-DD]

Signed: [Name, Role, Date]
```

---

## Part 2 — DSP Incident Reporting (Regulation 13)

### 2.1 Legal Basis

**Regulation 13** of SI 2018/506 requires DSPs to notify the ICO (Information Commissioner's Office) of incidents having a **substantial impact** on the provision of a digital service.

### 2.2 What Is a Substantial Impact?

The NIS Regulations prescribe specific parameters for DSP impact assessment:

| Parameter | Threshold |
|-----------|-----------|
| **Number of users affected** | Particularly users relying on the service for business/professional purposes |
| **Duration** | Hours of service disruption |
| **Geographic spread** | Area in the UK (and EEA where applicable) affected |
| **Extent of disruption** | The degree to which the digital service is impaired |
| **Impact on societal and economic activities** | Whether downstream activities dependent on the DSP are affected |
| **System integrity** | Whether systems have been compromised, affecting availability, authenticity, or integrity |

Guidance from the ICO specifies concrete thresholds that indicate a substantial impact (these are guidelines, not fixed legal thresholds):

- More than **1 million user accounts** affected
- Service unavailability exceeding **5% of users** for more than 30 minutes
- Data integrity or confidentiality compromise affecting business users

### 2.3 Notification Timeline (DSP)

Without undue delay and, where feasible, **within 72 hours** of becoming aware of the incident.

### 2.4 Who to Notify (DSP)

**Primary notification:** Information Commissioner's Office (ICO)
- ICO NIS notification: ico.org.uk/for-organisations/cybersecurity/
- ICO helpline: 0303 123 1113

Where the incident also constitutes a personal data breach under UK GDPR, the same report to the ICO may cover both obligations, but the organisation should clearly identify it as both a NIS notification and a UK GDPR Article 33 notification.

Also notify the **NCSC** at report.ncsc.gov.uk for technical coordination.

### 2.5 DSP Notification Template

```
NIS INCIDENT NOTIFICATION — DIGITAL SERVICE PROVIDER

Submission Date/Time: [YYYY-MM-DD HH:MM UTC]
Notification Type: [ ] Initial  [ ] Updated  [ ] Final

-- ORGANISATION DETAILS --
Organisation Name:
DSP Type:  [ ] Online Marketplace  [ ] Online Search Engine  [ ] Cloud Computing
UK Establishment Address:
Primary NIS Contact Name:
Primary NIS Contact Role:
Primary NIS Contact Email:
Primary NIS Contact Telephone:

-- INCIDENT DETAILS --
Date/Time Incident Detected (UTC): [YYYY-MM-DD HH:MM]
Date/Time Incident Started (if known, UTC): [YYYY-MM-DD HH:MM]
Systems / Services Affected: [Describe affected components of the digital service]
Nature of the Incident:
  [ ] Cyber attack (malware, ransomware, DDoS, etc.)
  [ ] Unauthorised access / data breach
  [ ] Processing failure / system crash
  [ ] Third-party / supply chain compromise
  [ ] Other (describe below)

-- IMPACT ASSESSMENT --
Is the incident still ongoing?  [ ] Yes  [ ] No — resolved at: [YYYY-MM-DD HH:MM]
Estimated number of users affected (total):
Estimated number of business/professional users affected:
Duration of disruption:
Geographic area affected:
Was the availability, authenticity, integrity, or confidentiality of systems impacted?  [ ] Yes  [ ] No
Describe impact on societal/economic activities:

-- RESPONSE ACTIONS --
Actions taken to contain and respond:
External assistance engaged (NCSC, law enforcement, etc.):

-- CROSS-REGULATORY NOTE --
Does this incident also constitute a UK GDPR personal data breach?
  [ ] No  [ ] Yes — UK GDPR Art. 33 report also submitted?  [ ] Yes  [ ] No
Has law enforcement been notified?  [ ] No  [ ] Yes

-- NEXT STEPS --
Planned remediation:
Estimated full restoration timeframe:
Next update expected: [YYYY-MM-DD]

Signed: [Name, Role, Date]
```

---

## Part 3 — Post-Incident Requirements

### 3.1 Follow-Up Notifications

Initial notifications are often partial. Both OES and DSPs should submit:
1. **Initial notification** — as soon as practicable after becoming aware
2. **Interim updates** — as significant new information becomes available
3. **Final notification** — once the incident is resolved, confirming full details of cause, impact, and remediation

### 3.2 Record-Keeping

Organisations must retain records of:
- All NIS incidents (regardless of reporting threshold)
- Notification submissions and acknowledgements
- Correspondence with Competent Authorities and the NCSC
- Incident timeline, evidence, and investigation findings
- Post-incident review reports and lessons learned

Recommended retention period: **minimum 3 years**; longer if there is ongoing regulatory engagement.

### 3.3 Interaction with Other Reporting Obligations

| Regime | Interaction with NIS Reporting |
|--------|-------------------------------|
| **UK GDPR (Art. 33)** | If the incident involves personal data breach, report to ICO under UK GDPR within 72 hours in addition to NIS notification (for OES: separate reports; for DSPs: may be combined with ICO) |
| **Network and information systems — Ofcom** | Ofcom-regulated communications providers have additional reporting obligations under the Communications Act 2003 / electronic communications security regulations |
| **FCA (financial sector)** | Financial services firms may have concurrent FCA operational resilience/incident reporting obligations |
| **NHS DSPT / DSPT** | NHS organisations have concurrent Data Security and Protection Toolkit reporting requirements |
| **Police / NCSC** | Significant cyber incidents should be reported to relevant law enforcement (Action Fraud, Regional Organised Crime Units) and NCSC |

---

## Part 4 — Non-Reportable Incidents

Not all incidents need to be reported under NIS. The following should be logged internally but are unlikely to meet the NIS reporting threshold:

- Minor malware infections with no impact on essential service delivery
- Single workstation compromise with no access to NIS
- Phishing emails intercepted before any click/compromise
- Brief system unavailability due to planned maintenance
- Failed attack attempts with no breach or service impact

Always document the assessment of why an incident did not meet the significant/substantial impact threshold.
