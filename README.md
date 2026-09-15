## 7. Prepare and Deploy the Application

The Cookiecutter template creates the application source code and environment-specific pipeline configuration under the `app/` directory.

For this guide, the repository will use the following structure:

```text
my-cool-app/
├── .gitlab-ci.yml
├── app/
└── deploy/
```

The directories have separate purposes:

```text
app/       Application source code and local development configuration
deploy/    Helm, Zarf, and UDS deployment configuration
```

Expedition 0 deployments use GitLab pipelines and Infrastructure-as-Code to build, scan, authorize, package, and deploy the application.

---

### 7.1 Review the Current Repository Structure

Return to the repository root:

```bash
cd ~/my-cool-app
```

View the current structure:

```bash
tree -a -L 4
```

Before adding the deployment files, the repository should resemble:

```text
my-cool-app/
└── app/
    ├── .env
    ├── .gitignore
    ├── .gitlab-ci.yml
    ├── .gitlab/
    │   ├── expedition-0/
    │   │   ├── dev/
    │   │   ├── test/
    │   │   └── prod/
    │   └── oasis/
    │       ├── dev/
    │       ├── test/
    │       └── prod/
    ├── Makefile
    ├── README.md
    ├── backend/
    ├── compose.yml
    ├── database/
    ├── docs/
    └── frontend/
```

The Cookiecutter template already provides environment-specific pipeline and cDSO configuration files.

Do not recreate those files from scratch.

---

### 7.2 Move the Main GitLab Pipeline and Update Pipeline Paths

The Cookiecutter template creates the primary `.gitlab-ci.yml` inside the `app/` directory.

For this guide, move the primary pipeline to the repository root:

```bash
cd ~/my-cool-app

mv app/.gitlab-ci.yml .gitlab-ci.yml
```

Because the environment-specific pipelines remain under:

```text
app/.gitlab/
```

their generated paths must also be updated.

Run:

```bash
sed -i 's|include: \.gitlab/|include: app/.gitlab/|g' .gitlab-ci.yml && \
find app/.gitlab -type f -name ".gitlab-ci.yml" -exec \
sed -i 's|cdso_config_path: \.gitlab/|cdso_config_path: app/.gitlab/|g' {} +
```

This changes the parent pipeline from:

```yaml
include: .gitlab/$PLATFORM_DIR/$ENVIRONMENT/.gitlab-ci.yml
```

to:

```yaml
include: app/.gitlab/$PLATFORM_DIR/$ENVIRONMENT/.gitlab-ci.yml
```

It also changes child-pipeline references such as:

```yaml
cdso_config_path: .gitlab/expedition-0/dev/cdso_config.yml
```

to:

```yaml
cdso_config_path: app/.gitlab/expedition-0/dev/cdso_config.yml
```

The command applies to the generated pipelines under:

```text
app/.gitlab/expedition-0/dev/
app/.gitlab/expedition-0/test/
app/.gitlab/expedition-0/prod/

app/.gitlab/oasis/dev/
app/.gitlab/oasis/test/
app/.gitlab/oasis/prod/
```

Verify the parent pipeline:

```bash
grep -n "include:" .gitlab-ci.yml
```

Verify all child-pipeline paths:

```bash
grep -R "cdso_config_path:" app/.gitlab
```

Every returned path should begin with:

```text
app/.gitlab/
```

> **Screenshot:** WSL terminal showing the updated parent pipeline and child pipeline paths.

![Updated Pipeline Paths](photos/update-pipeline-paths.png)

---

### 7.3 Add the Deployment Task Selector

Open:

```text
.gitlab-ci.yml
```

Add the following variable under the existing `variables:` section:

```yaml
UDS_BUNDLE_TASK:
  description: "What do you want to do with the UDS bundle?"
  options:
    - nothing
    - deploy
    - remove
  value: nothing
```

The beginning of the file should resemble:

```yaml
variables:
  PLATFORM:
    description: "Which PLATFORM do you want to target?"
    options:
      - "Expedition 0"
      - "Oasis"
    value: "Expedition 0"

  UDS_BUNDLE_TASK:
    description: "What do you want to do with the UDS bundle?"
    options:
      - nothing
      - deploy
      - remove
    value: nothing
```

Use:

```text
nothing
```

for the normal build, scan, and delivery process.

Use:

```text
deploy
```

