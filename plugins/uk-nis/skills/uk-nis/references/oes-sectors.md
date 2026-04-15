# UK NIS — OES Sectors, Competent Authorities, and Designation Reference
## NIS Regulations 2018 — Schedule 2 and Competent Authority Designations

---

## Overview

Under the NIS Regulations 2018, Operators of Essential Services (OES) are designated by Competent Authorities within the sectors listed in **Schedule 2** of the Regulations. This reference provides the complete sector breakdown, Competent Authority details, designation criteria, and key considerations for each sector.

---

## Sector 1 — Energy

### 1.1 Electricity

**Competent Authority:** Ofgem (Office of Gas and Electricity Markets)

**Scope:**
- Electricity generation operators (above designation threshold)
- Electricity transmission system operators (National Grid ESO / NESO)
- Electricity distribution network operators
- Electricity suppliers providing to business and/or domestic consumers

**Designation Criteria:**
Ofgem applies thresholds related to installed generation capacity, volume of electricity transmitted/distributed, and number of customers served. Over 250 megawatts installed capacity is a typical benchmark for generation OES designation.

**Key Regulatory Context:**
- Ofgem coordinates with National Cyber Security Centre (NCSC) and DSIT
- Alignment with NERC CIP (North American Electric Reliability Corporation Critical Infrastructure Protection) is relevant for interconnected systems
- Electricity sector also subject to Critical National Infrastructure (CNI) designation by the Centre for the Protection of National Infrastructure (CPNI/NPSA)

---

### 1.2 Oil

**Competent Authority:** Department for Energy Security and Net Zero (DESNZ) (previously BEIS)

**Scope:**
- Oil pipeline operators
- Oil storage/terminal operators
- Oil distribution operators

**Key Regulatory Context:**
- Applies to entities operating crude oil and petroleum product pipelines, terminals, and distribution systems
- Excludes retail petrol stations (not designated NIS OES)
- DESNZ works with NCSC for technical guidance

---

### 1.3 Gas

**Competent Authority:** Ofgem

**Scope:**
- Gas transmission system operators (National Grid Gas Transmission)
- Gas distribution network operators
- Gas storage operators (e.g. underground storage, LNG facilities)
- Gas suppliers

**Key Regulatory Context:**
- Gas networks are defined as High-Pressure Transmission System (HPTS) and Local Distribution Zones (LDZ) operated by Gas Distribution Networks (GDNs)
- Ofgem's Network Security Guidelines reference the NIS Regulations

---

## Sector 2 — Transport

### 2.1 Air Transport

**Competent Authority:** Civil Aviation Authority (CAA)

**Scope:**
- UK-licensed air carriers with significant UK operations
- UK airport operators (above passenger volume threshold — typically major international airports)
- Air traffic management / Air navigation service providers (NATS)

**Key Regulatory Context:**
- CAA's Civil Aviation Security Regulations 2016 run alongside NIS
- NATS coordinates with NCSC on critical air traffic management system security
- Passenger threshold: airports handling over 10 million passengers per annum are likely designated OES; exact threshold is sector-specific guidance from CAA

---

### 2.2 Rail Transport

**Competent Authority:** Office of Rail and Road (ORR)

**Scope:**
- Network Rail (infrastructure operator)
- Train operating companies (TOCs) managing significant rail operations
- London Underground (TfL)
- European Rail Traffic Management System (ERTMS) systems

**Key Regulatory Context:**
- ORR NIS guidance references CAF as the primary assessment tool
- Key concern: signalling systems, operational control systems, ticketing infrastructure

---

### 2.3 Road Transport

**Competent Authority:** Department for Transport (DfT)

**Scope:**
- Intelligent Transport Systems (ITS) operators
- Road operators with significant motorway/trunk road digital infrastructure (e.g. National Highways)

**Key Regulatory Context:**
- Road OES designation is more limited in scope than other transport sectors
- Focus on critical traffic management and road safety systems

---

### 2.4 Water Transport (Maritime)

**Competent Authority:** Department for Transport (DfT) / Maritime and Coastguard Agency (MCA)

**Scope:**
- UK port operators (major ports above passenger/freight threshold)
- Ship operators of UK-flagged vessels (above applicable gross tonnage thresholds)
- Vessel Traffic Services (VTS)

**Key Regulatory Context:**
- International Maritime Organization (IMO) Maritime Cyber Risk Management guidelines (MSC-FAL.1/Circ.3) are relevant
- Port operators align with ISPS Code (International Ship and Port Facility Security Code)

---

## Sector 3 — Health

**Competent Authority:** Department of Health and Social Care (DHSC) / NHS England

**Scope:**
- NHS Trusts (Acute, Mental Health, Ambulance, Community) in England
- NHS Scotland, NHS Wales, HSCNI (devolved; equivalent frameworks apply)
- Independent healthcare providers contracted by the NHS for significant clinical services
- GP federations and health networks above designation threshold

**Key Regulatory Context:**
- NHS Data Security and Protection Toolkit (DSPT) aligns with and supplements NIS requirements
- CAF is used alongside DSPT for OES assessment
- Critical concern: Electronic Patient Record (EPR) systems, NHS Spine connectivity, diagnostic imaging, prescription management
- DHSC works with NHS England and NCSC on threat intelligence and assurance

---

## Sector 4 — Drinking Water

**Competent Authority:** Drinking Water Inspectorate (DWI)

**Scope:**
- Water companies providing potable water supply and distribution (e.g. Severn Trent, Thames Water, Yorkshire Water, United Utilities, Anglian Water, South West Water, and others)
- Water treatment works operators above relevant supply volume thresholds

