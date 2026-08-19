# Tickets Ready (auto-file candidates)

304 findings meet the auto-ticket threshold (score ≥ 40).

## Ticket 1: [P3] zlib: heap-based buffer over-read and overflow in inflate() in inflate.c via a large gzip header extra field

- **Score:** 53.5 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-37434  ·  **CWE:** CWE-787
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** critical  ·  **EPSS:** 0.17852 (pct 0.96912)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=24.5, epss=14.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-37434; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package zlib from 1.2.12-r0 to 1.2.12-r2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade zlib from 1.2.12-r0 to 1.2.12-r2

## Ticket 2: [P3] moment.js: regular expression denial of service

- **Score:** 53.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4055  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.09905 (pct 0.95159)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=14.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4055; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package moment from 2.0.0 to >=2.11.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade moment from 2.0.0 to >=2.11.2

## Ticket 3: [P3] node-ip: Incomplete fix for CVE-2023-42282

- **Score:** 53.2 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2024-29415  ·  **CWE:** CWE-918
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.08279 (pct 0.94429)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=24.5, epss=14.2, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Block outbound traffic to internal/metadata ranges at the firewall; disable the vulnerable fetcher.
- *full_remediation:* Validate and allow-list server-side request targets; use an outbound proxy with deny rules for RFC1918/metadata.
- *scanner_guidance:* node-ip: Incomplete fix for CVE-2023-42282

## Ticket 4: [P3] nodejs-jsonwebtoken: verification step bypass with an altered token

- **Score:** 52.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2015-9235  ·  **CWE:** CWE-20
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.08655 (pct 0.94643)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-9235; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package jsonwebtoken from 0.1.0 to 4.2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade jsonwebtoken from 0.1.0 to 4.2.2

## Ticket 5: [P3] tough-cookie: prototype pollution in cookie memstore

- **Score:** 51.5 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-26136  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.02542 (pct 0.83617)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=24.5, epss=12.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-26136; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tough-cookie from 2.4.3 to 4.1.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tough-cookie from 2.4.3 to 4.1.3

## Ticket 6: [P3] openssl: Memory corruption in the ASN.1 encoder

- **Score:** 51.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2108  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.77906 (pct 0.99534)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2108; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.19

## Ticket 7: [P3] mysql: general_log can write to configuration files, leading to privilege escalation (CPU Oct 2016)

- **Score:** 51.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6662  ·  **CWE:** CWE-264
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.6773 (pct 0.99257)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6662; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.52-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.52-0ubuntu0.14.04.1

## Ticket 8: [P3] glibc: stack guard protection bypass

- **Score:** 51.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2019-1010022  ·  **CWE:** CWE-119
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** low  ·  **EPSS:** 0.03223 (pct 0.87151)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* glibc: stack guard protection bypass

## Ticket 9: [P3] openssl: doapr_outch function does not verify that certain memory allocation succeeds

- **Score:** 51.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2842  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.53655 (pct 0.98906)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2842; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18

## Ticket 10: [P3] OpenSSL: Fix memory issues in BIO_*printf functions

- **Score:** 51.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-0799  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.32414 (pct 0.98185)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-0799; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18

## Ticket 11: [P3] OpenSSL: Double-free in DSA code

- **Score:** 51.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-0705  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.26335 (pct 0.97828)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-0705; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18

## Ticket 12: [P3] python: Heap overflow in zipimporter module

- **Score:** 51.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5636  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.26316 (pct 0.97826)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5636; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.3

## Ticket 13: [P3] libxml2: Incorrect limit used for port values

- **Score:** 51.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-7376  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.23286 (pct 0.97579)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-7376; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.10

## Ticket 14: [P3] git: path_name() integer truncation and overflow leading to buffer overflow

- **Score:** 51.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2324  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.18808 (pct 0.97032)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2324; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.3

## Ticket 15: [P3] git: path_name() integer truncation and overflow leading to buffer overflow

- **Score:** 51.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2315  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.17979 (pct 0.96928)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2315; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.3

## Ticket 16: [P3] curl: NTLM password overflow via integer overflow

- **Score:** 50.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-14618  ·  **CWE:** CWE-122
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.11115 (pct 0.95555)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-14618; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.17

## Ticket 17: [P3] php: buffer overflow in handling of long link names in tar phar archives

- **Score:** 50.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2554  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.10997 (pct 0.95511)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2554; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 18: [P3] libxml2: Use after free via namespace node in XPointer ranges

- **Score:** 50.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4658  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.08559 (pct 0.9459)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4658; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.9 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.9

## Ticket 19: [P3] libxml2: Format string vulnerability

- **Score:** 50.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4448  ·  **CWE:** CWE-134
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.07039 (pct 0.93626)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4448; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.9 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.9

## Ticket 20: [P3] perl-DBD-MySQL: Use after free in mysql_dr_error

- **Score:** 50.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2014-9906  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06026 (pct 0.92714)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2014-9906; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libdbd-mysql-perl from 4.025-1 to 4.025-1ubuntu0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libdbd-mysql-perl from 4.025-1 to 4.025-1ubuntu0.1

## Ticket 21: [P3] nodejs-lodash: command injection via template

- **Score:** 50.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2021-23337  ·  **CWE:** CWE-94
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.21333 (pct 0.97387)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=14.6, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2021-23337; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package lodash from 2.4.2 to 4.17.21 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade lodash from 2.4.2 to 4.17.21

## Ticket 22: [P3] perl-DBD-MySQL: Use after free when my_login fails

- **Score:** 50.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8949  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.04485 (pct 0.90647)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=25.0, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8949; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libdbd-mysql-perl from 4.025-1 to 4.025-1ubuntu0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libdbd-mysql-perl from 4.025-1 to 4.025-1ubuntu0.1

## Ticket 23: [P3] nodejs-ip: arbitrary code execution via the isPublic() function

- **Score:** 50.1 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-42282  ·  **CWE:** CWE-918
- **Endpoint:** Node.js
- **Severity:** low  ·  **EPSS:** 0.01613 (pct 0.73887)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=24.5, epss=11.1, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-42282; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ip from 1.1.5 to 2.0.1, 1.1.9 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ip from 1.1.5 to 2.0.1, 1.1.9

## Ticket 24: [P3] undici: Undici: HTTP Request Smuggling and Denial of Service due to duplicate Content-Length headers

- **Score:** 50.0 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-1525  ·  **CWE:** CWE-444
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.00493 (pct 0.40145)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=24.5, epss=6.0, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-1525; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package undici from 5.29.0 to 6.24.0, 7.24.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade undici from 5.29.0 to 6.24.0, 7.24.0

## Ticket 25: [P3] glibc: running ldd on malicious ELF leads to code execution because of wrong size computation

- **Score:** 49.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2019-1010023  ·  **CWE:** -
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** low  ·  **EPSS:** 0.03044 (pct 0.86385)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.0, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* glibc: running ldd on malicious ELF leads to code execution because of wrong size computation

## Ticket 26: [P3] http-cache-semantics: Regular Expression Denial of Service (ReDoS) vulnerability

- **Score:** 49.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-25881  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01613 (pct 0.73888)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=11.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-25881; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package http-cache-semantics from 3.8.1 to 4.1.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade http-cache-semantics from 3.8.1 to 4.1.1

## Ticket 27: [P3] crypto-js: PBKDF2 1,000 times weaker than specified in 1993 and 1.3M times weaker than current standard

- **Score:** 49.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2023-46233  ·  **CWE:** CWE-328
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.00635 (pct 0.47456)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=22.7, epss=7.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-46233; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package crypto-js from 3.3.0 to 4.2.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade crypto-js from 3.3.0 to 4.2.0

## Ticket 28: [P3] Incorrect sanitation of the 302 redirect field in HTTP transport metho ...

- **Score:** 49.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-3462  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.14555 (pct 0.9634)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=23.2, epss=14.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-3462; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apt from 1.0.1ubuntu2.10 to 1.0.1ubuntu2.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apt from 1.0.1ubuntu2.10 to 1.0.1ubuntu2.19

## Ticket 29: [P3] nodejs-lodash: prototype pollution in defaultsDeep function leading to modifying properties

- **Score:** 49.2 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2019-10744  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.05006 (pct 0.91502)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.7, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-10744; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package lodash from 2.4.2 to 4.17.12 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade lodash from 2.4.2 to 4.17.12

## Ticket 30: [P3] supervisor: Command injection via malicious XML-RPC request

- **Score:** 49.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-11610  ·  **CWE:** CWE-276
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.87378 (pct 0.99741)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=22.5, epss=15.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-11610; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package supervisor from 3.0b2-1 to 3.0b2-1ubuntu0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade supervisor from 3.0b2-1 to 3.0b2-1ubuntu0.1

## Ticket 31: [P3] git: cvsserver command injection

- **Score:** 48.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-14867  ·  **CWE:** CWE-78
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.35757 (pct 0.98329)  ·  **KEV:** no
- **Escalation potential:** 0.95

**Score breakdown:** cvss=22.5, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-14867; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.7

## Ticket 32: [P3] libxml2: Heap-buffer-overflow in xmlStrncat

- **Score:** 48.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1834  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.04622 (pct 0.90904)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=23.2, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1834; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8

## Ticket 33: [P3] nodejs-y18n: prototype pollution vulnerability

- **Score:** 48.2 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2020-7774  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.69377 (pct 0.993)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.9, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2020-7774; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package y18n from 3.2.1 to 3.2.2, 4.0.1, 5.0.5 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade y18n from 3.2.1 to 3.2.2, 4.0.1, 5.0.5

## Ticket 34: [P3] decode-uri-component: improper input validation resulting in DoS

- **Score:** 48.0 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-38900  ·  **CWE:** CWE-20
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.24928 (pct 0.97723)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.7, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-38900; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package decode-uri-component from 0.2.0 to 0.2.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade decode-uri-component from 0.2.0 to 0.2.1

## Ticket 35: [P3] pcre: inefficient posix character class syntax check (8.38/16)

- **Score:** 48.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8391  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06404 (pct 0.9307)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=22.5, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8391; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 36: [P3] openssl: X.400 address type confusion in X.509 GeneralName

- **Score:** 47.9 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-0286  ·  **CWE:** CWE-843
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** high  ·  **EPSS:** 0.59501 (pct 0.99045)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.5, epss=14.9, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-0286; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0

## Ticket 37: [P3] openssl: double free after calling PEM_read_bio_ex