when an approved application version is ready to deploy.

Use:

```text
remove
```

when a deployed application must be removed.

---

### 7.4 Update the cDSO Configuration Paths

Open:

```text
app/.gitlab/expedition-0/dev/cdso_config.yml
```

Because the application source remains under `app/`, update the Dockerfile paths.

Change:

```yaml
dockerfile_folder: backend
```

to:

```yaml
dockerfile_folder: app/backend
```

Change:

```yaml
dockerfile_folder: frontend
```

to:

```yaml
dockerfile_folder: app/frontend
```

The development configuration should resemble:

```yaml
organization: expedition-0
security_group: ai2c
deployment_level: DEVELOPMENT

backend:
  project_type: container
  dockerfile_folder: app/backend
  container_lifespan: PERSISTENT
  connection_context: INTERNAL

  zap:
    service_ports:
      - 5432
    gitlab_services:
      - name: registry.cdso.army.mil/ai2c/postgresql/database:548010
        alias: database
    scanned_image_variables:
      DB_HOST: database
      DB_NAME: postgres
      DB_USER: postgres
      DB_PASS: postgres
      DB_PORT: "5432"

frontend:
  project_type: container
  dockerfile_folder: app/frontend
  container_lifespan: PERSISTENT
  connection_context: EXTERNAL
```

The PostgreSQL service under `zap` is used during backend security scanning. It does not by itself define the application's deployed runtime database.

---

### 7.5 Create the Deployment Directory

Return to the repository root:

```bash
cd ~/my-cool-app
```

Create the deployment directories:

```bash
mkdir -p deploy/uds
mkdir -p deploy/zarf/helm/backend/templates
mkdir -p deploy/zarf/helm/frontend/templates
mkdir -p deploy/zarf/helm/package/templates
```

Create the initial files:

```bash
touch deploy/uds/uds-bundle.yaml

touch deploy/zarf/zarf.yaml

touch deploy/zarf/helm/backend/Chart.yaml
touch deploy/zarf/helm/backend/values.yaml
touch deploy/zarf/helm/backend/templates/deployment.yaml
touch deploy/zarf/helm/backend/templates/service.yaml

touch deploy/zarf/helm/frontend/Chart.yaml
touch deploy/zarf/helm/frontend/values.yaml
touch deploy/zarf/helm/frontend/templates/deployment.yaml
touch deploy/zarf/helm/frontend/templates/service.yaml

touch deploy/zarf/helm/package/Chart.yaml
touch deploy/zarf/helm/package/values.yaml
touch deploy/zarf/helm/package/templates/uds-package.yaml
```

The repository should now resemble:

```text
my-cool-app/
├── .gitlab-ci.yml
│
├── app/
│   ├── .env
│   ├── .gitignore
│   ├── .gitlab/
│   ├── Makefile
│   ├── README.md
│   ├── backend/
│   ├── compose.yml
│   ├── database/
│   ├── docs/
│   └── frontend/
│
└── deploy/
    ├── uds/
    │   └── uds-bundle.yaml
    │
    └── zarf/
        ├── zarf.yaml
        └── helm/
            ├── backend/
            │   ├── Chart.yaml
            │   ├── values.yaml
            │   └── templates/
            │       ├── deployment.yaml
            │       └── service.yaml
            │
            ├── frontend/
            │   ├── Chart.yaml
            │   ├── values.yaml
            │   └── templates/
            │       ├── deployment.yaml
            │       └── service.yaml
            │
            └── package/
                ├── Chart.yaml
                ├── values.yaml
                └── templates/
                    └── uds-package.yaml
```

A Helm application component should contain at minimum a Deployment and Service. The recommended structure also includes `Chart.yaml` and `values.yaml`.

> **Screenshot:** Visual Studio Code showing `app/` and `deploy/` as sibling directories.

![Application and Deployment Structure](photos/app-deploy-structure.png)

---

### 7.6 Add the Application Deployment Entry

Open:

```text
app/.gitlab/expedition-0/dev/cdso_config.yml
```

Add an application-level entry:

```yaml
my-cool-app:
  project_type: sdd
  zarf_directory: deploy/zarf
  uds_directory: deploy/uds
```

The complete development configuration should now resemble:

