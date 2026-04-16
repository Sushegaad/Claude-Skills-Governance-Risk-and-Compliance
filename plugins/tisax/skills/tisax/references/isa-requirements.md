# TISAX VDA ISA Requirements Reference
## Source: VDA ISA 6.0 (Verband der Automobilindustrie Information Security Assessment)

---

## Important Note on VDA ISA

The VDA ISA questionnaire is published by VDA (Verband der Automobilindustrie) and is
freely available for download at https://www.vda.de/en/education-and-training/isa.
The current version is **VDA ISA 6.0** (2023). This reference summarizes the chapter
structure, key requirement areas, must criteria, and evidence indicators based on the
published framework. The full questionnaire with all individual question text must be
obtained from the official VDA source.

---

## Chapter 1 — Information Security Policy

**Objective:** Establish management commitment to information security through a formal
policy framework with defined objectives, roles, and review processes.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| IS policy documented | Must | Formal information security policy exists, is documented, and approved by senior management |
| IS policy communicated | Must | Policy communicated to all employees and relevant external parties |
| IS policy reviewed | Must | Policy reviewed at planned intervals (at least annually) or after significant changes |
| IS objectives defined | Standard | Measurable IS objectives aligned with organizational strategy |
| IS roles and responsibilities | Must | CISO/IS Manager role defined with accountability and authority |
| Management review of IS | Standard | Management regularly reviews IS performance indicators |
| Exceptions and deviations | Standard | Process for granting, documenting, and reviewing IS policy exceptions |

### Evidence for Maturity Level 3

- Signed, dated information security policy document
- Policy distribution records (email, portal, training acknowledgement)
- CISO/IS Manager job description or role charter
- Annual management review meeting minutes referencing IS
- IS objectives register with measurement approach

---

## Chapter 2 — Organization of Information Security

**Objective:** Establish an organizational structure for information security with clear
responsibilities, coordination mechanisms, and controls for mobile and remote working.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Segregation of duties | Must | Conflicting duties separated to prevent fraud or error in IS-critical functions |
| Contact with authorities | Standard | Defined process for contact with law enforcement and regulatory bodies |
| Contact with special interest groups | Standard | Participation in IS community, CERT feeds, threat intelligence |
| Information security in projects | Standard | IS requirements considered in all project types (IT, facilities, etc.) |
| Mobile device security | Must | Policy and controls for mobile devices handling confidential information |
| Telework/remote work | Must | Controls and policy for remote working arrangements; secure remote access |
| ISMS scope definition | Standard | ISMS scope is documented and reviewed |
| Responsibility for IS assets | Must | Asset owners defined for all information assets |

### Evidence for Maturity Level 3

- Organizational chart showing IS function and reporting lines
- Mobile device management (MDM) policy and deployment evidence
- Remote access policy and VPN configuration records
- ISMS scope document
- Project IS requirements checklist

---

## Chapter 3 — Asset Management

**Objective:** Identify organizational information assets, classify them by sensitivity, and
define handling rules appropriate to each classification level.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Asset inventory | Must | Comprehensive inventory of information assets including hardware, software, data, services |
| Asset ownership | Must | Each asset has an identified owner responsible for its protection |
| Information classification | Must | Classification scheme defined (e.g., public, internal, confidential, strictly confidential) |
| Labeling and handling of information | Must | Procedures for labeling, storing, transmitting, and destroying information by classification |
| Acceptable use of assets | Standard | Rules for acceptable use of information and associated assets |
| Return of assets | Standard | Employees and contractors return company assets upon termination |
| Media disposal | Must | Secure disposal or reuse of media containing classified information |

### Evidence for Maturity Level 3

- Asset register/CMDB with classification column
- Information classification policy with examples per level
- Labeling procedures (file naming, email handling, physical markings)
- Media disposal records/certificates
- Asset return checklist used at employee offboarding

---

## Chapter 4 — Information Security in Human Resources

**Objective:** Ensure employees and contractors understand their information security
responsibilities before, during, and after employment.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Background screening | Must | Background checks performed prior to employment per applicable laws |
| Terms and conditions of employment | Must | IS responsibilities documented in employment contracts or Role/Function descriptions |
| Management responsibilities | Standard | Managers actively enforce IS policies within their teams |
| IS awareness and training | Must | Regular IS awareness program; all employees trained; training records maintained |
| Disciplinary process | Standard | Formal disciplinary process for IS policy violations |
| Responsibilities upon termination | Must | Clear rules for information, access, and asset handling during and after termination |
| Confidentiality agreements | Must | NDAs or confidentiality clauses in contracts for personnel with access to CBI |

