# CMMC 2.0 - All 110 Practices (NIST SP 800-171 Rev 2 Mapped)

Level codes: **L1** = Level 1 (the 15 security requirements of FAR 52.204-21(b)(1)(i)–(xv), which map to the 17 L1-tagged 800-171 requirements below because one FAR item spans 3.10.3, 3.10.4, and 3.10.5) · **L2** = Level 2 (all 110) · **L3** = Level 3 (110 + SP 800-172 enhancements)

---

## AC - Access Control (22 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| AC.L1-3.1.1 | L1 | Limit system access to authorized users, processes acting on behalf of authorized users, and devices (including other systems). |
| AC.L1-3.1.2 | L1 | Limit system access to the types of transactions and functions authorized users are permitted to execute. |
| AC.L2-3.1.3 | L2 | Control the flow of CUI in accordance with approved authorizations. |
| AC.L2-3.1.4 | L2 | Separate the duties of individuals to reduce the risk of malevolent activity without collusion. |
| AC.L2-3.1.5 | L2 | Employ the principle of least privilege, including for specific security functions and privileged accounts. |
| AC.L2-3.1.6 | L2 | Use non-privileged accounts or roles when accessing non-security functions. |
| AC.L2-3.1.7 | L2 | Prevent non-privileged users from executing privileged functions and capture the execution in audit logs. |
| AC.L2-3.1.8 | L2 | Limit unsuccessful logon attempts. |
| AC.L2-3.1.9 | L2 | Provide privacy and security notices consistent with CUI rules. |
| AC.L2-3.1.10 | L2 | Use session lock with pattern-hiding displays after a period of inactivity. |
| AC.L2-3.1.11 | L2 | Terminate (automatically) a user session after a defined condition. |
| AC.L2-3.1.12 | L2 | Monitor and control remote access sessions. |
| AC.L2-3.1.13 | L2 | Employ cryptographic mechanisms to protect the confidentiality of remote access sessions. |
| AC.L2-3.1.14 | L2 | Route remote access via managed access control points. |
| AC.L2-3.1.15 | L2 | Authorize remote execution of privileged commands and access to security-relevant information via remote access only for documented operational needs. |
| AC.L2-3.1.16 | L2 | Authorize wireless access prior to allowing connections. |
| AC.L2-3.1.17 | L2 | Protect wireless access using authentication and encryption. |
| AC.L2-3.1.18 | L2 | Control connection of mobile devices. |
| AC.L2-3.1.19 | L2 | Encrypt CUI on mobile devices and mobile computing platforms. |
| AC.L1-3.1.20 | L1 | Verify and control/limit connections to external systems. |
| AC.L2-3.1.21 | L2 | Limit use of portable storage devices on external systems. |
| AC.L1-3.1.22 | L1 | Control CUI posted or processed on publicly accessible systems. |

---

## AT - Awareness and Training (3 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| AT.L2-3.2.1 | L2 | Ensure personnel are aware of the security risks associated with their activities and policies/procedures related to CUI. |
| AT.L2-3.2.2 | L2 | Ensure personnel are trained to carry out assigned security responsibilities. |
| AT.L2-3.2.3 | L2 | Provide security awareness training on recognizing and reporting potential indicators of insider threat. |

---

## AU - Audit and Accountability (9 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| AU.L2-3.3.1 | L2 | Create and retain system audit logs and records to enable monitoring, analysis, investigation, and reporting of unlawful or unauthorized activity. |
| AU.L2-3.3.2 | L2 | Ensure that the actions of individual users can be uniquely traced to those users. |
| AU.L2-3.3.3 | L2 | Review and update logged events. |
| AU.L2-3.3.4 | L2 | Alert in the event of an audit logging process failure. |
| AU.L2-3.3.5 | L2 | Correlate audit record review, analysis, and reporting processes. |
| AU.L2-3.3.6 | L2 | Provide audit record reduction and report generation to support analysis and reporting. |
| AU.L2-3.3.7 | L2 | Provide a system capability that compares and synchronizes internal clocks with authoritative sources. |
| AU.L2-3.3.8 | L2 | Protect audit information and tools from unauthorized access, modification, and deletion. |
| AU.L2-3.3.9 | L2 | Limit management of audit logging to a subset of privileged users. |

---

