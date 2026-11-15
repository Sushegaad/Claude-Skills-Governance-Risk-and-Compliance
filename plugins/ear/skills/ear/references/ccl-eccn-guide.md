# EAR Commerce Control List (CCL) and ECCN Classification Guide

## How to Use This Reference

This guide covers: (1) detailed ECCN lookup methodology, (2) key ECCNs by category, (3) Commerce Country Chart usage, and (4) jurisdiction determination between EAR and ITAR.

---

## ECCN Classification Methodology

### Step 1: Determine if the Item is "Subject to the EAR" (§ 734.3)

An item is subject to the EAR if it is:
- All items **physically in the United States** (including in Foreign Trade Zones)
- All items of **US origin** (manufactured in the US), regardless of location
- **Foreign-made items** that incorporate controlled US-origin content above the de minimis threshold (§ 734.4) - 10% or 25% depending on destination
- **Foreign direct products** of US technology/software that meet the FDPR criteria (§ 734.9)
- Items the president has placed under EAR jurisdiction by executive order

**Not subject to EAR:** Publicly available information (§ 734.7), basic scientific research (fundamental research exclusion, § 734.8), patent applications, and items exclusively controlled by another US agency (ITAR/USML, NRC, FDA, etc.)

---

### Step 2: Apply the Order of Review (§ 732.3)

| Step | Check | If Yes |
|------|-------|--------|
| 1 | Is the item on the USML (22 CFR Part 121)? | → ITAR jurisdiction; stop here |
| 2 | Is it exclusively controlled by another US agency? | → That agency's regulations |
| 3 | Is it subject to the EAR per § 734.3? | → Continue to CCL lookup |
| 4 | Is it on the CCL? | → Assign ECCN |
| 5 | Not on CCL | → EAR99 designation |

---

### Step 3: Search the CCL (Part 774, Supplement No. 1)

Search strategies (in order of preference):
1. **Interactive CCL** at bis.gov/regulations/ear/interactive-commerce-control-list
2. **Self-classification:** Compare item's technical parameters (frequency, performance, materials) to CCL entry technical notes and parameters
3. **CCATS request:** Submit BIS-748P-A via SNAP-R for official classification determination
4. **CJ request to DDTC:** If jurisdiction between ITAR and EAR is unclear

**Reading a CCL Entry:**
Each ECCN entry contains:
- **Entry heading:** ECCN number and title
- **List of Items Controlled:** Specific technical parameters that determine if item falls under this ECCN
- **Unit:** The unit of measure for reporting
- **Reasons for Control (RFCs):** NS, AT, CB, NP, MT, etc.
- **Country Chart columns:** Which RFC columns on the Country Chart to check
- **License Exceptions:** Which exceptions (LVS, GBS, STA, etc.) are available
- **List of Items Controlled - Related Controls:** References to other ECCNs or USML categories
- **Technical Notes:** Clarifications on measurement and interpretation

---

### Step 4: EAR99 - When to Use

If after searching the CCL you cannot find an ECCN that covers the item:
- The item is **EAR99**
- EAR99 items **do not appear on the CCL** and have no ECCN number
- They are subject to EAR jurisdiction but generally do not require a license for export

**EAR99 items still require a license if:**
- Destined for **embargoed countries** (Cuba, Iran, North Korea, Syria - Part 746)
- Destined for **Russia or Belarus** under enhanced controls (Part 746.8)
- The end-user is on the **Entity List** (Supplement 4, Part 744)
- The end-use is for **WMD development** (§ 744.2–744.6)
- Exporter has **knowledge** of prohibited end-use or end-user

---

## Key ECCNs by Category

### Category 0 - Nuclear Materials, Facilities, and Equipment

| ECCN | Description |
|------|-------------|
| 0A001 | Nuclear reactors and specially designed equipment |
| 0B001 | Nuclear test/measurement equipment |
| 0C001 | "Natural uranium," "depleted uranium," special nuclear material |
| 0D001 | Software for items controlled in Category 0 |
| 0E001 | Technology for nuclear items |

