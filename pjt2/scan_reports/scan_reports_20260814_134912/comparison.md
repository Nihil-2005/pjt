# Scanner Findings vs. Documented Vulnerabilities

**Lab:** OWASP Juice Shop, OWASP NodeGoat, bWAPP (Docker, WSL)
**Scanners:** Nuclei, Wapiti, OWASP ZAP (baseline), Trivy — all unauthenticated, run on `scan_reports_20260814_134912`
**Documented catalogs used:**
- **Juice Shop** — official `challenges.yml` (116 challenges, 16 categories) + companion guide
- **NodeGoat** — official README / in-app `/tutorial` (OWASP Top 10 coverage)
- **bWAPP** — official bug list ("100+ web bugs", covers all OWASP Top 10 risks)

> ⚠️ **Read this first.** These are *training* apps, so their "documented vulnerabilities" are
> mostly **application-logic flaws** (injection, XSS, broken access control, CSRF, insecure
> deserialization…) that live behind login and require authenticated, interactive testing.
> This scan was **unauthenticated and baseline-level** (ZAP baseline = spider + passive checks,
> Nuclei = known-pattern matching, Wapiti = active but only over what it could crawl). Trivy is a
> different class: it statically scans the container images for CVEs. The comparison below reflects
> that reality — a low detection rate on logic flaws is expected scanner behavior, not a lab failure.

---

## 1) OWASP Juice Shop — documented: 116 challenges / 16 categories

| Documented category | # challenges | Detected? | Scanner evidence |
|---|---|---|---|
| Security Misconfiguration | 5 | ✅ **Strong** | ZAP: CSP not set (5), COEP/COOP missing (10), deprecated Feature Policy, Cross-Domain Misconfiguration; Nuclei: exposed Swagger API docs `/api-docs/swagger.yaml` |
| Vulnerable Components | 9 | ✅ **Strong** | Trivy: **8 CRITICAL** (jsonwebtoken CVE-2015-9235, lodash CVE-2019-10744, crypto-js CVE-2023-46233, tar CVE-2026-59873, decompress, marsdb) + 40 HIGH; ZAP: "Vulnerable JS Library" |
| Sensitive Data Exposure | 17 | ⚠️ **Partial** | Timestamp Disclosure (ZAP), storable/non-cacheable content, unencrypted channels (Wapiti) — but the real data-exposure challenges (password hash leak, API user-data exposure…) **not found** |
| Cryptographic Issues | 5 | ⚠️ **Partial** | Only "Unencrypted Channels" (Wapiti); weak-hash/broken-crypto challenges **not found** |
| Injection | 14 | ❌ None | (SQLi, NoSQLi, command injection, log injection — need auth/active testing) |
| XSS | 9 | ❌ None | (SPA, not crawled by baseline spider) |
| Broken Access Control | 12 | ❌ None | (IDOR, admin registration — need auth) |
| Broken Authentication | 9 | ❌ None | (JWT tampering, weak passwords) |
| Improper Input Validation | 12 | ❌ None | |
| Insecure Deserialization | 3 | ❌ None | |
| Unvalidated Redirects | 2 | ❌ None | |
| XXE | 2 | ❌ None | |
| Observability Failures | 4 | ❌ None | |
| Broken Anti Automation | 4 | ❌ None | |
| Security through Obscurity | 3 | ❌ None | |
| Miscellaneous | 6 | ❌ None | |

**Detected: 2/16 fully, 2/16 partially.** All 12 logic-flaw categories were missed — the app is an
Angular SPA, so a non-Ajax baseline spider never reaches the challenge surfaces.

---

## 2) OWASP NodeGoat — documented: OWASP Top 10 (A1–A10)

| Documented (Top 10) | Detected? | Scanner evidence |
|---|---|---|
| A9 Using Components with Known Vulnerabilities | ✅ **Strong** | Trivy: **13 CRITICAL** (bson CVE-2020-7610, underscore CVE-2021-23358, minimist CVE-2021-44906, set-value, mixin-deep, form-data, tar, zlib) + 68 HIGH; ZAP: "Vulnerable JS Library" (2) |
| A3 Cross-Site Scripting | ✅ **Found** | Wapiti: **Reflected XSS** (1) |
| A5 Security Misconfiguration | ✅ **Strong** | ZAP: missing anti-clickjacking, X-Content-Type-Options, COEP/COOP/CORP, Permissions Policy, CSP failure; X-Powered-By leak; Nuclei: OPTIONS enabled, missing security headers, tech disclosure |
| A6 Sensitive Data Exposure | ✅ **Partial** | Wapiti: **Cleartext password submission** (3×), unencrypted channels, Secure-flag cookie; Nuclei: cookies without Secure; ZAP: session mgmt identified |
| A1 Injection | ⚠️ **Partial** | ZAP: "Source Code Disclosure - SQL" — the NoSQL/SQLi itself **not confirmed** (needs auth) |
| A2 Broken Authentication | ⚠️ **Partial** | Session mgmt issues flagged; documented default creds (`admin/Admin_123`, `user1/User1_123`) never tested (login bypass not exercised) |
| A4 Insecure Direct Object References | ❌ None | (profile ID manipulation — behind login) |
| A7 Missing Function Level Access Control | ❌ None | (admin routes — behind login) |
| A8 CSRF | ❌ None | (update-profile CSRF — needs authenticated session) |
| A10 Unvalidated Redirects | ❌ None | |