## CM - Configuration Management (9 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| CM.L2-3.4.1 | L2 | Establish and maintain baseline configurations and inventories of organizational systems (hardware, software, firmware, and documentation). |
| CM.L2-3.4.2 | L2 | Establish and enforce security configuration settings for IT products employed in systems. |
| CM.L2-3.4.3 | L2 | Track, review, approve, and log changes to systems. |
| CM.L2-3.4.4 | L2 | Analyze the security impact of changes prior to implementation. |
| CM.L2-3.4.5 | L2 | Define, document, approve, and enforce physical and logical access restrictions associated with changes. |
| CM.L2-3.4.6 | L2 | Employ the principle of least functionality by configuring systems to provide only essential capabilities. |
| CM.L2-3.4.7 | L2 | Restrict, disable, or prevent the use of nonessential programs, functions, ports, protocols, and services. |
| CM.L2-3.4.8 | L2 | Apply deny-by-exception (blacklisting) policy to prevent use of unauthorized software or deny-all, permit-by-exception (whitelisting). |
| CM.L2-3.4.9 | L2 | Control and monitor user-installed software. |

---

## IA - Identification and Authentication (11 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| IA.L1-3.5.1 | L1 | Identify system users, processes acting on behalf of users, and devices. |
| IA.L1-3.5.2 | L1 | Authenticate (or verify) the identities of users, processes, or devices before allowing access. |
| IA.L2-3.5.3 | L2 | Use multifactor authentication (MFA) for local and network access to privileged accounts and for network access to non-privileged accounts. |
| IA.L2-3.5.4 | L2 | Employ replay-resistant authentication mechanisms for network access. |
| IA.L2-3.5.5 | L2 | Employ identifier management to prevent reuse of identifiers for a defined period. |
| IA.L2-3.5.6 | L2 | Disable identifiers after a defined inactivity period. |
| IA.L2-3.5.7 | L2 | Enforce a minimum password complexity and change requirements. |
| IA.L2-3.5.8 | L2 | Prohibit password reuse for a specified number of generations. |
| IA.L2-3.5.9 | L2 | Allow temporary password use with immediate change requirement. |
| IA.L2-3.5.10 | L2 | Store and transmit only cryptographically-protected passwords (FIPS 140-2/3 validated). |
| IA.L2-3.5.11 | L2 | Obscure feedback of authentication information. |

---

## IR - Incident Response (3 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| IR.L2-3.6.1 | L2 | Establish an operational incident-handling capability including preparation, detection, analysis, containment, recovery, and user response activities. |
| IR.L2-3.6.2 | L2 | Track, document, and report incidents to designated officials and/or authorities both internal and external. |
| IR.L2-3.6.3 | L2 | Test the organizational incident response capability. |

---

## MA - Maintenance (6 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| MA.L2-3.7.1 | L2 | Perform maintenance on organizational systems. |
| MA.L2-3.7.2 | L2 | Provide controls on the tools, techniques, mechanisms, and personnel that conduct system maintenance. |
| MA.L2-3.7.3 | L2 | Ensure equipment removed for off-site maintenance is sanitized of CUI. |
| MA.L2-3.7.4 | L2 | Check media containing diagnostic and test programs for malicious code before the media are used. |
| MA.L2-3.7.5 | L2 | Require MFA to establish remote maintenance sessions and terminate sessions when maintenance is complete. |
| MA.L2-3.7.6 | L2 | Supervise the maintenance activities of personnel without required access authorization. |

---

## MP - Media Protection (9 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| MP.L1-3.8.3 | L1 | Sanitize or destroy system media before disposal or reuse. |
| MP.L2-3.8.1 | L2 | Protect (i.e., physically control and securely store) system media containing CUI, both paper and digital. |
| MP.L2-3.8.2 | L2 | Limit access to CUI on system media to authorized users. |
| MP.L2-3.8.4 | L2 | Mark media with necessary CUI markings and distribution limitations. |
| MP.L2-3.8.5 | L2 | Control access to media containing CUI and maintain accountability for media during transport. |
| MP.L2-3.8.6 | L2 | Implement cryptographic mechanisms to protect CUI during transport unless otherwise protected by alternative physical safeguards. |
| MP.L2-3.8.7 | L2 | Control the use of removable media on system components. |
| MP.L2-3.8.8 | L2 | Prohibit the use of portable storage devices when such devices have no identifiable owner. |
| MP.L2-3.8.9 | L2 | Protect the backups of CUI at storage locations. |

---