### Category 1 - Chemicals, Microorganisms, and Toxins

| ECCN | Description |
|------|-------------|
| 1C350 | Chemical weapons precursors (Schedule 2 and 3 chemicals) |
| 1C351 | Human and zoonotic pathogens (Select Agents) |
| 1C352 | Animal pathogens not in 1C351 |
| 1C354 | Plant pathogens |
| 1C810 | Ammonium nitrate (precursor concerns) |

### Category 3 - Electronics

| ECCN | Description |
|------|-------------|
| 3A001 | Electronic components (advanced semiconductors, MMICs, SAW devices) |
| 3A090 | Integrated circuits for advanced computing (high-bandwidth memory) |
| 3B001 | Equipment for manufacturing electronic components (wafer fab) |
| 3D001 | Software for Category 3 equipment |
| 3E001 | Technology for Category 3 items |

### Category 4 - Computers

| ECCN | Description |
|------|-------------|
| 4A003 | Electronic computers and related equipment (performance thresholds) |
| 4A090 | Computers/electronic assemblies for advanced computing (AI chips) |
| 4D001 | Software for high-performance computers |
| 4E001 | Technology for Category 4 items |

### Category 5 - Telecommunications and Information Security

| ECCN | Description |
|------|-------------|
| 5A001 | Telecommunications equipment |
| 5A991 | Telecommunications equipment not controlled by 5A001 (residual, AT only) |
| 5A002 | Information security systems and equipment (cryptographic) |
| 5A992 | Mass-market cryptographic equipment not controlled by 5A002 (residual) |
| 5B002 | Information security test, inspection, and production equipment |
| 5D002 | Software for information security/encryption |
| 5E002 | Technology for information security items |
| 5D992 | Mass-market encryption software |

### Category 7 - Navigation and Avionics

| ECCN | Description |
|------|-------------|
| 7A001 | Accelerometers with specific performance |
| 7A004 | Star trackers and attitude control equipment |
| 7A101 | Accelerometers for missiles |
| 7A102 | Gyroscopes for missiles |
| 7E001 | Technology for navigation items |

### Category 9 - Aerospace and Propulsion

| ECCN | Description |
|------|-------------|
| 9A001 | Aero gas turbine engines and components |
| 9A004 | Space launch vehicles and spacecraft |
| 9A515 | Spacecraft and related items (satellites) |
| 9E003 | Technology for turbofan and turboprop engines |

---

## Commerce Country Chart - How to Use (Part 738, Supplement 1)

### Purpose
The Country Chart determines if a license is required based on the combination of the item's **Reason(s) for Control** and the **destination country**.

### Reading the Chart
1. Find the destination country (rows, alphabetical)
2. Find the RFC column(s) for your item's ECCNs (e.g., NS Column 1, AT Column 1, CB Column 1)
3. If the cell shows an "**X**" → a license is generally required
4. If blank → generally no license required for that RFC/country combination

### Important: Multiple RFCs
If your ECCN has multiple RFCs (e.g., NS and AT), check **all applicable columns** for the destination. A license is required if any RFC/country cell shows "X" **unless** a license exception applies for that specific RFC.

### Country Chart Column Codes

| Column | Meaning |
|--------|---------|
| NS Column 1 | National security - sensitive items |
| NS Column 2 | National security - less sensitive items |
| MT Column 1 | Missile technology |
| NP Column 1 | Nuclear nonproliferation - major suppliers group |
| NP Column 2 | Nuclear nonproliferation - trigger list |
| CB Column 1 | Chemical and biological - Australia Group |
| CB Column 2 | Chemical and biological - non-Australia Group |
| RS Column 1 | Regional stability - most items |
| RS Column 2 | Regional stability - less sensitive |
| CC Column 1 | Crime control - all items |
| CC Column 2 | Crime control - shotguns |
| CC Column 3 | Crime control - used equipment |
| AT Column 1 | Anti-terrorism - all items |
| AT Column 2 | Anti-terrorism - shotguns |
| UN | UN embargo |

