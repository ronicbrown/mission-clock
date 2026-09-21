# yaml-language-server: $schema=https://raw.githubusercontent.com/defenseunicorns/uds-cli/main/zarf.schema.json

---
kind: ZarfPackageConfig
metadata:
  # The Zarf package name configured here will be the name of the package reference in the uds-bundle.yaml
  name: squidfall
  # This description will show in the Overview tab of the UDS Registry
  description: "Squidfall is a basic application that is used as a template for new application builds."
  authors: "AI2C - Infrastructure and Platforms Portfolio"
  version: v1.0.0
  # The following annotations are specific to a Zarf package and will be used to display the package on the UDS Registry
  annotations:
    # The title of the application's Zarf package
    dev.uds.title: "Squidfall"
    # Label displayed under the package title
    dev.uds.tagline: "AI2C Application Template"
    # Searchable tags to associate with this application (comma separated for more multiple tags)
    dev.uds.categories: Application Template
    # Base64 encoded icon to associate with this Zarf package
    dev.uds.icon: "data:image/png;base64,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"

# Variables can be used to allow changes when the package is DEPLOYED (zarf package deploy).
# These variables are defined by a short name in this variables section, but used
# in combonation with the '###ZARF_VAR_###' prefix (ex. ###ZARF_VAR_DOMAIN###).
#
# A variable defined in this section can be used within the Helm charts and values.
#
variables:
  # Name of the variable
  - name: DOMAIN
    # Short description. Describes the variable in the UDS Registry
    description: "Cluster domain"
    # Default value to use
    default: "ai.army.mil"
    # Optional regex pattern to ensure the entered value is compliant, in this case a valid domain name pattern
    pattern: ^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$
    # Whether or not to prompt the User for input
    # prompt: true
    # Whether or not to hide the value of this variable in the output
    # sensitive: true
  - name: VERSION
    # Short description. Describes the variable in the UDS Registry
    description: 'The version of bundle, package, and images'
    # The value to use when creating the package
    default: 'v1.0.0'

# Constants differ from varaibles in that are used in the CREATE part (zarf package create)
# and do not change on DEPLOY.
# These are a way to standarize downstream values based on a singular reference point.
#
# Contants are used within downstream components with the '###ZARF_CONST_###' prefix.
# (ex. ###ZARF_CONST_ACR_NAME###)
#
# (This constant can be seen in action within the values.yaml for each container)
constants:
  # Name of the constant
  - name: ACR_NAME
    # Short description. Describes the variable in the UDS Registry
    description: 'The name of the Azure Container Registry'
    # The value to use when creating the package
    value: 'cazcaravanpecoreacr.azurecr.us'

# The documentation section can be used to add documentation to the Zarf package.
# A User can extract documents within this package using 'zarf package inspect documentation'
# documentation:
#   readme: ../../../../README.md

# Component entries should be the individual components that make up the entire application.
# Refrain from adding multiple Helm charts under the same component unless both charts are
# needed for that component to function.
#
# Example: This application has a backend and frontend container. While the entire
# application relies on each container, one container does not rely on another to run.
# Therefor each container should be it's own component entry.
#
components:
  - name: backend
    required: true
    charts:
      - name: backend
        namespace: squidfall
        version: v1.0.0
        localPath: helm/backend
        valuesFiles:
          - helm/backend/values.yaml
    # To be a truly airgapped Zarf package, an image should be included. If an image block
    # is not configured, the zarf-agent will need to locate and pull the image the container
    # is configured with.
    images:
      - "cazcaravanpecoreacr.azurecr.us/ai2c/application-templates/react-django-app/backend:v1.0.0"

  - name: frontend
    required: true
    charts:
      - name: frontend
        namespace: squidfall
        version: v1.0.0
        localPath: helm/frontend
        valuesFiles: 
          - helm/frontend/values.yaml
    images:
      - "cazcaravanpecoreacr.azurecr.us/ai2c/application-templates/react-django-app/frontend:v1.0.0"

  - name: uds-package
    # The required field can be set to 'false' if the component may not apply to all deployments
    # of this Zarf package. This 'uds-package' is specific to deploying this application onto
    # UDS Core and therefor would not mean anything on a standalone deployment.
    #
    # Since this template is created to deploy onto UDS Core, this component is set to required.
    required: true
    manifests:
      - name: squidfall-package
        namespace: squidfall
        files:
          # local manifests are specified relative to the `zarf.yaml` that uses them:
          - ../uds-package.yaml