### Evidence for Maturity Level 3

- Background screening policy and recent screening records (anonymized)
- Employment contract extract showing IS clause or signed IS obligation
- Training completion records with names, dates, and content description
- IS awareness training materials (slides, e-learning)
- Offboarding checklist with IS sections

---

## Chapter 5 — Physical and Environmental Security

**Objective:** Prevent unauthorized physical access and protect organizational information
and IT assets from physical and environmental threats.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Physical security perimeter | Must | Defined secure areas with physical boundaries (locked rooms, controlled zones) |
| Physical access controls | Must | Entry controls ensuring only authorized personnel access secure areas |
| Securing offices and facilities | Must | IT equipment and sensitive areas secured against unauthorized entry |
| Environmental threats | Standard | Protection from fire, flood, heat, power failures, and other environmental risks |
| Working in secure areas | Standard | Rules for working in secure areas (no photography, clean desk, etc.) |
| Delivery and loading areas | Standard | Controlled access to delivery areas; goods checked before entry |
| Equipment placement and protection | Must | Equipment sited to reduce risk of unauthorized access and environmental damage |
| Clear desk and clear screen policy | Must | Clear desk and screen lock policy enforced consistently |
| Equipment disposal/reuse | Must | Storage media sanitized before disposal or reuse |

### Evidence for Maturity Level 3

- Site/facility security plan or procedures
- Access control logs or badge system records
- Equipment inventory with disposal records
- Physical security walk-through evidence (photos with description, if permissible)
- Clean desk observation results or audit records

---

## Chapter 6 — Target Compliant Management of IT Systems

**Objective:** Maintain secure operational IT environments through documented procedures
for system management, configuration hardening, and malware protection.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Documented operating procedures | Must | Operating procedures for IT systems documented and accessible to authorized users |
| Change management | Must | Changes to systems formally tested, assessed, and approved before implementation |
| Capacity management | Standard | Capacity monitored and planned to ensure system availability |
| Separation of development, test, and production | Must | Dev/test environments separated from production; production data not used in testing |
| Protection against malware | Must | Anti-malware tools deployed, updated, and monitored on all endpoints |
| Logging and event monitoring | Must | Security-relevant events logged; logs protected and regularly reviewed |
| Management of technical vulnerabilities | Must | Vulnerability scanning conducted; critical patches applied within defined timeframe |
| System hardening | Must | Systems configured to remove unnecessary services, accounts, and features |
| Software licensing | Standard | Software inventory maintained; license compliance ensured |
| Clock synchronization | Standard | System clocks synchronized with authoritative NTP source |

### Evidence for Maturity Level 3

- Change management procedure and recent change records
- Anti-malware console screenshots showing all endpoints covered
- Vulnerability scan reports with remediation tracking
- Hardening configuration checklists (CIS Benchmarks or equivalent)
- Log management configuration and retention settings
- Patch management reports with SLA compliance metrics

---

## Chapter 7 — Access Control and Authentication

**Objective:** Ensure only authorized users have access to information assets, systems, and
facilities, with appropriate controls to prevent unauthorized or excessive access.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Access control policy | Must | Policy defining access control rules, roles, and review obligations |
| User registration and de-registration | Must | Formal process for granting and revoking user access; linked to HR lifecycle |
| Privileged access management | Must | Privileged accounts strictly controlled, logged, and reviewed |
| Secret authentication information | Must | Passwords managed securely; minimum complexity and change requirements enforced |
| Access to networks and network services | Must | Access to networks restricted to authorized users and devices |
| Review of user access rights | Must | Periodic review (at least annually) of all user accounts and access rights |
| Removal of access rights | Must | Access removed promptly upon termination, role change, or contract end |
| Multi-factor authentication | Must (for remote/privileged) | MFA required for remote access and all privileged accounts |
| Logging of privileged access | Must | All privileged access events logged and auditable |
| Guest and visitor access | Standard | Guest network separated; visitor access time-limited and supervised |

### Evidence for Maturity Level 3

- Access control policy
- User provisioning and de-provisioning procedure with records
- Active Directory or IAM user export (with roles)
- Access review records (dated, signed/approved)
- MFA deployment confirmation (VPN, admin interfaces, cloud access)
- Privileged access log samples

---

## Chapter 8 — Cryptography