- **Score:** 47.9 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-4450  ·  **CWE:** CWE-415
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** high  ·  **EPSS:** 0.20444 (pct 0.9727)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.6, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-4450; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0

## Ticket 38: [P3] sanitize-html: insecure global regular expression replacement logic may lead to ReDoS

- **Score:** 47.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-25887  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01155 (pct 0.64317)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=9.6, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-25887; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package sanitize-html from 1.4.2 to 2.7.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade sanitize-html from 1.4.2 to 2.7.1

## Ticket 39: [P3] undici: undici: Denial of Service via unbounded memory consumption during WebSocket permessage-deflate decompression

- **Score:** 47.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-1526  ·  **CWE:** CWE-409
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.0115 (pct 0.64168)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=9.6, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-1526; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package undici from 5.29.0 to 6.24.0, 7.24.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade undici from 5.29.0 to 6.24.0, 7.24.0

## Ticket 40: [P3] express: "qs" prototype poisoning causes the hang of the node process

- **Score:** 47.8 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-24999  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.14663 (pct 0.96361)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-24999; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package qs from 6.5.2 to 6.10.3, 6.9.7, 6.8.3, 6.7.3, 6.6.1, 6.5.3, 6.4.1, 6.3.3, 6.2.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade qs from 6.5.2 to 6.10.3, 6.9.7, 6.8.3, 6.7.3, 6.6.1, 6.5.3, 6.4.1, 6.3.3, 6.2.4

## Ticket 41: [P3] socket.io parser is a socket.io encoder and decoder written in JavaScr ...

- **Score:** 47.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2023-32695  ·  **CWE:** CWE-20
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01059 (pct 0.61676)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=9.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-32695; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package socket.io-parser from 4.0.5 to 4.2.3, 3.4.3, 3.3.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade socket.io-parser from 4.0.5 to 4.2.3, 3.4.3, 3.3.4

## Ticket 42: [P3] engine.io: Specially crafted HTTP request can trigger an uncaught exception

- **Score:** 47.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-41940  ·  **CWE:** CWE-248
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01939 (pct 0.78368)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=11.8, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-41940; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package engine.io from 4.1.2 to 3.6.1, 6.2.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade engine.io from 4.1.2 to 3.6.1, 6.2.1

## Ticket 43: [P3] glibc: Incorrect handling of RPATH in elf/dl-load.c can be used to execute code loaded from arbitrary libraries

- **Score:** 47.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-16997  ·  **CWE:** CWE-426
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.02698 (pct 0.84639)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=23.2, epss=12.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-16997; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14

## Ticket 44: [P3] lodash: Prototype pollution in utilities function

- **Score:** 47.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2018-16487  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01553 (pct 0.72987)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=10.9, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-16487; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package lodash from 2.4.2 to >=4.17.11 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade lodash from 2.4.2 to >=4.17.11

## Ticket 45: [P3] nodejs-ansi-regex: Regular expression denial of service (ReDoS) matching ANSI escape codes

- **Score:** 47.2 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2021-3807  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.03552 (pct 0.88308)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=13.2, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2021-3807; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ansi-regex from 3.0.0 to 6.0.1, 5.0.1, 4.1.1, 3.0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ansi-regex from 3.0.0 to 6.0.1, 5.0.1, 4.1.1, 3.0.1

## Ticket 46: [P3] minimist: prototype pollution

- **Score:** 46.9 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2021-44906  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.04581 (pct 0.90829)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2021-44906; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package minimist from 0.0.10 to 1.2.6, 0.2.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade minimist from 0.0.10 to 1.2.6, 0.2.4

## Ticket 47: [P3] openssl: use-after-free following BIO_new_NDEF

- **Score:** 46.9 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-0215  ·  **CWE:** CWE-416
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** high  ·  **EPSS:** 0.04494 (pct 0.90666)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-0215; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0

## Ticket 48: [P3] decompress: @xhmikosr/decompress: Decompress: Arbitrary file read/write via crafted archive extraction

- **Score:** 46.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-53486  ·  **CWE:** CWE-22
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.00643 (pct 0.47813)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=20.2, epss=7.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Block traversal patterns at the WAF and disable symbolic links on the webroot.
- *full_remediation:* Use an allow-listed file API and canonicalize paths before access; never join user input into filesystem paths.
- *scanner_guidance:* decompress: @xhmikosr/decompress: Decompress: Arbitrary file read/write via crafted archive extraction

## Ticket 49: [P3] undici: Undici: Denial of Service via invalid WebSocket permessage-deflate extension parameter

- **Score:** 46.7 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-2229  ·  **CWE:** CWE-248
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00874 (pct 0.55916)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=8.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-2229; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package undici from 5.29.0 to 6.24.0, 7.24.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade undici from 5.29.0 to 6.24.0, 7.24.0

## Ticket 50: [P3] openssl: Denial of service by excessive resource usage in verifying X509 policy constraints

- **Score:** 46.6 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-0464  ·  **CWE:** CWE-295
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** high  ·  **EPSS:** 0.03658 (pct 0.88659)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.3, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-0464; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r2

## Ticket 51: [P3] nodejs-ini: Prototype pollution via malicious INI file

- **Score:** 46.6 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2020-7788  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.03612 (pct 0.88488)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.3, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2020-7788; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ini from 1.3.5 to 1.3.6 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ini from 1.3.5 to 1.3.6

## Ticket 52: [P3] nodejs-mixin-deep: prototype pollution in function mixin-deep

- **Score:** 46.5 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2019-10746  ·  **CWE:** CWE-88
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.03508 (pct 0.88184)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.2, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-10746; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package mixin-deep from 1.3.1 to 1.3.2, 2.0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade mixin-deep from 1.3.1 to 1.3.2, 2.0.1

## Ticket 53: [P3] node-tar: tar: node-tar: Arbitrary file creation via path traversal bypass in hardlink security check

- **Score:** 46.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-24842  ·  **CWE:** CWE-22
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00541 (pct 0.4293)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=20.5, epss=6.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-24842; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tar from 6.2.1 to 7.5.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tar from 6.2.1 to 7.5.7

## Ticket 54: [P3] The uglify-js package before 2.6.0 for Node.js allows attackers to cau ...

- **Score:** 46.3 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8858  ·  **CWE:** CWE-399
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.02358 (pct 0.82302)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=12.3, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8858; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package uglify-js from 2.4.24 to >=2.6.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade uglify-js from 2.4.24 to >=2.6.0

## Ticket 55: [P3] undici: undici: Denial of Service due to unbounded memory growth via WebSocket frames

- **Score:** 46.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-12151  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00789 (pct 0.53185)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=8.0, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-12151; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package undici from 5.29.0 to 6.27.0, 7.28.0, 8.5.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade undici from 5.29.0 to 6.27.0, 7.28.0, 8.5.0

## Ticket 56: [P3] ws: ws: Denial of Service via memory exhaustion from small WebSocket fragments

- **Score:** 46.2 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-48779  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00782 (pct 0.52957)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=7.9, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-48779; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ws from 7.4.6 to 5.2.5, 6.2.4, 7.5.11, 8.21.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ws from 7.4.6 to 5.2.5, 6.2.4, 7.5.11, 8.21.0

## Ticket 57: [P3] Multer vulnerable to Denial of Service from maliciously crafted requests

- **Score:** 46.2 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2025-47944  ·  **CWE:** CWE-248
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.0077 (pct 0.52574)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=7.9, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2025-47944; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package multer from 1.4.5-lts.2 to 2.0.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade multer from 1.4.5-lts.2 to 2.0.0

## Ticket 58: [P3] php: use of uninitialized pointer in PharFileInfo::getContent

- **Score:** 46.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4342  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05345 (pct 0.91928)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=20.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4342; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 59: [P3] nodejs-semver: Regular expression denial of service

- **Score:** 46.1 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-25883  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.02761 (pct 0.85012)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=12.8, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-25883; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package semver from 5.6.0 to 7.5.2, 6.3.1, 5.7.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade semver from 5.6.0 to 7.5.2, 6.3.1, 5.7.2

## Ticket 60: [P3] Multer vulnerable to Denial of Service via memory leaks from unclosed streams

- **Score:** 46.1 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2025-47935  ·  **CWE:** CWE-401
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00754 (pct 0.52038)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=7.8, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2025-47935; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package multer from 1.4.5-lts.2 to 2.0.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade multer from 1.4.5-lts.2 to 2.0.0

## Ticket 61: [P3] openssl: OCSP Status Request extension unbounded memory growth

- **Score:** 45.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6304  ·  **CWE:** CWE-401
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.63029 (pct 0.9913)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6304; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.20

## Ticket 62: [P3] openssh: Denial of service via very long passwords

- **Score:** 45.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6515  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.58568 (pct 0.99023)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6515; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.8

## Ticket 63: [P3] glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c

- **Score:** 45.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2018-20796  ·  **CWE:** CWE-674
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** low  ·  **EPSS:** 0.05757 (pct 0.92419)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=13.9, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c

## Ticket 64: [P3] multer: Multer: Denial of Service via malformed requests

- **Score:** 45.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-3520  ·  **CWE:** CWE-674
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00713 (pct 0.50589)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=7.6, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-3520; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package multer from 1.4.5-lts.2 to 2.1.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade multer from 1.4.5-lts.2 to 2.1.1

## Ticket 65: [P3] crypto-js is a JavaScript library of crypto standards. Versions of cry ...

- **Score:** 45.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-71851  ·  **CWE:** CWE-331
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.00317 (pct 0.2445)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=22.7, epss=3.7, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-71851; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package crypto-js from 3.3.0 to 4.0.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade crypto-js from 3.3.0 to 4.0.0

## Ticket 66: [P3] Moment.js: Path traversal  in moment.locale

- **Score:** 45.8 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-24785  ·  **CWE:** CWE-22
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.0552 (pct 0.92119)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=12.5, epss=13.8, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-24785; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package moment from 2.0.0 to 2.29.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade moment from 2.0.0 to 2.29.2

## Ticket 67: [P3] nodejs-set-value: prototype pollution in function set-value

- **Score:** 45.8 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2019-10747  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.02475 (pct 0.83156)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=12.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-10747; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package set-value from 0.4.3 to 2.0.1, 3.0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade set-value from 0.4.3 to 2.0.1, 3.0.1

## Ticket 68: [P3] nodejs-set-value: type confusion allows bypass of CVE-2019-10747