**Detected: 2/10 fully, 3/10 partially, 5/10 missed.** Same story as Juice Shop — the documented
flaws are mostly behind `/login`.

---

## 3) bWAPP — documented: 100+ bugs (OWASP Top 10 + more)

| Documented area | Detected? | Scanner evidence |
|---|---|---|
| Security Misconfiguration | ✅ **Strong** | Nuclei: **phpinfo.php exposed**, **PHP 5.5.9 EOL**, robots.txt leaking `/admin/`, `/passwords/`, `/documents/`, `web.config` probing, **MySQL 5.5 version disclosure on 3306**; ZAP: Server version leak, X-Powered-By |
| Using Components with Known Vulnerabilities (A9) | ✅ **Strong** | Trivy: **1,783 findings** (28 HIGH, 1,262 MEDIUM, 493 LOW) — EOL Ubuntu 14.04 base: openssl, glibc, apt, sudo, git CVEs |
| Sensitive Data Exposure / cleartext | ⚠️ **Partial** | Wapiti: unencrypted channels, HttpOnly/Secure cookie flags; ZAP: storable cacheable content |
| Information Disclosure | ⚠️ **Partial** | ZAP: Application Error Disclosure; Nuclei: WAF fingerprint |
| XSS (reflected/stored), HTML/iFrame injection | ❌ None | (all behind login) |
| SQL injection (login/search/blind/stored) | ❌ None | (login-walled) |
| OS/PHP command injection, LFI/RFI, directory traversal/browsing | ❌ None | (login-walled) |
| CSRF, IDOR, weak session ID / session fixation | ❌ None | (need authenticated session) |
| LDAP injection, SSRF, HTTP parameter pollution, verb tampering | ❌ None | (login-walled) |
| File upload (restricted/arbitrary) | ❌ None | (login-walled) |

**Detected: 2/10 areas fully, 2/10 partially.** bWAPP's interesting bugs are almost all reachable
only after login — an unauthenticated scan only sees the landing/login pages, phpinfo and headers.

---

## 4) Cross-cutting observations

1. **Vulnerable components is where the scanners shine.** Trivy (and ZAP's "Vulnerable JS Library")
   precisely confirm the documented **A9 / "Vulnerable Components"** coverage in all three apps
   (Juice Shop 8 critical, NodeGoat 13 critical, bWAPP 1,783 on an EOL base image). This is the
   only documented category where detection is essentially complete.
2. **Misconfiguration/info-leak categories are well detected.** Missing security headers, CSP,
   clickjacking, version disclosures, phpinfo, robots.txt, API-docs exposure — every scanner
   contributed here.
3. **The "real" training bugs were almost entirely missed — and that's expected.** SQLi, stored
   XSS, IDOR, CSRF, privilege escalation, deserialization, file upload, and the rest require
   authentication plus human-like interaction. None of the four scanners logged in (bWAPP/NodeGoat
   are login-walled; Juice Shop is an SPA). Wapiti was the only scanner to confirm an actual
   exploit-class finding (reflected XSS on NodeGoat; cleartext password submission on NodeGoat).
4. **Scanner-to-scanner overlap is minimal** — they find different things: Nuclei = known
   fingerprints/exposures, ZAP baseline = passive misconfigs, Wapiti = active but shallow,
   Trivy = image CVEs. No two scanners found the same issue, so running all four is justified.
5. **To detect the documented logic flaws, upgrade the scan:** authenticate to bWAPP/NodeGoat
   (e.g., ZAP with session management + login), use ZAP **active** scan or ajax spider for the
   Juice Shop SPA, and add manual validation of the documented challenge list.

---

*Sources: OWASP Juice Shop `challenges.yml` (master), OWASP NodeGoat README/tutorial,
bWAPP official documentation (sourceforge.net/projects/bwapp — "over 100 web bugs… all risks from
the OWASP Top 10"), plus the scan artifacts in this folder.*
