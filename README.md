# mission-clock

ronicbrown@CAZVW0FVAA3-59K:~/my-cool-app/app$ curl -I http://localhost/static/index.js
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 14 Sep 2026 15:46:57 GMT
Content-Type: application/javascript
Content-Length: 1348918
Last-Modified: Fri, 11 Sep 2026 20:28:58 GMT
Connection: keep-alive
Accept-Ranges: bytes

ronicbrown@CAZVW0FVAA3-59K:~/my-cool-app/app$ curl -i http://localhost/api/messages/
HTTP/1.1 500 Internal Server Error
Server: nginx
Date: Mon, 14 Sep 2026 15:47:04 GMT
Content-Type: text/html
Content-Length: 179701
Connection: keep-alive
content-security-policy: default-src 'self'; script-src 'self' 'nonce-zTc7/5SgWx+3rsMcPCE1JQ=='; style-src 'self' 'nonce-zTc7/5SgWx+3rsMcPCE1JQ=='; style-src-elem 'self' 'nonce-zTc7/5SgWx+3rsMcPCE1JQ=='; frame-ancestors 'self'; form-action 'self';
x-frame-options: DENY
vary: Cookie
x-content-type-options: nosniff
referrer-policy: same-origin
cross-origin-opener-policy: same-origin

<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>OperationalError
          at /api/messages/</title>
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background-color:#fff; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size: 0.6875rem; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #info { padding: 0; }
    #info > * { padding:10px 20px; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size: 0.7rem; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5rem; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>

  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>