```yaml
organization: expedition-0
security_group: ai2c
deployment_level: DEVELOPMENT

my-cool-app:
  project_type: sdd
  zarf_directory: deploy/zarf
  uds_directory: deploy/uds

backend:
  project_type: container
  dockerfile_folder: app/backend
  container_lifespan: PERSISTENT
  connection_context: INTERNAL

  zap:
    service_ports:
      - 5432
    gitlab_services:
      - name: registry.cdso.army.mil/ai2c/postgresql/database:548010
        alias: database
    scanned_image_variables:
      DB_HOST: database
      DB_NAME: postgres
      DB_USER: postgres
      DB_PASS: postgres
      DB_PORT: "5432"

frontend:
  project_type: container
  dockerfile_folder: app/frontend
  container_lifespan: PERSISTENT
  connection_context: EXTERNAL
```

`zarf_directory` identifies the directory containing the application's `zarf.yaml`.

`uds_directory` identifies the directory containing the application's UDS bundle.

---

### 7.7 Configure the Backend Helm Chart

Open:

```text
deploy/zarf/helm/backend/Chart.yaml
```

Add:

```yaml
apiVersion: v2
name: my-cool-app-backend
description: Backend Helm chart for My Cool App
type: application
version: 0.0.1
appVersion: "0.0.1"
```

Open:

```text
deploy/zarf/helm/backend/values.yaml
```

The previous Expedition 0 deployment example uses an image naming pattern similar to:

```text
cazcaravandecoreacr.azurecr.us/ai2c/caravan/<application>/<component>:<version>
```

For example, the previous deployment documentation shows:

```text
cazcaravandecoreacr.azurecr.us/ai2c/caravan/app/backend:v0.0.1
```

for a backend container.

For My Cool App, use the expected repository pattern:

```yaml
replicaCount: 1

image:
  repository: cazcaravandecoreacr.azurecr.us/ai2c/caravan/my-cool-app/backend
  tag: v0.0.1
  pullPolicy: IfNotPresent

service:
  port: 8000
```

> **Important:** This repository follows the naming convention shown in the Expedition 0 example. The exact image location will be verified later using the application's successful `deliver` job before deployment.

Open:

```text
deploy/zarf/helm/backend/templates/deployment.yaml
```

Add:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: my-cool-app-backend

spec:
  replicas: {{ .Values.replicaCount }}

  selector:
    matchLabels:
      app: my-cool-app-backend

  template:
    metadata:
      labels:
        app: my-cool-app-backend

    spec:
      containers:
        - name: backend
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}

          ports:
            - containerPort: 8000
```

Open:

```text
deploy/zarf/helm/backend/templates/service.yaml
```

Add:

```yaml
apiVersion: v1
kind: Service

metadata:
  name: my-cool-app-backend-service

spec:
  selector:
    app: my-cool-app-backend

  ports:
    - port: 8000
      targetPort: 8000
```

---

### 7.8 Configure the Frontend Helm Chart

Open:

```text
deploy/zarf/helm/frontend/Chart.yaml
```

Add:

```yaml
apiVersion: v2
name: my-cool-app-frontend
description: Frontend Helm chart for My Cool App
type: application
version: 0.0.1
appVersion: "0.0.1"
```

Open:

```text
deploy/zarf/helm/frontend/values.yaml
```

Add:

```yaml
replicaCount: 1

image:
  repository: cazcaravandecoreacr.azurecr.us/ai2c/caravan/my-cool-app/frontend
  tag: v0.0.1
  pullPolicy: IfNotPresent

service:
  port: 80
```

The exact frontend image repository will also be verified after the tagged delivery pipeline runs.

Open:

```text
deploy/zarf/helm/frontend/templates/deployment.yaml
```

Add:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: my-cool-app-frontend

spec:
  replicas: {{ .Values.replicaCount }}

  selector:
    matchLabels:
      app: my-cool-app-frontend

  template:
    metadata:
      labels:
        app: my-cool-app-frontend

    spec:
      containers:
        - name: frontend
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}

          ports:
            - containerPort: 80
```

Open:

```text
deploy/zarf/helm/frontend/templates/service.yaml
```

Add:

```yaml
apiVersion: v1
kind: Service

metadata:
  name: my-cool-app-frontend-service

spec:
  selector:
    app: my-cool-app-frontend

  ports:
    - port: 80
      targetPort: 80
```

---

### 7.9 Configure the Runtime Database

The local application uses the PostgreSQL container located under:

```text
app/database/
```

This database is started locally through Docker Compose.

The PostgreSQL service configured under the cDSO `zap` configuration is used during security scanning and should not automatically be treated as the deployed production database.

Before deploying the application, determine which approved PostgreSQL option is used by the target Expedition 0 environment.

The backend requires:

```text
DB_HOST
DB_NAME
DB_USER
DB_PASS
DB_PORT
```

Do not hard-code production database credentials into Git.

The provided deployment documentation does not define the runtime PostgreSQL configuration for this specific Cookiecutter application, so this guide does not invent one.

---

### 7.10 Create the UDS Package Helm Chart

Open:

```text
deploy/zarf/helm/package/Chart.yaml
```

Add:

```yaml
apiVersion: v2
name: my-cool-app-package
description: UDS Package configuration for My Cool App
type: application
version: 0.0.1
appVersion: "0.0.1"
```

The `values.yaml` file may remain empty until reusable package values are required.

Open:

```text
deploy/zarf/helm/package/templates/uds-package.yaml
```

Add:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/defenseunicorns/uds-core/refs/heads/main/schemas/package-v1alpha1.schema.json

apiVersion: uds.dev/v1alpha1
kind: Package

metadata:
  name: my-cool-app-package
  namespace: my-cool-app

spec:
  network:
    expose:
      - service: my-cool-app-frontend-service
        selector:
          app: my-cool-app-frontend
        host: my-cool-app
        port: 80

    allow:
      - description: "Allow egress communication between pods within this namespace."
        direction: Egress
        remoteGenerated: IntraNamespace

      - description: "Allow ingress communication between pods within this namespace."
        direction: Ingress
        remoteGenerated: IntraNamespace
```

The UDS Package defines runtime configuration such as networking and can also contain SSO configuration when required.

The preferred method is to include the UDS Package inside the Zarf package so that it is deployed and removed with the application.

---

### 7.11 Create the Zarf Package

Open:

```text
deploy/zarf/zarf.yaml
```

Add:

```yaml
kind: ZarfPackageConfig

metadata:
  name: my-cool-app-zarf
  version: v0.0.1

components:
  - name: my-cool-app-backend
    required: true

    charts:
      - name: my-cool-app-backend
        namespace: my-cool-app
        version: v0.0.1
        localPath: helm/backend
        valuesFiles:
          - helm/backend/values.yaml

  - name: my-cool-app-frontend
    required: true

    charts:
      - name: my-cool-app-frontend
        namespace: my-cool-app
        version: v0.0.1
        localPath: helm/frontend
        valuesFiles:
          - helm/frontend/values.yaml

  - name: my-cool-app-package
    required: true

    charts:
      - name: my-cool-app-package
        namespace: my-cool-app
        version: v0.0.1
        localPath: helm/package
        valuesFiles:
          - helm/package/values.yaml
```

For Expedition 0, the deployment guidance notes that the cluster's Zarf initialization is already configured with the Expedition 0 ACR. Images may therefore be referenced through the Helm configuration.

For a fully self-contained air-gapped package, an `images:` block would still be required.

---

### 7.12 Create the UDS Bundle

Open:

```text
deploy/uds/uds-bundle.yaml
```

The UDS bundle must reference the Zarf package created for My Cool App.

The previous Expedition 0 documentation confirms that the UDS bundle is what is ultimately deployed to the AKS cluster and that it references the application's Zarf package.

Use the current AI2C deployment template as the source for the exact `uds-bundle.yaml` structure and update the application package name and version to:

```text
my-cool-app-zarf
v0.0.1
```

> **Important:** Do not copy a registry or package URL from another application. The final package reference must match the artifact delivered by the My Cool App pipeline.

---

### 7.13 Add Deploy and Remove Pipeline Components

Open:

```text
app/.gitlab/expedition-0/dev/.gitlab-ci.yml
```

Add the deployment stages:

```yaml
stages:
  - pre-build
  - pre-test
  - build
  - post-build
  - post-test
  - review
  - clean
  - deliver
  - deploy
  - remove
```

For the existing review and delivery components, add:

```yaml
rules:
  - if: |
      $UDS_BUNDLE_TASK != "deploy" &&
      $UDS_BUNDLE_TASK != "remove"
