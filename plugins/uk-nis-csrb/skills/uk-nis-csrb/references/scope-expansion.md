# UK CSRB — Scope Expansion Reference
## Cyber Security and Resilience Bill: New Categories and Scope Determination

> **Important — Bill Status:** The CSRB is proposed legislation as of the date of this file. All scope
> provisions are based on published policy intent, DSIT consultations, and the introduced Bill.
> Final scope definitions will be established in the enacted legislation and associated secondary
> legislation (statutory instruments). Verify at bills.parliament.uk and gov.uk/dsit.

---

## 1. Retained Scope: OES and DSP Categories

The CSRB retains all existing NIS Regulations 2018 scope categories without change. Entities
currently designated as OES or registered as DSPs remain subject to equivalent obligations.

### 1.1 Operators of Essential Services (OES) — Retained

| Sector | Sub-sector | Competent Authority |
|--------|-----------|---------------------|
| Energy | Electricity (generation, transmission, distribution, supply) | Ofgem |
| Energy | Oil (transport, distribution, storage) | DESNZ |
| Energy | Gas (transmission, distribution, storage, supply) | Ofgem |
| Transport | Air transport | Civil Aviation Authority (CAA) |
| Transport | Rail transport | Office of Rail and Road (ORR) |
| Transport | Road transport | Department for Transport (DfT) |
| Transport | Water transport / maritime | DfT / Maritime and Coastguard Agency (MCA) |
| Health | Healthcare providers (NHS, independent) | DHSC / NHS England |
| Drinking Water | Supply and distribution | Drinking Water Inspectorate (DWI) |
| Digital Infrastructure | Internet Exchange Points (IXPs) | Ofcom |
| Digital Infrastructure | DNS service providers | Ofcom |
| Digital Infrastructure | TLD registries | Ofcom |

### 1.2 Digital Service Providers (DSP) — Retained

| DSP Type | Competent Authority |
|----------|---------------------|
| Online marketplace | ICO |
| Online search engine | ICO |
| Cloud computing (IaaS, PaaS, SaaS — excluding micro/small enterprises) | ICO |

---

## 2. New Category 1: Managed Service Providers (MSPs)

### 2.1 Policy Rationale

The UK government's decision to bring MSPs into scope is based on empirical evidence of systemic risk:

- **MOVEit vulnerability exploitation (2023):** A zero-day in Progress Software's MOVEit Transfer product was exploited by the Cl0p ransomware group, resulting in data exfiltration from hundreds of organisations globally via their managed service and cloud transfer providers. UK organisations affected included the BBC, British Airways, Boots, and the NHS.
- **Capita breach (2023):** A cyber incident at IT outsourcing company Capita affected numerous public sector clients including NHS Trusts and local authorities.
- **SolarWinds (2020):** Supply chain compromise of SolarWinds Orion MSP platform affected thousands of organisations worldwide including government agencies.

These incidents demonstrate that MSPs represent a concentrated attack surface — compromise of a single MSP can give attackers access to dozens or hundreds of client organisations simultaneously.

### 2.2 Definition of Managed Service Provider (Indicative)

For CSRB purposes, an MSP is expected to be defined as an entity that:
- Provides ongoing, contracted IT or security management services to one or more customer organisations
- Typically has privileged remote access to customer networks, systems, or data
- The services are delivered remotely (or remotely supervised)
- The MSP's systems or access could, if compromised, enable access to customer systems

**Services expected to be in scope:**
| Service Category | In-scope Indication |
|-----------------|---------------------|
| Managed SOC / MDR (Managed Detection and Response) | Yes |
| Managed Network Services (WAN, firewall, SD-WAN) | Yes |
| Managed Backup and DR | Yes |
| Managed Cloud Services (hosting, infrastructure management) | Yes |
| Managed Identity and Access Management | Yes |
| Managed Endpoint Detection and Response (EDR/XDR) | Yes |
| IT outsourcing with ongoing remote management | Yes |
| MSSP (Managed Security Service Provider) | Yes |

**Services less likely to be in scope (based on policy intent):**
| Service | In-scope Indication |
|---------|---------------------|
| One-off IT consultancy (no ongoing access) | Unlikely |
| Software licensing / resale (no managed access) | Unlikely |
| Break-fix IT support (ad-hoc, no permanent access) | Unlikely |
| SaaS application providers with no customer system management | Unlikely |
| IT hardware supply without managed services | Unlikely |

### 2.3 MSP Scope Thresholds