</head>
<body>
<header id="summary">
  <h1>OperationalError
       at /api/messages/</h1>
  <pre class="exception_value">failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve</pre>
  <table class="meta">

    <tr>
      <th scope="row">Request Method:</th>
      <td>GET</td>
    </tr>
    <tr>
      <th scope="row">Request URL:</th>
      <td>http://backend:8000/api/messages/</td>
    </tr>

    <tr>
      <th scope="row">Django Version:</th>
      <td>6.0.5</td>
    </tr>

    <tr>
      <th scope="row">Exception Type:</th>
      <td>OperationalError</td>
    </tr>


    <tr>
      <th scope="row">Exception Value:</th>
      <td><pre>failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve</pre></td>
    </tr>


    <tr>
      <th scope="row">Exception Location:</th>
      <td><span class="fname">/usr/local/lib/python3.14/site-packages/psycopg/_conninfo_attempts.py</span>, line 55, in conninfo_attempts</td>
    </tr>


    <tr>
      <th scope="row">Raised during:</th>
      <td>demo.views.messages</td>
    </tr>

    <tr>
      <th scope="row">Python Executable:</th>
      <td>/usr/local/bin/python3</td>
    </tr>
    <tr>
      <th scope="row">Python Version:</th>
      <td>3.14.7</td>
    </tr>
    <tr>
      <th scope="row">Python Path:</th>
      <td><pre><code>[&#x27;&#x27;,
 &#x27;/home/my-cool-app&#x27;,
 &#x27;/usr/local/lib/python314.zip&#x27;,
 &#x27;/usr/local/lib/python3.14&#x27;,
 &#x27;/usr/local/lib/python3.14/lib-dynload&#x27;,
 &#x27;/usr/local/lib/python3.14/site-packages&#x27;]</code></pre></td>
    </tr>
    <tr>
      <th scope="row">Server time:</th>
      <td>Mon, 14 Sep 2026 15:47:04 +0000</td>
    </tr>
  </table>
</header>

<main id="info">




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" role="button" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py</code>, line 279, in ensure_connection



            <div class="context" id="c126093136901696">

                <ol start="272" class="pre-context" id="pre126093136901696">

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        &quot;&quot;&quot;Guarantee that a connection to the database is established.&quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        if self.connection is None:</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>            if self.in_atomic_block and self.closed_in_transaction:</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                raise ProgrammingError(</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                    &quot;Cannot open a new connection in an atomic block.&quot;</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                )</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>            with self.wrap_database_errors:</pre></li>

                </ol>

              <ol start="279" class="context-line">
                <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                self.connect()
                     ^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='280' class="post-context" id="post126093136901696">

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>    # ##### Backend-specific wrappers for PEP-249 connection methods #####</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>    def _prepare_cursor(self, cursor):</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        Validate the connection is usable and perform database cursor wrapping.</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901696">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py</code>, line 26, in inner



            <div class="context" id="c126093136901568">

                <ol start="19" class="pre-context" id="pre126093136901568">

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                get_running_loop()</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            except RuntimeError:</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                pass</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            else:</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                if not os.environ.get(&quot;DJANGO_ALLOW_ASYNC_UNSAFE&quot;):</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                    raise SynchronousOnlyOperation(message)</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            # Pass onward.</pre></li>

                </ol>

              <ol start="26" class="context-line">
                <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='27' class="post-context" id="post126093136901568">

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>        return inner</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>    # If the message is actually a function, then be a no-arguments decorator.</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>    if callable(message):</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>        func = message</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901568">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;,)</pre></td>
                  </tr>

                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function BaseDatabaseWrapper.connect at 0x72ae5c85ca90&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>message</td>
                    <td class="code"><pre>&#x27;You cannot call this from an async context - use a thread or sync_to_async.&#x27;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py</code>, line 256, in connect



            <div class="context" id="c126093136901248">

                <ol start="249" class="pre-context" id="pre126093136901248">

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.close_at = None if max_age is None else time.monotonic() + max_age</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.closed_in_transaction = False</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.errors_occurred = False</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        # New connections are healthy.</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.health_check_done = True</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        # Establish the connection</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        conn_params = self.get_connection_params()</pre></li>

                </ol>

              <ol start="256" class="context-line">
                <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.connection = self.get_new_connection(conn_params)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='257' class="post-context" id="post126093136901248">

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.set_autocommit(self.settings_dict[&quot;AUTOCOMMIT&quot;])</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.init_connection_state()</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        connection_created.send(sender=self.__class__, connection=self)</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.run_on_commit = []</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre></pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901248">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>conn_params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;context&#x27;: &lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;,
 &#x27;cursor_factory&#x27;: &lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;prepare_threshold&#x27;: None,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>max_age</td>
                    <td class="code"><pre>0</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py</code>, line 26, in inner



            <div class="context" id="c126093136901376">

                <ol start="19" class="pre-context" id="pre126093136901376">

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                get_running_loop()</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            except RuntimeError:</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                pass</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            else:</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                if not os.environ.get(&quot;DJANGO_ALLOW_ASYNC_UNSAFE&quot;):</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                    raise SynchronousOnlyOperation(message)</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            # Pass onward.</pre></li>

                </ol>

              <ol start="26" class="context-line">
                <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='27' class="post-context" id="post126093136901376">

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>        return inner</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>    # If the message is actually a function, then be a no-arguments decorator.</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>    if callable(message):</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>        func = message</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901376">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;,
 {&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
  &#x27;context&#x27;: &lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;,
  &#x27;cursor_factory&#x27;: &lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;,
  &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
  &#x27;host&#x27;: &#x27;db&#x27;,
  &#x27;port&#x27;: &#x27;5432&#x27;,
  &#x27;prepare_threshold&#x27;: None,
  &#x27;user&#x27;: &#x27;postgres&#x27;})</pre></td>
                  </tr>

                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function DatabaseWrapper.get_new_connection at 0x72ae5b3dd4e0&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>message</td>
                    <td class="code"><pre>&#x27;You cannot call this from an async context - use a thread or sync_to_async.&#x27;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/postgresql/base.py</code>, line 333, in get_new_connection



            <div class="context" id="c126093136901440">

                <ol start="326" class="pre-context" id="pre126093136901440">

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>                    f&quot;specified. Use one of the psycopg.IsolationLevel values.&quot;</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>                )</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        if self.pool:</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # If nothing else has opened the pool, open it now.</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            self.pool.open()</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            connection = self.pool.getconn()</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        else:</pre></li>

                </ol>

              <ol start="333" class="context-line">
                <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            connection = self.Database.connect(**conn_params)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='334' class="post-context" id="post126093136901440">

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        if set_isolation_level:</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            connection.isolation_level = self.isolation_level</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        if not is_psycopg3:</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # Register dummy loads() to avoid a round trip from psycopg2&#x27;s</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # decode to json.dumps() to json.loads(), when using a custom</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # decoder in JSONField.</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901440">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>conn_params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;context&#x27;: &lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;,
 &#x27;cursor_factory&#x27;: &lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;prepare_threshold&#x27;: None,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>options</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>set_isolation_level</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame user">

            <code class="fname">/usr/local/lib/python3.14/site-packages/psycopg/connection.py</code>, line 100, in connect



            <div class="context" id="c126093136901504">

                <ol start="93" class="pre-context" id="pre126093136901504">

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        Connect to a database server and return a new `Connection` instance.</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        params = cls._get_connection_params(conninfo, **kwargs)</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        timeout = timeout_from_conninfo(params)</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        rv = None</pre></li>

                </ol>

              <ol start="100" class="context-line">
                <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        attempts = conninfo_attempts(params)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='101' class="post-context" id="post126093136901504">

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        conn_errors: list[tuple[e.Error, str]] = []</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        for attempt in attempts:</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            tdescr = (attempt.get(&quot;host&quot;), attempt.get(&quot;port&quot;), attempt.get(&quot;hostaddr&quot;))</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            descr = &quot;host: %r, port: %r, hostaddr: %r&quot; % tdescr</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            logger.debug(&quot;connection attempt: %s&quot;, descr)</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            try:</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901504">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>autocommit</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;psycopg.Connection&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>conninfo</td>
                    <td class="code"><pre>&#x27;&#x27;</pre></td>
                  </tr>

                  <tr>
                    <td>context</td>
                    <td class="code"><pre>&lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>cursor_factory</td>
                    <td class="code"><pre>&lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>prepare_threshold</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>row_factory</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>rv</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>timeout</td>
                    <td class="code"><pre>130</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame user">

            <code class="fname">/usr/local/lib/python3.14/site-packages/psycopg/_conninfo_attempts.py</code>, line 55, in conninfo_attempts



            <div class="context" id="c126093139195776">

                <ol start="48" class="pre-context" id="pre126093139195776">

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>                f&quot;failed to resolve host {attempt.get(&#x27;host&#x27;)!r}: {ex}&quot;</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>            )</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>            logger.debug(&quot;%s&quot;, last_exc)</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre></pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    if not attempts:</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        assert last_exc</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        # We couldn&#x27;t resolve anything</pre></li>

                </ol>

              <ol start="55" class="context-line">
                <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        raise last_exc
            ^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='56' class="post-context" id="post126093139195776">

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre></pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    if get_param(params, &quot;load_balance_hosts&quot;) == &quot;random&quot;:</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        shuffle(attempts)</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre></pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    # Order matters: first try all the load-balanced host in standby mode,</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    # then allow primary</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093139195776">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>attempt</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>attempts</td>
                    <td class="code"><pre>[]</pre></td>
                  </tr>

                  <tr>
                    <td>last_exc</td>
                    <td class="code"><pre>OperationalError(&quot;failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve&quot;)</pre></td>
                  </tr>

                  <tr>
                    <td>params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>prefer_standby</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


          <li class="cause"><h3>

            The above exception (failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve) was the direct cause of the following exception:

        </h3></li>

        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/core/handlers/exception.py</code>, line 42, in inner



            <div class="context" id="c126093136899264">

                <ol start="35" class="pre-context" id="pre126093136899264">

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>    can rely on getting a response instead of an exception.</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>    &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>    if iscoroutinefunction(get_response):</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre></pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>        @wraps(get_response)</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>        async def inner(request):</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>            try:</pre></li>

                </ol>

              <ol start="42" class="context-line">
                <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>                response = await get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='43' class="post-context" id="post126093136899264">

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>            except Exception as exc:</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>                response = await sync_to_async(</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>                    response_for_exception, thread_sensitive=False</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>                )(request, exc)</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre>            return response</pre></li>

                  <li onclick="toggle('pre126093136899264', 'post126093136899264')"><pre></pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136899264">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>OperationalError(&quot;failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve&quot;)</pre></td>
                  </tr>

                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response_async of &lt;django.core.handlers.asgi.ASGIHandler object at 0x72ae5b446a50&gt;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;ASGIRequest: GET &#x27;/api/messages/&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/core/handlers/base.py</code>, line 254, in _get_response_async



            <div class="context" id="c126093136899584">

                <ol start="247" class="pre-context" id="pre126093136899584">

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>            # If it is a synchronous view, run it in a subthread</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>            if not iscoroutinefunction(wrapped_callback):</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                wrapped_callback = sync_to_async(</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                    wrapped_callback, thread_sensitive=True</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                )</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>            try:</pre></li>

                </ol>

              <ol start="254" class="context-line">
                <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                response = await wrapped_callback(
                                </pre> <span>…</span></li>
              </ol>

                <ol start='255' class="post-context" id="post126093136899584">

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                    request, *callback_args, **callback_kwargs</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                )</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>            except Exception as e:</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                response = await sync_to_async(</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                    self.process_exception_by_middleware,</pre></li>

                  <li onclick="toggle('pre126093136899584', 'post126093136899584')"><pre>                    thread_sensitive=True,</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136899584">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function messages at 0x72ae5afe2820&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>

                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;asgiref.sync.SyncToAsync object at 0x72ae5b447a10&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;ASGIRequest: GET &#x27;/api/messages/&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.asgi.ASGIHandler object at 0x72ae5b446a50&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;asgiref.sync.SyncToAsync object at 0x72ae58a34290&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame user">

            <code class="fname">/usr/local/lib/python3.14/site-packages/asgiref/sync.py</code>, line 508, in func



            <div class="context" id="c126093136902528">

                <ol start="501" class="pre-context" id="pre126093136902528">

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>        # re-homes any Local storage to the worker thread so it stays visible</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>        # there (see _restore_context), and finally calls ``child``.</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>        def func(child: Callable[[], _R]) -&gt; _R:</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>            def run_child() -&gt; _R:</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>                _restore_context(context)</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>                return child()</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre></pre></li>

                </ol>

              <ol start="508" class="context-line">
                <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>            return context.run(run_child)
                        ^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='509' class="post-context" id="post126093136902528">

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>        task_context: list[asyncio.Task[Any]] = []</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>        # Run the code in the right thread</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>        exec_coro = loop.run_in_executor(</pre></li>

                  <li onclick="toggle('pre126093136902528', 'post126093136902528')"><pre>            executor,</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902528">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>child</td>
                    <td class="code"><pre>functools.partial(&lt;function messages at 0x72ae5afe2820&gt;, &lt;ASGIRequest: GET &#x27;/api/messages/&#x27;&gt;)</pre></td>
                  </tr>

                  <tr>
                    <td>context</td>
                    <td class="code"><pre>&lt;_contextvars.Context object at 0x72ae5afd8ec0&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>run_child</td>
                    <td class="code"><pre>&lt;function SyncToAsync.__call__.&lt;locals&gt;.func.&lt;locals&gt;.run_child at 0x72ae58c64f60&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame user">

            <code class="fname">/usr/local/lib/python3.14/site-packages/asgiref/sync.py</code>, line 506, in run_child



            <div class="context" id="c126093136902464">

                <ol start="499" class="pre-context" id="pre126093136902464">

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>        # On the worker thread, thread_handler runs ``func(child)``. ``func``</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>        # enters ``context`` (via context.run); then, inside it, ``run_child``</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>        # re-homes any Local storage to the worker thread so it stays visible</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>        # there (see _restore_context), and finally calls ``child``.</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>        def func(child: Callable[[], _R]) -&gt; _R:</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>            def run_child() -&gt; _R:</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>                _restore_context(context)</pre></li>

                </ol>

              <ol start="506" class="context-line">
                <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>                return child()
                            ^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='507' class="post-context" id="post126093136902464">

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>            return context.run(run_child)</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>        task_context: list[asyncio.Task[Any]] = []</pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902464', 'post126093136902464')"><pre>        # Run the code in the right thread</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902464">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>child</td>
                    <td class="code"><pre>functools.partial(&lt;function messages at 0x72ae5afe2820&gt;, &lt;ASGIRequest: GET &#x27;/api/messages/&#x27;&gt;)</pre></td>
                  </tr>

                  <tr>
                    <td>context</td>
                    <td class="code"><pre>&lt;_contextvars.Context object at 0x72ae5afd8ec0&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/views/decorators/http.py</code>, line 64, in inner



            <div class="context" id="c126093136902400">

                <ol start="57" class="pre-context" id="pre126093136902400">

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                        &quot;Method Not Allowed (%s): %s&quot;,</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                        request.method,</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                        request.path,</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                        response=response,</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                        request=request,</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                    )</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                    return response</pre></li>

                </ol>

              <ol start="64" class="context-line">
                <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>                return func(request, *args, **kwargs)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='65' class="post-context" id="post126093136902400">

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>        return inner</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre>    return decorator</pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902400', 'post126093136902400')"><pre></pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902400">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>

                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function messages at 0x72ae5afe2770&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;ASGIRequest: GET &#x27;/api/messages/&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>request_method_list</td>
                    <td class="code"><pre>[&#x27;GET&#x27;, &#x27;POST&#x27;]</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame user">

            <code class="fname">/home/my-cool-app/demo/views.py</code>, line 30, in messages



            <div class="context" id="c126093136902336">

                <ol start="23" class="pre-context" id="pre126093136902336">

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>        saved_messages = Message.objects.order_by(&quot;-created_at&quot;).values(</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>            &quot;id&quot;,</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>            &quot;text&quot;,</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>            &quot;created_at&quot;,</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>        )</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>        return JsonResponse(</pre></li>

                </ol>

              <ol start="30" class="context-line">
                <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>            {&quot;messages&quot;: list(saved_messages)}
                             ^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='31' class="post-context" id="post126093136902336">

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>        )</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>    try:</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>        data = json.loads(request.body)</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>    except json.JSONDecodeError:</pre></li>

                  <li onclick="toggle('pre126093136902336', 'post126093136902336')"><pre>        return JsonResponse(</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902336">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;ASGIRequest: GET &#x27;/api/messages/&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>saved_messages</td>
                    <td class="code"><pre>Error in formatting: OperationalError: failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/models/query.py</code>, line 390, in __iter__



            <div class="context" id="c126093136902272">

                <ol start="383" class="pre-context" id="pre126093136902272">

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>            2. sql.compiler.results_iter()</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>               - Returns one row at time. At this point the rows are still just</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>                 tuples. In some cases the return values are converted to</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>                 Python values at this location.</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>            3. self.iterator()</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>               - Responsible for turning the rows into model objects.</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>        &quot;&quot;&quot;</pre></li>

                </ol>

              <ol start="390" class="context-line">
                <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>        self._fetch_all()
             ^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='391' class="post-context" id="post126093136902272">

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>        return iter(self._result_cache)</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>    def __aiter__(self):</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>        # Remember, __aiter__ itself is synchronous, it&#x27;s the thing it returns</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>        # that is async!</pre></li>

                  <li onclick="toggle('pre126093136902272', 'post126093136902272')"><pre>        async def generator():</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902272">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>Error in formatting: OperationalError: failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/models/query.py</code>, line 2000, in _fetch_all



            <div class="context" id="c126093136900288">

                <ol start="1993" class="pre-context" id="pre126093136900288">

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        c._known_related_objects = self._known_related_objects</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        c._iterable_class = self._iterable_class</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        c._fields = self._fields</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        return c</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre></pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>    def _fetch_all(self):</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        if self._result_cache is None:</pre></li>

                </ol>

              <ol start="2000" class="context-line">
                <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>            self._result_cache = list(self._iterable_class(self))
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='2001' class="post-context" id="post126093136900288">

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        if self._prefetch_related_lookups and not self._prefetch_done:</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>            self._prefetch_related_objects()</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre></pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>    def _next_is_sticky(self):</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136900288', 'post126093136900288')"><pre>        Indicate that the next filter call and the one following that should</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136900288">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>Error in formatting: OperationalError: failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/models/query.py</code>, line 222, in __iter__



            <div class="context" id="c126093136902208">

                <ol start="215" class="pre-context" id="pre126093136902208">

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>            # extra(select=...) cols are always at the start of the row.</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>            names = [</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>                *query.extra_select,</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>                *query.values_select,</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>                *query.annotation_select,</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>            ]</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>        indexes = range(len(names))</pre></li>

                </ol>

              <ol start="222" class="context-line">
                <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>        for row in compiler.results_iter(
                        </pre> <span>…</span></li>
              </ol>

                <ol start='223' class="post-context" id="post126093136902208">

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>            chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>        ):</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>            yield {names[i]: row[i] for i in indexes}</pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902208', 'post126093136902208')"><pre>class ValuesListIterable(BaseIterable):</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902208">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>compiler</td>
                    <td class="code"><pre>&lt;SQLCompiler model=Message connection=&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt; using=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>indexes</td>
                    <td class="code"><pre>range(0, 3)</pre></td>
                  </tr>

                  <tr>
                    <td>names</td>
                    <td class="code"><pre>[&#x27;id&#x27;, &#x27;text&#x27;, &#x27;created_at&#x27;]</pre></td>
                  </tr>

                  <tr>
                    <td>query</td>
                    <td class="code"><pre>&lt;django.db.models.sql.query.Query object at 0x72ae58c46030&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>queryset</td>
                    <td class="code"><pre>Error in formatting: OperationalError: failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.db.models.query.ValuesIterable object at 0x72ae58a343b0&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/models/sql/compiler.py</code>, line 1573, in results_iter



            <div class="context" id="c126093136902144">

                <ol start="1566" class="pre-context" id="pre126093136902144">

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        results=None,</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        tuple_expected=False,</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        chunked_fetch=False,</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        chunk_size=GET_ITERATOR_CHUNK_SIZE,</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>    ):</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        &quot;&quot;&quot;Return an iterator over the results from executing this query.&quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        if results is None:</pre></li>

                </ol>

              <ol start="1573" class="context-line">
                <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>            results = self.execute_sql(
                            </pre> <span>…</span></li>
              </ol>

                <ol start='1574' class="post-context" id="post126093136902144">

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>                MULTI, chunked_fetch=chunked_fetch, chunk_size=chunk_size</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>            )</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        fields = [s[0] for s in self.select[0 : self.col_count]]</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        converters = self.get_converters(fields)</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        rows = chain.from_iterable(results)</pre></li>

                  <li onclick="toggle('pre126093136902144', 'post126093136902144')"><pre>        if converters:</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902144">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>chunk_size</td>
                    <td class="code"><pre>100</pre></td>
                  </tr>

                  <tr>
                    <td>chunked_fetch</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

                  <tr>
                    <td>results</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;SQLCompiler model=Message connection=&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt; using=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>tuple_expected</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/models/sql/compiler.py</code>, line 1622, in execute_sql



            <div class="context" id="c126093136902080">

                <ol start="1615" class="pre-context" id="pre126093136902080">

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            if result_type == MULTI:</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>                return iter([])</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            else:</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>                return</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>        if chunked_fetch:</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            cursor = self.connection.chunked_cursor()</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>        else:</pre></li>

                </ol>

              <ol start="1622" class="context-line">
                <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            cursor = self.connection.cursor()
                           ^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='1623' class="post-context" id="post126093136902080">

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>        try:</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            cursor.execute(sql, params)</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>        except Exception:</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            # Might fail for server-side cursors (e.g. connection closed)</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            cursor.close()</pre></li>

                  <li onclick="toggle('pre126093136902080', 'post126093136902080')"><pre>            raise</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902080">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>chunk_size</td>
                    <td class="code"><pre>100</pre></td>
                  </tr>

                  <tr>
                    <td>chunked_fetch</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

                  <tr>
                    <td>params</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>

                  <tr>
                    <td>result_type</td>
                    <td class="code"><pre>&#x27;multi&#x27;</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;SQLCompiler model=Message connection=&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt; using=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>sql</td>
                    <td class="code"><pre>(&#x27;SELECT &quot;demo_message&quot;.&quot;id&quot; AS &quot;id&quot;, &quot;demo_message&quot;.&quot;text&quot; AS &quot;text&quot;, &#x27;
 &#x27;&quot;demo_message&quot;.&quot;created_at&quot; AS &quot;created_at&quot; FROM &quot;demo_message&quot; ORDER BY 3 &#x27;
 &#x27;DESC&#x27;)</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py</code>, line 26, in inner



            <div class="context" id="c126093136902016">

                <ol start="19" class="pre-context" id="pre126093136902016">

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>                get_running_loop()</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>            except RuntimeError:</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>                pass</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>            else:</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>                if not os.environ.get(&quot;DJANGO_ALLOW_ASYNC_UNSAFE&quot;):</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>                    raise SynchronousOnlyOperation(message)</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>            # Pass onward.</pre></li>

                </ol>

              <ol start="26" class="context-line">
                <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='27' class="post-context" id="post126093136902016">

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>        return inner</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre></pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>    # If the message is actually a function, then be a no-arguments decorator.</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>    if callable(message):</pre></li>

                  <li onclick="toggle('pre126093136902016', 'post126093136902016')"><pre>        func = message</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136902016">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;,)</pre></td>
                  </tr>

                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function BaseDatabaseWrapper.cursor at 0x72ae5c85d170&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>message</td>
                    <td class="code"><pre>&#x27;You cannot call this from an async context - use a thread or sync_to_async.&#x27;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py</code>, line 320, in cursor



            <div class="context" id="c126093136901952">

                <ol start="313" class="pre-context" id="pre126093136901952">

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>                return self.connection.close()</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>    # ##### Generic wrappers for PEP-249 connection methods #####</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>    @async_unsafe</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>    def cursor(self):</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>        &quot;&quot;&quot;Create a cursor, opening a connection if necessary.&quot;&quot;&quot;</pre></li>

                </ol>

              <ol start="320" class="context-line">
                <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>        return self._cursor()
                    ^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='321' class="post-context" id="post126093136901952">

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>    @async_unsafe</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>    def commit(self):</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>        &quot;&quot;&quot;Commit a transaction and reset the dirty flag.&quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>        self.validate_thread_sharing()</pre></li>

                  <li onclick="toggle('pre126093136901952', 'post126093136901952')"><pre>        self.validate_no_atomic_block()</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901952">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py</code>, line 296, in _cursor



            <div class="context" id="c126093136901888">

                <ol start="289" class="pre-context" id="pre126093136901888">

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>            wrapped_cursor = self.make_debug_cursor(cursor)</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>        else:</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>            wrapped_cursor = self.make_cursor(cursor)</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>        return wrapped_cursor</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>    def _cursor(self, name=None):</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>        self.close_if_health_check_failed()</pre></li>

                </ol>

              <ol start="296" class="context-line">
                <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>        self.ensure_connection()
             ^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='297' class="post-context" id="post126093136901888">

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>        with self.wrap_database_errors:</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>            return self._prepare_cursor(self.create_cursor(name))</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>    def _commit(self):</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>        if self.connection is not None:</pre></li>

                  <li onclick="toggle('pre126093136901888', 'post126093136901888')"><pre>            with debug_transaction(self, &quot;COMMIT&quot;), self.wrap_database_errors:</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901888">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>name</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py</code>, line 26, in inner



            <div class="context" id="c126093136901824">

                <ol start="19" class="pre-context" id="pre126093136901824">

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>                get_running_loop()</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>            except RuntimeError:</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>                pass</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>            else:</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>                if not os.environ.get(&quot;DJANGO_ALLOW_ASYNC_UNSAFE&quot;):</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>                    raise SynchronousOnlyOperation(message)</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>            # Pass onward.</pre></li>

                </ol>

              <ol start="26" class="context-line">
                <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='27' class="post-context" id="post126093136901824">

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>        return inner</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>    # If the message is actually a function, then be a no-arguments decorator.</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>    if callable(message):</pre></li>

                  <li onclick="toggle('pre126093136901824', 'post126093136901824')"><pre>        func = message</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901824">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;,)</pre></td>
                  </tr>

                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function BaseDatabaseWrapper.ensure_connection at 0x72ae5c85cca0&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>message</td>
                    <td class="code"><pre>&#x27;You cannot call this from an async context - use a thread or sync_to_async.&#x27;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py</code>, line 278, in ensure_connection



            <div class="context" id="c126093136901632">

                <ol start="271" class="pre-context" id="pre126093136901632">

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>    def ensure_connection(self):</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>        &quot;&quot;&quot;Guarantee that a connection to the database is established.&quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>        if self.connection is None:</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>            if self.in_atomic_block and self.closed_in_transaction:</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>                raise ProgrammingError(</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>                    &quot;Cannot open a new connection in an atomic block.&quot;</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>                )</pre></li>

                </ol>

              <ol start="278" class="context-line">
                <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>            with self.wrap_database_errors:
                      ^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='279' class="post-context" id="post126093136901632">

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>                self.connect()</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>    # ##### Backend-specific wrappers for PEP-249 connection methods #####</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>    def _prepare_cursor(self, cursor):</pre></li>

                  <li onclick="toggle('pre126093136901632', 'post126093136901632')"><pre>        &quot;&quot;&quot;</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901632">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/utils.py</code>, line 94, in __exit__



            <div class="context" id="c126093136901760">

                <ol start="87" class="pre-context" id="pre126093136901760">

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>            db_exc_type = getattr(self.wrapper.Database, dj_exc_type.__name__)</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>            if issubclass(exc_type, db_exc_type):</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>                dj_exc_value = dj_exc_type(*exc_value.args)</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>                # Only set the &#x27;errors_occurred&#x27; flag for errors that may make</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>                # the connection unusable.</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>                if dj_exc_type not in (DataError, IntegrityError):</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>                    self.wrapper.errors_occurred = True</pre></li>

                </ol>

              <ol start="94" class="context-line">
                <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>                raise dj_exc_value.with_traceback(traceback) from exc_value
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='95' class="post-context" id="post126093136901760">

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>    def __call__(self, func):</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>        # Note that we are intentionally not using @wraps here for performance</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>        # reasons. Refs #21109.</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>        def inner(*args, **kwargs):</pre></li>

                  <li onclick="toggle('pre126093136901760', 'post126093136901760')"><pre>            with self:</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901760">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>db_exc_type</td>
                    <td class="code"><pre>&lt;class &#x27;psycopg.OperationalError&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>dj_exc_type</td>
                    <td class="code"><pre>&lt;class &#x27;django.db.utils.OperationalError&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>dj_exc_value</td>
                    <td class="code"><pre>OperationalError(&quot;failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve&quot;)</pre></td>
                  </tr>

                  <tr>
                    <td>exc_type</td>
                    <td class="code"><pre>&lt;class &#x27;psycopg.OperationalError&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>exc_value</td>
                    <td class="code"><pre>OperationalError(&quot;failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve&quot;)</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.db.utils.DatabaseErrorWrapper object at 0x72ae5b052710&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>traceback</td>
                    <td class="code"><pre>&lt;traceback object at 0x72ae58a23640&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py</code>, line 279, in ensure_connection



            <div class="context" id="c126093136901696">

                <ol start="272" class="pre-context" id="pre126093136901696">

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        &quot;&quot;&quot;Guarantee that a connection to the database is established.&quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        if self.connection is None:</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>            if self.in_atomic_block and self.closed_in_transaction:</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                raise ProgrammingError(</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                    &quot;Cannot open a new connection in an atomic block.&quot;</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                )</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>            with self.wrap_database_errors:</pre></li>

                </ol>

              <ol start="279" class="context-line">
                <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>                self.connect()
                     ^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='280' class="post-context" id="post126093136901696">

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>    # ##### Backend-specific wrappers for PEP-249 connection methods #####</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>    def _prepare_cursor(self, cursor):</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901696', 'post126093136901696')"><pre>        Validate the connection is usable and perform database cursor wrapping.</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901696">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py</code>, line 26, in inner



            <div class="context" id="c126093136901568">

                <ol start="19" class="pre-context" id="pre126093136901568">

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                get_running_loop()</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            except RuntimeError:</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                pass</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            else:</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                if not os.environ.get(&quot;DJANGO_ALLOW_ASYNC_UNSAFE&quot;):</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>                    raise SynchronousOnlyOperation(message)</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            # Pass onward.</pre></li>

                </ol>

              <ol start="26" class="context-line">
                <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='27' class="post-context" id="post126093136901568">

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>        return inner</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>    # If the message is actually a function, then be a no-arguments decorator.</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>    if callable(message):</pre></li>

                  <li onclick="toggle('pre126093136901568', 'post126093136901568')"><pre>        func = message</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901568">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;,)</pre></td>
                  </tr>

                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function BaseDatabaseWrapper.connect at 0x72ae5c85ca90&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>message</td>
                    <td class="code"><pre>&#x27;You cannot call this from an async context - use a thread or sync_to_async.&#x27;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py</code>, line 256, in connect



            <div class="context" id="c126093136901248">

                <ol start="249" class="pre-context" id="pre126093136901248">

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.close_at = None if max_age is None else time.monotonic() + max_age</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.closed_in_transaction = False</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.errors_occurred = False</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        # New connections are healthy.</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.health_check_done = True</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        # Establish the connection</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        conn_params = self.get_connection_params()</pre></li>

                </ol>

              <ol start="256" class="context-line">
                <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.connection = self.get_new_connection(conn_params)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='257' class="post-context" id="post126093136901248">

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.set_autocommit(self.settings_dict[&quot;AUTOCOMMIT&quot;])</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.init_connection_state()</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        connection_created.send(sender=self.__class__, connection=self)</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre>        self.run_on_commit = []</pre></li>

                  <li onclick="toggle('pre126093136901248', 'post126093136901248')"><pre></pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901248">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>conn_params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;context&#x27;: &lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;,
 &#x27;cursor_factory&#x27;: &lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;prepare_threshold&#x27;: None,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>max_age</td>
                    <td class="code"><pre>0</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py</code>, line 26, in inner



            <div class="context" id="c126093136901376">

                <ol start="19" class="pre-context" id="pre126093136901376">

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                get_running_loop()</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            except RuntimeError:</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                pass</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            else:</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                if not os.environ.get(&quot;DJANGO_ALLOW_ASYNC_UNSAFE&quot;):</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>                    raise SynchronousOnlyOperation(message)</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            # Pass onward.</pre></li>

                </ol>

              <ol start="26" class="context-line">
                <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='27' class="post-context" id="post126093136901376">

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>        return inner</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>    # If the message is actually a function, then be a no-arguments decorator.</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>    if callable(message):</pre></li>

                  <li onclick="toggle('pre126093136901376', 'post126093136901376')"><pre>        func = message</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901376">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;,
 {&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
  &#x27;context&#x27;: &lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;,
  &#x27;cursor_factory&#x27;: &lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;,
  &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
  &#x27;host&#x27;: &#x27;db&#x27;,
  &#x27;port&#x27;: &#x27;5432&#x27;,
  &#x27;prepare_threshold&#x27;: None,
  &#x27;user&#x27;: &#x27;postgres&#x27;})</pre></td>
                  </tr>

                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function DatabaseWrapper.get_new_connection at 0x72ae5b3dd4e0&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>message</td>
                    <td class="code"><pre>&#x27;You cannot call this from an async context - use a thread or sync_to_async.&#x27;</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame django">

            <code class="fname">/usr/local/lib/python3.14/site-packages/django/db/backends/postgresql/base.py</code>, line 333, in get_new_connection



            <div class="context" id="c126093136901440">

                <ol start="326" class="pre-context" id="pre126093136901440">

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>                    f&quot;specified. Use one of the psycopg.IsolationLevel values.&quot;</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>                )</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        if self.pool:</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # If nothing else has opened the pool, open it now.</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            self.pool.open()</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            connection = self.pool.getconn()</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        else:</pre></li>

                </ol>

              <ol start="333" class="context-line">
                <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            connection = self.Database.connect(**conn_params)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='334' class="post-context" id="post126093136901440">

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        if set_isolation_level:</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            connection.isolation_level = self.isolation_level</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>        if not is_psycopg3:</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # Register dummy loads() to avoid a round trip from psycopg2&#x27;s</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # decode to json.dumps() to json.loads(), when using a custom</pre></li>

                  <li onclick="toggle('pre126093136901440', 'post126093136901440')"><pre>            # decoder in JSONField.</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901440">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>conn_params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;context&#x27;: &lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;,
 &#x27;cursor_factory&#x27;: &lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;prepare_threshold&#x27;: None,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>options</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>

                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;DatabaseWrapper vendor=&#x27;postgresql&#x27; alias=&#x27;default&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>set_isolation_level</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame user">

            <code class="fname">/usr/local/lib/python3.14/site-packages/psycopg/connection.py</code>, line 100, in connect



            <div class="context" id="c126093136901504">

                <ol start="93" class="pre-context" id="pre126093136901504">

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        Connect to a database server and return a new `Connection` instance.</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        &quot;&quot;&quot;</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre></pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        params = cls._get_connection_params(conninfo, **kwargs)</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        timeout = timeout_from_conninfo(params)</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        rv = None</pre></li>

                </ol>

              <ol start="100" class="context-line">
                <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        attempts = conninfo_attempts(params)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='101' class="post-context" id="post126093136901504">

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        conn_errors: list[tuple[e.Error, str]] = []</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>        for attempt in attempts:</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            tdescr = (attempt.get(&quot;host&quot;), attempt.get(&quot;port&quot;), attempt.get(&quot;hostaddr&quot;))</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            descr = &quot;host: %r, port: %r, hostaddr: %r&quot; % tdescr</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            logger.debug(&quot;connection attempt: %s&quot;, descr)</pre></li>

                  <li onclick="toggle('pre126093136901504', 'post126093136901504')"><pre>            try:</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093136901504">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>autocommit</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;psycopg.Connection&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>conninfo</td>
                    <td class="code"><pre>&#x27;&#x27;</pre></td>
                  </tr>

                  <tr>
                    <td>context</td>
                    <td class="code"><pre>&lt;psycopg.adapt.AdaptersMap object at 0x72ae5b0507d0&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>cursor_factory</td>
                    <td class="code"><pre>&lt;class &#x27;django.db.backends.postgresql.base.Cursor&#x27;&gt;</pre></td>
                  </tr>

                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>prepare_threshold</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>row_factory</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>rv</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>

                  <tr>
                    <td>timeout</td>
                    <td class="code"><pre>130</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>


        <li class="frame user">

            <code class="fname">/usr/local/lib/python3.14/site-packages/psycopg/_conninfo_attempts.py</code>, line 55, in conninfo_attempts



            <div class="context" id="c126093139195776">

                <ol start="48" class="pre-context" id="pre126093139195776">

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>                f&quot;failed to resolve host {attempt.get(&#x27;host&#x27;)!r}: {ex}&quot;</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>            )</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>            logger.debug(&quot;%s&quot;, last_exc)</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre></pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    if not attempts:</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        assert last_exc</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        # We couldn&#x27;t resolve anything</pre></li>

                </ol>

              <ol start="55" class="context-line">
                <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        raise last_exc
            ^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>

                <ol start='56' class="post-context" id="post126093139195776">

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre></pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    if get_param(params, &quot;load_balance_hosts&quot;) == &quot;random&quot;:</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>        shuffle(attempts)</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre></pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    # Order matters: first try all the load-balanced host in standby mode,</pre></li>

                  <li onclick="toggle('pre126093139195776', 'post126093139195776')"><pre>    # then allow primary</pre></li>

              </ol>

            </div>




              <details>
                <summary class="commands">Local vars</summary>

            <table class="vars" id="v126093139195776">
              <thead>
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Value</th>
                </tr>
              </thead>
              <tbody>

                  <tr>
                    <td>attempt</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>attempts</td>
                    <td class="code"><pre>[]</pre></td>
                  </tr>

                  <tr>
                    <td>last_exc</td>
                    <td class="code"><pre>OperationalError(&quot;failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve&quot;)</pre></td>
                  </tr>

                  <tr>
                    <td>params</td>
                    <td class="code"><pre>{&#x27;client_encoding&#x27;: &#x27;UTF8&#x27;,
 &#x27;dbname&#x27;: &#x27;my-cool-app&#x27;,
 &#x27;host&#x27;: &#x27;db&#x27;,
 &#x27;port&#x27;: &#x27;5432&#x27;,
 &#x27;user&#x27;: &#x27;postgres&#x27;}</pre></td>
                  </tr>

                  <tr>
                    <td>prefer_standby</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>

              </tbody>
            </table>
            </details>

        </li>

    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="OperationalError at /api/messages/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: GET
Request URL: http://backend:8000/api/messages/

Django Version: 6.0.5
Python Version: 3.14.7
Installed Applications:
[&#x27;demo.apps.DemoConfig&#x27;,
 &#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;middleware.csp_nonce.ContentSecurityPolicyNonceMiddleware&#x27;]



Traceback (most recent call last):
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py", line 279, in ensure_connection
    self.connect()
    ^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py", line 256, in connect
    self.connection = self.get_new_connection(conn_params)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/postgresql/base.py", line 333, in get_new_connection
    connection = self.Database.connect(**conn_params)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/psycopg/connection.py", line 100, in connect
    attempts = conninfo_attempts(params)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/psycopg/_conninfo_attempts.py", line 55, in conninfo_attempts
    raise last_exc
    ^^^^^^^^^^^^^^

The above exception (failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve) was the direct cause of the following exception:
  File "/usr/local/lib/python3.14/site-packages/django/core/handlers/exception.py", line 42, in inner
    response = await get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/core/handlers/base.py", line 254, in _get_response_async
    response = await wrapped_callback(

  File "/usr/local/lib/python3.14/site-packages/asgiref/sync.py", line 508, in func
    return context.run(run_child)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/asgiref/sync.py", line 506, in run_child
    return child()
           ^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/views/decorators/http.py", line 64, in inner
    return func(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/my-cool-app/demo/views.py", line 30, in messages
    {&quot;messages&quot;: list(saved_messages)}
                 ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/models/query.py", line 390, in __iter__
    self._fetch_all()
    ^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/models/query.py", line 2000, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/models/query.py", line 222, in __iter__
    for row in compiler.results_iter(

  File "/usr/local/lib/python3.14/site-packages/django/db/models/sql/compiler.py", line 1573, in results_iter
    results = self.execute_sql(

  File "/usr/local/lib/python3.14/site-packages/django/db/models/sql/compiler.py", line 1622, in execute_sql
    cursor = self.connection.cursor()
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py", line 320, in cursor
    return self._cursor()
           ^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py", line 296, in _cursor
    self.ensure_connection()
    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py", line 278, in ensure_connection
    with self.wrap_database_errors:
         ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/utils.py", line 94, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py", line 279, in ensure_connection
    self.connect()
    ^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/base/base.py", line 256, in connect
    self.connection = self.get_new_connection(conn_params)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/django/db/backends/postgresql/base.py", line 333, in get_new_connection
    connection = self.Database.connect(**conn_params)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/psycopg/connection.py", line 100, in connect
    attempts = conninfo_attempts(params)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/site-packages/psycopg/_conninfo_attempts.py", line 55, in conninfo_attempts
    raise last_exc
    ^^^^^^^^^^^^^^

Exception Type: OperationalError at /api/messages/
Exception Value: failed to resolve host &#x27;db&#x27;: [Errno -2] Name does not resolve
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>



    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>


  <h3 id="get-info">GET</h3>

    <p>No GET data</p>


  <h3 id="post-info">POST</h3>

    <p>No POST data</p>


  <h3 id="files-info">FILES</h3>

    <p>No FILES data</p>


  <h3 id="cookie-info">COOKIES</h3>

    <p>No cookie data</p>


  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th scope="col">Variable</th>
        <th scope="col">Value</th>
      </tr>
    </thead>
    <tbody>

        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>

        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>

        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;backend:8000&#x27;</pre></td>
        </tr>

        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>&#x27;curl/8.18.0&#x27;</pre></td>
        </tr>

        <tr>
          <td>HTTP_X_FORWARDED_FOR</td>
          <td class="code"><pre>&#x27;172.21.0.1&#x27;</pre></td>
        </tr>

        <tr>
          <td>HTTP_X_FORWARDED_PROTO</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>

        <tr>
          <td>HTTP_X_REAL_IP</td>
          <td class="code"><pre>&#x27;172.21.0.1&#x27;</pre></td>
        </tr>

        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/messages/&#x27;</pre></td>
        </tr>

        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>

        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;172.21.0.3&#x27;</pre></td>
        </tr>

        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;172.21.0.3&#x27;</pre></td>
        </tr>

        <tr>
          <td>REMOTE_PORT</td>
          <td class="code"><pre>35544</pre></td>
        </tr>

        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;GET&#x27;</pre></td>
        </tr>

        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>

        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;172.21.0.4&#x27;</pre></td>
        </tr>

        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>

        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>True</pre></td>
        </tr>

        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>

    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>my-cool-app.settings.dev.local_postgres</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th scope="col">Setting</th>
        <th scope="col">Value</th>
      </tr>
    </thead>
    <tbody>

        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>

        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;backend&#x27;, &#x27;*&#x27;]</pre></td>
        </tr>

        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>

        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/home/my-cool-app&#x27;)</pre></td>
        </tr>

        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>

        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>

        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>

        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>

        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>

        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>

        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>

        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>

        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>

        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.postgresql&#x27;,
             &#x27;HOST&#x27;: &#x27;db&#x27;,
             &#x27;NAME&#x27;: &#x27;my-cool-app&#x27;,
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;5432&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;postgres&#x27;}}</pre></td>
        </tr>

        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>

        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>

        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>

        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>

        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>

        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>

        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>

        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>

        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>

        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>

        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>

        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>

        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>

        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>

        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>

        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>

        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>

        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>

        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>

        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>

        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>

        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>

        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>

        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>

        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>

        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>

        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;demo.apps.DemoConfig&#x27;,
 &#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;]</pre></td>
        </tr>

        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;ht&#x27;, &#x27;Haitian Creole&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;ug&#x27;, &#x27;Uyghur&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>

        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ug&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>

        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>

        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>

        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>

        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>

        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>

        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>

        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;middleware.csp_nonce.ContentSecurityPolicyNonceMiddleware&#x27;]</pre></td>
        </tr>

        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>

        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>

        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>

        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;my-cool-app.urls&#x27;</pre></td>
        </tr>

        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>

        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>

        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>

        <tr>
          <td>SECURE_CSP</td>
          <td class="code"><pre>{}</pre></td>
        </tr>

        <tr>
          <td>SECURE_CSP_REPORT_ONLY</td>
          <td class="code"><pre>{}</pre></td>
        </tr>

        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>

        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>

        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>

        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>

        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>

        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>

        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>

        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>

        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>

        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>

        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>

        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;my-cool-app.settings.dev.local_postgres&#x27;</pre></td>
        </tr>

        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>

        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>

        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>

        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>

        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>

        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>

        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>

        <tr>
          <td>TASKS</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.tasks.backends.immediate.ImmediateBackend&#x27;}}</pre></td>
        </tr>

        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [PosixPath(&#x27;/home/my-cool-app/templates&#x27;)],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>

        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>

        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>

        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>

        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>

        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>

        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;UTC&#x27;</pre></td>
        </tr>

        <tr>
          <td>URLIZE_ASSUME_HTTPS</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>

        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>

        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>

        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;my-cool-app.wsgi.application&#x27;</pre></td>
        </tr>

        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>

        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>

    </tbody>
  </table>

</div>
</main>


  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </footer>

</body>
</html>
ronicbrown@CAZVW0FVAA3-59K:~/my-cool-app/app$