## PE - Physical Protection (6 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| PE.L1-3.10.1 | L1 | Limit physical access to systems to authorized individuals. |
| PE.L2-3.10.2 | L2 | Protect and monitor the physical facility and support infrastructure. |
| PE.L1-3.10.3 | L1 | Escort visitors and monitor visitor activity. |
| PE.L1-3.10.4 | L1 | Maintain audit logs of physical access. |
| PE.L1-3.10.5 | L1 | Control and manage physical access devices. |
| PE.L2-3.10.6 | L2 | Enforce safeguarding measures for CUI at alternate work sites. |

---

## PS - Personnel Security (2 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| PS.L2-3.9.1 | L2 | Screen individuals prior to authorizing access to systems containing CUI. |
| PS.L2-3.9.2 | L2 | Ensure CUI is protected during and after personnel actions such as terminations and transfers. |

---

## RA - Risk Assessment (3 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| RA.L2-3.11.1 | L2 | Periodically assess the risk to organizational operations, assets, and individuals from the operation of systems and associated CUI processing. |
| RA.L2-3.11.2 | L2 | Scan for vulnerabilities in organizational systems periodically and when new vulnerabilities affecting those systems are identified. |
| RA.L2-3.11.3 | L2 | Remediate vulnerabilities in accordance with risk assessments. |

---

## CA - Security Assessment (4 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| CA.L2-3.12.1 | L2 | Periodically assess the security controls in organizational systems to determine whether they are effective. |
| CA.L2-3.12.2 | L2 | Develop and implement plans of action designed to correct deficiencies and reduce or eliminate vulnerabilities. |
| CA.L2-3.12.3 | L2 | Monitor security controls on an ongoing basis to ensure the continued effectiveness. |
| CA.L2-3.12.4 | L2 | Develop, document, and periodically update system security plans (SSPs). |

---

## SC - System and Communications Protection (16 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| SC.L1-3.13.1 | L1 | Monitor, control, and protect communications at external boundaries and key internal boundaries. |
| SC.L1-3.13.5 | L1 | Implement subnetworks for publicly accessible system components. |
| SC.L2-3.13.2 | L2 | Employ architectural designs, software development techniques, and systems engineering principles that promote security. |
| SC.L2-3.13.3 | L2 | Separate user functionality from system management functionality. |
| SC.L2-3.13.4 | L2 | Prevent unauthorized and unintended information transfer via shared system resources. |
| SC.L2-3.13.6 | L2 | Deny network communications traffic by default and allow by exception (i.e., deny all, permit by exception). |
| SC.L2-3.13.7 | L2 | Prevent remote devices from simultaneously connecting to the system and to other resources (i.e., split tunneling). |
| SC.L2-3.13.8 | L2 | Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission (FIPS 140-2/3). |
| SC.L2-3.13.9 | L2 | Terminate network connections after a defined period of inactivity. |
| SC.L2-3.13.10 | L2 | Establish and manage cryptographic keys when cryptography is employed. |
| SC.L2-3.13.11 | L2 | Employ FIPS-validated cryptography when used to protect CUI. |
| SC.L2-3.13.12 | L2 | Prohibit remote activation of collaborative computing devices and provide indication of use to users present at the device. |
| SC.L2-3.13.13 | L2 | Control and monitor the use of mobile code. |
| SC.L2-3.13.14 | L2 | Control and monitor the use of VoIP technologies. |
| SC.L2-3.13.15 | L2 | Protect the authenticity of communications sessions. |
| SC.L2-3.13.16 | L2 | Protect CUI at rest. |

---

## SI - System and Information Integrity (7 practices)

| Practice ID | Level | Requirement |
|-------------|-------|-------------|
| SI.L1-3.14.1 | L1 | Identify, report, and correct information and system flaws in a timely manner. |
| SI.L1-3.14.2 | L1 | Provide protection from malicious code at appropriate locations within systems. |
| SI.L1-3.14.4 | L1 | Update malicious code protection mechanisms when new releases are available. |
| SI.L1-3.14.5 | L1 | Perform periodic scans of systems and real-time scans of files from external sources. |
| SI.L2-3.14.3 | L2 | Monitor system security alerts and advisories and take action in response. |
| SI.L2-3.14.6 | L2 | Monitor systems to detect attacks and indicators of potential attacks. |
| SI.L2-3.14.7 | L2 | Identify unauthorized use of systems. |
