ronicbrown@CAZVW0FVAA3-59K:~/message-board$ cd ~/message-board

grep -RInE \
  "SECRET_KEY|DB_HOST|DB_NAME|DB_USER|DB_PASS|DB_PORT|message-board-backend-secrets" \
  .gitlab-ci.yml app/.gitlab \
  2>/dev/null
app/.gitlab/expedition-0/dev/cdso_config.yml:18:     DB_HOST: database
app/.gitlab/expedition-0/dev/cdso_config.yml:19:     DB_NAME: postgres
app/.gitlab/expedition-0/dev/cdso_config.yml:20:     DB_USER: postgres
app/.gitlab/expedition-0/dev/cdso_config.yml:21:     DB_PASS: postgres
app/.gitlab/expedition-0/dev/cdso_config.yml:22:     DB_PORT: "5432"
app/.gitlab/expedition-0/test/cdso_config.yml:26:     DB_HOST: database
app/.gitlab/expedition-0/test/cdso_config.yml:27:     DB_NAME: postgres
app/.gitlab/expedition-0/test/cdso_config.yml:28:     DB_USER: postgres
app/.gitlab/expedition-0/test/cdso_config.yml:29:     DB_PASS: postgres
app/.gitlab/expedition-0/test/cdso_config.yml:30:     DB_PORT: "5432"
app/.gitlab/expedition-0/prod/cdso_config.yml:26:     DB_HOST: database
app/.gitlab/expedition-0/prod/cdso_config.yml:27:     DB_NAME: postgres
app/.gitlab/expedition-0/prod/cdso_config.yml:28:     DB_USER: postgres
app/.gitlab/expedition-0/prod/cdso_config.yml:29:     DB_PASS: postgres
app/.gitlab/expedition-0/prod/cdso_config.yml:30:     DB_PORT: "5432"
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:27:            - name: SECRET_KEY
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:30:                  name: message-board-backend-secrets
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:31:                  key: SECRET_KEY
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:33:            - name: DB_NAME
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:36:                  name: message-board-backend-secrets
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:37:                  key: DB_NAME
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:39:            - name: DB_USER
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:42:                  name: message-board-backend-secrets
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:43:                  key: DB_USER
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:45:            - name: DB_PASS
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:48:                  name: message-board-backend-secrets
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:49:                  key: DB_PASS
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:51:            - name: DB_HOST
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:54:                  name: message-board-backend-secrets
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:55:                  key: DB_HOST
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:57:            - name: DB_PORT
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:60:                  name: message-board-backend-secrets
app/.gitlab/expedition-0/prod/uds/zarf/helm/backend/templates/deployment.yaml:61:                  key: DB_PORT
app/.gitlab/oasis/dev/cdso_config.yml:18:     DB_HOST: database
app/.gitlab/oasis/dev/cdso_config.yml:19:     DB_NAME: postgres
app/.gitlab/oasis/dev/cdso_config.yml:20:     DB_USER: postgres
app/.gitlab/oasis/dev/cdso_config.yml:21:     DB_PASS: postgres
app/.gitlab/oasis/dev/cdso_config.yml:22:     DB_PORT: "5432"
app/.gitlab/oasis/test/cdso_config.yml:27:     DB_HOST: database
app/.gitlab/oasis/test/cdso_config.yml:28:     DB_NAME: postgres
app/.gitlab/oasis/test/cdso_config.yml:29:     DB_USER: postgres
app/.gitlab/oasis/test/cdso_config.yml:30:     DB_PASS: postgres
app/.gitlab/oasis/test/cdso_config.yml:31:     DB_PORT: "5432"
app/.gitlab/oasis/prod/cdso_config.yml:26:     DB_HOST: database
app/.gitlab/oasis/prod/cdso_config.yml:27:     DB_NAME: postgres
app/.gitlab/oasis/prod/cdso_config.yml:28:     DB_USER: postgres
app/.gitlab/oasis/prod/cdso_config.yml:29:     DB_PASS: postgres
app/.gitlab/oasis/prod/cdso_config.yml:30:     DB_PORT: "5432"
ronicbrown@CAZVW0FVAA3-59K:~/message-board$
