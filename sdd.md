---
organization: Artificial Intelligence Integration Center (AI2C)
software_name: Mission-Clock
software_version: v0.1.0
logo: docs/mission-clock-logo.png
classification: CUI
prepared_for:
  Organization: AI2C
  Name: CW3 Vic Fernandez III
  E-mail: victor.fernandez19.mil@army.mil
  Address: 6425 Living Place, Pittsburgh 15206
---
<!--
  NOTE: THIS MARKDOWN TEMPLATE IS NOT GITLAB FLAVORED, AND THUS WILL NOT RENDER CORRECTLY ON GITLAB IT IS DESIGNED TO BE RENDERED BY PANDOC INTO A PDF OR OTHER FORMAT. PLEASE REFER TO THE PANDOC DOCUMENTATION FOR MORE INFORMATION ON HOW TO DO THIS (https://pandoc.org/MANUAL.html#pandocs-markdown).
  THIS TEMPLATE IS DESIGNED TO BE USED WITH THE PANDOC CONTAINER IMAGE (https://code.code.cdso.army.mil/cdso/containers/tool/pandoc)
  THERE ARE PORTIONS OF THIS TEMPLATE THAT SERVE AS A FORM TO BE FILLED IN, AND OTHERS THAT ARE MEANT TO BE EDITED. PLEASE REFER TO THE COMMENTS IN THE TEMPLATE FOR MORE INFORMATION.
  THERE ARE ALSO PORTIONS THAT ARE FILLED OUT IN THEIR ENTIRETY AND ARE TARGETED FOR THE CDSO APPROVAL SYSTEM. DO NOT EDIT THESE UNLESS YOU HAVE A COMPELLING REASON TO OR ARE DEVIATING FROM THE CDSO PROCESS.
-->
<!--
 PORTION MARKINGS: You must use portion markings for all paragraphs and headers in this document. You must have specified the top-level classification of the SDD in the front-matter of this document (under the 'classification' key).
-->

## Classification Instruction
(U) Add the portion marking before each paragraph. This paragraph is marked as Unclassified, as denoted by the '(U)' at the beginning of this paragraph.

## Responsible Organization
(U) Who is the cognizant Authorizing Official (AO) for the organization?
Mr. Joseph Welch

(U) Is your system funded by Title 10 or Title 50?
| Title 10 | Title 50 |
| -------- | -------- |
| x        |          |

### Points of Contact
<!-- Refer to https://pandoc.org/MANUAL.html#tables for allowed table formats -->
<!-- We've provided the table below, but you can choose to provide this information in another format -->
<!-- At a minimum, you should provide a ISO/PM and an ISMM, but may also include a ISSOs -->
<!-- At a minimum, you should provide a Mission Owner, Mission Owner AO, ISO/PM and an ISMM, but may also include a ISSOs -->
<!-- Indicate whether your application is under Title 10 or Title 50 with an X in the appropriate section -->

| Name                     | Role                                | Phone Number   | Email                           |
| ------------------------ | ----------------------------------- | -------------- | ------------------------------- |
| MAJ Brian Schramke       | Mission Owner                       | (978) 654-3210 | brian.a.schramke.mil@army.mil   |
| CPT Andrew Zeiss         | Information System Owner            | (978) 654-3210 | andrew.r.zeiss.mil@army.mil    |
| CW3 Victor Fernandez III | Information System Security Manager | (978) 654-3210 | victor.fernandez19.mil@army.mil |
| CW2 Brian Pak            | Information System Security Officer | (978) 654-3210 | brian.y.pak.mil@army.mil   |

```{=latex}
\newpage
```

## cDSO Container Technology Pipeline Process
(U) The cDSO is a low cost, secure, flexible, and enterprise-wide containerized application development pipeline. Using the cDSO improves the quality and timeliness of the Risk Management Framework (RMF) process. It distributes the responsibility for security while enabling developers at all levels and organizations to develop and secure containerized applications with unmatched agility.

### Process
a. (U) System Owner completes CSDD and BoE with Cybersecurity Office assistance
b. (U) Cybersecurity Office POC reviews BoE and sends it to ISSM.
c. (U) ISSM reviews BoE and sends it to SCA-V or returns for rework.
d. (U) SCA-V reviews BoE and signs approval or returns for rework.
e. (U) ISSM signs approval. ISSM enters approval in the GitLab Merge Request.
f. (U) SCA-V enters approval in the GitLab Merge Request and Merges the CSDD.
g. (U) Container Software/Pipeline can now be installed, and BoE is incorporated into System BoE

```{=latex}
\newpage
```

## Software Overview

### Purpose
(U) Mission-Clock provides a centralized, synchronized web-based timing and countdown application used to coordinate operational activities, track mission execution phases, and provide a unified time reference (e.g., H-Hour, L-Hour) across distributed teams. Designed for AI2C and associated expeditionary forces, Mission-Clock ensures all operators share a common operating picture regarding time-sensitive mission milestones.

### Intended Users
a. (U) Administrators: Responsible for configuring mission phases, global time offsets, and managing active clocks.
b. (U) Users: Operators and analysts viewing the synchronized operational timelines and countdowns.

### Identification
Clearly identify the type of software/pipeline to be used, all organizations that will use the software/pipeline, and the networks/domains on which the software/pipeline will be deployed

```{=tex}
\begin{center}
\begin{tabular}{|c|c|}
\hline
\textbf{Software Name} & Mission-Clock \\
\hline
\textbf{Version}   & v0.1.0 \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 &\textbf{Software Type}  \\
\hline
 & Commercial Off-the-Shelf (COTS)  \\
\hline
X & Government Off-the-Shelf (GOTS)  \\
\hline
 & Free and Open Source Software (FOSS)  \\
\hline
 & Contract-Developed / Modified Off-the-Shelf (MOTS)  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 &\textbf{Architecture}  \\
\hline
 & Installed on Desktop  \\
\hline
X & Application Server with Database  \\
\hline
 & Application Server with Persistent Storage  \\
\hline
\end{tabular}

% NOTE: Please specify as narrowly as possible the organization/group your users are a part in the table below
\begin{tabular}{|c|c|}
\hline
 &\textbf{Users of the Software}  \\
\hline
X & U.S. Army Cyber Command  \\
\hline
 & U.S. Army Cyber Command and other DoD organizations  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 &\textbf{Networks} \\
\hline
 & JWICS  \\
\hline
 & SIPRNET  \\
\hline
X & NIPRNET  \\
\hline
 & STEMSNET  \\
\hline
 & Stand-Alone (Name: )  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 &\textbf{Privacy Act Data} \\
\hline
X & "Business" or "Rolodex" PII  \\
\hline
 & PII  \\
\hline
 & PHI  \\
\hline
\end{tabular}
\end{center}
```

```{=latex}
\newpage
```

## Security Overview

### System Categorization
(U) Security Categorization is the first step in the Risk Management Framework (RMF) and paramount because of its effect on all other steps in the framework, from selection of security controls to the level of effort required in assessing security control effectiveness. The Security Categorization will generally be determined based on the most sensitive or critical information collected by, consumed by, received by, processed in, stored in, and/or generated by the system/application.

**Security categorization of the system that is the consumer of this pipeline**:

**Confidentiality**
- [x] LOW
- [ ] MODERATE
- [ ] HIGH

**Integrity**
- [ ] LOW
- [x] MODERATE
- [ ] HIGH

**Availability**
- [ ] LOW
- [x] MODERATE
- [ ] HIGH

*(Note: Integrity and Availability marked as MODERATE due to the operational reliance on accurate, synchronized timing).*

```{=tex}
\begin{center}
\begin{tabular}{|c|c|}
\hline
 &\textbf{Anticipated Domain(s)} (CUI when filled out) \\
\hline
X & Unclass (IL2) (DEV)   \\
\hline
X & NIPRNet (IL5) (TEST, PROD)  \\
\hline
 & SIPRNet (DEV, TEST, PROD)  \\
\hline
 & JWICS (DEV, TEST, PROD)  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 &\textbf{Anticipated Dissemination Controls (SIPR)} (CUI when filled out) \\
\hline
 & NOFORN   \\
\hline
 & FRD  \\
\hline
 & NATO  \\
\hline
 & ORCON  \\
\hline
 & PROPIN  \\
\hline
 & RESEN  \\
\hline
 & REL TO USA, AUS, CAN, GBR  \\
\hline
 & REL TO USA, AUS, CAN, GBR, NZL  \\
\hline
 & Other: (Please specify)  \\
\hline
\end{tabular}

\begin{tabular}{|c|c|}
\hline
 &\textbf{Anticipated Dissemination Controls (JWICS)} (CUI when filled out) \\
\hline
 & SI-G   \\
\hline
 & TK  \\
\hline
 & HCS-P  \\
\hline
 & COMINT  \\
\hline
 & MASINT  \\
\hline
 & NATO  \\
\hline
 & REL TO USA, AUS, CAN, GBR \\
\hline
 & REL TO USA, AUS, CAN, GBR, NZL  \\
\hline
 & COMSEC  \\
\hline
 & Other: (Please specify)  \\
\hline
\end{tabular}
\end{center}
```

```{=latex}
\newpage
```

### Architecture Diagram
(U) The Mission-Clock architecture utilizes a microservices approach deployed via UDS Core and Zarf on an Azure Kubernetes Service (AKS) cluster. The frontend communicates with the backend API to fetch current clock states and mission milestones.

![Architecture Diagram](docs/architecture-diagram.png)

```{=latex}
\newpage
```

## Detailed Software Description

### Software Purpose / Goals
(U) The goal of Mission-Clock is to replace disparate, decentralized timing mechanisms with a single, authoritative, and synchronized web application. By ensuring all echelons and operational cells are viewing the exact same countdown timers and event milestones, the software mitigates the risk of misaligned operations and execution delays.

### Software Functionality
(U) Mission-Clock provides real-time, synchronized clocks displaying UTC, Local, and user-defined operational time zones. It allows administrators to create "Mission Events" (e.g., H-Hour) and dynamically generates count-up or count-down displays that update concurrently across all connected client browsers via WebSocket or polling mechanisms.

### Software Components
(U) **Frontend Container:** A web-based Graphical User Interface (GUI) that renders the clocks, dashboards, and event timelines. Hosted behind the UDS Core ingress controller.
(U) **Backend Container:** A RESTful/WebSocket API service that maintains the authoritative time state, manages database connections, and broadcasts updates to connected frontends.
(U) **Database:** A backend persistent storage component (e.g., PostgreSQL) used to store configured missions, user roles, and historical milestone data.
(U) **UDS Core Integration:** Handles Identity Management (SSO) and Network ingress routing.

### User Interface
(U) The User Interface is a browser-based Graphical User Interface (GUI). Upon accessing the URL, users are redirected to the UDS Core SSO gateway to authenticate via PKI/CAC. Once authenticated, users view a dark-themed dashboard featuring large digital clock faces and sequential mission event progress bars.

### Configuration Management
(U) Configurations are managed using Kubernetes ConfigMaps and Secrets deployed via the application's `uds-bundle.yaml` and `zarf.yaml` definitions. Environment variables are passed into the backend and frontend containers at runtime. Upgrades and configuration rollbacks are performed via GitOps pipelines in GitLab.

### Development and Testing
(U) Development utilizes a DevSecOps approach on the AI2C GitLab platform. Features are developed on isolated branches, merged to `main`, and deployed via tag-based pipelines. Automated testing includes static application security testing (SAST), software composition analysis (SCA) via Syft/Grype, and secrets scanning via TruffleHog.

#### Milestones
(U) Milestones are measured via Semantic Versioning (SemVer) tags and Git feature completion. Success is defined by the successful integration of the frontend/backend components into the Expedition 0 AKS environment with zero critical security findings.

#### Failure Conditions & Mitigations
(U) **Failure Condition:** Loss of network connectivity to the backend clock service causing desynchronization.
(U) **Mitigation:** The frontend UI includes logic to detect lost API heartbeats and visually warn the user that the displayed time is "Stale/Offline," preventing operators from acting on inaccurate timings.

```{=latex}
\newpage
```

## Technical Overview

### Networking Capabilities
(U) The application runs entirely within the Expedition 0 Azure Kubernetes Service (AKS) environment. It relies on UDS Core for external ingress via an Istio Gateway and requires internal East-West traffic allowances between the frontend pod, backend pod, and database.

### Ports / Protocol / Services
(U) **HTTPS (TCP 443):** End-user web traffic routed via UDS Core Ingress.
(U) **HTTP (TCP 8080):** Internal container traffic between the Ingress controller and the Frontend service.
(U) **Custom API Port (TCP 3000/5000):** Internal communication between the Frontend container and Backend container.
(U) **Database Port (TCP 5432):** Internal communication between the Backend container and the database.

### Encryption
(U) **Data in Transit:** Encrypted via TLS 1.2+ using UDS Core's Istio mutual TLS (mTLS) for intra-cluster traffic, and standard HTTPS/TLS for external client-to-cluster traffic.
(U) **Data at Rest:** Transparently encrypted by the underlying Expedition 0 platform storage classes.

### Authentication
(U) The application delegates authentication to the UDS Core SSO component. Users are authenticated using enterprise PKI/CAC via an OIDC/SAML flow before traffic is permitted to reach the frontend service.

### Operating System
(U) The software is containerized using DoD Iron Bank hardened base images (e.g., Red Hat Universal Base Image - UBI 8/9). It runs on standard Linux architecture (x86_64) within the Azure Kubernetes environment.

### Role-Based Access Control (RBAC)
(U) UDS Core Authservice enforces coarse-grained access. Fine-grained RBAC (e.g., distinguishing between an "Admin" who can edit the clock and a "Viewer" who can only read the clock) is handled programmatically within the backend API logic based on claims provided in the SSO JWT token.

<!-- START: DO NOT EDIT -->
### Audit Capabilities
This application uses the Continuous Integration (CI) services provided through Community DevSecOps (CDSO), which is an inner-sourced CI solution provided for use within the Department of the Army. The pipelines provided by CDSO are all open and auditable for anybody within the department of the Army. The source code for all components can be found here: https://code.code.cdso.army.mil/cdso. The documentation can be found here: https://cdso.pages.code.cdso.army.mil/.

### Dependencies
This application's dependencies can be viewed by looking at the pipeline artifacts for the most recent CI iteration under the `syft-grype` job artifacts.
This job produces a `syft.json` artifact which contains the Software Bill of Materials (SBOM) for the application image.

### Assumptions
List any assumptions made during the design of this application. This could include assumptions about the network or operating environment, assumptions about the end-user, etc.
```{=latex}
\newpage
```

## Constraints
(U) The application must operate strictly within the IL5 unclassified environment bounds and cannot process classified mission timings. Deployments must occur exclusively via authorized Git tags.

### Scanning Tools & Remediation
This application uses all of the scanning tools as defined in the `application-security-review` Pipeline from CDSO. You can find details about the pipeline and its tools here: https://cdso.pages.code.cdso.army.mil/components/pipelines/#application-security-reviewyml .
Its definition can be found here: https://code.code.cdso.army.mil/cdso/cdso/-/blob/main/pipelines/application-security-review.yml.
<!-- END: DO NOT EDIT -->

### Security Technical Implementation Guides (STIGs)
(U) The application inherits compliance from the DoD Container Base Image STIG. Application-level code follows the Application Security and Development (ASD) STIG.

```{=latex}
\newpage
```

# Appendix A -- References
(U) Defense Unicorns UDS Core Documentation (https://docs.defenseunicorns.com/)
(U) Zarf Declarative Packaging (https://zarf.dev/)
(U) AI2C Caravan Deployment Guide

```{=latex}
\newpage
```

# Appendix B -- Acronyms
Make sure to add any acronyms used in this CSDD that are pertinent to your organization and application/pipeline.

| Acronym | Definition                                     |
| ------- | ---------------------------------------------- |
| CDSO    | Community DevSecOps                            |
| CI / CD | Continuous Integration / Continuous Deployment |
| UDS     | Unicorn Delivery Service                       |
| AKS     | Azure Kubernetes Service                       |
| RBAC    | Role-Based Access Control                      |
| SSO     | Single Sign-On                                 |

```{=latex}
\newpage
```

## SRG (Security Requirements Guide)
(U) Cloud Computing SRG
(U) Application Security SRG
```