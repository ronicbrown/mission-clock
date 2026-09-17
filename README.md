sample files 

# uds/zarf/helm/backend/values.yaml

---
namespace: squidfall
replicaCount: 1
image: 
  pullPolicy: Always
  registry: "###ZARF_CONST_ACR_NAME###"
  repository: ai2c/application-templates/react-django-app/backend
  tag: "###ZARF_VAR_VERSION###"
service: 
  type: ClusterIP
  name: backend
  port: 8000
nodeSelector:
  agentPool: rucksack




# uds/zarf/helm/backend/Chart.yaml

---
# Chart metadata.
apiVersion: v2
type: application
version: v1.0.0 

# Component metadata.
name: backend
appVersion: v1.0.0




# uds/zarf/helm/backend/templates/deployment.yaml

---
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: {{ .Values.namespace }}
  name: {{ .Values.service.name }}
  labels:
    app.kubernetes.io/component: {{ .Values.service.name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app.kubernetes.io/component: {{ .Values.service.name }}
  template:
    metadata:
      labels:
        app.kubernetes.io/component: {{ .Values.service.name }}
    spec:
      containers:
        - name: {{ .Values.service.name }}
          image: {{ .Values.image.registry }}/{{ .Values.image.repository }}:{{ .Values.image.tag }}
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - containerPort: {{ .Values.service.port }}
      nodeSelector:
        kubernetes.azure.com/agentpool: {{ .Values.nodeSelector.agentPool }}
      tolerations:
      - key: "kubernetes.azure.com/scalesetpriority"
        operator: "Equal"
        value: "spot"
        effect: "NoSchedule"
    


# uds/zarf/helm/backend/templates/service.yaml

---
apiVersion: v1
kind: Service
metadata:
  namespace: {{ .Values.namespace }}
  name: {{ .Values.service.name }}
  labels:
    app.kubernetes.io/component: {{ .Values.service.name }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app.kubernetes.io/component: {{ .Values.service.name }}
  ports:
    - port: {{ .Values.service.port }}




# uds/zarf/helm/frontend/templates/deployment.yaml

---
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: {{ .Values.namespace }}
  name: {{ .Values.service.name }}
  labels:
    app.kubernetes.io/component: {{ .Values.service.name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app.kubernetes.io/component: {{ .Values.service.name }}
  template:
    metadata:
      labels:
        app.kubernetes.io/component: {{ .Values.service.name }}
    spec:
      containers:
        - name: {{ .Values.service.name }}
          image: {{ .Values.image.registry }}/{{ .Values.image.repository }}:{{ .Values.image.tag }}
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - containerPort: {{ .Values.service.port }}
          volumeMounts:
            {{- range .Values.volumes }}
            - name: {{ .name }}
              mountPath: {{ .mountPath }}
            {{- end }}
      volumes:
        {{- range .Values.volumes }}
        - name: {{ .name }}
          emptyDir: {}
        {{- end }}
      nodeSelector:
        kubernetes.azure.com/agentpool: {{ .Values.nodeSelector.agentPool }}
      tolerations:
      - key: "kubernetes.azure.com/scalesetpriority"
        operator: "Equal"
        value: "spot"
        effect: "NoSchedule"
    


# uds/zarf/helm/frontend/templates/service.yaml



Zarf and UDS: Component Interaction and Variable Substitution Guide
Introduction
This document explains the interactions between Helm charts, Zarf packages, and UDS bundles, with a specific focus on variable substitution and configuration overrides. By understanding how variables, constants, and templates propagate through these layers, you can streamline your deployments and manage configurations from a single source of truth.

Component Overview
Helm Chart
Role: The foundational building block that defines Kubernetes resources.
Values: Uses standard Go templating (e.g., {{ .Values.example }}) and reads defaults from a values.yaml file.
Zarf Package
Role: Packages Helm charts, images, and other resources into an airgap-friendly artifact.
Components: Contains Helm chart components and, for fully airgapped packages, the required OCI images.
Zarf Config (zarf-config.yaml)
Role: A centralized configuration file used to define both create and deploy values for Zarf.
Usage: Replicates and manages changes consistently across Zarf CLI commands, reducing the need for multiple manual overrides via the command line.
UDS Bundle
Role: Defines a collection of Zarf packages to deploy together as a unified bundle.
Images: Does not contain container images directly; it only references the components within the associated Zarf packages.
Overrides: Allows setting Zarf variables (###ZARF_VAR_EXAMPLE###) or modifying Helm Chart template values at the bundle level.
UDS Config (uds-config.yaml)
Role: Defines variable overrides utilized during a uds deploy.
Substitution: Automatically substitutes ###ZARF_VAR_EXAMPLE### placeholders across the bundle during deployment.
Variable Substitution and Overrides
1. Zarf Package Template Values (###ZARF_PKG_TMPL_EXAMPLE###)
Phase: Applied at zarf package create time.
Purpose: Dynamically changes configurations within the zarf.yaml during the creation phase.
Immutability: Once the package is created, these values are baked in and cannot be changed at deploy time.
Definition: Typically defined in a zarf-config.yaml under create configurations, or passed via the --set flag.
2. Zarf Constants (###ZARF_CONST_EXAMPLE###)
Phase: Applied at zarf package create time (Correction from original notes).
Purpose: Sets immutable constant values within a Helm chart or package configuration.
Immutability: Once the package is built, they cannot be dynamically altered using set flags during the deploy command.
Definition: The underlying values for constants can be templated using Zarf package template values (###ZARF_PKG_TMPL...###) from a zarf-config.yaml during package creation.
3. Zarf Variables (###ZARF_VAR_EXAMPLE###)
Phase: Applied at zarf package deploy time.
Purpose: Dynamically overrides values within a Helm chart or other manifests at deploy time.
Flexibility: Can be modified using the --set command-line flag or centrally managed in zarf-config.yaml.
Definition: The default value of a Zarf variable can also be established using Zarf package template values during creation.
4. Helm Chart Values ({{ .Values.example }})
Phase: Evaluated during Helm template rendering (triggered by a Zarf or UDS deployment).
Substitution: Zarf variables and constants can be passed down into Helm charts via Zarf's Helm component definitions (in the zarf.yaml) to override the standard values.yaml defaults.
Centralized Configuration Flow
To achieve a "single source of truth" where a configuration change in one file cascades automatically to multiple locations, you can chain these substitution mechanisms:

At Create Time: Use a zarf-config.yaml to define ###ZARF_PKG_TMPL_EXAMPLE### values. These templates set the default values for constants and variables inside the zarf.yaml before the package is built.
At Zarf Deploy Time: For individual Zarf package deployments, utilize the zarf-config.yaml to override ###ZARF_VAR_EXAMPLE### variables. Zarf injects these variable values into your Helm chart's values.yaml configuration.
At Bundle Deploy Time: When managing multiple packages via a UDS bundle, leverage the uds-config.yaml. This file acts as the highest-level configuration point, injecting values into bundle overrides. These bundle overrides cascade down to satisfy the ###ZARF_VAR_EXAMPLE### placeholders in the respective Zarf packages, which in turn feed into the underlying Helm templates.
Example:
🏗️ 1. The Helm Chart (The Foundation)
At the lowest level, your Helm chart expects standard Go templating to fill in its values. It defines a default in values.yaml, but relies on {{ .Values... }} in the actual templates.

my-chart/values.yaml


ingress:
  domain: "default.local" # This is the absolute base default
my-chart/templates/ingress.yaml


apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mission-app-ingress
spec:
  rules:
  - host: {{ .Values.ingress.domain }} # Helm template substitution
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mission-service
            port: 
              number: 80
📦 2. The Zarf Package (zarf.yaml)
Next, you wrap the Helm chart in a Zarf package. Here, you define a Zarf Variable and map it to the Helm chart's value using the set block. This is the critical bridge between Zarf's ###ZARF_VAR_...### syntax and Helm's values.yaml.

zarf.yaml


kind: ZarfPackageConfig
metadata:
  name: mission-app
  version: "1.0.0"

# Define the Zarf Variable
variables:
  - name: APP_DOMAIN
    description: "The domain name for the mission application"
    default: "zarf-default.local"

components:
  - name: app-deployment
    required: true
    charts:
      - name: my-chart
        localPath: charts/my-chart
        namespace: mission-ns
        # This maps the Zarf Variable to the Helm Chart Value
        set:
          ingress.domain: "###ZARF_VAR_APP_DOMAIN###"
🧩 3. The UDS Bundle (uds-bundle.yaml)
Now, you want to deploy this Zarf package alongside others (like an Istio gateway or a database). You define a UDS Bundle that points to your compiled Zarf package.

Note: The bundle definition itself usually doesn't hardcode the variable values; it just declares the packages.

uds-bundle.yaml


kind: UDSBundle
metadata:
  name: mission-platform
  version: "1.0.0"

packages:
  # Reference the Zarf package we just created
  - name: mission-app
    repository: ghcr.io/defenseunicorns/packages/mission-app
    ref: "1.0.0"
🎯 4. The UDS Config (uds-config.yaml) - Single Source of Truth
Finally, when it is time to deploy the UDS bundle to your environment, you use uds-config.yaml. This is where you define the dynamic override.

When you run uds deploy, UDS reads this file and pushes the variable down the chain.

uds-config.yaml


variables:
  # Target the specific bundle name
  mission-platform:
    # Target the specific Zarf package within the bundle
    mission-app:
      # Override the Zarf Variable
      APP_DOMAIN: "app.mission.dow.mil"
🌊 How the Cascade Operates at Deploy Time
When you execute uds deploy uds-bundle-mission-platform.tar.zst --config uds-config.yaml, the following sequence automatically occurs:

Step	Action	Tool Responsible	Current Value State
1	Reads uds-config.yaml and extracts the variable overrides for the mission-app package.	UDS CLI	APP_DOMAIN = "app.mission.dow.mil"
2	Injects the overridden variable into the Zarf package deployment process, replacing the default zarf-default.local.	UDS CLI -> Zarf CLI	###ZARF_VAR_APP_DOMAIN### = "app.mission.dow.mil"
3	Zarf reads the set: block in zarf.yaml and passes the substituted variable to the Helm chart.	Zarf CLI	ingress.domain = "app.mission.dow.mil"
4	Helm renders ingress.yaml, replacing {{ .Values.ingress.domain }} with the provided value.	Helm	host: app.mission.dow.mil
By structuring your files this way, you never have to manually edit the Helm chart or the Zarf package to change the domain name for different environments (e.g., Development vs. Production). You simply update the uds-config.yaml for that specific environment, and the change cascades all the way down.

---
apiVersion: v1
kind: Service
metadata:
  namespace: {{ .Values.namespace }}
  name: {{ .Values.service.name }}
  labels:
    app.kubernetes.io/component: {{ .Values.service.name }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app.kubernetes.io/component: {{ .Values.service.name }}
  ports:
    - port: {{ .Values.service.port }}



# uds/zarf/helm/frontend/Chart.yaml

---
# Chart metadata.
apiVersion: v2
type: application
version: v1.0.0 

# Component metadata.
name: frontend
appVersion: v1.0.0



# uds/zarf/helm/frontend/values.yaml

---
namespace: squidfall
replicaCount: 1
image:
  pullPolicy: Always
  registry: "###ZARF_CONST_ACR_NAME###"
  repository: ai2c/application-templates/react-django-app/frontend
  tag: "###ZARF_VAR_VERSION###"
service:
  type: ClusterIP
  name: frontend
  port: 5173
volumes:
  - name: logs
    mountPath: /var/log/nginx
  - name: tmp
    mountPath: /var/lib/nginx/tmp
nodeSelector:
  agentPool: rucksack