---

## Jurisdiction Determination: EAR vs. ITAR

### The "Order of Review" in Detail

The US government mandates exporters apply this order before determining export classification:

**STEP 1 - Consult the USML (22 CFR Part 121):**
- The USML has 21 categories (Cat. I–XXI) covering military articles
- If the item is "specially designed" or enumerated on the USML → ITAR jurisdiction, file with DDTC
- The "specially designed" standard is complex - items designed for civilian use that are identical to military articles may still be EAR

**STEP 2 - Consult the CCL:**
- If not on USML → check CCL
- If found on CCL → assign ECCN
- If not found → EAR99

**When jurisdiction is unclear - Submit a CJ Request:**
- **CJ (Commodity Jurisdiction) Request** - submitted to DDTC
- Used when: an item has both military and commercial versions; an item was transferred from USML to CCL under Export Control Reform; or there's genuine ambiguity
- Timeline: 45-day statutory deadline; in practice, can take longer
- **CCATS** - BIS's equivalent for confirming an ECCN (use SNAP-R portal)

### Common EAR/ITAR Boundary Areas

| Item Type | Likely Jurisdiction |
|-----------|-------------------|
| Consumer electronics, mass-market software | EAR (usually EAR99 or 5D992) |
| Dual-use encryption (commercial VPN, SSL) | EAR (5D002 or 5D992 ENC) |
| Military radios, tactical communications | ITAR (Cat. XI) |
| Satellite components (commercial comms sats) | EAR (9A515) after Export Control Reform |
| Satellite components (military reconnaissance) | ITAR (Cat. XV) |
| Firearms and ammunition | ITAR (Cat. I and III); some EAR (shotguns) |
| Chemical precursors (dual-use) | EAR (Category 1) |
| Chemical weapons agents | ITAR (Cat. XIV) |
| Aircraft parts (commercial) | EAR (Category 9, lower threshold) |
| Military aircraft engines | ITAR (Cat. VIII) |
| GPS (commercial grade) | EAR (7A994, EAR99) |
| GPS (military, high-performance) | ITAR (Cat. XV) |
| Cybersecurity tools (commercial pen-testing) | EAR (5D002, ENC exception may apply) |
| Cyberweapons and offensive capabilities | Likely ITAR or unilateral controls |

---

## EAR99 Items That Still Need Licenses - Common Mistakes

| Scenario | Why License Needed |
|----------|--------------------|
| EAR99 electronics exported to Iran | Part 746 embargo - license required |
| EAR99 software sold to Entity List party | Entity List requirement - license required |
| EAR99 pump sold for nuclear programme | WMD end-use control § 744.2 |
| EAR99 laptop reexported from Germany to Russia | Part 746.8 Russia controls apply to all items |
| EAR99 goods with 10%+ US content to D:5 country | De minimis rule - license may be required |
| EAR99 circuit board demonstrated to Iranian engineer in US | Deemed export to Iran - check § 734.13 |

---

## EAR Controls on Russia and China - Key 2022–2026 Developments

### Russia and Belarus (Part 746.8)
Following February 2022, BIS imposed broad new controls:
- **All items subject to EAR** require a license for export to Russia/Belarus (including EAR99)
- Extremely limited license exceptions available (humanitarian, safety of flight)
- Entity List additions: hundreds of Russian defence and intelligence entities
- **FDP Rule for Russia:** Expanded FDPR captures foreign-made items produced by US equipment/software used to fabricate circuits destined for Russia's military

### China Advanced Computing Controls (October 2022 / October 2023)
- New ECCNs 3A090, 4A090 control advanced AI chips above performance thresholds
- Entity List expanded with semiconductor-related entities (Huawei, affiliates, others)
- FDPR expanded to capture foreign-made chips using US equipment if destined for restricted Chinese entities
- "ITAR Carve-Out" items - some satellite/military items moved from ITAR to EAR under Export Control Reform but with strict CCL controls