- **Score:** 45.8 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2021-23440  ·  **CWE:** CWE-843
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.02457 (pct 0.83034)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=12.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2021-23440; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package set-value from 0.4.3 to 4.0.1, 2.0.1, 3.0.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade set-value from 0.4.3 to 4.0.1, 2.0.1, 3.0.3

## Ticket 69: [P3] openssl: ASN.1 BIO handling of large amounts of data

- **Score:** 45.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2109  ·  **CWE:** CWE-399
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.2921 (pct 0.98008)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2109; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.19

## Ticket 70: [P3] OpenSSL: Avoid memory leak in SRP

- **Score:** 45.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-0798  ·  **CWE:** CWE-399
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.24409 (pct 0.9768)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-0798; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.18

## Ticket 71: [P3] openssl: Possible DoS translating ASN.1 object identifiers

- **Score:** 45.6 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-2650  ·  **CWE:** CWE-770
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** medium  ·  **EPSS:** 0.75116 (pct 0.99469)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=14.9, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-2650; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1u-r0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1u-r0

## Ticket 72: [P3] multer: Multer: Denial of Service via dropped file upload connections

- **Score:** 45.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-2359  ·  **CWE:** CWE-772
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00663 (pct 0.48714)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=7.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-2359; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package multer from 1.4.5-lts.2 to 2.1.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade multer from 1.4.5-lts.2 to 2.1.0

## Ticket 73: [P3] multer: Multer: Denial of Service via malformed requests

- **Score:** 45.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-3304  ·  **CWE:** CWE-459
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00663 (pct 0.48714)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=7.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-3304; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package multer from 1.4.5-lts.2 to 2.1.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade multer from 1.4.5-lts.2 to 2.1.0

## Ticket 74: [P3] jsonwebtoken: Unrestricted key type could lead to legacy keys usagen

- **Score:** 45.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-23539  ·  **CWE:** CWE-327
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00479 (pct 0.39252)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=20.2, epss=5.9, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-23539; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package jsonwebtoken from 0.1.0 to 9.0.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade jsonwebtoken from 0.1.0 to 9.0.0

## Ticket 75: [P3] bson: Deserialization of Untrusted Data could result in Code injection or Excessive CPU load

- **Score:** 45.5 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2020-7610  ·  **CWE:** CWE-502
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.02218 (pct 0.81145)  ·  **KEV:** no
- **Escalation potential:** 0.912

**Score breakdown:** cvss=18.8, epss=12.2, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2020-7610; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package bson from 1.0.9 to 1.1.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade bson from 1.0.9 to 1.1.4

## Ticket 76: [P3] git: arbitrary code execution via .gitmodules

- **Score:** 45.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-17456  ·  **CWE:** CWE-88
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.97356 (pct 0.99892)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=15.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-17456; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.9 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.9

## Ticket 77: [P3] php: Stack-based buffer under-read in php_stream_url_wrap_http_ex() in http_fopen_wrapper.c when parsing HTTP response

- **Score:** 45.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-7584  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.87348 (pct 0.9974)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=15.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-7584; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.24 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.24

## Ticket 78: [P3] nodejs-moment: Regular expression denial of service

- **Score:** 45.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2017-18214  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.03649 (pct 0.88629)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=13.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-18214; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package moment from 2.0.0 to 2.19.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade moment from 2.0.0 to 2.19.3

## Ticket 79: [P3] A vulnerability classified as problematic has been found in debug-js d ...

- **Score:** 45.2 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2017-20165  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.02046 (pct 0.79544)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=11.9, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-20165; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package debug from 2.2.0 to 3.1.0, 2.6.9 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade debug from 2.2.0 to 3.1.0, 2.6.9

## Ticket 80: [P3] socket.io: Unhandled 'error' event

- **Score:** 45.2 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2024-38355  ·  **CWE:** CWE-20
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.0069 (pct 0.49784)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.2, epss=7.5, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2024-38355; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package socket.io from 3.1.2 to 2.5.1, 4.6.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade socket.io from 3.1.2 to 2.5.1, 4.6.2

## Ticket 81: [P3] openssl: Possible integer overflow vulnerabilities in codebase

- **Score:** 45.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2177  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.44505 (pct 0.98655)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2177; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.22

## Ticket 82: [P3] openssl: Out-of-bounds write caused by unchecked errors in BN_bn2dec()

- **Score:** 45.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2182  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.44218 (pct 0.98646)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2182; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.20

## Ticket 83: [P3] php: Use-after-free vulnerability when resizing the 'properties' hash table of a serialized object

- **Score:** 45.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7479  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.41943 (pct 0.98572)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7479; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21

## Ticket 84: [P3] httpd: mod_mime buffer overread

- **Score:** 45.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-7679  ·  **CWE:** CWE-126
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.39341 (pct 0.9848)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-7679; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.16

## Ticket 85: [P3] openssh: loading of untrusted PKCS#11 modules in ssh-agent

- **Score:** 45.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-10009  ·  **CWE:** CWE-426
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.37431 (pct 0.98401)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-10009; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.10

## Ticket 86: [P3] php: Use after free in WDDX Deserialize when processing XML data

- **Score:** 45.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-3141  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.36009 (pct 0.98338)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-3141; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 87: [P3] glibc: ASLR bypass using cache of thread stack and heap

- **Score:** 45.1 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2019-1010024  ·  **CWE:** CWE-200
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** low  ·  **EPSS:** 0.03193 (pct 0.87011)  ·  **KEV:** no
- **Escalation potential:** 0.513

**Score breakdown:** cvss=12.5, epss=13.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Restrict access to the exposed resource (auth, IP allow-list, remove from public routing).
- *full_remediation:* Redact/remove the sensitive data from responses and apply least-privilege access controls.
- *scanner_guidance:* glibc: ASLR bypass using cache of thread stack and heap

## Ticket 88: [P3] busybox: wget: Heap-based buffer overflow in the retrieve_file_data() function

- **Score:** 45.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1000517  ·  **CWE:** CWE-120
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.32919 (pct 0.98212)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1000517; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package busybox-initramfs from 1:1.21.0-1ubuntu1 to 1:1.21.0-1ubuntu1.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade busybox-initramfs from 1:1.21.0-1ubuntu1 to 1:1.21.0-1ubuntu1.4

## Ticket 89: [P3] openssl: Integer overflow in MDC2_Update()

- **Score:** 45.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6303  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.31985 (pct 0.98161)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6303; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libssl1.0.0 from 1.0.1f-1ubuntu2.16 to 1.0.1f-1ubuntu2.20

## Ticket 90: [P3] busybox: heap-based buffer overflow in OPTION_6RD parsing

- **Score:** 45.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2148  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.27111 (pct 0.97879)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2148; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package busybox-initramfs from 1:1.21.0-1ubuntu1 to 1:1.21.0-1ubuntu1.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade busybox-initramfs from 1:1.21.0-1ubuntu1 to 1:1.21.0-1ubuntu1.4

## Ticket 91: [P3] expat: Little entropy used for hash initialization

- **Score:** 45.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5300  ·  **CWE:** CWE-399
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06539 (pct 0.93201)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=19.5, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5300; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libexpat1 from 2.1.0-4ubuntu1.1 to 2.1.0-4ubuntu1.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libexpat1 from 2.1.0-4ubuntu1.1 to 2.1.0-4ubuntu1.3

## Ticket 92: [P3] python: Command injection in the shutil module

- **Score:** 44.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1000802  ·  **CWE:** CWE-77
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.20807 (pct 0.97333)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1000802; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.5 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.5

## Ticket 93: [P3] httpd: ap_get_basic_auth_pw() authentication bypass

- **Score:** 44.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-3167  ·  **CWE:** CWE-287
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.20231 (pct 0.97242)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=18.8, epss=14.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-3167; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.16

## Ticket 94: [P3] httpd: mod_ssl NULL pointer dereference

- **Score:** 44.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-3169  ·  **CWE:** CWE-476
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.19953 (pct 0.97203)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-3169; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.16

## Ticket 95: [P3] php: Format string vulnerability in php_snmp_error()

- **Score:** 44.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4071  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.19455 (pct 0.97131)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4071; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 96: [P3] jsonwebtoken: Insecure default algorithm in jwt.verify() could lead to signature validation bypass

- **Score:** 44.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-23540  ·  **CWE:** CWE-287
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.00532 (pct 0.42445)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=19.0, epss=6.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-23540; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package jsonwebtoken from 0.1.0 to 9.0.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade jsonwebtoken from 0.1.0 to 9.0.0

## Ticket 97: [P3] php: bypass __wakeup() in deserialization of an unexpected object

- **Score:** 44.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7124  ·  **CWE:** CWE-502
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.16612 (pct 0.96736)  ·  **KEV:** no
- **Escalation potential:** 0.912

**Score breakdown:** cvss=18.8, epss=14.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7124; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 98: [P3] php: Use After Free Vulnerability in PHP's GC algorithm and unserialize

- **Score:** 44.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5771  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.15484 (pct 0.96507)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5771; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 99: [P3] expat: Out-of-bounds heap read on crafted input causing crash

- **Score:** 44.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-0718  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.13802 (pct 0.96191)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-0718; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libexpat1 from 2.1.0-4ubuntu1.1 to 2.1.0-4ubuntu1.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libexpat1 from 2.1.0-4ubuntu1.1 to 2.1.0-4ubuntu1.2

## Ticket 100: [P3] openssh: possible fallback from untrusted to trusted X11 forwarding

- **Score:** 44.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1908  ·  **CWE:** CWE-287
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.13736 (pct 0.9618)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=18.8, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1908; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.7

## Ticket 101: [P3] php: Out-of-bounds heap memory read in exif_read_data() caused by malformed input

- **Score:** 44.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4543  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.12179 (pct 0.95804)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4543; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 102: [P3] curl: FTP path trickery leads to NIL byte out of bounds write

- **Score:** 44.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1000120  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.11823 (pct 0.95725)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1000120; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.15 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.15

## Ticket 103: [P3] curl: escape and unescape integer overflows

- **Score:** 44.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7167  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.11737 (pct 0.95702)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7167; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10

## Ticket 104: [P3] perl: Integer overflow leading to buffer overflow in Perl_my_setenv()

- **Score:** 44.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-18311  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.11676 (pct 0.95683)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-18311; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.7

## Ticket 105: [P3] nodejs-minimatch: ReDoS via the braceExpand function

- **Score:** 44.7 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-3517  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01751 (pct 0.75919)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=11.4, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-3517; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package minimatch from 3.0.4 to 3.0.5 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade minimatch from 3.0.4 to 3.0.5

