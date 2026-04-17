# Finding Severity Classification — NIST SP 800-53A Rev 5

This reference file defines the severity classification criteria for security control assessment findings. It draws on NIST SP 800-53A Rev 5, NIST SP 800-30 Rev 1 risk determination scales, and FedRAMP/FISMA programme guidance.

---

## Severity Scale Overview

When a control is assessed as **Other Than Satisfied (OTS)**, the finding must be assigned a severity level. Severity is determined by combining: (a) the impact of exploiting the vulnerability introduced by the deficiency, and (b) the likelihood that the deficiency could be exploited.

| Severity | Risk Level (SP 800-30) | Definition |
|---------|----------------------|-----------|
| **Critical** | Very High | A control is absent or fundamentally broken; exploitation is trivially easy and could result in complete loss of confidentiality, integrity, or availability; requires immediate remediation |
| **High** | High | A significant control deficiency exists; exploitation is feasible and would result in major adverse impact; remediation required before next ATO period |
| **Moderate** | Moderate | A meaningful deficiency; exploitation would require additional steps or has partial mitigations; remediation required within an acceptable timeframe |
| **Low** | Low | A minor deficiency with limited impact; compensating controls reduce risk to an acceptable level; remediation recommended |
| **Informational** | Very Low | No direct security risk; an observation or best practice recommendation; no POA&M required |

---

## Severity Criteria by Impact Area

### Assessing the Impact Component

| Impact | Description | Example |
|--------|-------------|---------|
| **Catastrophic** | Complete mission failure; loss of life possible; loss of major assets or resources; severe financial loss | Unencrypted Top Secret data exposed publicly; critical infrastructure control lost |
| **Severe** | Mission significantly degraded; major financial loss; major privacy breach | PII of thousands of individuals disclosed; critical system unavailable >72 hours |
| **Moderate** | Some mission degradation; significant operational disruption; limited financial loss | Sensitive internal data accessed unauthorisedly; critical system unavailable 8–72 hours |
| **Minor** | Noticeable degradation but mission continues; limited operational impact; minor financial loss | Internal non-sensitive data disclosed; system unavailable <8 hours |
| **Negligible** | Minimal or no impact on operations, assets, or individuals | No operational disruption; reputation impact only; minor inconvenience |

### Assessing the Likelihood Component

| Likelihood | Description | Conditions |
|-----------|-------------|-----------|
| **Very High** | Near certainty; uncontrolled deficiency actively exploitable; no barriers to exploitation | Known public exploitation; no authentication required; internet-facing |
| **High** | Highly probable; deficiency is exploitable by an adversary with standard capabilities | Publicly known vulnerability; low technical barrier; limited access controls |
| **Moderate** | Realistic possibility; requires some capability but achievable by determined adversary | Technical skill required; some access controls present but insufficient |
| **Low** | Unlikely but possible; significant barriers exist | High technical skill required; strong compensating controls in place |
| **Very Low** | Remote; deficiency only exploitable under very specific, unlikely conditions | Multiple strong compensating controls; very limited access; no known exploitation |

### Risk Determination Matrix (SP 800-30 Rev 1, Table I-2)

|                     | **Negligible** | **Minor** | **Moderate** | **Severe** | **Catastrophic** |
|---------------------|--------------|---------|------------|----------|----------------|
| **Very High**       | Low          | Moderate | High       | Very High | Very High      |
| **High**            | Low          | Moderate | Moderate   | High      | Very High      |
| **Moderate**        | Very Low     | Low      | Moderate   | Moderate  | High           |
| **Low**             | Very Low     | Very Low | Low        | Low       | Moderate       |
| **Very Low**        | Very Low     | Very Low | Very Low   | Low       | Low            |

Map the risk level to severity:
- Very High → **Critical**
- High → **High**
- Moderate → **Moderate**
- Low → **Low**
- Very Low → **Informational**

---

## Severity Examples by Control Area

### Critical Severity Examples

| Control | Finding |
|---------|---------|
| IA-2 | No authentication required to access an internet-facing administrative interface |
| AC-3 | Any unauthenticated user can access all system data (no access enforcement) |
| SC-28 | Sensitive PII stored in plaintext; no encryption at rest; publicly accessible storage |
| AU-2 | Audit logging completely disabled; no record of any access or actions |
| SI-3 | No malware protection on any endpoint; known malware present on active systems |

### High Severity Examples

