ronicbrown@CAZVW0FVAA3-59K:~/message-board/app/.gitlab/expedition-0/prod/uds/zarf$ cd ~/message-board/app/.gitlab/expedition-0/prod/app/.gitlab/expedition-0/prod

cat cdso_config.yml
organization: expedition-0
security_group: ai2c
deployment_level: PRODUCTION

backend:
  project_type: container
  dockerfile_folder: app/backend
  container_lifespan: PERSISTENT
  connection_context: INTERNAL
  semgrep:
    exclusions:
      #
      # False positive: {{ csp_nonce }} is used only in the nonce="" attribute of a
      # <script> tag (index.html:7), not in executable JS. The value is generated
      # server-side from os.urandom, never from user input. This is standard CSP usage.
      # https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP
      - app.rules.community.javascript.express.security.audit.xss.mustache.var-in-script-tag
       #
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
  mitigations:
  - CVE-2025-15366: >-
      DESCRIPTION: The imaplib module, when passed a user-controlled command, can have additional commands injected using newlines.
      MITIGATION: This application does not use imaplib or connect to any IMAP servers. The vulnerable module is not imported or exercised by any application code. No patched Python version available.
  - CVE-2025-15367: >-
      DESCRIPTION: The poplib module, when passed a user-controlled command, can have additional commands injected using newlines.
      MITIGATION: This application does not use poplib or connect to any POP3 servers. The vulnerable module is not imported or exercised by any application code. No patched Python version available.
  - CVE-2025-12781: >-
      DESCRIPTION: The base64 module b64decode functions always accept +/ characters regardless of the altchars parameter, potentially causing data integrity issues.
      MITIGATION: This application does not use altchars or urlsafe_b64decode on user-controlled input in a security-sensitive context. The CSP nonce uses base64.b64encode for output only. No patched Python version available yet.
  - CVE-2026-3298: >-
      DESCRIPTION: The method "sock_recvfrom_into()" of "asyncio.ProacterEventLoop" (Windows only) was missing a boundary check for the data buffer when using nbytes parameter. This allowed for an out-of-bounds buffer write if data was larger than the buffer size. Non-Windows platforms are not affected.
      MITIGATION: This application does not run on windows, and will be running on an Alpine Linux container and thus is non vunerable to this issue.
  - CVE-2026-6100: >-
      DESCRIPTION: Use-after-free (UAF) was possible in the `lzma.LZMADecompressor`, `bz2.BZ2Decompressor`, and `gzip.GzipFile` when a memory allocation fails with a `MemoryError` and the decompression instance is re-used. Thisscenario can be triggered if the process is under memory pressure. The fix cleans up the dangling pointer in this specific error condition.  The vulnerability is only present if the program re-uses decompressor instances across multiple decompression calls even after a `MemoryError` is raised during decompression. Using the helper functions to one-shot decompress data such as `lzma.decompress()`, `bz2.decompress()`, `gzip.decompress()`, and `zlib.decompress()` are not affected as a new decompressor instance is used per call. If the decompressor instance is not re-used after an error condition, this usage is similarly not vulnerable.
      MITIGATION:  This application does not utlize any of the vunerable functionality and therefore is not at risk from this issue.
  - CVE-2026-4786: >-
      DESCRIPTION: Mitgation of CVE-2026-4519 was incomplete. If the URL contained "%action" the mitigation could be bypassed for certain browser types the "webbrowser.open()" API could have commands injected into the underlying shell. See CVE-2026-4519 for details.
      MITIGATION: This application is a headless backend server and does not call webbrowser.open(). The vulnerable code path is not exercised. No patched Python version available yet.
  - CVE-2026-1502: >-
      DESCRIPTION: CR/LF bytes were not rejected by HTTP client proxy tunnel headers or host.
      MITIGATION: This application does not use the vulnerable http.client module. No patched Python version available yet.
  - CVE-2026-7210: >-
      DESCRIPTION: `xml.parsers.expat` and `xml.etree.ElementTree` use insufficient entropy for Expat hash-flooding protection, which allows a crafted XML document to trigger hash flooding.\r\n\r\nFully mitigating this vulnerability requires both updating libexpat to 2.8.0 or later and applying this patch.
      MITIGATION: This application does not accept or utilize XML documents.  This finding is a false positive for this application.  The library will be patched and updated when alpine linux provides an update."
  - CVE-2026-6019: >-
      DESCRIPTION: http.cookies.Morsel.js_output() returns an inline <script> snippet and only escapes " for JavaScript string context. It does not neutralize the HTML parser-sensitive sequence </script> inside the generated script element. Mitigation base64-encodes the cookie value to disallow escaping using cookie value.
      MITIGATION: This application does not utlize the http.cookies module and associated MOrsel.js_output() function. The finding is therefore not applicable. No patched Python version available.
  - CVE-2026-85091: >-
      DESCRIPTION: zlib versions 1.3.1.2 through 1.3.2 contain a heap buffer overflow in gz_vacate() when processing non-blocking gzwrite() operations with stale external buffer pointers.
      MITIGATION: The application does not call gzwrite(), gzprintf(), gzvprintf(), or perform non-blocking gzip stream writes. The vulnerable code path is not exercised by the application. The approved Alpine repository currently provides zlib 1.3.2-r0 with no newer package available. The package will be updated when a patched version becomes available in the approved base image.

  - CVE-2026-17084: >-
      DESCRIPTION: Python stringprep and IDNA 2003 processing may use Unicode codepoint attributes newer than Unicode 3.2.0, which can cause incorrect domain-name normalization or matching.
      MITIGATION: This application does not import or use stringprep and does not perform IDNA 2003 domain-name processing on user-controlled input. The vulnerable code path is not exercised by application code. The application will consume the patched Python runtime when it becomes available in the approved base image.

  - CVE-2026-19672: >-
      DESCRIPTION: Python tarfile extraction filters may create empty directories outside the intended extraction destination when processing specially crafted archive member paths.
      MITIGATION: This application does not import or use tarfile and does not accept, create, or extract user-supplied tar archives. The vulnerable archive extraction code path is not exercised by application code. The application will consume the patched Python runtime when it becomes available in the approved base image.

  - CVE-2026-87910: >-
      DESCRIPTION: Python tarfile may incorrectly process a hardlink fallback when a custom extraction filter rejects a member, allowing the rejected member to be processed under specific conditions.
      MITIGATION: This application does not import or use tarfile and does not extract tar archives or process archive hardlinks. The vulnerable extraction and custom-filter code paths are not exercised by application code. The application will consume the patched Python runtime when it becomes available in the approved base image.

  - CVE-2026-15806: >-
      DESCRIPTION: Python HTTPPasswordMgr and related urllib.request classes may match stored credentials without correctly considering the URL scheme, which could expose credentials during an HTTPS-to-HTTP downgrade.
      MITIGATION: This application does not use HTTPPasswordMgr, HTTPPasswordMgrWithDefaultRealm, HTTPPasswordMgrWithPriorAuth, or perform authenticated outbound requests using urllib.request. The vulnerable credential-management code path is not exercised by application code. The application will consume the patched Python runtime when it becomes available in the approved base image.

frontend:
  project_type: container
  dockerfile_folder: app/frontend
  container_lifespan: PERSISTENT
  connection_context: EXTERNAL
  semgrep:
   exclusions:
     # False positive: this public location is the application's intended entrypoint
     # and must remain externally reachable. Adding 'internal' would cause nginx to
     # return 404 for direct client requests. The upstream is fixed to backend:8000
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
ronicbrown@CAZVW0FVAA3-59K:~/message-board/app/.gitlab/expedition-0/prod$ grep -RIn \
  "SECRET_KEY\|DB_HOST\|DB_NAME\|DB_USER\|DB_PASS\|DB_PORT\|secretKeyRef\|envFrom" \
  .
./cdso_config.yml:26:     DB_HOST: database
./cdso_config.yml:27:     DB_NAME: postgres
./cdso_config.yml:28:     DB_USER: postgres
./cdso_config.yml:29:     DB_PASS: postgres
./cdso_config.yml:30:     DB_PORT: "5432"
ronicbrown@CAZVW0FVAA3-59K:~/message-board/app/.gitlab/expedition-0/prod$