Precise thresholds for MSP designation are to be set in secondary legislation. Relevant factors likely to be considered include:
- Number of critical sector (OES or public sector) customers managed
- Value of managed services revenue from critical sector customers
- Volume/value of data processed for critical sector customers
- Whether the MSP provides services that are critical to essential service delivery

### 2.4 MSP Obligations

MSPs that fall in scope of the CSRB are expected to have obligations equivalent to (or adapted from) OES or DSP requirements, including:
- Implementing appropriate and proportionate security measures (aligned to NCSC CAF or equivalent)
- Notifying the relevant Competent Authority of significant incidents
- Supporting Competent Authority audits and information requests
- Maintaining documented security policies and risk assessments

### 2.5 MSP Self-Assessment Framework

Until formal designation and CA guidance is issued, MSPs should self-assess using a CAF-equivalent framework covering:

| Area | Key Questions |
|------|--------------|
| Governance | Is there board-level accountability for cyber security? |
| Risk Management | Are risks to managed client environments systematically assessed? |
| Asset Management | Are all assets with client connectivity inventoried? |
| Supply Chain | Are sub-processors and tool vendors assessed? |
| Identity and Access Control | Is privileged client access tightly controlled and MFA-enforced? |
| Data Security | Is client data segregated, encrypted, and access-controlled? |
| System Security | Are MSP systems and tooling patched and hardened? |
| Monitoring | Are MSP and client environments monitored for compromise? |
| Incident Response | Is there an IRP covering cascading incidents across clients? |

---

## 3. New Category 2: Large Data Centres

### 3.1 Policy Rationale

Large data centres represent concentrated critical infrastructure. A significant proportion of UK critical services — including financial, healthcare, government, and communications services — rely on third-party data centre hosting. An attack on a major data centre could simultaneously affect hundreds of tenants.

The UK government assessed in its 2023 Critical National Infrastructure (CNI) designation review that large data centres warrant CNI-equivalent treatment. This is reflected in the CSRB.

### 3.2 Indicative Scope for Data Centres

The CSRB is expected to cover:
- Operator-neutral (colocation) data centres above a defined scale threshold
- Data centres hosting critical national infrastructure systems or government systems
- Hyperscale data centre facilities operated by cloud providers (where not already covered as DSPs)

**Likely threshold indicators:**
- Data centre capacity above a defined megawatt (MW) or square metre floor area threshold
- Number of customers above a defined level (especially critical sector customers)
- Whether the facility hosts government Tier 1 or Crown systems

### 3.3 Data Centre Security Obligations

Data centre operators in scope are expected to implement:
- Physical security measures (perimeter security, access control, CCTV, environmental controls — fire, flood, power)
- Cybersecurity measures for management systems (DCIM, remote monitoring, building management systems)
- Incident reporting obligations for significant disruptions
- Business continuity and disaster recovery capability

The NCSC has published separate guidance on data centre cyber security risk. CAF objectives B5 (Resilient Networks and Systems) and D1 (Response and Recovery) are particularly relevant for data centre operators.

---

## 4. Potential Further Scope Expansion

The CSRB policy documentation notes the possibility of future scope expansion through secondary legislation to include:

- **Public sector bodies** not currently designated as OES (e.g. local authorities, central government departments)
- **Downstream managed service dependencies** — sub-handlers or sub-processors used by in-scope MSPs
- **Further critical service providers** identified through ongoing CNI review

The Bill is designed to be forward-facing, with secondary legislation providing the mechanism to add categories without requiring new primary legislation.

---

## 5. Scope Determination Flowchart

To determine whether your organisation is in scope of the CSRB:

```
START
  |
  v
Are you currently designated as OES under NIS Regs 2018?
  YES --> You remain in scope (OES obligations continue + CSRB enhancements)
  NO  --> Continue
  |
  v
Are you currently a registered DSP under NIS Regs 2018?
  YES --> You remain in scope (DSP obligations continue + CSRB enhancements)
  NO  --> Continue
  |
  v
Do you provide ongoing managed IT or security services to critical sector orgs?
(remote access, managed SOC, managed network, managed backup, etc.)
  YES --> Likely in scope as MSP (new CSRB category)
  NO  --> Continue
  |
  v
Do you operate a significant-scale data centre?
(colocation, hosting critical infrastructure, large capacity)
  YES --> Likely in scope as Data Centre operator (new CSRB category)
  NO  --> Continue
  |
  v
Are you a public sector body with significant IT systems exposure?
  POTENTIALLY --> Monitor secondary legislation closely
  
  OTHERWISE --> Currently not in CSRB scope
               Continue monitoring DSIT publications for scope changes
               Consider voluntary compliance with CAF as good practice
END
```
