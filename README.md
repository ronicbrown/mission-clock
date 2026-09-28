ronicbrown@CAZVW0FVAA3-59K:~/message-board$ cd ~/message-board

echo "=== COOKIECUTTER CDSO CONFIG ==="
git show origin/cookiecuttertemp:app/.gitlab/expedition-0/prod/cdso_config.yml | tail -20

echo "=== COOKIECUTTER ZARF ==="
git show origin/cookiecuttertemp:app/.gitlab/expedition-0/prod/uds/zarf/zarf.yaml | head -40
=== COOKIECUTTER CDSO CONFIG ===
     # and is not derived from user input, so this is not an SSRF sink.
     # https://nginx.org/en/docs/http/ngx_http_core_module.html#internal
     - app.rules.community.generic.nginx.security.missing-internal
  mitigations:
  - CVE-2026-2673: >-
      DESCRIPTION: An OpenSSL TLS 1.3 server may fail to negotiate the expected preferred key exchange group when its key exchange group configuration includes the default by using the 'DEFAULT' keyword.
      MITIGATION: Not applicable in the current frontend image usage. The reported vulnerable artifacts are base-image OpenSSL libraries, but this container does not terminate HTTPS/TLS in its repository-managed nginx configuration. No nginx ssl listener, certificate, private key, or OpenSSL group-selection configuration is present. The issue is specific to TLS 1.3 server-side group negotiation using the DEFAULT keyword. Risk accepted pending a patched approved base image.
  - CVE-2026-85091: >-
      DESCRIPTION: zlib versions 1.3.1.2 through 1.3.2 contain a heap buffer overflow in gz_vacate() when processing non-blocking gzwrite() operations with stale external buffer pointers.
      MITIGATION: The frontend does not call gzwrite(), gzprintf(), gzvprintf(), or perform non-blocking gzip stream writes. NGINX gzip compression is not configured or enabled by this application, so the vulnerable code path is not exercised. The approved Alpine repository currently provides zlib 1.3.2-r0 with no newer package available. The package will be updated when a patched version becomes available in the approved base image.

message-board:
  project_type: sdd
  sdd_path: sdd.md
  zarf_directory: app/.gitlab/expedition-0/prod/uds/zarf
  uds_directory: app/.gitlab/expedition-0/prod/uds

message-board-tad:
  project_type: sdd
  tad_path: tad.md
=== COOKIECUTTER ZARF ===
kind: ZarfPackageConfig

metadata:
  name: message-board-zarf
  version: v1.0.0


variables:
  - name: VERSION
    description: "The version of bundle, package, and images"
    default: "v1.0.0"

  - name: DOMAIN
    description: "Cluster domain"
    default: "ai.army.mil"

  - name: SECRET_KEY
    description: "Django production secret key"
    prompt: true
    sensitive: true

  - name: DB_NAME
    description: "Production PostgreSQL database name"
    prompt: true

  - name: DB_USER
    description: "Production PostgreSQL username"
    prompt: true
    sensitive: true

  - name: DB_PASS
    description: "Production PostgreSQL password"
    prompt: true
    sensitive: true

  - name: DB_HOST
    description: "Production PostgreSQL hostname"
    prompt: true

  - name: DB_PORT
ronicbrown@CAZVW0FVAA3-59K:~/message-board$