```

This prevents normal container review and delivery jobs from running when the user explicitly requests a deployment or removal.

Add the application deployment component:

```yaml
- component: $CI_SERVER_FQDN/ai2c/caravan/pipelines/deploy@main

  rules:
    - if: '$UDS_BUNDLE_TASK == "deploy"'

  inputs:
    name: my-cool-app-deploy
    pipeline_type: bundle
    expedition: 0
    environment: dev
    cdso_config_path: app/.gitlab/expedition-0/dev/cdso_config.yml
```

Add the removal component:

```yaml
- component: $CI_SERVER_FQDN/ai2c/caravan/pipelines/remove@main

  rules:
    - if: '$UDS_BUNDLE_TASK == "remove"'

  inputs:
    name: my-cool-app-deploy
    pipeline_type: bundle
    expedition: 0
    environment: dev
    cdso_config_path: app/.gitlab/expedition-0/dev/cdso_config.yml
```

The Expedition 0 guidance requires review and delivery components for each deployable container and one deploy/remove pair for the application bundle.

---

### 7.14 Repeat the Configuration for Test and Production

The Cookiecutter also provides:

```text
app/.gitlab/expedition-0/test/
app/.gitlab/expedition-0/prod/
```

Use the same structure while changing environment-specific values.

The deployment levels are:

```text
dev  → DEVELOPMENT
test → TEST
prod → PRODUCTION
```

The corresponding configuration paths are:

```text
app/.gitlab/expedition-0/dev/cdso_config.yml
app/.gitlab/expedition-0/test/cdso_config.yml
app/.gitlab/expedition-0/prod/cdso_config.yml
```

Do not copy development-only settings directly into production without reviewing the environment requirements.

---

### 7.15 Verify the Deployment Configuration

Return to the repository root:

```bash
cd ~/my-cool-app
```

View the complete structure:

```bash
tree -a -L 6
```

Confirm that the repository contains:

```text
my-cool-app/
├── .gitlab-ci.yml
│
├── app/
│   ├── .gitlab/
│   │   ├── expedition-0/
│   │   │   ├── dev/
│   │   │   ├── test/
│   │   │   └── prod/
│   │   └── oasis/
│   ├── backend/
│   ├── database/
│   ├── frontend/
│   ├── Makefile
│   └── compose.yml
│
└── deploy/
    ├── uds/
    │   └── uds-bundle.yaml
    │
    └── zarf/
        ├── zarf.yaml
        └── helm/
            ├── backend/
            ├── frontend/
            └── package/
```

Review the current Git changes:

```bash
git status
```

---

### 7.16 Verify That Local Secrets Are Not Tracked

Before committing, verify that local credentials are ignored:

```bash
git check-ignore app/db-password.txt
git check-ignore app/backend/my-cool-app/settings/dev/.env
git check-ignore app/.env
```

Local passwords and environment credentials must not be committed.

Do not hard-code credentials into:

```text
values.yaml
deployment.yaml
uds-package.yaml
cdso_config.yml
.gitlab-ci.yml
```

---

### 7.17 Commit the Deployment Configuration

Stage the deployment changes:

```bash
git add .gitlab-ci.yml
git add app/.gitlab
git add deploy
```

Review the staged files:

```bash
git diff --cached --name-only
```

Confirm that no credentials appear in the staged file list.

Commit:

```bash
git commit -m "Configure Expedition 0 deployment"
```

Push the current feature branch:

```bash
git push
```

If `main` is protected, use the feature branch created earlier and merge the changes through a Merge Request.

---

### 7.18 Merge the Deployment Configuration

In GitLab:

1. Open the Merge Request.
2. Review the application and deployment configuration.
3. Confirm the pipeline configuration is valid.
4. Resolve any pipeline or review findings.
5. Merge the changes into the intended release branch.

Do not create a release tag until the configuration intended for release has been merged.

---

### 7.19 Create the First Release Tag

Expedition 0 uses Git tags to identify specific application releases.

In GitLab:

1. Navigate to **Code → Tags**.
2. Select **New tag**.
3. Enter:

```text
v0.0.1
```

4. Select the release branch.
5. Add a description for the release.
6. Select **Create tag**.

Git tags identify specific application release versions in the Expedition 0 authorization process.

A tagless pipeline normally performs build, review, and clean operations.

A tag-based pipeline adds the delivery process so approved artifacts can be delivered for deployment.

> **Screenshot:** GitLab New Tag page showing `v0.0.1`.

![Create Release Tag](photos/create-release-tag.png)

---

### 7.20 Monitor the Tagged Pipeline

Navigate to:

```text
Build → Pipelines
```

Open the pipeline associated with:

```text
v0.0.1
```

Monitor the backend and frontend jobs.

A new deployment environment may require security review before the delivery process can complete.

After approval, another tagged pipeline may be required to deliver the approved application images to the Expedition 0 Azure Container Registry.

---

### 7.21 Complete the Security Review

The first tagged release for a new environment may trigger a security review.

Review the generated security Merge Request and address any findings required by the security team.

Security authorization is tied to the deployment environment.

Approval for:

```text
dev
```

does not automatically approve:

```text
test
```

or:

```text
prod
```

After the application is approved, rerun the tagged pipeline if required so the application artifacts can be delivered.

---

### 7.22 Verify the Delivered Backend Image

After the backend `deliver` job completes successfully, open the job in GitLab.

Search the job log for:

```text
azurecr.us
```

The backend image should appear as a complete reference similar to:

```text
cazcaravandecoreacr.azurecr.us/ai2c/caravan/my-cool-app/backend:v0.0.1
```

Separate the value into:

```text
Repository:
cazcaravandecoreacr.azurecr.us/ai2c/caravan/my-cool-app/backend

