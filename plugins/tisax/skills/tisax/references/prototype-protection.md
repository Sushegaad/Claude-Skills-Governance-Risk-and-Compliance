# TISAX Prototype Protection Reference
## Chapter 15 — Prototype and Test Vehicle Protection Detailed Requirements

---

## Purpose and Scope

VDA ISA Chapter 15 applies only when an organization is pursuing the **Prototype** or
**Strict Prototype** TISAX label. These labels are required by OEMs when their suppliers
handle pre-release vehicles, prototype components, or related confidential manufacturing
and design information that has not yet been publicly disclosed.

Prototype protection is one of the most critical confidentiality requirements in the
automotive supply chain. The premature disclosure of a new vehicle design — through
unauthorized photography, leaks, or theft — can cause the OEM enormous competitive
and financial harm.

---

## What Is a Prototype?

For TISAX purposes, a **prototype** includes:

| Asset Type | Examples |
|-----------|---------|
| Pre-production vehicles | Mule vehicles, rolling prototypes, Erlkönig vehicles, pre-series vehicles |
| Prototype components | Unreleased body panels, interior elements, powertrain prototypes, electronics |
| Test vehicles | Vehicles fitted with unreleased technology or drive systems |
| Development data | CAD data, design sketches, 3D models, styling renders for unreleased vehicles |
| Related documents | Test reports, homologation plans, specification prototypes, camouflage requirements |
| Digital replicas | Digital twins, virtual prototype data, simulation models tied to unreleased designs |

---

## Prototype Label vs Strict Prototype Label

| Aspect | Prototype Label | Strict Prototype Label |
|--------|----------------|----------------------|
| VDA ISA Chapter | Chapter 15 standard requirements | Chapter 15 enhanced requirements |
| Assessment Level | AL 2 | AL 3 |
| Typical trigger | General prototype handling; established OEM supplier relationship | World premieres, flagships, high-sensitivity launches |
| Photography controls | Policy-based (NDAs, signs, rules) | Physical controls + monitoring + enforcement |
| Storage area windows | No specific requirement | No windows or window coverings/blackout required |
| Subcontractor use | Disclosure required; must meet same basic controls | OEM pre-approval required per job / engagement |
| External work sites | Supplier-managed controls | OEM must approve each external location |

---

## Chapter 15 Requirements — Prototype Label

### R15.1 — General Prototype Handling Policy

**Requirement:** A documented policy covering the handling, storage, use, and disposal
of prototype vehicles and components must exist and be communicated to all relevant
personnel.

**Must criteria:**
- Policy is documented, approved, and version-controlled
- Policy covers handling rules, access permissions, and consequences of non-compliance
- All personnel with prototype access have been briefed on the policy (documented acknowledgements)

**Evidence examples:**
- Prototype handling policy document with version and approval date
- Training/briefing records for workshop staff, logistics personnel, and drivers
- Role-based responsibility matrix for prototype handling

---

### R15.2 — Prototype Identification and Tracking

**Requirement:** All prototype assets must be uniquely identified and tracked throughout
their lifecycle.

**Must criteria:**
- Prototype vehicles and significant components are registered in a tracking record
- Tracking record shows location, responsible holder, and status for each prototype
- Unregistered prototypes or out-of-location assets quickly identified

**Evidence examples:**
- Prototype register/log showing asset IDs, current location, responsible person
- Vehicle tracking system or spreadsheet with movement history
- Handover records when prototypes transfer between personnel or locations

---

### R15.3 — Physical Access Controls for Prototype Areas

**Requirement:** Only authorized, trained personnel may access areas where prototypes
are stored, worked on, or displayed. Visitor access must be controlled and supervised.

**Must criteria:**
- Prototype storage and workshop areas are physically separated with controlled entry
- Access rights formally granted and reviewed; list of authorized personnel documented
- Visitor access requires prior approval; all visitors are escorted and logged
- Personnel removals immediately trigger access revocation

**Evidence examples:**
- Access control system records (electronic badge, key registry)
- List of authorized personnel with access
- Visitor log for prototype areas
- Offboarding checklist showing access revocation step

---

### R15.4 — Photography and Media Controls

**Requirement:** Unauthorized photography, filming, or recording of prototypes must be
prevented through policy, physical controls, and enforcement.

**Must criteria:**
- "No photography" policy formally documented and signed by all prototype area staff
- Physical signs prominently displayed in all prototype areas
- Mobile phone and camera controls enforced (device lock bags, camera cover stickers, phone-free zones)
- Policy violations are investigated and reported per incident procedure

**Evidence examples:**
- No-photography policy document
- Signed acknowledgements from personnel
- Photographs/evidence of posting in prototype areas
- Mobile device control deployment evidence (Faraday bags, camera blocking stickers)
- Incident reports related to photography violations (if any)

---

### R15.5 — Transport of Prototype Vehicles and Components

**Requirement:** Transport of prototypes must be conducted using secure procedures that
prevent visual identification, tracking, or unauthorized access during transit.

**Must criteria:**
- Transport procedure formally documented
- Prototypes transported in covered vehicles or enclosed trailers
- Driver is briefed and has signed an NDA
- Route pre-approval required where OEM has specified requirements
- Minimum personnel exposure during transport