| Control | Finding |
|---------|---------|
| IA-2(1) | Multi-factor authentication not enforced for privileged accounts |
| AC-2 | Numerous accounts for terminated employees remain active and unreviewed |
| SI-2 | Critical-rated CVEs from 12+ months ago unpatched on internet-facing systems |
| AU-9 | Audit logs can be modified or deleted by standard user accounts |
| CM-6 | Default passwords or manufacturer credentials in use on network devices |
| PE-3 | Physical access to the server room is uncontrolled; no badge readers |

### Moderate Severity Examples

| Control | Finding |
|---------|---------|
| AC-6 | Several non-privileged accounts have excessive permissions beyond role requirements; no documented justification |
| CP-9 | Backup restoration has not been tested in over 12 months; backups assumed working but unverified |
| RA-5 | Vulnerability scans are conducted but findings from 90+ days ago remain unaddressed without POA&M |
| AT-2 | 25% of users have not completed their annual security awareness training |
| CM-3 | Emergency changes are implemented without post-change documentation consistently |

### Low Severity Examples

| Control | Finding |
|---------|---------|
| PL-2 | SSP was last reviewed 14 months ago; policy requires review every 12 months |
| AT-3 | Role-based training for one non-critical role group is 2 months overdue |
| MA-2 | Maintenance logs exist but do not include technician identification in 20% of entries |
| PS-5 | Transfer checklist requires 2 days but documented completion in 3 of 10 reviewed cases showed 3-day completion |
| CM-1 | Configuration management procedure references a superseded NIST document |

### Informational Examples

| Control | Finding |
|---------|---------|
| AC-2 | Account naming convention is documented but inconsistently applied; no security impact |
| CM-6 | Some non-security-impacting settings deviate from baseline; deviations documented and accepted |
| AT-2 | Training content covers all required topics but could be enhanced with more interactive scenarios |

---

## Compensating Controls and Risk Reduction

When assigning severity, consider whether effective compensating controls reduce the actual risk posed by the deficiency:

| If the OTS finding is offset by... | Risk reduction |
|-----------------------------------|---------------|
| Strong detective controls (e.g., SIEM alert configured for the same attack vector) | May reduce severity by one level |
| Physical controls compensating for logical gaps | Evaluate proportionally |
| Mitigating network isolation (internal network only, no external exposure) | May reduce likelihood component |
| Continuous monitoring detecting exploitation quickly | May reduce impact estimate |

**Important**: Compensating controls reduce but do not eliminate a finding. Document the compensating control and the adjusted risk determination.

---

## Remediation Timeframes

Federal agencies generally follow these remediation timeframes, derived from OMB M-21-31 and CISA Known Exploited Vulnerabilities (KEV) guidance:

| Severity | Recommended Remediation Timeframe | POA&M Required? |
|---------|----------------------------------|----------------|
| Critical | Immediate to 15 days | Yes — immediate escalation to AO |
| High | 30 days | Yes |
| Moderate | 90 days | Yes |
| Low | 180 days | Yes |
| Informational | Best effort / next cycle | No — optional observation in SAR |

**POA&M milestone requirements**:
- Critical/High: Initial milestone within 7 days of SAR delivery; interim milestones monthly
- Moderate: Initial milestone within 30 days; quarterly updates
- Low: Annual review sufficient

---

## Aggregated Risk Considerations

Individual findings at a lower severity may collectively represent a higher risk where:
1. Multiple Moderate findings in the same control family indicate a systemic programme failure
2. Multiple Low findings in access control + audit + incident response together suggest an inability to detect and respond to incidents
3. A finding marked "Not Applicable" that is incorrectly justified should be flagged as a finding

When presenting aggregated risk to the AO, note:
- "This system has no Critical or High findings, but 8 Moderate findings in AC and AU create a combined elevated risk for [specific threat scenario]."

---

## AO Risk Decision Support

The SAR risk summary should enable the Authorising Official to make a risk-based authorization decision:

| Risk Profile | AO Options |
|-------------|-----------|
| No Critical/High findings, Moderate and below | Likely to support ATO with POA&M items |
| High findings with near-term POA&M milestones | ATO with conditions (POA&M milestones as conditions of authorisation) |
| Critical findings or multiple High findings without near-term remediation | May delay ATO until Critical/High findings remediated; or reject ATO |
| Critical findings that pose immediate risk | Immediate remediation required; system operation may need to be restricted pending fix |