## Ticket 106: [P3] nodejs-ws: denial of service when handling a request with many HTTP headers

- **Score:** 44.7 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2024-37890  ·  **CWE:** CWE-476
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01357 (pct 0.69297)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=14.8, epss=10.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2024-37890; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ws from 7.4.6 to 5.2.4, 6.2.3, 7.5.10, 8.17.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ws from 7.4.6 to 5.2.4, 6.2.3, 7.5.10, 8.17.1

## Ticket 107: [P3] curl: FTP wildcard out of bounds read

- **Score:** 44.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-8817  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.11175 (pct 0.95568)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-8817; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.13 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.13

## Ticket 108: [P3] perl: heap buffer overflow in pp_pack.c

- **Score:** 44.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-6913  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.10866 (pct 0.95474)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-6913; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.4

## Ticket 109: [P3] ntp: decodearr() can write beyond its buffer limit

- **Score:** 44.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-7183  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.10404 (pct 0.95328)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-7183; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.13 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.13

## Ticket 110: [P3] php: Invalid memory access in function xmlrpc_decode()

- **Score:** 44.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-9020  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.10059 (pct 0.95214)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-9020; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.27 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.27

## Ticket 111: [P3] php: Heap-based buffer over-read in PHAR reading functions

- **Score:** 44.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-9021  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.10059 (pct 0.95213)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-9021; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.27 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.27

## Ticket 112: [P3] php: Double Free Corruption in wddx_deserialize

- **Score:** 44.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5772  ·  **CWE:** CWE-415
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.09674 (pct 0.95074)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5772; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 113: [P3] php: Double free in _php_mb_regex_ereg_replace_exec

- **Score:** 44.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5768  ·  **CWE:** CWE-415
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0963 (pct 0.95058)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5768; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 114: [P3] decompress: Decompress: Arbitrary file write leading to remote code execution via crafted ZIP archive (Zip Slip)

- **Score:** 44.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-10732  ·  **CWE:** CWE-29
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.00521 (pct 0.41815)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=6.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* decompress: Decompress: Arbitrary file write leading to remote code execution via crafted ZIP archive (Zip Slip)

## Ticket 115: [P3] minimatch: minimatch: Denial of Service via specially crafted glob patterns

- **Score:** 44.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-26996  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00519 (pct 0.41698)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=6.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-26996; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package minimatch from 3.0.5 to 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade minimatch from 3.0.5 to 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3

## Ticket 116: [P3] php: Uninitialized read in exif_process_IFD_in_TIFF

- **Score:** 44.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-9641  ·  **CWE:** CWE-908
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.09395 (pct 0.94972)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-9641; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.29 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.29

## Ticket 117: [P3] libX11: Out of Bounds write in XListExtensions in ListExt.c

- **Score:** 44.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-14600  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.09341 (pct 0.94948)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-14600; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1

## Ticket 118: [P3] php: Heap-based buffer over-read in mbstring regular expression functions

- **Score:** 44.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-9023  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.09317 (pct 0.94939)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-9023; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.27 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.27

## Ticket 119: [P3] php: ZipArchive class Use After Free Vulnerability in PHP's GC algorithm and unserialize

- **Score:** 44.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5773  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.0926 (pct 0.94919)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5773; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 120: [P3] pcre: workspace overflow for (*ACCEPT) with deeply nested parentheses (8.39/13, 10.22/12)

- **Score:** 44.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-3191  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0843 (pct 0.94519)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-3191; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 121: [P3] php: Integer Overflows in mcrypt_generic() and mdecrypt_generic() resulting in heap overflows

- **Score:** 44.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5769  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.08361 (pct 0.94472)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5769; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 122: [P3] Sandbox escape in notevil and argencoders-notevil

- **Score:** 44.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2021-23771  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01013 (pct 0.60285)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=9.0, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* Sandbox escape in notevil and argencoders-notevil

## Ticket 123: [P3] socket.io: Socket.IO: Denial of Service due to excessive buffering of specially crafted packets

- **Score:** 44.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-33151  ·  **CWE:** CWE-20
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00514 (pct 0.41386)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=6.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-33151; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package socket.io-parser from 4.0.5 to 3.3.5, 3.4.4, 4.2.6 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade socket.io-parser from 4.0.5 to 3.3.5, 3.4.4, 4.2.6

## Ticket 124: [P3] python: Integer overflow in PyString_DecodeEscape results in heap-base buffer overflow

- **Score:** 44.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-1000158  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07944 (pct 0.94232)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-1000158; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.4

## Ticket 125: [P3] php: Zend/zend_exceptions.c does not validate certain Exception objects

- **Score:** 44.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8876  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07705 (pct 0.94084)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8876; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 126: [P3] oniguruma: Heap buffer overflow in next_state_val() during regular expression compilation

- **Score:** 44.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-9226  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07511 (pct 0.9396)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-9226; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 127: [P3] php: Off-by-one error in phar_parse_pharfile when loading crafted phar archive

- **Score:** 44.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-10160  ·  **CWE:** CWE-193
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07322 (pct 0.93842)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-10160; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21

## Ticket 128: [P3] php: mb_strcut() Negative size parameter in memcpy

- **Score:** 44.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4073  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07287 (pct 0.93818)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4073; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 129: [P3] glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c

- **Score:** 44.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2019-9192  ·  **CWE:** CWE-674
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** low  ·  **EPSS:** 0.02427 (pct 0.82817)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=12.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c

## Ticket 130: [P3] http-cache-semantics: Regular Expression Denial of Service (ReDoS) vulnerability

- **Score:** 44.4 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-25881  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01613 (pct 0.73888)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=11.1, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-25881; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package http-cache-semantics from 3.8.1 to 4.1.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade http-cache-semantics from 3.8.1 to 4.1.1

## Ticket 131: [P3] gnutls: Stack overflow in cdk_pk_get_keyid

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-5336  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07071 (pct 0.93651)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-5336; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libgnutls-openssl27 from 2.12.23-12ubuntu2.4 to 2.12.23-12ubuntu2.6 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libgnutls-openssl27 from 2.12.23-12ubuntu2.4 to 2.12.23-12ubuntu2.6

## Ticket 132: [P3] pcre: Buffer overflow caused by lookbehind assertion (8.38/6)

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8386  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.07059 (pct 0.93642)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8386; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 133: [P3] php: Invalid read when wddx decodes empty boolean element

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-9935  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07031 (pct 0.9362)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-9935; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21

## Ticket 134: [P3] php: buffer over-read in finish_nested_data function

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-12933  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.0694 (pct 0.93541)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-12933; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.23 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.23

## Ticket 135: [P3] php: Out of bounds heap read when verifying signature of zip phar in phar_parse_zipfile

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7414  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06842 (pct 0.93456)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7414; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 136: [P3] php: Missing type check when unserializing SplArray

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7417  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06842 (pct 0.93456)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7417; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 137: [P3] php: imagegammacorrect allows arbitrary write access

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7127  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06842 (pct 0.93455)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7127; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 138: [P3] php: wddx_deserialize allows illegal memory access

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7129  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06842 (pct 0.93455)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7129; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 139: [P3] php: Out-of-bounds heap memory read in exif_read_data() caused by malformed input

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4544  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06689 (pct 0.93318)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4544; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 140: [P3] php: Use after free in wddx_deserialize

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7413  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06654 (pct 0.9329)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7413; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 141: [P3] oniguruma: Out-of-bounds stack read in match_at() during regular expression searching

- **Score:** 44.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-9224  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0654 (pct 0.93202)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-9224; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 142: [P3] nodejs-got: missing verification of requested URLs allows redirects to UNIX sockets

- **Score:** 44.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-33987  ·  **CWE:** -
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.02307 (pct 0.81881)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=12.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-33987; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package got from 8.3.2 to 12.1.0, 11.8.5 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade got from 8.3.2 to 12.1.0, 11.8.5

## Ticket 143: [P3] dhcp: unclosed TCP connections to OMAPI or failover ports can cause DoS

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2774  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.73622 (pct 0.99426)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.8, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2774; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package isc-dhcp-client from 4.2.4-7ubuntu12.4 to 4.2.4-7ubuntu12.12 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade isc-dhcp-client from 4.2.4-7ubuntu12.4 to 4.2.4-7ubuntu12.12

## Ticket 144: [P3] php: Heap buffer overflow vulnerability in simplestring_addn in simplestring.c

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6296  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06271 (pct 0.92961)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6296; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 145: [P3] oniguruma: Out-of-bounds stack read in mbc_enc_len() during regular expression searching

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-9227  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06265 (pct 0.92954)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-9227; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 146: [P3] oniguruma: Out-of-bounds heap write in bitset_set_range()

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-9228  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06261 (pct 0.9295)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-9228; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 147: [P3] php: xml_parse_into_struct() can crash when XML parser is re-used

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4539  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06229 (pct 0.92919)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4539; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 148: [P3] php: OOB read in grapheme_stripos and grapheme_strpos when negative offset is used

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4540  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06229 (pct 0.92919)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4540; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 149: [P3] php: OOB read in grapheme_stripos and grapheme_strpos when negative offset is used

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4541  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06229 (pct 0.92919)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4541; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 150: [P3] php: bcpowmod accepts negative scale causing heap buffer overflow corrupting _one_ definition

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4538  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06229 (pct 0.92918)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4538; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 151: [P3] php: type confusion issue in Soap Client call() method

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8835  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06195 (pct 0.92883)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8835; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 152: [P3] gnutls: Heap read overflow in read-packet.c

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-5337  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06179 (pct 0.92869)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-5337; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libgnutls-openssl27 from 2.12.23-12ubuntu2.4 to 2.12.23-12ubuntu2.6 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libgnutls-openssl27 from 2.12.23-12ubuntu2.4 to 2.12.23-12ubuntu2.6

## Ticket 153: [P3] php: Out-of-bounds heap memory read in exif_read_data() caused by malformed input

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4542  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06063 (pct 0.92755)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4542; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 154: [P3] glibc: Unbounded stack allocation in catopen function

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8779  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05966 (pct 0.92652)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8779; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8

## Ticket 155: [P3] php: Out-of-bounds access in locale_accept_from_http

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6294  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05956 (pct 0.92643)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6294; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 156: [P3] php: Invalid memory write in phar on filename containing \0 inside name

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4072  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05932 (pct 0.92617)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4072; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 157: [P3] The AMF3CD_AddProp function in amf.c in RTMPDump 2.4 allows remote RTM ...

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8271  ·  **CWE:** CWE-123
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05923 (pct 0.92605)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8271; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package librtmp0 from 2.4+20121230.gitdf6c518-1 to 2.4+20121230.gitdf6c518-1ubuntu0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade librtmp0 from 2.4+20121230.gitdf6c518-1 to 2.4+20121230.gitdf6c518-1ubuntu0.1