**Key Regulatory Context:**
- DWI has close coordination with Ofwat (economic regulation) and NCSC
- OT/SCADA systems for water treatment and distribution are in scope (SCADA, SCADA-adjacent systems, industrial control systems)
- Separation of IT from OT is a consistent DWI requirement

---

## Sector 5 — Digital Infrastructure

**Competent Authority:** Ofcom

**Scope:**
- Internet Exchange Points (IXPs) — facilities where different networks interconnect to exchange traffic
- Domain Name System (DNS) service providers — organisations providing recursive and/or authoritative DNS resolution services at scale
- Top-Level Domain (TLD) name registries — organisations managing .uk, .co.uk, and other UK-relevant TLDs (notably Nominet)

**Key Regulatory Context:**
- Ofcom designation applies to entities meeting significance thresholds for these services
- The number of DNS queries resolved, interconnection capacity (Gbps), and domain names managed are relevant designation factors
- Significant overlap with the NIS Category 1 definition

---

## Digital Service Providers (DSPs)

DSPs are not designated by Competent Authorities — they fall within scope automatically based on the services they provide and their size. The Competent Authority for all DSPs in the UK is the **Information Commissioner's Office (ICO)**.

| DSP Type | Scope Description |
|----------|------------------|
| Online marketplace | A digital service that allows consumers and/or traders to conclude online sales or service contracts with traders |
| Online search engine | A digital service that allows users to perform searches of, in principle, all websites, or websites in a particular language |
| Cloud computing service | A digital service that enables access to a scalable and elastic pool of shareable computing resources — including IaaS, PaaS, and SaaS models |

**DSP size exemption:** Micro enterprises (fewer than 10 employees; turnover/balance sheet not exceeding 2 million EUR) and small enterprises (fewer than 50 employees; turnover/balance sheet not exceeding 10 million EUR) are **exempt** from DSP NIS requirements.

---

## Competent Authority Contact Summary

| Competent Authority | Sectors | Primary NIS Contact Route |
|--------------------|---------|--------------------------|
| Ofgem | Electricity, Gas | ofgem.gov.uk — contact via network security team |
| DESNZ | Oil | gov.uk/desnz |
| CAA | Air transport | caa.co.uk — Security & Facilitation Division |
| ORR | Rail transport | orr.gov.uk — digital and cyber team |
| DfT | Road transport, Maritime | gov.uk/dft |
| MCA | Maritime (shipping/ports) | gov.uk/mca |
| DHSC / NHS England | Health | england.nhs.uk — CISO / Data Security |
| DWI | Drinking water | dwi.gov.uk |
| Ofcom | Digital infrastructure | ofcom.org.uk — Communications Security |
| ICO | DSPs | ico.org.uk/for-organisations/cybersecurity/ |

**Lead Government Authority (NIS Policy):**
Department for Science, Innovation and Technology (DSIT) — gov.uk/dsit

**National Technical Authority:**
National Cyber Security Centre (NCSC) — ncsc.gov.uk

---

## CA Powers Under the NIS Regulations

Under Regulations 15–19, Competent Authorities have the following statutory powers:

| Power | Regulation | Description |
|-------|-----------|-------------|
| Information requests | Reg 15 | CAs may request information to assess compliance with the Regulations |
| Security audits | Reg 16 | CAs may carry out (or commission) security audits of OES/DSPs |
| Inspections | Reg 17 | CAs may conduct site inspections of OES/DSPs |
| Enforcement notices | Reg 18 | CAs may issue notices requiring OES/DSPs to take specific steps to comply |
| Penalty notices | Reg 19 | CAs may impose financial penalties following non-compliance with an enforcement notice |
| Inspectors' powers | Reg 20 | Inspectors acting for CAs have powers to enter premises and examine documents |

---

## NIS Regulations 2018 — Key Provisions Summary

| Regulation | Subject |
|-----------|---------|
| Regulation 1 | Citation, commencement, and interpretation |
| Regulation 3 | Obligation on Secretary of State to designate Competent Authorities |
| Regulation 5 | Designation of OES by Competent Authorities |
| Regulation 6 | Competent Authority registers of OES |
| Regulation 7 | Relevant digital services (DSP scope) |
| Regulation 8 | Point of establishment / representative for non-UK DSPs |
| Regulation 10 | OES security obligation (take appropriate and proportionate measures) |
| Regulation 11 | OES incident notification obligation |
| Regulation 12 | DSP security obligation |
| Regulation 13 | DSP incident notification obligation |
| Regulation 14 | NCA (NCSC) functions as national cybersecurity authority |
| Regulation 15 | CA power to request information |
| Regulation 16 | CA power to audit |
| Regulation 17 | CA power to inspect |
| Regulation 18 | Enforcement notices |
| Regulation 19 | Penalty notices |
| Schedule 1 | Essential services sectors and sub-sectors |
| Schedule 2 | Competent Authority designations by sector |
| Schedule 3 | Digital services in scope (DSP types) |

---

## devolved Administrations

The NIS Regulations 2018 apply across the **United Kingdom** (England, Scotland, Wales, and Northern Ireland). Devolved institutions apply the Regulations within their devolved health and other portfolios but the UK-wide framework remains consistent.

- **NHS Scotland**: Scottish Government Health Directorate / NHS National Services Scotland
- **NHS Wales**: Welsh Government / Digital Health and Care Wales
- **HSCNI**: Department of Health Northern Ireland