**Objective:** Ensure appropriate and effective use of cryptography to protect information
confidentiality, integrity, and authenticity.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Cryptographic policy | Must | Policy on use of cryptographic controls, approved algorithms, and minimum key lengths |
| Key management lifecycle | Must | Key generation, distribution, storage, revocation, and destruction procedures |
| Encryption at rest | Must | Sensitive and confidential data encrypted at rest on portable and removable media |
| Encryption in transit | Must | Sensitive data encrypted in transit using current TLS standards (1.2 minimum; 1.3 preferred) |
| Approved algorithms | Must | Only industry-standard, non-deprecated algorithms used (AES-256, RSA-2048+, SHA-256+) |
| Certificate management | Standard | Digital certificates managed; expiry tracked and renewed in advance |

### Evidence for Maturity Level 3

- Cryptography policy
- Key management procedure
- Encryption implementation evidence (BitLocker, TLS configuration, file encryption)
- List of approved cryptographic algorithms
- Certificate inventory with expiry dates

---

## Chapter 9 — Communication Security

**Objective:** Maintain security of networks and information transferred within and outside
the organization.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Network controls | Must | Network managed and controlled to protect systems and information |
| Network segregation | Must | Groups of information services, users, and systems segregated (VLANs, DMZ) |
| Information transfer policies | Must | Formal policy and procedures for transfer of information between organizations |
| Agreements on information transfer | Must | Confidentiality/transfer agreements in place with partners and customers |
| Electronic messaging security | Must | Email and messaging platforms secured; scanning for malicious content |
| Secure transfer of confidential information | Must | Encrypted channels or physical controls when transferring CBI externally |

### Evidence for Maturity Level 3

- Network architecture diagram showing segmentation
- Firewall policy documentation
- Information transfer policy
- NDAs and data exchange agreements with partners
- Email security configuration (TLS enforcement, anti-spam/phishing, DLP)

---

## Chapter 10 — System Acquisition, Development and Maintenance

**Objective:** Ensure information security requirements are incorporated throughout the
lifecycle of IT systems and software.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| IS requirements in new systems | Standard | IS requirements defined and agreed at the outset of new system projects |
| Secure development policy | Standard | Secure coding principles and guidelines in place for development teams |
| System change procedures | Must | Changes to live systems follow formal change management process |
| Test data security | Standard | Sensitive production data not used in test environments unless anonymized |
| Third-party system security | Standard | Security of third-party software and systems assessed |
| Security in DevOps | Standard | Security testing integrated into CI/CD pipelines |

### Evidence for Maturity Level 3

- Secure development policy or SDLC document
- Change management records for recent system changes
- Test data handling procedure
- Static/Dynamic Application Security Testing (SAST/DAST) results if applicable
- Third-party software security assessment records

---

## Chapter 11 — Supplier Relationships

**Objective:** Protect organizational information accessible to or processed by suppliers,
including TISAX-relevant supplier security assessments.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| IS policy for supplier relationships | Must | IS requirements addressed in agreements with all suppliers that handle CBI |
| Addressing IS within supplier agreements | Must | Contractual IS requirements; right to audit; incident notification obligations |
| Supplier IS monitoring | Standard | Supplier IS performance monitored throughout the relationship |
| Managing changes to supplier services | Standard | Changes by suppliers reviewed for IS impact |
| Cloud services | Must | Cloud services assessed; contractual obligations and data residency confirmed |
| TISAX flow-down | Must | Where supplier processes CBI on behalf of TISAX-certified company, requirements extended or supplier assessed |

### Evidence for Maturity Level 3

- Supplier IS policy / vendor management policy
- Supplier contract templates with IS clauses
- Critical supplier list with security assessment status
- Cloud services register with assessment evidence
- Supplier security questionnaire or audit records

---

## Chapter 12 — Incident Management

**Objective:** Ensure consistent and effective approach to the management of information
security incidents.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Responsibilities and procedures | Must | Documented incident response procedure with defined roles |
| Reporting IS events and weaknesses | Must | Process for employees to report IS incidents and suspicious activity |
| Assessment of IS events | Must | Events assessed against defined criteria to determine incident classification |
| Response to IS incidents | Must | Incidents responded to per documented procedure; containment, eradication, recovery |
| Learning from IS incidents | Standard | Root cause analysis and lessons-learned incorporated into procedures |
| Collection of evidence | Standard | Evidence preserved and documented in a forensically sound manner where needed |

### Evidence for Maturity Level 3

- Incident response plan/procedure
- Incident register (anonymized examples acceptable)
- Incident reporting channel (email alias, ticketing system)
- Post-incident review records for recent incidents
- Tabletop exercise completion records

---

## Chapter 13 — Business Continuity Management