## Ticket 158: [P3] php: bcpowmod accepts negative scale causing heap buffer overflow corrupting _one_ definition

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4537  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05873 (pct 0.92566)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4537; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 159: [P3] curl: Integer overflow leading to heap-based buffer overflow in Curl_sasl_create_plain_message()

- **Score:** 44.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-16839  ·  **CWE:** CWE-122
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05782 (pct 0.92445)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-16839; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.19

## Ticket 160: [P3] nodejs-underscore: Arbitrary code execution via the template function

- **Score:** 44.2 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2021-23358  ·  **CWE:** CWE-94
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.04087 (pct 0.89846)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=13.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2021-23358; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package underscore from 1.9.1 to 1.12.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade underscore from 1.9.1 to 1.12.1

## Ticket 161: [P3] glibc: information disclosure of heap addresses of pthread_created thread

- **Score:** 44.2 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2019-1010025  ·  **CWE:** CWE-330
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** low  ·  **EPSS:** 0.02267 (pct 0.81537)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=12.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* glibc: information disclosure of heap addresses of pthread_created thread

## Ticket 162: [P3] php: Memory corruption when destructing deserialized object

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7411  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05649 (pct 0.92297)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7411; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 163: [P3] pcre: buffer overflow caused by named forward reference to duplicate group number (8.38/30)

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8385  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05623 (pct 0.92271)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8385; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 164: [P3] php: Out-of-bounds access in exif_process_IFD_in_MAKERNOTE

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6291  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05598 (pct 0.92228)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6291; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 165: [P3] glibc: Integer overflow in hcreate and hcreate_r

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8778  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05515 (pct 0.92115)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8778; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8

## Ticket 166: [P3] php: improper nul termination leading to out-of-bounds read in get_icu_value_internal

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5093  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05487 (pct 0.92088)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5093; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 167: [P3] krb5: Automatic sec context deletion could lead to double-free

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-11462  ·  **CWE:** CWE-415
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05481 (pct 0.92077)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-11462; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package krb5-locales from 1.12+dfsg-2ubuntu5.2 to 1.12+dfsg-2ubuntu5.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade krb5-locales from 1.12+dfsg-2ubuntu5.2 to 1.12+dfsg-2ubuntu5.4

## Ticket 168: [P3] php: Use after free in unserialize() with Unexpected Session Deserialization

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6290  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0548 (pct 0.92077)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6290; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 169: [P3] php: Use-after-free vulnerability in the spl_ptr_heap_insert function

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-4116  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05466 (pct 0.92063)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-4116; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 170: [P3] php: Use after free in SNMP with GC and unserialize()

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6295  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05417 (pct 0.9201)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6295; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 171: [P3] file: Buffer over-write in finfo_open with malformed magic file

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8865  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05415 (pct 0.92008)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8865; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package file from 1:5.14-2ubuntu3.3 to 1:5.14-2ubuntu3.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade file from 1:5.14-2ubuntu3.3 to 1:5.14-2ubuntu3.4

## Ticket 172: [P3] php: Use after free in unserialize()

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-9137  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05363 (pct 0.9195)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-9137; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21

## Ticket 173: [P3] pcre: infinite recursion compiling pattern with recursive reference in a group with indefinite repeat (8.36/20)

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-2328  ·  **CWE:** CWE-19
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05244 (pct 0.91822)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-2328; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 174: [P3] rsync: Heap-based buffer over-read in receive_xattr function

- **Score:** 44.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-16548  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05163 (pct 0.91717)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-16548; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package rsync from 3.1.0-2ubuntu0.2 to 3.1.0-2ubuntu0.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade rsync from 3.1.0-2ubuntu0.2 to 3.1.0-2ubuntu0.4

## Ticket 175: [P3] php: Buffer over-read in php_url_parse_ex

- **Score:** 44.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6288  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05055 (pct 0.91574)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6288; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 176: [P3] curl: Double-free in krb5 code

- **Score:** 44.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-8619  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.04989 (pct 0.91482)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-8619; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10

## Ticket 177: [P3] php: stack buffer overflow in locale_get_display_name

- **Score:** 44.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2014-9912  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04948 (pct 0.91421)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2014-9912; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.21

## Ticket 178: [P3] curl: Double-free in curl_maprintf

- **Score:** 44.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-8618  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.04837 (pct 0.91242)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-8618; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10

## Ticket 179: [P3] pcre: Integer overflow caused by missing check for certain conditions (8.38/31)

- **Score:** 44.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8394  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04815 (pct 0.91205)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8394; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 180: [P3] libX11: Off-by-one error in XListExtensions in ListExt.c

- **Score:** 44.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-14599  ·  **CWE:** CWE-193
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.04799 (pct 0.91182)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-14599; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1

## Ticket 181: [P3] braces: fails to limit the number of characters it can handle

- **Score:** 44.0 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2024-4068  ·  **CWE:** CWE-1050
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01471 (pct 0.71546)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=10.7, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2024-4068; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package braces from 2.3.2 to 3.0.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade braces from 2.3.2 to 3.0.3

## Ticket 182: [P3] glibc: realpath() buffer underflow when getcwd() returns relative path allows privilege escalation

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1000001  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.13368 (pct 0.9608)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.0, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1000001; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14

## Ticket 183: [P3] curl: URL unescape heap overflow via integer truncation

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-8622  ·  **CWE:** CWE-122
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0467 (pct 0.9098)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-8622; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10

## Ticket 184: [P3] curl: Glob parser write/read out of bounds

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-8620  ·  **CWE:** CWE-120
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.04667 (pct 0.90973)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-8620; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.10

## Ticket 185: [P3] file: malformed elf file causes access to uninitialized memory

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2014-9653  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04648 (pct 0.90945)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2014-9653; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package file from 1:5.14-2ubuntu3.3 to 1:5.14-2ubuntu3.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade file from 1:5.14-2ubuntu3.3 to 1:5.14-2ubuntu3.4

## Ticket 186: [P3] php: Integer overflow in php_html_entities()

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5094  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.0464 (pct 0.90932)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5094; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 187: [P3] pcre: uninitialized memory read triggered by malformed posix character class (8.38/22)

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8390  ·  **CWE:** CWE-908
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04618 (pct 0.90894)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8390; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 188: [P3] pcre: OOB write when pcre_exec() is called with ovecsize of 1 (8.38/10)

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8380  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04436 (pct 0.90561)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8380; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 189: [P3] php: Integer underflow causing arbitrary null write in fread/gzread

- **Score:** 43.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5096  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04397 (pct 0.90483)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5096; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 190: [P3] openssl: timing attack in RSA Decryption implementation

- **Score:** 43.8 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-4304  ·  **CWE:** CWE-203
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** medium  ·  **EPSS:** 0.16195 (pct 0.96656)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=14.8, epss=14.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-4304; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1t-r0

## Ticket 191: [P3] libX11: Insufficient validation of server responses in FontNames

- **Score:** 43.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7943  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04286 (pct 0.90268)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7943; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1

## Ticket 192: [P3] libX11: Insufficient validation of server responses in XGetImage()

- **Score:** 43.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7942  ·  **CWE:** CWE-264
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04286 (pct 0.90267)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7942; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libx11-6 from 2:1.6.2-1ubuntu2 to 2:1.6.2-1ubuntu2.1

## Ticket 193: [P3] sanitize-html: improper handling of internationalized domain name (IDN) can lead to bypass hostname whitelist validation

- **Score:** 43.8 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2021-26539  ·  **CWE:** -
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01953 (pct 0.78535)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=11.8, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2021-26539; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package sanitize-html from 1.4.2 to 2.3.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade sanitize-html from 1.4.2 to 2.3.1

## Ticket 194: [P3] undici: Undici: Denial of Service via excessive decompression steps

- **Score:** 43.8 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-22036  ·  **CWE:** CWE-770
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.0044 (pct 0.36645)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=5.5, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-22036; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package undici from 5.29.0 to 7.18.2, 6.23.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade undici from 5.29.0 to 7.18.2, 6.23.0

## Ticket 195: [P3] libidn2: Integer overflow in puny_decode.c/decode_digit

- **Score:** 43.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-14062  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03858 (pct 0.89256)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-14062; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libidn11 from 1.28-1ubuntu2 to 1.28-1ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libidn11 from 1.28-1ubuntu2 to 1.28-1ubuntu2.2

## Ticket 196: [P3] ntp: Null pointer dereference when trap service is enabled

- **Score:** 43.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-9311  ·  **CWE:** CWE-476
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.11174 (pct 0.95567)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.8, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-9311; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.11 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.11

## Ticket 197: [P3] pcre: Integer overflow in subroutine calls (8.38/8)

- **Score:** 43.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8387  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.03641 (pct 0.88602)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8387; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 198: [P3] tar: node-tar: Denial of Service via crafted gzip bomb

- **Score:** 43.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-59873  ·  **CWE:** CWE-770
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** 0.00424 (pct 0.35394)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=5.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-59873; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tar from 6.2.1 to 7.5.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tar from 6.2.1 to 7.5.19

## Ticket 199: [P3] glibc: getaddrinfo stack-based buffer overflow

- **Score:** 43.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-7547  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.89557 (pct 0.99775)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=15.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-7547; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.7

## Ticket 200: [P3] httpd: <FilesMatch> bypass with a trailing newline in the file name

- **Score:** 43.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-15715  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.8572 (pct 0.99708)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=15.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-15715; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.20

## Ticket 201: [P3] ntp: assertion failure in ntpd on duplicate IPs on unconfig directives

- **Score:** 43.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-2516  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.08948 (pct 0.94791)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.8, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-2516; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.10

## Ticket 202: [P3] mysql: Server: Partition unspecified vulnerability (CPU Jan 2018)

- **Score:** 43.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-2562  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03389 (pct 0.87777)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-2562; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1

## Ticket 203: [P3] rsync: daemon does not check for fnamecmp filenames allowing for access restriction bypass

- **Score:** 43.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-17434  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03362 (pct 0.8769)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-17434; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package rsync from 3.1.0-2ubuntu0.2 to 3.1.0-2ubuntu0.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade rsync from 3.1.0-2ubuntu0.2 to 3.1.0-2ubuntu0.3

