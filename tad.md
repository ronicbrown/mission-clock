---
# ─────────────────────────────────────────────────────────────────────────────
# DOCUMENT METADATA
# ─────────────────────────────────────────────────────────────────────────────

classification: CUI   # Unclassified | CUI | Confidential | Secret | Top Secret | Top Secret//SCI
logo: docs/mission-clock-logo.png # relative path from repo root; remove line to omit logo

doc:
  title: Tenant Agreement
  platform: CARAVAN
  app: Mission-Clock
  version: v1.0.0
  owner:
    name: Roni Brown
    email: roni.c.brown.mil@army.mil


# ─────────────────────────────────────────────────────────────────────────────
# CHANGE LOG
# ─────────────────────────────────────────────────────────────────────────────

change:
  - date: 2026-08-04
    description: new markdown file for TAD
    author: 1LT Roni Brown


# ─────────────────────────────────────────────────────────────────────────────
# SECTIONS
#
# type: text       — body paragraph + optional note callout
# type: roles      — subsection per role with name, email, description bullet
# type: items      — preamble + subsections each with bullet list
# type: services   — baseline[] and on_request[] service groups
# type: table      — key/value attribute table
# type: signatures — signature blocks per entry
# ─────────────────────────────────────────────────────────────────────────────

sections:

  - title: Introduction
    type: text
    newpage: false
    body: >
      The purpose of this Tenant Agreement is to define the responsibilities
      and services provided by the Platform Name platform to the App Name
      application. Platform Name operates within the cARMY Azure environment
      at IL5, and its goal is to enable consistent and secure cloud onboarding
      of applications in support of the unit's mission. This agreement follows
      the Cloud Shared Responsibility Model, where Platform Name is responsible
      for "Security OF the Platform" and the App Name team is responsible for
      "Security IN the Platform."
    note: >
      This document will evolve over time as new services, capabilities, and
      responsibilities are introduced. This document is reviewed annually. Any
      revisions will result in updates being sent to all Tenant Owners for
      situational awareness.

  - title: Roles & Responsibilities
    type: roles
    newpage: true
    roles:
      - role: Authorizing Official (AO)
        name: SES Joseph Welch
        email: joseph.d.welch16.civ@army.mil
        description: >
          Ensures all appropriate RMF tasks are initiated and completed, with
          appropriate documentation, for assigned IS and Platform Information
          Technology (PIT) systems. Monitors and tracks overall execution of
          system-level Plans of Action & Milestones (POA&M) and promotes
          reciprocity.

      - role: Information System Owner (ISO)
        name: CPT Andrew R. Zeiss
        email: andrew.r.zeiss.mil@army.mil
        description: >
          Holds statutory, management, or operational authority for specific
          information to establish the policies and procedures governing its
          generation, collection, processing, dissemination, and disposal of
          the system.

      - role: Information System Security Manager (O-ISSM Primary)
        name: CW3 Victor Fernandez III
        email: victor.fernandez19.mil@army.mil
        description: >
          Serves as a principal advisor on all matters, technical and
          otherwise, involving the security of the platform system. Ensures
          physical and environmental protection, personnel security, incident
          handling, and security training and awareness are completed.

      - role: Information System Security Manager (O-ISSM Alternate)
        name: CW3 Carlos H. Gil
        email: carlos.h.gil.mil@army.mil
        description: >
          Serves as a principal advisor on all matters, technical and
          otherwise, involving the security of the platform system. Ensures
          physical and environmental protection, personnel security, incident
          handling, and security training and awareness are completed.

      - role: Information System Security Officer (ISSO)
        name: Geoffrey E. McCreary
        email: geoffrey.e.mccreary.ctr@army.mil
        description: >
          Responsible for maintaining the appropriate operational security
          posture for an IS or program.

      - role: System Administrator (SA)
        name: CW3 Justin Whitten
        email: justin.whitten.mil@army.mil
        description: >
          Responsible for applying technical functionality and security
          controls on the IS.

  - title: Tenant Responsibilities
    type: items
    newpage: true
    preamble: >
      Under the DevSecOps Standard Operating Procedure, the App Name team is
      responsible for the following duties as they iterate through Dev, Test,
      and Production environments:
    items:
      - title: Documentation & Framework Adherence
        items:
          - "Tenant Agreement (TA): Must be reviewed and signed prior to onboarding."
          - "Software Design Document (SDD): The Tenant must develop and maintain an SDD
            for every application. This document is a mandatory prerequisite for
            development inside cDSO."
          - "Maintain Document Accuracy: All required documentation for specified platform 
            must be reviewed and updated to ensure it is current. Inaccurate documentation
            will be returned by the Security Team during MR process for correction."
          - "cDSO Framework Usage: All building, testing, releasing, and deploying must
            occur within the approved cDSO framework. Bypassing this framework is not
            permitted."

      - title: Secure Development & Vulnerability Management
        items:
          - "Secure Practices: Identify and mitigate vulnerabilities during iterative
            development. Responsible for scanning their application code and remediating
            findings and vulnerabilities."
          - "Vulnerability Mitigation: Critical and CAT I findings must have mitigations
            and POA&M comments prepared. The comments should indicate the specific
            mitigations in place that lower the risk. Residual Risk should follow the
            NETCOM guidance for Risk Analysis if not fully remediated."

      - title: Continuous Monitoring & Reporting
        items:
          - "Post-Release Monitoring: Participation in continuous monitoring activities
            is required to ensure the application remains within risk thresholds after
            approval."
          - "Policy Reporting: Security concerns or abnormal activity must be reported
            immediately to the ISSM and Platform Team."

      - title: Backup Requirements
        items:
          - "Tenant teams are responsible for backup and recovery of their own application data."
          - "Backups must be verified monthly to ensure recoverability."

      - title: Account Lifecycle
        items:
          - "Notification of Change: Notify Platform Team immediately when an individual
            no longer requires access or when their need-to-know conditions change."
          - "Separation of Duties: The Tenant Owner is responsible for ensuring that
            personnel removal from application-level groups is reported to the platform
            team to trigger credential/key re-issuance."
          - "Shared Accounts: Permitted only under conditions defined in AC policy and
            documented in the SDD."

      - title: Offboarding
        items:
          - "Termination Procedures: Revoke all credentials and access immediately upon departure."
          - "Exit Requirements: The Tenant Owner is responsible for conducting security
            exit interviews that cover the return of assets and revocation of digital
            certificates."
          - "Post-Employment Acknowledgement: Departing personnel must be formally
            notified of, and acknowledge in writing, their ongoing requirements to
            protect organizational information."

      - title: Compliance Enforcement
        items:
          - "Consequences of Non-Compliance: Failure to adhere to these personnel and
            access security procedures — such as failing to report a departure — will
            result in a formal security review and potential suspension of the
            application's Authority to Connect (ATC)."

      # == Insert additional responsibility sections here ==

  - title: Services
    type: services
    newpage: true
    preamble: >
      Platform Name provides the foundational infrastructure and security
      controls required for the application team to operate within the Azure
      environment. All resources are provisioned via Infrastructure-as-Code
      (IaC) to ensure consistency and compliance with the DevSecOps SOP.
    baseline:
      preamble: >
        Every tenant is automatically provisioned with a standard environment
        suite designed to support the DevSecOps SOP requirements:
      services:
        - name: Compute
          description: >
            Platform manages the underlying container orchestration cluster.
            Tenant is assigned a dedicated isolated namespace for application
            workloads.
          items:
            - Dedicated namespace within the shared cluster
            - Resource quota enforcement per tenant

        - name: Networking
          description: Dedicated subnet within the platform Virtual Network.
          items:
            - Pre-configured firewall/security group rules to enforce traffic isolation
            - Standardized egress/ingress routing through the platform security stack

        - name: Identity & Access Management
          description: Centralized authentication and secrets management.
          items:
            - Integration with enterprise identity provider for centralized authentication
            - Dedicated secrets store for managing application-specific credentials and certificates

        - name: Monitoring & Logging
          description: >
            Centralized observability stack integrated with platform logging
            infrastructure.
          items:
            - Integration with platform monitoring tooling
            - Log retention in compliance with Army auditing requirements

        - name: Storage
          description: Standard object/file storage for general data persistence.
          items:
            - Object storage for general data persistence
            - Tenant responsible for configuring application-specific backup schedules

    on_request:
      preamble: >
        The following services are available but require coordination with the
        Platform Team to discuss requirements, scaling, and potential cost
        implications:
      services: []
        # == Insert on-request services here ==
        # - name: Service Name
        #   description: Description here.
        #   items:
        #     - Item one
        #     - Item two

  - title: Cloud Environment
    type: table
    newpage: true
    rows:
      - attribute: Cloud Provider
        value: Azure
      - attribute: Service Provider
        value: cARMY
      - attribute: Region
        value: Azure Gov
      - attribute: Impact Level
        value: IL5
      - attribute: emass record
        value: 5815
---