**Objective:** Ensure information security continuity and availability of IT systems during
disruption events.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Planning IS continuity | Must | IS continuity requirements incorporated into BCM processes |
| Implementing IS continuity | Must | IS continuity procedures implemented and tested |
| IT service continuity | Must | RTO and RPO defined for critical IT systems; backup/recovery procedures in place |
| Redundancies | Standard | Redundant infrastructure for critical systems where required by recovery objectives |
| Backup and restore | Must | Regular backup of critical information; backups tested for restorability |
| Emergency access procedures | Standard | Emergency access to critical systems defined and tested |

### Evidence for Maturity Level 3

- Business Continuity Plan (BCP) and IT Disaster Recovery Plan (DRP)
- RTO/RPO register per system
- Backup procedure and recent backup test records
- BCP/DRP test exercise records (dated)

---

## Chapter 14 — Compliance

**Objective:** Avoid breaches of legal, statutory, regulatory, or contractual obligations
related to information security.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Identification of applicable legislation | Must | Inventory of applicable laws, regulations, and contractual obligations |
| Intellectual property rights | Standard | Procedures ensure compliance with IPR obligations |
| Protection of records | Standard | Records protected in line with legal and regulatory requirements |
| Privacy and protection of personal data | Must (if processing personal data) | GDPR or applicable data protection law requirements met |
| Review of IS independent of third parties | Standard | Independent reviews of IS implementation periodically conducted |
| Compliance with IS policies and standards | Must | Technical compliance with IS policies verified (automated or manual) |

### Evidence for Maturity Level 3

- Legal and regulatory inventory (laws, regulations, contracts applicable to IS)
- Data protection policy (if personal data processed)
- IS compliance review records (internal audit or self-assessment)
- Evidence of periodic management review

---

## Chapter 15 — Prototype and Test Vehicle Protection

**Objective (applies to Prototype and Strict Prototype labels only):** Ensure confidential
pre-release automotive prototypes are protected from unauthorized disclosure or photography.

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Prototype handling rules | Must | Rules for handling, storing, transporting, and working with prototype vehicles and components |
| Prototype identification and marking | Must | Prototypes marked/identified as confidential and tracking documented |
| Access control for prototypes | Must | Only authorized personnel access prototype vehicles; visitor controls enforced |
| Photography and media use | Must | Strict rules and physical controls preventing unauthorized photography of prototypes |
| Transport of prototypes | Must | Secure transport procedures including route approval, vehicle security, and driver briefing |
| Prototype area security (Strict) | Must for Strict label | Dedicated prototype areas with enhanced physical controls (no windows, shielded storage) |
| External prototype work (Strict) | Must for Strict label | External suppliers who work with prototypes meet equivalent Strict Prototype requirements |
| Destruction of prototype materials | Must | Decommissioned prototype parts and documents securely destroyed |
| Incident reporting for prototypes | Must | Prototype security incidents (e.g., unauthorized photography) promptly reported and investigated |

### Evidence for Maturity Level 3

- Prototype handling and protection procedure
- Prototype vehicle/component register
- Access log for prototype storage/workshop areas
- Photography control evidence (signs, camera blocking, NDAs)
- Transport security procedure and recent transport records
- Destruction records for prototype materials

---

## Chapter 16 — Data Protection

**Objective (applies to Data label only):** Ensure personal data is processed in accordance
with applicable data protection legislation, primarily the EU General Data Protection
Regulation (GDPR).

### Key Requirement Areas

| Req Area | Must? | Description |
|---------|-------|-------------|
| Legal basis for processing | Must | All personal data processing has a documented lawful basis under GDPR Art. 6 |
| Records of processing activities (ROPA) | Must | ROPA maintained per GDPR Art. 30 |
| Data subject rights | Must | Processes in place to handle DSAR, erasure, portability, rectification |
| Privacy notices | Must | Privacy notices provided to data subjects (employees, test drivers, customers) |
| Data protection officer | Must (if applicable) | DPO appointed where required; accessible and independent |
| Privacy by design and by default | Must | Privacy impact assessments conducted for new processing; default settings privacy-protective |
| Data processor agreements | Must | DPA (Data Processing Agreement) in place with all processors per GDPR Art. 28 |
| International data transfers | Must | Lawful mechanism in place for transfers outside EEA (SCCs, adequacy decision, etc.) |
| Data breach notification | Must | Procedure for 72-hour breach notification to supervisory authority; customer notification |

### Evidence for Maturity Level 3

- Records of Processing Activities (ROPA) document
- Privacy notices for relevant data subject groups
- DSAR handling procedure and example records
- Data Processing Agreements with processors
- DPIA (Data Protection Impact Assessment) for high-risk processing
- Breach notification procedure and test/exercise records
- DPO appointment (if required)