## Ticket 204: [P3] tar: Node-tar: Denial of Service via malformed tar archive header

- **Score:** 43.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-59874  ·  **CWE:** CWE-835
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00418 (pct 0.34864)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=5.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-59874; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tar from 6.2.1 to 7.5.18 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tar from 6.2.1 to 7.5.18

## Ticket 205: [P3] git: Command injection via malicious ssh URLs

- **Score:** 43.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-1000117  ·  **CWE:** CWE-601
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.77823 (pct 0.99531)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-1000117; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.6 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.6

## Ticket 206: [P3] sanitize-html: improper validation of hostnames set by the "allowedIframeHostnames" option can lead to bypass hostname whitelist for iframe element

- **Score:** 43.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2021-26540  ·  **CWE:** -
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01754 (pct 0.7598)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=11.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2021-26540; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package sanitize-html from 1.4.2 to 2.3.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade sanitize-html from 1.4.2 to 2.3.2

## Ticket 207: [P3] node-tar: node-tar: Denial of Service due to incorrect PAX path handling

- **Score:** 43.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-59871  ·  **CWE:** CWE-704
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.0041 (pct 0.34119)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=5.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-59871; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tar from 6.2.1 to 7.5.18 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tar from 6.2.1 to 7.5.18

## Ticket 208: [P3] HTTPD: sets environmental variable based on user supplied Proxy request header

- **Score:** 43.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5387  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.55724 (pct 0.98955)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5387; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.13 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.13

## Ticket 209: [P3] git: arbitrary code execution when recursively cloning a malicious repository

- **Score:** 43.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-11235  ·  **CWE:** CWE-22
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.48752 (pct 0.98774)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=17.0, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-11235; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.8

## Ticket 210: [P3] libidn: out-of-bounds read with stringprep on invalid UTF-8

- **Score:** 43.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-2059  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.03185 (pct 0.8697)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-2059; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libidn11 from 1.28-1ubuntu2 to 1.28-1ubuntu2.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libidn11 from 1.28-1ubuntu2 to 1.28-1ubuntu2.1

## Ticket 211: [P3] perl: segmentation fault in S_regmatch on negative backreference

- **Score:** 43.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2013-7422  ·  **CWE:** CWE-189
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.03045 (pct 0.8639)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=13.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2013-7422; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.1

## Ticket 212: [P3] Command Injection in marsdb

- **Score:** 43.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** GHSA-5mrr-rgp6-x4gr  ·  **CWE:** -
- **Endpoint:** Node.js
- **Severity:** critical  ·  **EPSS:** - (pct -)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=23.8, epss=0.0, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* Command Injection in marsdb

## Ticket 213: [P3] vim: Lack of validation of values for few options results in code exection

- **Score:** 43.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1248  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.25314 (pct 0.97757)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1248; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package vim-common from 2:7.4.052-1ubuntu3 to 2:7.4.052-1ubuntu3.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade vim-common from 2:7.4.052-1ubuntu3 to 2:7.4.052-1ubuntu3.1

## Ticket 214: [P3] glibc: Buffer overflow in glob with GLOB_TILDE

- **Score:** 43.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-15670  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.02977 (pct 0.86097)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=12.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-15670; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14

## Ticket 215: [P3] php: Stack-based buffer over-read in msgfmt_parse_message function

- **Score:** 43.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-11362  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.0291 (pct 0.85804)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=12.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-11362; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 216: [P3] nodejs-minimist: prototype pollution allows adding or modifying properties of Object.prototype using a constructor or __proto__ payload

- **Score:** 43.2 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2020-7598  ·  **CWE:** CWE-1321
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01931 (pct 0.78271)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=11.7, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2020-7598; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package minimist from 0.0.10 to 0.2.1, 1.2.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade minimist from 0.0.10 to 0.2.1, 1.2.3

## Ticket 217: [P3] glibc: Buffer overflow during unescaping of user names with the ~ operator

- **Score:** 43.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-15804  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.02801 (pct 0.85254)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=12.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-15804; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14

## Ticket 218: [P3] jsonwebtoken: Insecure implementation of key retrieval function could lead to Forgeable Public/Private Tokens from RSA to HMAC

- **Score:** 43.1 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2022-23541  ·  **CWE:** CWE-287
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.00753 (pct 0.52015)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=15.8, epss=7.8, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-23541; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package jsonwebtoken from 0.1.0 to 9.0.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade jsonwebtoken from 0.1.0 to 9.0.0

## Ticket 219: [P3] httpd: Weak Digest auth nonce generation in mod_auth_digest

- **Score:** 43.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1312  ·  **CWE:** CWE-287
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.15885 (pct 0.96601)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=17.0, epss=14.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1312; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.20

## Ticket 220: [P3] php: Integer overflow in php_filter_full_special_chars

- **Score:** 42.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5095  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.02636 (pct 0.84255)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=12.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5095; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 221: [P3] libxml2: Missing validation for external entities in xmlParsePEReference

- **Score:** 42.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-7375  ·  **CWE:** CWE-611
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.02591 (pct 0.83964)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=18.8, epss=12.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-7375; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.10

## Ticket 222: [P3] php: Improper error handling in bzread()

- **Score:** 42.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5399  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.09844 (pct 0.95137)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5399; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 223: [P3] sudo: Privilege escalation in via improper get_process_ttyname() parsing

- **Score:** 42.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-1000367  ·  **CWE:** CWE-362
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** high  ·  **EPSS:** 0.07953 (pct 0.94239)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.2, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-1000367; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package sudo from 1.8.9p5-1ubuntu1.2 to 1.8.9p5-1ubuntu1.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade sudo from 1.8.9p5-1ubuntu1.2 to 1.8.9p5-1ubuntu1.4

## Ticket 224: [P3] php: Heap overflow in mysqlnd when not receiving UNSIGNED_FLAG in BIT field

- **Score:** 42.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-7412  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0885 (pct 0.94748)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-7412; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.20

## Ticket 225: [P3] curl: Use of connection struct after free

- **Score:** 42.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5421  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.08037 (pct 0.94281)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5421; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.8

## Ticket 226: [P3] socket.io: engine.io: Socket.IO: Denial of Service via invalid binary POST requests

- **Score:** 42.6 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-59725  ·  **CWE:** CWE-404
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00354 (pct 0.28549)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=4.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-59725; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package engine.io from 4.1.2 to 6.6.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade engine.io from 4.1.2 to 6.6.7

## Ticket 227: [P3] mysql: unspecified vulnerability in subcomponent: Server: Optimizer (CPU October 2016)

- **Score:** 42.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-3492  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06499 (pct 0.93167)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-3492; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.52-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.52-0ubuntu0.14.04.1

## Ticket 228: [P3] Arbitrary local file read vulnerability during template rendering

- **Score:** 42.5 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-25345  ·  **CWE:** CWE-22
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.01042 (pct 0.6114)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=18.8, epss=9.2, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Block traversal patterns at the WAF and disable symbolic links on the webroot.
- *full_remediation:* Use an allow-listed file API and canonicalize paths before access; never join user input into filesystem paths.
- *scanner_guidance:* Arbitrary local file read vulnerability during template rendering

## Ticket 229: [P3] php: buffer overflow in ext/phar/tar.c

- **Score:** 42.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-9675  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06021 (pct 0.9271)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-9675; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.29 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.29

## Ticket 230: [P3] mysql: unspecified vulnerability in subcomponent: Server: Types (CPU July 2016)

- **Score:** 42.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-3521  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05826 (pct 0.92508)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-3521; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.50-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.50-0ubuntu0.14.04.1

## Ticket 231: [P3] socket.io-parser: Socket.IO: Denial of Service via memory exhaustion from crafted packets

- **Score:** 42.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-69185  ·  **CWE:** CWE-20
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00346 (pct 0.27655)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=4.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-69185; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package socket.io-parser from 4.0.5 to 4.2.7, 3.4.5, 3.3.6 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade socket.io-parser from 4.0.5 to 4.2.7, 3.4.5, 3.3.6

## Ticket 232: [P3] httpd: Uninitialized memory reflection in mod_auth_digest

- **Score:** 42.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-9788  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.5677 (pct 0.98981)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-9788; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.17

## Ticket 233: [P3] libtasn1: Stack-based buffer overflow in asn1_find_node()

- **Score:** 42.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-6891  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05585 (pct 0.92207)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-6891; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libtasn1-6 from 3.4-3ubuntu0.3 to 3.4-3ubuntu0.5 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libtasn1-6 from 3.4-3ubuntu0.3 to 3.4-3ubuntu0.5

## Ticket 234: [P3] libxml2: Heap use-after-free in xmlSAX2AttributeNs

- **Score:** 42.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1835  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05576 (pct 0.92195)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1835; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8

## Ticket 235: [P3] patch: Malicious patch files cause ed to execute arbitrary commands

- **Score:** 42.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1000156  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0543 (pct 0.92023)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1000156; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package patch from 2.7.1-4ubuntu2.3 to 2.7.1-4ubuntu2.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade patch from 2.7.1-4ubuntu2.3 to 2.7.1-4ubuntu2.4

## Ticket 236: [P3] php: Stack-based buffer overflow vulnerability in php_stream_zip_opener

- **Score:** 42.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6297  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05265 (pct 0.91847)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6297; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 237: [P3] uuid: uuid: Out-of-bounds write vulnerability impacts data integrity and confidentiality

- **Score:** 42.3 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-41907  ·  **CWE:** CWE-787
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.00337 (pct 0.26663)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=4.0, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-41907; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package uuid from 8.3.2 to 11.1.1, 12.0.1, 13.0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade uuid from 8.3.2 to 11.1.1, 12.0.1, 13.0.1

## Ticket 238: [P3] krb5: Metadata taken from the unauthenticated plaintext

- **Score:** 42.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-11103  ·  **CWE:** CWE-345
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05118 (pct 0.91658)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-11103; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libasn1-8-heimdal from 1.6~git20131207+dfsg-1ubuntu1.1 to 1.6~git20131207+dfsg-1ubuntu1.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libasn1-8-heimdal from 1.6~git20131207+dfsg-1ubuntu1.1 to 1.6~git20131207+dfsg-1ubuntu1.2

## Ticket 239: [P3] glibc: buffer overflow in gethostbyname_r() and related functions with misaligned buffer

- **Score:** 42.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-1781  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05012 (pct 0.91511)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-1781; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8

## Ticket 240: [P3] curl: printf floating point buffer overflow

- **Score:** 42.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-9586  ·  **CWE:** CWE-122
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04935 (pct 0.91397)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-9586; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.11 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.11

