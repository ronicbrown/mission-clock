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
