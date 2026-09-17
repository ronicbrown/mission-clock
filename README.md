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