## Ticket 241: [P3] glibc: heap/stack gap jumping via unbounded stack allocations

- **Score:** 42.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-1000366  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.02733 (pct 0.84833)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.0, epss=12.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-1000366; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.13 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.13

## Ticket 242: [P3] git: Escape out of git-shell

- **Score:** 42.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-8386  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.12387 (pct 0.95852)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=14.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-8386; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.5 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.5

## Ticket 243: [P3] glibc: glob implementation can cause excessive CPU and memory consumption due to crafted glob expressions

- **Score:** 42.1 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2010-4756  ·  **CWE:** CWE-399
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** low  ·  **EPSS:** 0.02611 (pct 0.8409)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=10.0, epss=12.6, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* glibc: glob implementation can cause excessive CPU and memory consumption due to crafted glob expressions

## Ticket 244: [P3] procps: incorrect integer size in proc/alloc.* leading to truncation / integer overflow issues

- **Score:** 42.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1126  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.01993 (pct 0.78961)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=11.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1126; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libprocps3 from 1:3.3.9-1ubuntu2.2 to 1:3.3.9-1ubuntu2.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libprocps3 from 1:3.3.9-1ubuntu2.2 to 1:3.3.9-1ubuntu2.3

## Ticket 245: [P3] php: Uninitialized pointer in phar_make_dirstream()

- **Score:** 42.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-4343  ·  **CWE:** CWE-824
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0421 (pct 0.90112)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-4343; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.17

## Ticket 246: [P3] php: libxml_disable_entity_loader setting is shared between threads

- **Score:** 42.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8866  ·  **CWE:** CWE-611
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.04026 (pct 0.89707)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=17.0, epss=13.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8866; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 247: [P3] mysql: Server: Optimizer unspecified vulnerability (CPU Jan 2018)

- **Score:** 41.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-2668  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03952 (pct 0.89528)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-2668; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1

## Ticket 248: [P3] mysql: Server: DDL unspecified vulnerability (CPU Jan 2018)

- **Score:** 41.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-2622  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03952 (pct 0.89527)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-2622; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1

## Ticket 249: [P3] mysql: Server: Optimizer unspecified vulnerability (CPU Jan 2018)

- **Score:** 41.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-2640  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03952 (pct 0.89527)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-2640; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1

## Ticket 250: [P3] mysql: Server: Optimizer unspecified vulnerability (CPU Jan 2018)

- **Score:** 41.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-2665  ·  **CWE:** -
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03952 (pct 0.89527)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-2665; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.59-0ubuntu0.14.04.1

## Ticket 251: [P3] glibc: _IO_wstr_overflow integer overflow

- **Score:** 41.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8983  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03871 (pct 0.89294)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8983; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.10

## Ticket 252: [P3] glibc: multiple overflows in strxfrm()

- **Score:** 41.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8982  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03797 (pct 0.89078)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8982; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.10

## Ticket 253: [P3] php: Integer overflow leads to buffer overflow in virtual_file_ex

- **Score:** 41.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6289  ·  **CWE:** CWE-190
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03792 (pct 0.89058)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6289; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 254: [P3] lodash: Prototype pollution in utilities function

- **Score:** 41.9 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2018-3721  ·  **CWE:** CWE-471
- **Endpoint:** Node.js
- **Severity:** low  ·  **EPSS:** 0.02413 (pct 0.82707)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=10.0, epss=12.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-3721; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package lodash from 2.4.2 to >=4.17.5 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade lodash from 2.4.2 to >=4.17.5

## Ticket 255: [P3] ntp: Mode 6 unauthenticated trap information disclosure and DDoS vector

- **Score:** 41.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-9310  ·  **CWE:** CWE-400
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.11162 (pct 0.95564)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-9310; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.11 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.11

## Ticket 256: [P3] perl: Heap-based buffer read overflow in S_grok_bslash_N()

- **Score:** 41.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-18313  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.09524 (pct 0.9502)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=14.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-18313; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.7

## Ticket 257: [P3] sanitize-html: Information Exposure when used on the backend

- **Score:** 41.8 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2024-21501  ·  **CWE:** CWE-200
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01018 (pct 0.60421)  ·  **KEV:** no
- **Escalation potential:** 0.513

**Score breakdown:** cvss=13.2, epss=9.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2024-21501; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package sanitize-html from 1.4.2 to 2.12.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade sanitize-html from 1.4.2 to 2.12.1

## Ticket 258: [P3] curl: RTSP RTP buffer over-read

- **Score:** 41.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1000122  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.09208 (pct 0.94893)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=14.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1000122; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.15 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.15

## Ticket 259: [P3] openssl: Excessive time spent checking DH keys and parameters

- **Score:** 41.7 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-3446  ·  **CWE:** CWE-606
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** medium  ·  **EPSS:** 0.06531 (pct 0.93192)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=13.2, epss=14.0, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-3446; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1u-r2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1u-r2

## Ticket 260: [P3] ntp: Potential Overflows in ctl_put() functions

- **Score:** 41.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-6458  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06515 (pct 0.93176)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-6458; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.11 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.11

## Ticket 261: [P3] php: Stack based 1-byte buffer over-write in zend_ini_do_op() function Zend/zend_ini_parser.c

- **Score:** 41.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-11628  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03365 (pct 0.87699)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-11628; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 262: [P3] mysql: insecure error log file handling in mysqld_safe (CPU Oct 2016)

- **Score:** 41.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-6664  ·  **CWE:** CWE-59
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0308 (pct 0.86535)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.2, epss=13.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-6664; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.52-0ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libmysqlclient18 from 5.5.47-0ubuntu0.14.04.1 to 5.5.52-0ubuntu0.14.04.1

## Ticket 263: [P3] php: Out-of-bounds memory read via gdImageRotateInterpolated

- **Score:** 41.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1903  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.07806 (pct 0.94146)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1903; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 264: [P3] perl: Directory traversal in Archive::Tar

- **Score:** 41.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-12015  ·  **CWE:** CWE-59
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.07251 (pct 0.93794)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=14.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-12015; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.6 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.6

## Ticket 265: [P3] busybox: Insufficient sanitization of filenames when autocompleting

- **Score:** 41.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-16544  ·  **CWE:** CWE-94
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0624 (pct 0.92929)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-16544; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package busybox-initramfs from 1:1.21.0-1ubuntu1 to 1:1.21.0-1ubuntu1.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade busybox-initramfs from 1:1.21.0-1ubuntu1 to 1:1.21.0-1ubuntu1.4

## Ticket 266: [P3] libxml2: Heap-buffer-overflow in xmlFAParserPosCharGroup

- **Score:** 41.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1840  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03239 (pct 0.87215)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=13.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1840; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8

## Ticket 267: [P3] minimatch: Minimatch: Denial of Service via catastrophic backtracking in glob expressions

- **Score:** 41.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-27904  ·  **CWE:** CWE-1333
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00472 (pct 0.38781)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=5.8, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-27904; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package minimatch from 3.0.5 to 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade minimatch from 3.0.5 to 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4

## Ticket 268: [P3] curl: IMAP FETCH response out of bounds read

- **Score:** 41.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-1000257  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06224 (pct 0.92913)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-1000257; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.12 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.12

## Ticket 269: [P3] curl: Out-of-bounds heap read when missing RTSP headers allows information leak or denial of service

- **Score:** 41.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-1000301  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05927 (pct 0.92609)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-1000301; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcurl3-gnutls from 7.35.0-1ubuntu2.6 to 7.35.0-1ubuntu2.16

## Ticket 270: [P3] perl: Buffer over-read in regular expression parser

- **Score:** 41.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-12883  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.05908 (pct 0.92588)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-12883; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade perl from 5.18.2-2ubuntu1 to 5.18.2-2ubuntu1.3

## Ticket 271: [P3] libxml2: Use after free in xmlXPathCompOpEvalPositionalPredicate() function in xpath.c

- **Score:** 41.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-15412  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.02938 (pct 0.85924)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=12.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-15412; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.12 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.12

## Ticket 272: [P3] php: Zend OPCache code permission/sensitive data protection issues

- **Score:** 41.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8994  ·  **CWE:** CWE-264
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.02937 (pct 0.85919)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=12.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8994; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 273: [P3] body-parser: Denial of Service Vulnerability in body-parser

- **Score:** 41.4 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2024-45590  ·  **CWE:** CWE-405
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00824 (pct 0.54319)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=8.1, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2024-45590; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package body-parser from 1.18.3 to 1.20.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade body-parser from 1.18.3 to 1.20.3

## Ticket 274: [P3] node-tar: tar: node-tar: Arbitrary file creation via path traversal bypass in hardlink security check

- **Score:** 41.4 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2026-24842  ·  **CWE:** CWE-22
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00541 (pct 0.4293)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=20.5, epss=6.4, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-24842; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tar from 4.4.19 to 7.5.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tar from 4.4.19 to 7.5.7

## Ticket 275: [P3] multer: Multer: Denial of Service via deeply nested field names in multipart form data

- **Score:** 41.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-5079  ·  **CWE:** CWE-400
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00278 (pct 0.20353)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=3.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-5079; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package multer from 1.4.5-lts.2 to 2.2.0, 3.0.0-alpha.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade multer from 1.4.5-lts.2 to 2.2.0, 3.0.0-alpha.2

## Ticket 276: [P3] php: Out-of-bounds read in phar_parse_zipfile()

- **Score:** 41.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-3142  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.05181 (pct 0.91741)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-3142; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 277: [P3] openssl: Generating excessively long X9.42 DH keys or checking excessively long X9.42 DH keys or parameters may be very slow

- **Score:** 41.3 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-5678  ·  **CWE:** CWE-606
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** medium  ·  **EPSS:** 0.04459 (pct 0.90609)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=13.2, epss=13.6, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-5678; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1w-r1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1w-r1

## Ticket 278: [P3] php: Out-of-bounds read in phar_parse_pharfile

- **Score:** 41.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-11147  ·  **CWE:** CWE-125
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0471 (pct 0.91045)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-11147; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.22

## Ticket 279: [P3] Forgeable Public/Private Tokens

- **Score:** 41.2 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1000223  ·  **CWE:** -
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** - (pct -)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=21.7, epss=0.0, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1000223; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package jws from 0.2.6 to >=3.0.0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade jws from 0.2.6 to >=3.0.0

## Ticket 280: [P3] glibc: Segmentation fault caused by passing out-of-range data to strftime()