**Evidence examples:**
- Prototype transport procedure
- Sample transport job records / driver briefing checklists
- Evidence of covered transport (enclosed trailers, vehicle wraps, body panels covered)
- NDA signed by transport drivers and logistics staff

---

### R15.6 — Confidentiality Agreements

**Requirement:** All personnel with access to prototypes must have signed a confidentiality
or non-disclosure agreement explicitly covering prototype protection.

**Must criteria:**
- NDAs in place for all employees with prototype access
- NDAs in place for contractors, temporary workers, and third-party service staff
- NDAs reference prototype confidentiality specifically (not just general employment NDA)
- NDA records retained throughout employment and for an agreed period post-employment

**Evidence examples:**
- NDA template referencing prototypes and pre-production vehicles
- Signed NDA records for current employees in prototype roles
- Contractor NDA records
- Process for onboarding new personnel requiring prototype NDA before access granted

---

### R15.7 — Prototype Incident Reporting

**Requirement:** Unauthorized photography, disclosure, theft, or loss of prototype assets
must be reported promptly through a defined process, including notification to the OEM
where required.

**Must criteria:**
- Incident reporting process specifically covering prototype incidents
- Responsible person for reporting identified (Security Officer, IS Manager)
- Time frame for internal escalation and OEM notification defined
- All prototype incidents logged and investigated

**Evidence examples:**
- Incident response procedure with prototype-specific section
- Incident log (anonymized examples acceptable if real incidents confidential)
- OEM notification template or contact list for prototype incidents
- Evidence of a recent tabletop exercise or test of the prototype incident process

---

### R15.8 — Destruction and Disposal of Prototype Materials

**Requirement:** Decommissioned prototype vehicles, components, and documents must be
securely destroyed or disposed of to prevent unauthorized reconstruction or disclosure.

**Must criteria:**
- Disposal procedure for physical prototype components (crushing, shredding, recycling with security controls)
- Secure document destruction (shredding, burning) for prototype documentation
- Disposal records maintained
- OEM approval obtained before disposal where required by contract

**Evidence examples:**
- Prototype disposal procedure
- Disposal records with dates and method
- Certificates of destruction from certified disposal contractors
- OEM sign-off confirmation where required

---

## Chapter 15 Additional Requirements — Strict Prototype Label

### R15-S.1 — Prototype Storage Areas: No Visual Exposure

**Requirement (Strict):** Prototype storage areas must not have windows or external
visibility that could allow unauthorized visual observation of the vehicle from outside.

**Implementation options:**
- Windowless dedicated storage bays
- Blacked-out / frosted windows with no visibility from outside
- Internal storage with no external-facing windows
- If windows are unavoidable: permanent blackout film or shutters with a controlled opening procedure

---

### R15-S.2 — External Work: OEM Pre-Approval

**Requirement (Strict):** Any work on Strict Prototype vehicles performed at an external
location (supplier's site, subcontractor, testing facility) must receive prior written
approval from the OEM for each individual engagement.

**Process:**
1. Supplier identifies need for external work
2. External location assessed against Strict Prototype IS requirements
3. Supplier submits request to OEM contact with location details, security measures, personnel list
4. OEM reviews and provides written approval
5. Work proceeds only after approval received
6. Post-work confirmation provided to OEM

---

### R15-S.3 — Subcontractor Controls for Strict Prototype

**Requirement (Strict):** Any subcontractor that will work with Strict Prototype assets
must be:
- Pre-approved by the OEM before work commences
- Subject to the same Strict Prototype protection requirements as the prime supplier
- Covered by a contractual IS agreement explicitly referencing Strict Prototype requirements

---

### R15-S.4 — Enhanced Physical Monitoring

**Requirement (Strict):** Active monitoring systems within prototype areas (e.g., CCTV,
access attempt logging) should be deployed and records retained for an agreed period.

---

## Prototype Protection Quick Reference Checklist

```
Access Control
[ ] Prototype area physically restricted (door, fence, controlled entry)
[ ] Electronic access control or key register
[ ] Authorized personnel list maintained and reviewed regularly
[ ] Visitor policy: prior approval + escort + log
[ ] Offboarding: access revoked immediately on departure

Photography / Media
[ ] "No photography" policy documented and signed by all staff
[ ] Physical signs posted in all prototype areas
[ ] Mobile phone camera controls enforced
[ ] Device control records or policy deployment evidence

Documentation and NDAs
[ ] Prototype handling policy documented and version-controlled
[ ] All prototype staff have signed prototype NDA
[ ] Contractor / temp worker NDAs in place

Asset Tracking
[ ] Prototype register with vehicle IDs, locations, responsible holder
[ ] Movement records when prototypes transferred
[ ] Regular reconciliation of register vs physical assets

Transport
[ ] Transport procedure documented
[ ] Covered vehicles/trailers used
[ ] Drivers briefed and under NDA
[ ] OEM route approval obtained where required

Incidents
[ ] Prototype incident type coverage in incident response plan
[ ] OEM notification obligation and contact known
[ ] Incident log maintained

Disposal
[ ] Disposal procedure for physical and document prototype assets
[ ] Disposal records with method and date
[ ] OEM approval process for disposal where required

[Strict Prototype Only]
[ ] Storage area has no external windows (or permanent blackout)
[ ] External work requires OEM pre-approval per engagement
[ ] Subcontractors pre-approved by OEM
[ ] CCTV or active monitoring deployed in prototype areas
```
