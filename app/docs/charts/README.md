## Helm Charts
The steps below describe how the Helm chart was created. It assumes you already have `make` installed and have ran `make init` from the root of this project. The `init` target in the provided Makefile installs the following tools: `az`, `kubelogin`, `kubectl`, `helm`, `pandoc`, a PostgreSQL client, `zarf`, and `uds`.

**Step 1.** Create a new chart.
```bash
helm create deploy
```

**Step 2.** Open the `deploy/Chart.yaml` and replace what it contains with the content below.
```yaml
apiVersion: v2
name: mission-clock
description: A fictional software project.
type: application
version: 0.1.0
appVersion: "1.16.0"
```


**Step 2.** Open the `deploy/values.yaml` and replace what it contains with the content below.
```yaml
replicaCount: 1
frontend:
  image: cazcaravandecoreacr.azurecr.us/ai2c/application-templates/expedition-0-tenant-application/frontend
  tag: v1.0.0
backend:
  image: cazcaravandecoreacr.azurecr.us/ai2c/application-templates/expedition-0-tenant-application/backend
  tag: v1.0.0
service:
  type: ClusterIP
  ports:
    frontend: 5173
    backend: 8000
```

**Step 3.** Open the `deploy/templates/deployment.yaml` and replace what it contains with the content below.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Chart.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Chart.Name }}
  template:
    metadata:
      labels:
        app: {{ .Chart.Name }}
    spec:
      containers:
        - name: frontend
          image: {{ .Values.frontend.image }}:{{ .Values.frontend.tag }}
          ports:
            - containerPort: {{ .Values.service.ports.frontend }}
        - name: backend
          image: {{ .Values.backend.image }}:{{ .Values.backend.tag }}
          ports:
            - containerPort: {{ .Values.service.ports.backend }}
```

**Step 4.** Open the `deploy/templates/service.yaml` and replace what it contains with the content below.
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Chart.Name }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app: {{ .Chart.Name }}
  ports:
    - name: frontend
      port: {{ .Values.service.ports.frontend }}
      targetPort: {{ .Values.service.ports.frontend }}
    - name: backend
      port: {{ .Values.service.ports.backend }}
      targetPort: {{ .Values.service.ports.backend }}
```



**Step 5.** Remove files that are not required. 
```bash
rm deploy/templates/serviceaccount.yaml
rm deploy/templates/ingress.yaml
rm deploy/templates/hpa.yaml
rm deploy/templates/NOTE.txt
```