- **Score:** 41.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8776  ·  **CWE:** CWE-189
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04613 (pct 0.90883)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8776; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.8

## Ticket 281: [P3] php: out-of-bounds write in fpm_log.c

- **Score:** 41.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5114  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04489 (pct 0.90654)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5114; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.19

## Ticket 282: [P3] httpd: mod_auth_digest: access control bypass due to race condition

- **Score:** 41.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-0217  ·  **CWE:** CWE-362
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.17359 (pct 0.96849)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=15.0, epss=14.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-0217; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.22 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade apache2 from 2.4.7-1ubuntu4.9 to 2.4.7-1ubuntu4.22

## Ticket 283: [P3] php: Regular Expression Uninitialized Pointer Information Disclosure Vulnerability (ZDI-CAN-2547)

- **Score:** 41.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2015-8382  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.04072 (pct 0.89811)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2015-8382; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpcre3 from 1:8.31-2ubuntu2.1 to 1:8.31-2ubuntu2.2

## Ticket 284: [P3] openssh: Improper validation of object names allows malicious server to overwrite files via scp client

- **Score:** 40.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2019-6111  ·  **CWE:** CWE-22
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.58204 (pct 0.99014)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=14.5, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2019-6111; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.13 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.13

## Ticket 285: [P3] ntp: ntpd switching to interleaved mode with spoofed packets

- **Score:** 40.9 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1548  ·  **CWE:** CWE-19
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03844 (pct 0.89216)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.4, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1548; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade ntpdate from 1:4.2.6.p5+dfsg-3ubuntu2.14.04.6 to 1:4.2.6.p5+dfsg-3ubuntu2.14.04.10

## Ticket 286: [P3] git: git-prompt.sh does not sanitize branch names in $PS1

- **Score:** 40.8 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2014-9938  ·  **CWE:** CWE-116
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.0232 (pct 0.81994)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=12.3, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2014-9938; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade git from 1:1.9.1-1ubuntu0.2 to 1:1.9.1-1ubuntu0.4

## Ticket 287: [P3] OpenSSL: Excessive time spent checking DH q parameter value

- **Score:** 40.7 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2023-3817  ·  **CWE:** CWE-606
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** medium  ·  **EPSS:** 0.03047 (pct 0.86399)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=13.2, epss=13.0, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2023-3817; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1v-r0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1v-r0

## Ticket 288: [P3] libxml2: Use after free triggered by XPointer paths beginning with range-to

- **Score:** 40.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-5131  ·  **CWE:** CWE-416
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.02251 (pct 0.81409)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=12.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-5131; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.9 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.9

## Ticket 289: [P3] sensible-browser in sensible-utils before 0.0.11 does not validate str ...

- **Score:** 40.7 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-17512  ·  **CWE:** CWE-74
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.02235 (pct 0.81285)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=12.2, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-17512; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package sensible-utils from 0.0.9 to 0.0.9ubuntu0.14.04.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade sensible-utils from 0.0.9 to 0.0.9ubuntu0.14.04.1

## Ticket 290: [P3] Cross-Site Scripting in sanitize-html

- **Score:** 40.7 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2017-16016  ·  **CWE:** CWE-79
- **Endpoint:** Node.js
- **Severity:** medium  ·  **EPSS:** 0.01357 (pct 0.69299)  ·  **KEV:** no
- **Escalation potential:** 0.456

**Score breakdown:** cvss=10.8, epss=10.4, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-16016; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package sanitize-html from 1.4.2 to 1.11.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade sanitize-html from 1.4.2 to 1.11.4

## Ticket 291: [P3] openssl: AES OCB fails to encrypt some bytes

- **Score:** 40.6 / 100  ·  **Owner:** appsec-node  ·  **SLA:** 168h
- **Product:** nodegoat  ·  **Scanner:** trivy
- **CVE:** CVE-2022-2097  ·  **CWE:** CWE-327
- **Endpoint:** nodegoat-web:latest (alpine 3.15.4)
- **Severity:** medium  ·  **EPSS:** 0.04425 (pct 0.90533)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=12.5, epss=13.6, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2022-2097; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libcrypto1.1 from 1.1.1n-r0 to 1.1.1q-r0 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libcrypto1.1 from 1.1.1n-r0 to 1.1.1q-r0

## Ticket 292: [P3] libxml2: Heap buffer overflow in xmlAddID

- **Score:** 40.6 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-0663  ·  **CWE:** CWE-787
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.02142 (pct 0.80479)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=17.0, epss=12.1, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-0663; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.10

## Ticket 293: [P3] python: smtplib StartTLS stripping attack

- **Score:** 40.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-0772  ·  **CWE:** CWE-693
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.1503 (pct 0.96426)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=14.5, epss=14.5, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-0772; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libpython2.7-minimal from 2.7.6-8ubuntu0.2 to 2.7.6-8ubuntu0.3

## Ticket 294: [P3] php: Type confusion vulnerability in make_http_soap_request()

- **Score:** 40.5 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-3185  ·  **CWE:** CWE-20
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.03146 (pct 0.86809)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.0, epss=13.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-3185; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libapache2-mod-php5 from 5.5.9+dfsg-1ubuntu4.14 to 5.5.9+dfsg-1ubuntu4.16

## Ticket 295: [P3] minimatch: minimatch: Denial of Service due to unbounded recursive backtracking via crafted glob patterns

- **Score:** 40.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-27903  ·  **CWE:** CWE-407
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00517 (pct 0.41611)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=14.8, epss=6.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-27903; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package minimatch from 3.0.5 to 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade minimatch from 3.0.5 to 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3

## Ticket 296: [P3] node-tar: node-tar: Arbitrary file read/write via malicious archive hardlink creation

- **Score:** 40.5 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-26960  ·  **CWE:** CWE-22
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00288 (pct 0.21314)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=17.8, epss=3.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-26960; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tar from 6.2.1 to 7.5.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tar from 6.2.1 to 7.5.8

## Ticket 297: [P3] bash: Arbitrary code execution via malicious hostname

- **Score:** 40.4 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-0634  ·  **CWE:** CWE-78
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.06019 (pct 0.92707)  ·  **KEV:** no
- **Escalation potential:** 0.95

**Score breakdown:** cvss=15.0, epss=13.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-0634; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package bash from 4.3-7ubuntu1.5 to 4.3-7ubuntu1.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade bash from 4.3-7ubuntu1.5 to 4.3-7ubuntu1.7

## Ticket 298: [P3] node-tar: hardlink path traversal via drive-relative linkpath

- **Score:** 40.4 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-29786  ·  **CWE:** CWE-22
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00408 (pct 0.33994)  ·  **KEV:** no
- **Escalation potential:** 0.798

**Score breakdown:** cvss=15.8, epss=5.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2026-29786; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package tar from 6.2.1 to 7.5.10 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade tar from 6.2.1 to 7.5.10

## Ticket 299: [P3] krb5: null dereference in kadmind or DN container check bypass by supplying special crafted data

- **Score:** 40.3 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2018-5729  ·  **CWE:** CWE-476
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.02582 (pct 0.83898)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=12.6, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2018-5729; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package krb5-locales from 1.12+dfsg-2ubuntu5.2 to 1.12+dfsg-2ubuntu5.4 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade krb5-locales from 1.12+dfsg-2ubuntu5.2 to 1.12+dfsg-2ubuntu5.4

## Ticket 300: [P3] glibc: Memory leak reachable via LD_HWCAP_MASK

- **Score:** 40.2 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2017-1000408  ·  **CWE:** CWE-772
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.0145 (pct 0.71118)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.0, epss=10.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2017-1000408; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libc-bin from 2.19-0ubuntu6.6 to 2.19-0ubuntu6.14

## Ticket 301: [P3] node-jws: auth0/node-jws: Improper signature verification in HS256 algorithm

- **Score:** 40.2 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2025-65945  ·  **CWE:** CWE-347
- **Endpoint:** Node.js
- **Severity:** high  ·  **EPSS:** 0.00219 (pct 0.12606)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=18.8, epss=1.9, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2025-65945; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package jws from 0.2.6 to 3.2.3, 4.0.1 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade jws from 0.2.6 to 3.2.3, 4.0.1

## Ticket 302: [P3] openssh: missing sanitisation of input for X11 forwarding

- **Score:** 40.1 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-3115  ·  **CWE:** CWE-93
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** low  ·  **EPSS:** 0.37016 (pct 0.98387)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=13.8, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-3115; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.7 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade openssh-client from 1:6.6p1-2ubuntu2.6 to 1:6.6p1-2ubuntu2.7

## Ticket 303: [P3] libxml2: Heap-based buffer-overread in xmlNextChar

- **Score:** 40.0 / 100  ·  **Owner:** appsec-legacy  ·  **SLA:** 168h
- **Product:** bwapp  ·  **Scanner:** trivy
- **CVE:** CVE-2016-1762  ·  **CWE:** CWE-119
- **Endpoint:** raesene/bwapp:latest (ubuntu 14.04)
- **Severity:** medium  ·  **EPSS:** 0.06466 (pct 0.93138)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=14.5, epss=14.0, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0

**Remediation:**
- *first_aid:* Apply the vendor security patch for CVE-2016-1762; if unavailable, isolate the container and restrict egress.
- *full_remediation:* Upgrade package libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8 (fixed version) in the image and rebuild/redeploy.
- *scanner_guidance:* Upgrade libxml2 from 2.9.1+dfsg1-3ubuntu4.7 to 2.9.1+dfsg1-3ubuntu4.8

## Ticket 304: [P3] glibc: glibc: Application crash or uninitialized memory read via crafted DNS response

- **Score:** 40.0 / 100  ·  **Owner:** appsec-web  ·  **SLA:** 168h
- **Product:** juice_shop  ·  **Scanner:** trivy
- **CVE:** CVE-2026-6238  ·  **CWE:** CWE-126
- **Endpoint:** bkimminich/juice-shop:latest (debian 13.6)
- **Severity:** medium  ·  **EPSS:** 0.00358 (pct 0.28955)  ·  **KEV:** no
- **Escalation potential:** 0.0

**Score breakdown:** cvss=16.2, epss=4.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0

**Remediation:**
- *first_aid:* Disable or restrict the affected functionality/endpoint at the perimeter (WAF rule, network ACL, feature flag) while the fix is prepared.
- *full_remediation:* Patch or upgrade the affected component to the latest fixed version and re-run the scan to confirm the finding is gone.
- *scanner_guidance:* glibc: glibc: Application crash or uninitialized memory read via crafted DNS response