Tag:
v0.0.1
```

Compare the result with:

```text
deploy/zarf/helm/backend/values.yaml
```

The configured values should match:

```yaml
image:
  repository: cazcaravandecoreacr.azurecr.us/ai2c/caravan/my-cool-app/backend
  tag: v0.0.1
```

> **Important:** The delivery job is the authoritative source for the actual image repository.

If the path differs, use the exact repository displayed by the delivery job.

> **Screenshot:** GitLab backend delivery job showing the complete ACR backend image reference.

![Backend Delivered Image](photos/backend-delivered-image.png)

---

### 7.23 Verify the Delivered Frontend Image

Open the successful frontend `deliver` job.

Search for:

```text
azurecr.us
```

The complete frontend image should resemble:

```text
cazcaravandecoreacr.azurecr.us/ai2c/caravan/my-cool-app/frontend:v0.0.1
```

Compare it with:

```text
deploy/zarf/helm/frontend/values.yaml
```

The expected configuration is:

```yaml
image:
  repository: cazcaravandecoreacr.azurecr.us/ai2c/caravan/my-cool-app/frontend
  tag: v0.0.1
```

If the path differs, use the exact repository displayed by the delivery pipeline.

---

### 7.24 Correct an Image Repository if Necessary

If the delivery pipeline confirms that an image repository is different from the expected value, update the appropriate file:

```text
deploy/zarf/helm/backend/values.yaml
```

or:

```text
deploy/zarf/helm/frontend/values.yaml
```

For example:

```yaml
image:
  repository: <EXACT_REPOSITORY_FROM_DELIVER_JOB>
  tag: v0.0.1
```

Because this changes release configuration, commit the correction:

```bash
git add deploy/zarf/helm
git commit -m "Correct delivered image repositories"
git push
```

Merge the correction.

Create a new release tag rather than modifying the configuration associated with the previous release.

For example:

```text
v0.0.2
```

The Git release tag, Helm image tag, and application version should continue to represent the same release.

---

### 7.25 Verify the UDS Bundle Package Reference

After the application's delivery jobs have completed successfully, confirm the exact Zarf package reference produced by the delivery pipeline.

Update:

```text
deploy/uds/uds-bundle.yaml
```

if necessary so that it references the package actually delivered for:

```text
my-cool-app-zarf
```

and the correct application version.

Do not use another application's Zarf package location.

---

### 7.26 Deploy the Approved Application

Before deploying, confirm:

```text
Application configuration committed
Release tag created
Security review completed
Backend image delivered
Frontend image delivered
Helm image references verified
UDS bundle package reference verified
```

In GitLab, navigate to:

```text
Build → Pipelines
```

Select:

```text
New pipeline
```

Select the approved release tag.

For Expedition 0, use:

```text
PLATFORM = Expedition 0
UDS_BUNDLE_TASK = deploy
```

Run the pipeline.

The root pipeline creates environment-specific manual jobs.

Select:

```text
dev
```

for the development environment.

The child pipeline should run the application deployment component rather than the normal container review jobs.

---

### 7.27 Monitor the Deployment Pipeline

Open the development child pipeline.

Verify that the deployment job completes successfully.

The UDS bundle is the application artifact ultimately deployed to the Expedition 0 AKS cluster.

> **Screenshot:** GitLab pipeline showing the successful Expedition 0 development deployment.

![Expedition 0 Deployment](photos/expedition0-deployment.png)

---

### 7.28 Configure the Development Host Entry

After the development deployment succeeds, Windows may require a hosts-file entry to reach the application.

The hostname is based on the `host` configured in:

```text
deploy/zarf/helm/package/templates/uds-package.yaml
```

For this guide:

```yaml
host: my-cool-app
```

The resulting hostname is expected to follow the Expedition 0 development domain pattern:

```text
my-cool-app.dev.ai.army.mil
```

Verify the current Expedition 0 host and IP information before editing the Windows hosts file because platform addresses may change.

Open PowerShell as Administrator and edit:

```text
C:\Windows\System32\drivers\etc\hosts
```

Add the current Expedition 0 development IP and application hostname according to the current platform guidance.

---

### 7.29 Verify the Deployed Application

Open:

```text
https://my-cool-app.dev.ai.army.mil
```

The My Cool App message board should load.

Enter:

```text
Hello Expedition 0
```

Select **Submit**.

Confirm that the message appears under:

```text
Saved Messages
```

Refresh the page.

If the message remains, the deployed application flow is working:

```text
User
 ↓
UDS / Application Host
 ↓
React Frontend
 ↓
Django Backend
 ↓
PostgreSQL
 ↓
Django Backend
 ↓
React Frontend
 ↓
Saved Message Displayed
```

> **Screenshot:** My Cool App running in the Expedition 0 development environment with a saved message displayed.

![My Cool App on Expedition 0](photos/my-cool-app-expedition0.png)

---

### 7.30 Remove a Development Deployment

If the application needs to be removed, create a new pipeline using the approved release tag.

Select:

```text
PLATFORM = Expedition 0
UDS_BUNDLE_TASK = remove
```

Run the pipeline.

Select the:

```text
dev
```

environment job.

The removal pipeline removes the application's deployed UDS bundle.

Only use this option when the application is intended to be removed.

---

### 7.31 Deploying to Test and Production

After the development deployment has been validated, the same general workflow can be used for:

```text
test
prod
```

Each environment has its own cDSO configuration under:

```text
app/.gitlab/expedition-0/test/
app/.gitlab/expedition-0/prod/
```

Review the environment-specific requirements before deploying.

Security authorization for one environment does not automatically authorize another environment.

---

### 7.32 Deploying to Oasis

The Cookiecutter template also creates Oasis-specific configuration under:

```text
app/.gitlab/oasis/
```

including:

```text
dev/
test/
prod/
```

The root pipeline allows the platform to be selected using:

```text
PLATFORM = Oasis
```

Oasis deployment requirements may differ from Expedition 0.

Do not assume that Expedition 0 networking, UDS, Zarf, authorization, or infrastructure configuration can be copied directly to Oasis without reviewing the current Oasis deployment requirements.

---

### 7.33 Deployment Complete

The completed repository follows:

```text
my-cool-app/
├── .gitlab-ci.yml
│
├── app/
│   ├── .gitlab/
│   ├── backend/
│   ├── database/
│   ├── frontend/
│   ├── Makefile
│   └── compose.yml
│
└── deploy/
    ├── uds/
    │   └── uds-bundle.yaml
    │
    └── zarf/
        ├── zarf.yaml
        └── helm/
            ├── backend/
            ├── frontend/
            └── package/
```

The application source remains under:

```text
app/
```

The platform deployment configuration remains under:

```text
deploy/
```

The overall deployment workflow is:

```text
Develop and Test Application
          ↓
Configure GitLab Pipeline
          ↓
Create Helm / Zarf / UDS Files
          ↓
Commit and Merge
          ↓
Create Release Tag
          ↓
Build and Security Review
          ↓
Deliver Container Images
          ↓
Verify ACR Image References
          ↓
Verify Zarf / UDS Package Reference
          ↓
Deploy Approved UDS Bundle
          ↓
Verify Application
```

This keeps application development and Expedition 0 deployment configuration separate while allowing both to be maintained in the same Git repository.

