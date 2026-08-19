# Top Action List — Risk Prioritized Findings

Run: 2026-08-16T13:22:06  ·  Products: juice_shop, nodegoat, bwapp

Raw findings: **2122** → unique: **767** → after filtering: **730** (dedup **63.85%**)

| Rank | Score | Pri | SLA | Owner | Product | Title | CVE | CWE | Endpoint |
|-----:|------:|-----|----:|-------|---------|-------|-----|-----|----------|
| 1 | 53.5 | P3 | 168h | appsec-node | nodegoat | zlib: heap-based buffer over-read and overflow in inflate()  | CVE-2022-37434 | CWE-787 | nodegoat-web:latest (alpine 3.15.4) |
| 2 | 53.3 | P3 | 168h | appsec-web | juice_shop | moment.js: regular expression denial of service | CVE-2016-4055 | CWE-400 | Node.js |
| 3 | 53.2 | P3 | 168h | appsec-node | nodegoat | node-ip: Incomplete fix for CVE-2023-42282 | CVE-2024-29415 | CWE-918 | Node.js |
| 4 | 52.5 | P3 | 168h | appsec-web | juice_shop | nodejs-jsonwebtoken: verification step bypass with an altere | CVE-2015-9235 | CWE-20 | Node.js |
| 5 | 51.5 | P3 | 168h | appsec-node | nodegoat | tough-cookie: prototype pollution in cookie memstore | CVE-2023-26136 | CWE-1321 | Node.js |
| 6 | 51.4 | P3 | 168h | appsec-legacy | bwapp | openssl: Memory corruption in the ASN.1 encoder | CVE-2016-2108 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 7 | 51.4 | P3 | 168h | appsec-legacy | bwapp | mysql: general_log can write to configuration files, leading | CVE-2016-6662 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 8 | 51.4 | P3 | 168h | appsec-web | juice_shop | glibc: stack guard protection bypass | CVE-2019-1010022 | CWE-119 | bkimminich/juice-shop:latest (debian 13.6) |
| 9 | 51.3 | P3 | 168h | appsec-legacy | bwapp | openssl: doapr_outch function does not verify that certain m | CVE-2016-2842 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 10 | 51.2 | P3 | 168h | appsec-legacy | bwapp | OpenSSL: Fix memory issues in BIO_*printf functions | CVE-2016-0799 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 11 | 51.2 | P3 | 168h | appsec-legacy | bwapp | OpenSSL: Double-free in DSA code | CVE-2016-0705 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 12 | 51.2 | P3 | 168h | appsec-legacy | bwapp | python: Heap overflow in zipimporter module | CVE-2016-5636 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 13 | 51.1 | P3 | 168h | appsec-legacy | bwapp | libxml2: Incorrect limit used for port values | CVE-2017-7376 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 14 | 51.1 | P3 | 168h | appsec-legacy | bwapp | git: path_name() integer truncation and overflow leading to  | CVE-2016-2324 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 15 | 51.0 | P3 | 168h | appsec-legacy | bwapp | git: path_name() integer truncation and overflow leading to  | CVE-2016-2315 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 16 | 50.8 | P3 | 168h | appsec-legacy | bwapp | curl: NTLM password overflow via integer overflow | CVE-2018-14618 | CWE-122 | raesene/bwapp:latest (ubuntu 14.04) |
| 17 | 50.8 | P3 | 168h | appsec-legacy | bwapp | php: buffer overflow in handling of long link names in tar p | CVE-2016-2554 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 18 | 50.7 | P3 | 168h | appsec-legacy | bwapp | libxml2: Use after free via namespace node in XPointer range | CVE-2016-4658 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 19 | 50.5 | P3 | 168h | appsec-legacy | bwapp | libxml2: Format string vulnerability | CVE-2016-4448 | CWE-134 | raesene/bwapp:latest (ubuntu 14.04) |
| 20 | 50.4 | P3 | 168h | appsec-legacy | bwapp | perl-DBD-MySQL: Use after free in mysql_dr_error | CVE-2014-9906 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 21 | 50.3 | P3 | 168h | appsec-web | juice_shop | nodejs-lodash: command injection via template | CVE-2021-23337 | CWE-94 | Node.js |
| 22 | 50.1 | P3 | 168h | appsec-legacy | bwapp | perl-DBD-MySQL: Use after free when my_login fails | CVE-2015-8949 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 23 | 50.1 | P3 | 168h | appsec-node | nodegoat | nodejs-ip: arbitrary code execution via the isPublic() funct | CVE-2023-42282 | CWE-918 | Node.js |
| 24 | 50.0 | P3 | 168h | appsec-web | juice_shop | undici: Undici: HTTP Request Smuggling and Denial of Service | CVE-2026-1525 | CWE-444 | Node.js |
| 25 | 49.5 | P3 | 168h | appsec-web | juice_shop | glibc: running ldd on malicious ELF leads to code execution  | CVE-2019-1010023 |  | bkimminich/juice-shop:latest (debian 13.6) |
| 26 | 49.4 | P3 | 168h | appsec-web | juice_shop | http-cache-semantics: Regular Expression Denial of Service ( | CVE-2022-25881 | CWE-1333 | Node.js |
| 27 | 49.3 | P3 | 168h | appsec-web | juice_shop | crypto-js: PBKDF2 1,000 times weaker than specified in 1993  | CVE-2023-46233 | CWE-328 | Node.js |
| 28 | 49.2 | P3 | 168h | appsec-legacy | bwapp | Incorrect sanitation of the 302 redirect field in HTTP trans | CVE-2019-3462 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 29 | 49.2 | P3 | 168h | appsec-web | juice_shop | nodejs-lodash: prototype pollution in defaultsDeep function  | CVE-2019-10744 | CWE-1321 | Node.js |
| 30 | 49.0 | P3 | 168h | appsec-legacy | bwapp | supervisor: Command injection via malicious XML-RPC request | CVE-2017-11610 | CWE-276 | raesene/bwapp:latest (ubuntu 14.04) |
| 31 | 48.7 | P3 | 168h | appsec-legacy | bwapp | git: cvsserver command injection | CVE-2017-14867 | CWE-78 | raesene/bwapp:latest (ubuntu 14.04) |
| 32 | 48.3 | P3 | 168h | appsec-legacy | bwapp | libxml2: Heap-buffer-overflow in xmlStrncat | CVE-2016-1834 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 33 | 48.2 | P3 | 168h | appsec-node | nodegoat | nodejs-y18n: prototype pollution vulnerability | CVE-2020-7774 | CWE-1321 | Node.js |
| 34 | 48.0 | P3 | 168h | appsec-node | nodegoat | decode-uri-component: improper input validation resulting in | CVE-2022-38900 | CWE-20 | Node.js |
| 35 | 48.0 | P3 | 168h | appsec-legacy | bwapp | pcre: inefficient posix character class syntax check (8.38/1 | CVE-2015-8391 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 36 | 47.9 | P3 | 168h | appsec-node | nodegoat | openssl: X.400 address type confusion in X.509 GeneralName | CVE-2023-0286 | CWE-843 | nodegoat-web:latest (alpine 3.15.4) |
| 37 | 47.9 | P3 | 168h | appsec-node | nodegoat | openssl: double free after calling PEM_read_bio_ex | CVE-2022-4450 | CWE-415 | nodegoat-web:latest (alpine 3.15.4) |
| 38 | 47.9 | P3 | 168h | appsec-web | juice_shop | sanitize-html: insecure global regular expression replacemen | CVE-2022-25887 | CWE-1333 | Node.js |
| 39 | 47.9 | P3 | 168h | appsec-web | juice_shop | undici: undici: Denial of Service via unbounded memory consu | CVE-2026-1526 | CWE-409 | Node.js |
| 40 | 47.8 | P3 | 168h | appsec-node | nodegoat | express: "qs" prototype poisoning causes the hang of the nod | CVE-2022-24999 | CWE-1321 | Node.js |
| 41 | 47.6 | P3 | 168h | appsec-web | juice_shop | socket.io parser is a socket.io encoder and decoder written  | CVE-2023-32695 | CWE-20 | Node.js |
| 42 | 47.5 | P3 | 168h | appsec-web | juice_shop | engine.io: Specially crafted HTTP request can trigger an unc | CVE-2022-41940 | CWE-248 | Node.js |
| 43 | 47.4 | P3 | 168h | appsec-legacy | bwapp | glibc: Incorrect handling of RPATH in elf/dl-load.c can be u | CVE-2017-16997 | CWE-426 | raesene/bwapp:latest (ubuntu 14.04) |
| 44 | 47.4 | P3 | 168h | appsec-web | juice_shop | lodash: Prototype pollution in utilities function | CVE-2018-16487 | CWE-400 | Node.js |
| 45 | 47.2 | P3 | 168h | appsec-node | nodegoat | nodejs-ansi-regex: Regular expression denial of service (ReD | CVE-2021-3807 | CWE-1333 | Node.js |
| 46 | 46.9 | P3 | 168h | appsec-node | nodegoat | minimist: prototype pollution | CVE-2021-44906 | CWE-1321 | Node.js |
| 47 | 46.9 | P3 | 168h | appsec-node | nodegoat | openssl: use-after-free following BIO_new_NDEF | CVE-2023-0215 | CWE-416 | nodegoat-web:latest (alpine 3.15.4) |
| 48 | 46.9 | P3 | 168h | appsec-web | juice_shop | decompress: @xhmikosr/decompress: Decompress: Arbitrary file | CVE-2026-53486 | CWE-22 | Node.js |
| 49 | 46.7 | P3 | 168h | appsec-web | juice_shop | undici: Undici: Denial of Service via invalid WebSocket perm | CVE-2026-2229 | CWE-248 | Node.js |
| 50 | 46.6 | P3 | 168h | appsec-node | nodegoat | openssl: Denial of service by excessive resource usage in ve | CVE-2023-0464 | CWE-295 | nodegoat-web:latest (alpine 3.15.4) |
| 51 | 46.6 | P3 | 168h | appsec-node | nodegoat | nodejs-ini: Prototype pollution via malicious INI file | CVE-2020-7788 | CWE-1321 | Node.js |
| 52 | 46.5 | P3 | 168h | appsec-node | nodegoat | nodejs-mixin-deep: prototype pollution in function mixin-dee | CVE-2019-10746 | CWE-88 | Node.js |
| 53 | 46.4 | P3 | 168h | appsec-web | juice_shop | node-tar: tar: node-tar: Arbitrary file creation via path tr | CVE-2026-24842 | CWE-22 | Node.js |
| 54 | 46.3 | P3 | 168h | appsec-node | nodegoat | The uglify-js package before 2.6.0 for Node.js allows attack | CVE-2015-8858 | CWE-399 | Node.js |
| 55 | 46.3 | P3 | 168h | appsec-web | juice_shop | undici: undici: Denial of Service due to unbounded memory gr | CVE-2026-12151 | CWE-400 | Node.js |
| 56 | 46.2 | P3 | 168h | appsec-web | juice_shop | ws: ws: Denial of Service via memory exhaustion from small W | CVE-2026-48779 | CWE-400 | Node.js |
| 57 | 46.2 | P3 | 168h | appsec-web | juice_shop | Multer vulnerable to Denial of Service from maliciously craf | CVE-2025-47944 | CWE-248 | Node.js |
| 58 | 46.1 | P3 | 168h | appsec-legacy | bwapp | php: use of uninitialized pointer in PharFileInfo::getConten | CVE-2016-4342 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 59 | 46.1 | P3 | 168h | appsec-node | nodegoat | nodejs-semver: Regular expression denial of service | CVE-2022-25883 | CWE-1333 | Node.js |
| 60 | 46.1 | P3 | 168h | appsec-web | juice_shop | Multer vulnerable to Denial of Service via memory leaks from | CVE-2025-47935 | CWE-401 | Node.js |
| 61 | 45.9 | P3 | 168h | appsec-legacy | bwapp | openssl: OCSP Status Request extension unbounded memory grow | CVE-2016-6304 | CWE-401 | raesene/bwapp:latest (ubuntu 14.04) |
| 62 | 45.9 | P3 | 168h | appsec-legacy | bwapp | openssh: Denial of service via very long passwords | CVE-2016-6515 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 63 | 45.9 | P3 | 168h | appsec-web | juice_shop | glibc: uncontrolled recursion in function check_dst_limits_c | CVE-2018-20796 | CWE-674 | bkimminich/juice-shop:latest (debian 13.6) |
| 64 | 45.9 | P3 | 168h | appsec-web | juice_shop | multer: Multer: Denial of Service via malformed requests | CVE-2026-3520 | CWE-674 | Node.js |
| 65 | 45.9 | P3 | 168h | appsec-web | juice_shop | crypto-js is a JavaScript library of crypto standards. Versi | CVE-2026-71851 | CWE-331 | Node.js |
| 66 | 45.8 | P3 | 168h | appsec-web | juice_shop | Moment.js: Path traversal  in moment.locale | CVE-2022-24785 | CWE-22 | Node.js |
| 67 | 45.8 | P3 | 168h | appsec-node | nodegoat | nodejs-set-value: prototype pollution in function set-value | CVE-2019-10747 | CWE-400 | Node.js |
| 68 | 45.8 | P3 | 168h | appsec-node | nodegoat | nodejs-set-value: type confusion allows bypass of CVE-2019-1 | CVE-2021-23440 | CWE-843 | Node.js |
| 69 | 45.7 | P3 | 168h | appsec-legacy | bwapp | openssl: ASN.1 BIO handling of large amounts of data | CVE-2016-2109 | CWE-399 | raesene/bwapp:latest (ubuntu 14.04) |
| 70 | 45.7 | P3 | 168h | appsec-legacy | bwapp | OpenSSL: Avoid memory leak in SRP | CVE-2016-0798 | CWE-399 | raesene/bwapp:latest (ubuntu 14.04) |
| 71 | 45.6 | P3 | 168h | appsec-node | nodegoat | openssl: Possible DoS translating ASN.1 object identifiers | CVE-2023-2650 | CWE-770 | nodegoat-web:latest (alpine 3.15.4) |
| 72 | 45.6 | P3 | 168h | appsec-web | juice_shop | multer: Multer: Denial of Service via dropped file upload co | CVE-2026-2359 | CWE-772 | Node.js |
| 73 | 45.6 | P3 | 168h | appsec-web | juice_shop | multer: Multer: Denial of Service via malformed requests | CVE-2026-3304 | CWE-459 | Node.js |
| 74 | 45.6 | P3 | 168h | appsec-web | juice_shop | jsonwebtoken: Unrestricted key type could lead to legacy key | CVE-2022-23539 | CWE-327 | Node.js |
| 75 | 45.5 | P3 | 168h | appsec-node | nodegoat | bson: Deserialization of Untrusted Data could result in Code | CVE-2020-7610 | CWE-502 | Node.js |
| 76 | 45.3 | P3 | 168h | appsec-legacy | bwapp | git: arbitrary code execution via .gitmodules | CVE-2018-17456 | CWE-88 | raesene/bwapp:latest (ubuntu 14.04) |
| 77 | 45.3 | P3 | 168h | appsec-legacy | bwapp | php: Stack-based buffer under-read in php_stream_url_wrap_ht | CVE-2018-7584 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 78 | 45.3 | P3 | 168h | appsec-web | juice_shop | nodejs-moment: Regular expression denial of service | CVE-2017-18214 | CWE-400 | Node.js |
| 79 | 45.2 | P3 | 168h | appsec-node | nodegoat | A vulnerability classified as problematic has been found in  | CVE-2017-20165 | CWE-1333 | Node.js |
| 80 | 45.2 | P3 | 168h | appsec-web | juice_shop | socket.io: Unhandled 'error' event | CVE-2024-38355 | CWE-20 | Node.js |
| 81 | 45.1 | P3 | 168h | appsec-legacy | bwapp | openssl: Possible integer overflow vulnerabilities in codeba | CVE-2016-2177 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 82 | 45.1 | P3 | 168h | appsec-legacy | bwapp | openssl: Out-of-bounds write caused by unchecked errors in B | CVE-2016-2182 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 83 | 45.1 | P3 | 168h | appsec-legacy | bwapp | php: Use-after-free vulnerability when resizing the 'propert | CVE-2016-7479 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 84 | 45.1 | P3 | 168h | appsec-legacy | bwapp | httpd: mod_mime buffer overread | CVE-2017-7679 | CWE-126 | raesene/bwapp:latest (ubuntu 14.04) |
| 85 | 45.1 | P3 | 168h | appsec-legacy | bwapp | openssh: loading of untrusted PKCS#11 modules in ssh-agent | CVE-2016-10009 | CWE-426 | raesene/bwapp:latest (ubuntu 14.04) |
| 86 | 45.1 | P3 | 168h | appsec-legacy | bwapp | php: Use after free in WDDX Deserialize when processing XML  | CVE-2016-3141 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 87 | 45.1 | P3 | 168h | appsec-web | juice_shop | glibc: ASLR bypass using cache of thread stack and heap | CVE-2019-1010024 | CWE-200 | bkimminich/juice-shop:latest (debian 13.6) |
| 88 | 45.0 | P3 | 168h | appsec-legacy | bwapp | busybox: wget: Heap-based buffer overflow in the retrieve_fi | CVE-2018-1000517 | CWE-120 | raesene/bwapp:latest (ubuntu 14.04) |
| 89 | 45.0 | P3 | 168h | appsec-legacy | bwapp | openssl: Integer overflow in MDC2_Update() | CVE-2016-6303 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 90 | 45.0 | P3 | 168h | appsec-legacy | bwapp | busybox: heap-based buffer overflow in OPTION_6RD parsing | CVE-2016-2148 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 91 | 45.0 | P3 | 168h | appsec-legacy | bwapp | expat: Little entropy used for hash initialization | CVE-2016-5300 | CWE-399 | raesene/bwapp:latest (ubuntu 14.04) |
| 92 | 44.9 | P3 | 168h | appsec-legacy | bwapp | python: Command injection in the shutil module | CVE-2018-1000802 | CWE-77 | raesene/bwapp:latest (ubuntu 14.04) |
| 93 | 44.9 | P3 | 168h | appsec-legacy | bwapp | httpd: ap_get_basic_auth_pw() authentication bypass | CVE-2017-3167 | CWE-287 | raesene/bwapp:latest (ubuntu 14.04) |
| 94 | 44.9 | P3 | 168h | appsec-legacy | bwapp | httpd: mod_ssl NULL pointer dereference | CVE-2017-3169 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 95 | 44.9 | P3 | 168h | appsec-legacy | bwapp | php: Format string vulnerability in php_snmp_error() | CVE-2016-4071 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 96 | 44.9 | P3 | 168h | appsec-web | juice_shop | jsonwebtoken: Insecure default algorithm in jwt.verify() cou | CVE-2022-23540 | CWE-287 | Node.js |
| 97 | 44.8 | P3 | 168h | appsec-legacy | bwapp | php: bypass __wakeup() in deserialization of an unexpected o | CVE-2016-7124 | CWE-502 | raesene/bwapp:latest (ubuntu 14.04) |
| 98 | 44.8 | P3 | 168h | appsec-legacy | bwapp | php: Use After Free Vulnerability in PHP's GC algorithm and  | CVE-2016-5771 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 99 | 44.7 | P3 | 168h | appsec-legacy | bwapp | expat: Out-of-bounds heap read on crafted input causing cras | CVE-2016-0718 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 100 | 44.7 | P3 | 168h | appsec-legacy | bwapp | openssh: possible fallback from untrusted to trusted X11 for | CVE-2016-1908 | CWE-287 | raesene/bwapp:latest (ubuntu 14.04) |
| 101 | 44.7 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds heap memory read in exif_read_data() caus | CVE-2016-4543 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 102 | 44.7 | P3 | 168h | appsec-legacy | bwapp | curl: FTP path trickery leads to NIL byte out of bounds writ | CVE-2018-1000120 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 103 | 44.7 | P3 | 168h | appsec-legacy | bwapp | curl: escape and unescape integer overflows | CVE-2016-7167 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 104 | 44.7 | P3 | 168h | appsec-legacy | bwapp | perl: Integer overflow leading to buffer overflow in Perl_my | CVE-2018-18311 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 105 | 44.7 | P3 | 168h | appsec-node | nodegoat | nodejs-minimatch: ReDoS via the braceExpand function | CVE-2022-3517 | CWE-400 | Node.js |
| 106 | 44.7 | P3 | 168h | appsec-web | juice_shop | nodejs-ws: denial of service when handling a request with ma | CVE-2024-37890 | CWE-476 | Node.js |
| 107 | 44.6 | P3 | 168h | appsec-legacy | bwapp | curl: FTP wildcard out of bounds read | CVE-2017-8817 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 108 | 44.6 | P3 | 168h | appsec-legacy | bwapp | perl: heap buffer overflow in pp_pack.c | CVE-2018-6913 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 109 | 44.6 | P3 | 168h | appsec-legacy | bwapp | ntp: decodearr() can write beyond its buffer limit | CVE-2018-7183 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 110 | 44.6 | P3 | 168h | appsec-legacy | bwapp | php: Invalid memory access in function xmlrpc_decode() | CVE-2019-9020 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 111 | 44.6 | P3 | 168h | appsec-legacy | bwapp | php: Heap-based buffer over-read in PHAR reading functions | CVE-2019-9021 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 112 | 44.6 | P3 | 168h | appsec-legacy | bwapp | php: Double Free Corruption in wddx_deserialize | CVE-2016-5772 | CWE-415 | raesene/bwapp:latest (ubuntu 14.04) |
| 113 | 44.6 | P3 | 168h | appsec-legacy | bwapp | php: Double free in _php_mb_regex_ereg_replace_exec | CVE-2016-5768 | CWE-415 | raesene/bwapp:latest (ubuntu 14.04) |
| 114 | 44.6 | P3 | 168h | appsec-web | juice_shop | decompress: Decompress: Arbitrary file write leading to remo | CVE-2026-10732 | CWE-29 | Node.js |
| 115 | 44.6 | P3 | 168h | appsec-web | juice_shop | minimatch: minimatch: Denial of Service via specially crafte | CVE-2026-26996 | CWE-1333 | Node.js |
| 116 | 44.5 | P3 | 168h | appsec-legacy | bwapp | php: Uninitialized read in exif_process_IFD_in_TIFF | CVE-2019-9641 | CWE-908 | raesene/bwapp:latest (ubuntu 14.04) |
| 117 | 44.5 | P3 | 168h | appsec-legacy | bwapp | libX11: Out of Bounds write in XListExtensions in ListExt.c | CVE-2018-14600 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 118 | 44.5 | P3 | 168h | appsec-legacy | bwapp | php: Heap-based buffer over-read in mbstring regular express | CVE-2019-9023 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 119 | 44.5 | P3 | 168h | appsec-legacy | bwapp | php: ZipArchive class Use After Free Vulnerability in PHP's  | CVE-2016-5773 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 120 | 44.5 | P3 | 168h | appsec-legacy | bwapp | pcre: workspace overflow for (*ACCEPT) with deeply nested pa | CVE-2016-3191 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 121 | 44.5 | P3 | 168h | appsec-legacy | bwapp | php: Integer Overflows in mcrypt_generic() and mdecrypt_gene | CVE-2016-5769 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 122 | 44.5 | P3 | 168h | appsec-web | juice_shop | Sandbox escape in notevil and argencoders-notevil | CVE-2021-23771 | CWE-1321 | Node.js |
| 123 | 44.5 | P3 | 168h | appsec-web | juice_shop | socket.io: Socket.IO: Denial of Service due to excessive buf | CVE-2026-33151 | CWE-20 | Node.js |
| 124 | 44.4 | P3 | 168h | appsec-legacy | bwapp | python: Integer overflow in PyString_DecodeEscape results in | CVE-2017-1000158 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 125 | 44.4 | P3 | 168h | appsec-legacy | bwapp | php: Zend/zend_exceptions.c does not validate certain Except | CVE-2015-8876 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 126 | 44.4 | P3 | 168h | appsec-legacy | bwapp | oniguruma: Heap buffer overflow in next_state_val() during r | CVE-2017-9226 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 127 | 44.4 | P3 | 168h | appsec-legacy | bwapp | php: Off-by-one error in phar_parse_pharfile when loading cr | CVE-2016-10160 | CWE-193 | raesene/bwapp:latest (ubuntu 14.04) |
| 128 | 44.4 | P3 | 168h | appsec-legacy | bwapp | php: mb_strcut() Negative size parameter in memcpy | CVE-2016-4073 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 129 | 44.4 | P3 | 168h | appsec-web | juice_shop | glibc: uncontrolled recursion in function check_dst_limits_c | CVE-2019-9192 | CWE-674 | bkimminich/juice-shop:latest (debian 13.6) |
| 130 | 44.4 | P3 | 168h | appsec-node | nodegoat | http-cache-semantics: Regular Expression Denial of Service ( | CVE-2022-25881 | CWE-1333 | Node.js |
| 131 | 44.3 | P3 | 168h | appsec-legacy | bwapp | gnutls: Stack overflow in cdk_pk_get_keyid | CVE-2017-5336 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 132 | 44.3 | P3 | 168h | appsec-legacy | bwapp | pcre: Buffer overflow caused by lookbehind assertion (8.38/6 | CVE-2015-8386 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 133 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: Invalid read when wddx decodes empty boolean element | CVE-2016-9935 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 134 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: buffer over-read in finish_nested_data function | CVE-2017-12933 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 135 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: Out of bounds heap read when verifying signature of zip | CVE-2016-7414 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 136 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: Missing type check when unserializing SplArray | CVE-2016-7417 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 137 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: imagegammacorrect allows arbitrary write access | CVE-2016-7127 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 138 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: wddx_deserialize allows illegal memory access | CVE-2016-7129 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 139 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds heap memory read in exif_read_data() caus | CVE-2016-4544 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 140 | 44.3 | P3 | 168h | appsec-legacy | bwapp | php: Use after free in wddx_deserialize | CVE-2016-7413 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 141 | 44.3 | P3 | 168h | appsec-legacy | bwapp | oniguruma: Out-of-bounds stack read in match_at() during reg | CVE-2017-9224 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 142 | 44.3 | P3 | 168h | appsec-web | juice_shop | nodejs-got: missing verification of requested URLs allows re | CVE-2022-33987 |  | Node.js |
| 143 | 44.2 | P3 | 168h | appsec-legacy | bwapp | dhcp: unclosed TCP connections to OMAPI or failover ports ca | CVE-2016-2774 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 144 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: Heap buffer overflow vulnerability in simplestring_addn | CVE-2016-6296 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 145 | 44.2 | P3 | 168h | appsec-legacy | bwapp | oniguruma: Out-of-bounds stack read in mbc_enc_len() during  | CVE-2017-9227 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 146 | 44.2 | P3 | 168h | appsec-legacy | bwapp | oniguruma: Out-of-bounds heap write in bitset_set_range() | CVE-2017-9228 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 147 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: xml_parse_into_struct() can crash when XML parser is re | CVE-2016-4539 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 148 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: OOB read in grapheme_stripos and grapheme_strpos when n | CVE-2016-4540 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 149 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: OOB read in grapheme_stripos and grapheme_strpos when n | CVE-2016-4541 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 150 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: bcpowmod accepts negative scale causing heap buffer ove | CVE-2016-4538 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 151 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: type confusion issue in Soap Client call() method | CVE-2015-8835 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 152 | 44.2 | P3 | 168h | appsec-legacy | bwapp | gnutls: Heap read overflow in read-packet.c | CVE-2017-5337 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 153 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds heap memory read in exif_read_data() caus | CVE-2016-4542 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 154 | 44.2 | P3 | 168h | appsec-legacy | bwapp | glibc: Unbounded stack allocation in catopen function | CVE-2015-8779 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 155 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds access in locale_accept_from_http | CVE-2016-6294 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 156 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: Invalid memory write in phar on filename containing \0  | CVE-2016-4072 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 157 | 44.2 | P3 | 168h | appsec-legacy | bwapp | The AMF3CD_AddProp function in amf.c in RTMPDump 2.4 allows  | CVE-2015-8271 | CWE-123 | raesene/bwapp:latest (ubuntu 14.04) |
| 158 | 44.2 | P3 | 168h | appsec-legacy | bwapp | php: bcpowmod accepts negative scale causing heap buffer ove | CVE-2016-4537 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 159 | 44.2 | P3 | 168h | appsec-legacy | bwapp | curl: Integer overflow leading to heap-based buffer overflow | CVE-2018-16839 | CWE-122 | raesene/bwapp:latest (ubuntu 14.04) |
| 160 | 44.2 | P3 | 168h | appsec-node | nodegoat | nodejs-underscore: Arbitrary code execution via the template | CVE-2021-23358 | CWE-94 | Node.js |
| 161 | 44.2 | P3 | 168h | appsec-web | juice_shop | glibc: information disclosure of heap addresses of pthread_c | CVE-2019-1010025 | CWE-330 | bkimminich/juice-shop:latest (debian 13.6) |
| 162 | 44.1 | P3 | 168h | appsec-legacy | bwapp | php: Memory corruption when destructing deserialized object | CVE-2016-7411 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 163 | 44.1 | P3 | 168h | appsec-legacy | bwapp | pcre: buffer overflow caused by named forward reference to d | CVE-2015-8385 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 164 | 44.1 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds access in exif_process_IFD_in_MAKERNOTE | CVE-2016-6291 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 165 | 44.1 | P3 | 168h | appsec-legacy | bwapp | glibc: Integer overflow in hcreate and hcreate_r | CVE-2015-8778 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 166 | 44.1 | P3 | 168h | appsec-legacy | bwapp | php: improper nul termination leading to out-of-bounds read  | CVE-2016-5093 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 167 | 44.1 | P3 | 168h | appsec-legacy | bwapp | krb5: Automatic sec context deletion could lead to double-fr | CVE-2017-11462 | CWE-415 | raesene/bwapp:latest (ubuntu 14.04) |
| 168 | 44.1 | P3 | 168h | appsec-legacy | bwapp | php: Use after free in unserialize() with Unexpected Session | CVE-2016-6290 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 169 | 44.1 | P3 | 168h | appsec-legacy | bwapp | php: Use-after-free vulnerability in the spl_ptr_heap_insert | CVE-2015-4116 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 170 | 44.1 | P3 | 168h | appsec-legacy | bwapp | php: Use after free in SNMP with GC and unserialize() | CVE-2016-6295 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 171 | 44.1 | P3 | 168h | appsec-legacy | bwapp | file: Buffer over-write in finfo_open with malformed magic f | CVE-2015-8865 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 172 | 44.1 | P3 | 168h | appsec-legacy | bwapp | php: Use after free in unserialize() | CVE-2016-9137 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 173 | 44.1 | P3 | 168h | appsec-legacy | bwapp | pcre: infinite recursion compiling pattern with recursive re | CVE-2015-2328 | CWE-19 | raesene/bwapp:latest (ubuntu 14.04) |
| 174 | 44.1 | P3 | 168h | appsec-legacy | bwapp | rsync: Heap-based buffer over-read in receive_xattr function | CVE-2017-16548 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 175 | 44.0 | P3 | 168h | appsec-legacy | bwapp | php: Buffer over-read in php_url_parse_ex | CVE-2016-6288 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 176 | 44.0 | P3 | 168h | appsec-legacy | bwapp | curl: Double-free in krb5 code | CVE-2016-8619 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 177 | 44.0 | P3 | 168h | appsec-legacy | bwapp | php: stack buffer overflow in locale_get_display_name | CVE-2014-9912 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 178 | 44.0 | P3 | 168h | appsec-legacy | bwapp | curl: Double-free in curl_maprintf | CVE-2016-8618 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 179 | 44.0 | P3 | 168h | appsec-legacy | bwapp | pcre: Integer overflow caused by missing check for certain c | CVE-2015-8394 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 180 | 44.0 | P3 | 168h | appsec-legacy | bwapp | libX11: Off-by-one error in XListExtensions in ListExt.c | CVE-2018-14599 | CWE-193 | raesene/bwapp:latest (ubuntu 14.04) |
| 181 | 44.0 | P3 | 168h | appsec-node | nodegoat | braces: fails to limit the number of characters it can handl | CVE-2024-4068 | CWE-1050 | Node.js |
| 182 | 43.9 | P3 | 168h | appsec-legacy | bwapp | glibc: realpath() buffer underflow when getcwd() returns rel | CVE-2018-1000001 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 183 | 43.9 | P3 | 168h | appsec-legacy | bwapp | curl: URL unescape heap overflow via integer truncation | CVE-2016-8622 | CWE-122 | raesene/bwapp:latest (ubuntu 14.04) |
| 184 | 43.9 | P3 | 168h | appsec-legacy | bwapp | curl: Glob parser write/read out of bounds | CVE-2016-8620 | CWE-120 | raesene/bwapp:latest (ubuntu 14.04) |
| 185 | 43.9 | P3 | 168h | appsec-legacy | bwapp | file: malformed elf file causes access to uninitialized memo | CVE-2014-9653 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 186 | 43.9 | P3 | 168h | appsec-legacy | bwapp | php: Integer overflow in php_html_entities() | CVE-2016-5094 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 187 | 43.9 | P3 | 168h | appsec-legacy | bwapp | pcre: uninitialized memory read triggered by malformed posix | CVE-2015-8390 | CWE-908 | raesene/bwapp:latest (ubuntu 14.04) |
| 188 | 43.9 | P3 | 168h | appsec-legacy | bwapp | pcre: OOB write when pcre_exec() is called with ovecsize of  | CVE-2015-8380 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 189 | 43.9 | P3 | 168h | appsec-legacy | bwapp | php: Integer underflow causing arbitrary null write in fread | CVE-2016-5096 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 190 | 43.8 | P3 | 168h | appsec-node | nodegoat | openssl: timing attack in RSA Decryption implementation | CVE-2022-4304 | CWE-203 | nodegoat-web:latest (alpine 3.15.4) |
| 191 | 43.8 | P3 | 168h | appsec-legacy | bwapp | libX11: Insufficient validation of server responses in FontN | CVE-2016-7943 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 192 | 43.8 | P3 | 168h | appsec-legacy | bwapp | libX11: Insufficient validation of server responses in XGetI | CVE-2016-7942 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 193 | 43.8 | P3 | 168h | appsec-web | juice_shop | sanitize-html: improper handling of internationalized domain | CVE-2021-26539 |  | Node.js |
| 194 | 43.8 | P3 | 168h | appsec-web | juice_shop | undici: Undici: Denial of Service via excessive decompressio | CVE-2026-22036 | CWE-770 | Node.js |
| 195 | 43.7 | P3 | 168h | appsec-legacy | bwapp | libidn2: Integer overflow in puny_decode.c/decode_digit | CVE-2017-14062 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 196 | 43.6 | P3 | 168h | appsec-legacy | bwapp | ntp: Null pointer dereference when trap service is enabled | CVE-2016-9311 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 197 | 43.6 | P3 | 168h | appsec-legacy | bwapp | pcre: Integer overflow in subroutine calls (8.38/8) | CVE-2015-8387 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 198 | 43.6 | P3 | 168h | appsec-web | juice_shop | tar: node-tar: Denial of Service via crafted gzip bomb | CVE-2026-59873 | CWE-770 | Node.js |
| 199 | 43.5 | P3 | 168h | appsec-legacy | bwapp | glibc: getaddrinfo stack-based buffer overflow | CVE-2015-7547 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 200 | 43.5 | P3 | 168h | appsec-legacy | bwapp | httpd: <FilesMatch> bypass with a trailing newline in the fi | CVE-2017-15715 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 201 | 43.5 | P3 | 168h | appsec-legacy | bwapp | ntp: assertion failure in ntpd on duplicate IPs on unconfig  | CVE-2016-2516 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 202 | 43.5 | P3 | 168h | appsec-legacy | bwapp | mysql: Server: Partition unspecified vulnerability (CPU Jan  | CVE-2018-2562 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 203 | 43.5 | P3 | 168h | appsec-legacy | bwapp | rsync: daemon does not check for fnamecmp filenames allowing | CVE-2017-17434 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 204 | 43.5 | P3 | 168h | appsec-web | juice_shop | tar: Node-tar: Denial of Service via malformed tar archive h | CVE-2026-59874 | CWE-835 | Node.js |
| 205 | 43.4 | P3 | 168h | appsec-legacy | bwapp | git: Command injection via malicious ssh URLs | CVE-2017-1000117 | CWE-601 | raesene/bwapp:latest (ubuntu 14.04) |
| 206 | 43.4 | P3 | 168h | appsec-web | juice_shop | sanitize-html: improper validation of hostnames set by the " | CVE-2021-26540 |  | Node.js |
| 207 | 43.4 | P3 | 168h | appsec-web | juice_shop | node-tar: node-tar: Denial of Service due to incorrect PAX p | CVE-2026-59871 | CWE-704 | Node.js |
| 208 | 43.3 | P3 | 168h | appsec-legacy | bwapp | HTTPD: sets environmental variable based on user supplied Pr | CVE-2016-5387 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 209 | 43.3 | P3 | 168h | appsec-legacy | bwapp | git: arbitrary code execution when recursively cloning a mal | CVE-2018-11235 | CWE-22 | raesene/bwapp:latest (ubuntu 14.04) |
| 210 | 43.3 | P3 | 168h | appsec-legacy | bwapp | libidn: out-of-bounds read with stringprep on invalid UTF-8 | CVE-2015-2059 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 211 | 43.3 | P3 | 168h | appsec-legacy | bwapp | perl: segmentation fault in S_regmatch on negative backrefer | CVE-2013-7422 | CWE-189 | raesene/bwapp:latest (ubuntu 14.04) |
| 212 | 43.3 | P3 | 168h | appsec-web | juice_shop | Command Injection in marsdb | GHSA-5mrr-rgp6-x4gr |  | Node.js |
| 213 | 43.2 | P3 | 168h | appsec-legacy | bwapp | vim: Lack of validation of values for few options results in | CVE-2016-1248 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 214 | 43.2 | P3 | 168h | appsec-legacy | bwapp | glibc: Buffer overflow in glob with GLOB_TILDE | CVE-2017-15670 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 215 | 43.2 | P3 | 168h | appsec-legacy | bwapp | php: Stack-based buffer over-read in msgfmt_parse_message fu | CVE-2017-11362 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 216 | 43.2 | P3 | 168h | appsec-node | nodegoat | nodejs-minimist: prototype pollution allows adding or modify | CVE-2020-7598 | CWE-1321 | Node.js |
| 217 | 43.1 | P3 | 168h | appsec-legacy | bwapp | glibc: Buffer overflow during unescaping of user names with  | CVE-2017-15804 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 218 | 43.1 | P3 | 168h | appsec-web | juice_shop | jsonwebtoken: Insecure implementation of key retrieval funct | CVE-2022-23541 | CWE-287 | Node.js |
| 219 | 43.0 | P3 | 168h | appsec-legacy | bwapp | httpd: Weak Digest auth nonce generation in mod_auth_digest | CVE-2018-1312 | CWE-287 | raesene/bwapp:latest (ubuntu 14.04) |
| 220 | 42.9 | P3 | 168h | appsec-legacy | bwapp | php: Integer overflow in php_filter_full_special_chars | CVE-2016-5095 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 221 | 42.9 | P3 | 168h | appsec-legacy | bwapp | libxml2: Missing validation for external entities in xmlPars | CVE-2017-7375 | CWE-611 | raesene/bwapp:latest (ubuntu 14.04) |
| 222 | 42.8 | P3 | 168h | appsec-legacy | bwapp | php: Improper error handling in bzread() | CVE-2016-5399 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 223 | 42.8 | P3 | 168h | appsec-legacy | bwapp | sudo: Privilege escalation in via improper get_process_ttyna | CVE-2017-1000367 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 224 | 42.7 | P3 | 168h | appsec-legacy | bwapp | php: Heap overflow in mysqlnd when not receiving UNSIGNED_FL | CVE-2016-7412 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 225 | 42.6 | P3 | 168h | appsec-legacy | bwapp | curl: Use of connection struct after free | CVE-2016-5421 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 226 | 42.6 | P3 | 168h | appsec-web | juice_shop | socket.io: engine.io: Socket.IO: Denial of Service via inval | CVE-2026-59725 | CWE-404 | Node.js |
| 227 | 42.5 | P3 | 168h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Op | CVE-2016-3492 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 228 | 42.5 | P3 | 168h | appsec-node | nodegoat | Arbitrary local file read vulnerability during template rend | CVE-2023-25345 | CWE-22 | Node.js |
| 229 | 42.4 | P3 | 168h | appsec-legacy | bwapp | php: buffer overflow in ext/phar/tar.c | CVE-2019-9675 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 230 | 42.4 | P3 | 168h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Ty | CVE-2016-3521 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 231 | 42.4 | P3 | 168h | appsec-web | juice_shop | socket.io-parser: Socket.IO: Denial of Service via memory ex | CVE-2026-69185 | CWE-20 | Node.js |
| 232 | 42.3 | P3 | 168h | appsec-legacy | bwapp | httpd: Uninitialized memory reflection in mod_auth_digest | CVE-2017-9788 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 233 | 42.3 | P3 | 168h | appsec-legacy | bwapp | libtasn1: Stack-based buffer overflow in asn1_find_node() | CVE-2017-6891 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 234 | 42.3 | P3 | 168h | appsec-legacy | bwapp | libxml2: Heap use-after-free in xmlSAX2AttributeNs | CVE-2016-1835 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 235 | 42.3 | P3 | 168h | appsec-legacy | bwapp | patch: Malicious patch files cause ed to execute arbitrary c | CVE-2018-1000156 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 236 | 42.3 | P3 | 168h | appsec-legacy | bwapp | php: Stack-based buffer overflow vulnerability in php_stream | CVE-2016-6297 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 237 | 42.3 | P3 | 168h | appsec-web | juice_shop | uuid: uuid: Out-of-bounds write vulnerability impacts data i | CVE-2026-41907 | CWE-787 | Node.js |
| 238 | 42.2 | P3 | 168h | appsec-legacy | bwapp | krb5: Metadata taken from the unauthenticated plaintext | CVE-2017-11103 | CWE-345 | raesene/bwapp:latest (ubuntu 14.04) |
| 239 | 42.2 | P3 | 168h | appsec-legacy | bwapp | glibc: buffer overflow in gethostbyname_r() and related func | CVE-2015-1781 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 240 | 42.2 | P3 | 168h | appsec-legacy | bwapp | curl: printf floating point buffer overflow | CVE-2016-9586 | CWE-122 | raesene/bwapp:latest (ubuntu 14.04) |
| 241 | 42.2 | P3 | 168h | appsec-legacy | bwapp | glibc: heap/stack gap jumping via unbounded stack allocation | CVE-2017-1000366 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 242 | 42.1 | P3 | 168h | appsec-legacy | bwapp | git: Escape out of git-shell | CVE-2017-8386 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 243 | 42.1 | P3 | 168h | appsec-web | juice_shop | glibc: glob implementation can cause excessive CPU and memor | CVE-2010-4756 | CWE-399 | bkimminich/juice-shop:latest (debian 13.6) |
| 244 | 42.1 | P3 | 168h | appsec-legacy | bwapp | procps: incorrect integer size in proc/alloc.* leading to tr | CVE-2018-1126 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 245 | 42.0 | P3 | 168h | appsec-legacy | bwapp | php: Uninitialized pointer in phar_make_dirstream() | CVE-2016-4343 | CWE-824 | raesene/bwapp:latest (ubuntu 14.04) |
| 246 | 42.0 | P3 | 168h | appsec-legacy | bwapp | php: libxml_disable_entity_loader setting is shared between  | CVE-2015-8866 | CWE-611 | raesene/bwapp:latest (ubuntu 14.04) |
| 247 | 41.9 | P3 | 168h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Jan  | CVE-2018-2668 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 248 | 41.9 | P3 | 168h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Jan 2018) | CVE-2018-2622 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 249 | 41.9 | P3 | 168h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Jan  | CVE-2018-2640 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 250 | 41.9 | P3 | 168h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Jan  | CVE-2018-2665 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 251 | 41.9 | P3 | 168h | appsec-legacy | bwapp | glibc: _IO_wstr_overflow integer overflow | CVE-2015-8983 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 252 | 41.9 | P3 | 168h | appsec-legacy | bwapp | glibc: multiple overflows in strxfrm() | CVE-2015-8982 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 253 | 41.9 | P3 | 168h | appsec-legacy | bwapp | php: Integer overflow leads to buffer overflow in virtual_fi | CVE-2016-6289 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 254 | 41.9 | P3 | 168h | appsec-web | juice_shop | lodash: Prototype pollution in utilities function | CVE-2018-3721 | CWE-471 | Node.js |
| 255 | 41.8 | P3 | 168h | appsec-legacy | bwapp | ntp: Mode 6 unauthenticated trap information disclosure and  | CVE-2016-9310 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 256 | 41.8 | P3 | 168h | appsec-legacy | bwapp | perl: Heap-based buffer read overflow in S_grok_bslash_N() | CVE-2018-18313 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 257 | 41.8 | P3 | 168h | appsec-web | juice_shop | sanitize-html: Information Exposure when used on the backend | CVE-2024-21501 | CWE-200 | Node.js |
| 258 | 41.7 | P3 | 168h | appsec-legacy | bwapp | curl: RTSP RTP buffer over-read | CVE-2018-1000122 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 259 | 41.7 | P3 | 168h | appsec-node | nodegoat | openssl: Excessive time spent checking DH keys and parameter | CVE-2023-3446 | CWE-606 | nodegoat-web:latest (alpine 3.15.4) |
| 260 | 41.7 | P3 | 168h | appsec-legacy | bwapp | ntp: Potential Overflows in ctl_put() functions | CVE-2017-6458 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 261 | 41.7 | P3 | 168h | appsec-legacy | bwapp | php: Stack based 1-byte buffer over-write in zend_ini_do_op( | CVE-2017-11628 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 262 | 41.7 | P3 | 168h | appsec-legacy | bwapp | mysql: insecure error log file handling in mysqld_safe (CPU  | CVE-2016-6664 | CWE-59 | raesene/bwapp:latest (ubuntu 14.04) |
| 263 | 41.6 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds memory read via gdImageRotateInterpolated | CVE-2016-1903 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 264 | 41.6 | P3 | 168h | appsec-legacy | bwapp | perl: Directory traversal in Archive::Tar | CVE-2018-12015 | CWE-59 | raesene/bwapp:latest (ubuntu 14.04) |
| 265 | 41.6 | P3 | 168h | appsec-legacy | bwapp | busybox: Insufficient sanitization of filenames when autocom | CVE-2017-16544 | CWE-94 | raesene/bwapp:latest (ubuntu 14.04) |
| 266 | 41.6 | P3 | 168h | appsec-legacy | bwapp | libxml2: Heap-buffer-overflow in xmlFAParserPosCharGroup | CVE-2016-1840 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 267 | 41.5 | P3 | 168h | appsec-web | juice_shop | minimatch: Minimatch: Denial of Service via catastrophic bac | CVE-2026-27904 | CWE-1333 | Node.js |
| 268 | 41.4 | P3 | 168h | appsec-legacy | bwapp | curl: IMAP FETCH response out of bounds read | CVE-2017-1000257 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 269 | 41.4 | P3 | 168h | appsec-legacy | bwapp | curl: Out-of-bounds heap read when missing RTSP headers allo | CVE-2018-1000301 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 270 | 41.4 | P3 | 168h | appsec-legacy | bwapp | perl: Buffer over-read in regular expression parser | CVE-2017-12883 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 271 | 41.4 | P3 | 168h | appsec-legacy | bwapp | libxml2: Use after free in xmlXPathCompOpEvalPositionalPredi | CVE-2017-15412 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 272 | 41.4 | P3 | 168h | appsec-legacy | bwapp | php: Zend OPCache code permission/sensitive data protection  | CVE-2015-8994 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 273 | 41.4 | P3 | 168h | appsec-node | nodegoat | body-parser: Denial of Service Vulnerability in body-parser | CVE-2024-45590 | CWE-405 | Node.js |
| 274 | 41.4 | P3 | 168h | appsec-node | nodegoat | node-tar: tar: node-tar: Arbitrary file creation via path tr | CVE-2026-24842 | CWE-22 | Node.js |
| 275 | 41.4 | P3 | 168h | appsec-web | juice_shop | multer: Multer: Denial of Service via deeply nested field na | CVE-2026-5079 | CWE-400 | Node.js |
| 276 | 41.3 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds read in phar_parse_zipfile() | CVE-2016-3142 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 277 | 41.3 | P3 | 168h | appsec-node | nodegoat | openssl: Generating excessively long X9.42 DH keys or checki | CVE-2023-5678 | CWE-606 | nodegoat-web:latest (alpine 3.15.4) |
| 278 | 41.2 | P3 | 168h | appsec-legacy | bwapp | php: Out-of-bounds read in phar_parse_pharfile | CVE-2017-11147 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 279 | 41.2 | P3 | 168h | appsec-web | juice_shop | Forgeable Public/Private Tokens | CVE-2016-1000223 |  | Node.js |
| 280 | 41.1 | P3 | 168h | appsec-legacy | bwapp | glibc: Segmentation fault caused by passing out-of-range dat | CVE-2015-8776 | CWE-189 | raesene/bwapp:latest (ubuntu 14.04) |
| 281 | 41.1 | P3 | 168h | appsec-legacy | bwapp | php: out-of-bounds write in fpm_log.c | CVE-2016-5114 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 282 | 41.0 | P3 | 168h | appsec-legacy | bwapp | httpd: mod_auth_digest: access control bypass due to race co | CVE-2019-0217 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 283 | 41.0 | P3 | 168h | appsec-legacy | bwapp | php: Regular Expression Uninitialized Pointer Information Di | CVE-2015-8382 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 284 | 40.9 | P3 | 168h | appsec-legacy | bwapp | openssh: Improper validation of object names allows maliciou | CVE-2019-6111 | CWE-22 | raesene/bwapp:latest (ubuntu 14.04) |
| 285 | 40.9 | P3 | 168h | appsec-legacy | bwapp | ntp: ntpd switching to interleaved mode with spoofed packets | CVE-2016-1548 | CWE-19 | raesene/bwapp:latest (ubuntu 14.04) |
| 286 | 40.8 | P3 | 168h | appsec-legacy | bwapp | git: git-prompt.sh does not sanitize branch names in $PS1 | CVE-2014-9938 | CWE-116 | raesene/bwapp:latest (ubuntu 14.04) |
| 287 | 40.7 | P3 | 168h | appsec-node | nodegoat | OpenSSL: Excessive time spent checking DH q parameter value | CVE-2023-3817 | CWE-606 | nodegoat-web:latest (alpine 3.15.4) |
| 288 | 40.7 | P3 | 168h | appsec-legacy | bwapp | libxml2: Use after free triggered by XPointer paths beginnin | CVE-2016-5131 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 289 | 40.7 | P3 | 168h | appsec-legacy | bwapp | sensible-browser in sensible-utils before 0.0.11 does not va | CVE-2017-17512 | CWE-74 | raesene/bwapp:latest (ubuntu 14.04) |
| 290 | 40.7 | P3 | 168h | appsec-web | juice_shop | Cross-Site Scripting in sanitize-html | CVE-2017-16016 | CWE-79 | Node.js |
| 291 | 40.6 | P3 | 168h | appsec-node | nodegoat | openssl: AES OCB fails to encrypt some bytes | CVE-2022-2097 | CWE-327 | nodegoat-web:latest (alpine 3.15.4) |
| 292 | 40.6 | P3 | 168h | appsec-legacy | bwapp | libxml2: Heap buffer overflow in xmlAddID | CVE-2017-0663 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 293 | 40.5 | P3 | 168h | appsec-legacy | bwapp | python: smtplib StartTLS stripping attack | CVE-2016-0772 | CWE-693 | raesene/bwapp:latest (ubuntu 14.04) |
| 294 | 40.5 | P3 | 168h | appsec-legacy | bwapp | php: Type confusion vulnerability in make_http_soap_request( | CVE-2016-3185 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 295 | 40.5 | P3 | 168h | appsec-web | juice_shop | minimatch: minimatch: Denial of Service due to unbounded rec | CVE-2026-27903 | CWE-407 | Node.js |
| 296 | 40.5 | P3 | 168h | appsec-web | juice_shop | node-tar: node-tar: Arbitrary file read/write via malicious  | CVE-2026-26960 | CWE-22 | Node.js |
| 297 | 40.4 | P3 | 168h | appsec-legacy | bwapp | bash: Arbitrary code execution via malicious hostname | CVE-2016-0634 | CWE-78 | raesene/bwapp:latest (ubuntu 14.04) |
| 298 | 40.4 | P3 | 168h | appsec-web | juice_shop | node-tar: hardlink path traversal via drive-relative linkpat | CVE-2026-29786 | CWE-22 | Node.js |
| 299 | 40.3 | P3 | 168h | appsec-legacy | bwapp | krb5: null dereference in kadmind or DN container check bypa | CVE-2018-5729 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 300 | 40.2 | P3 | 168h | appsec-legacy | bwapp | glibc: Memory leak reachable via LD_HWCAP_MASK | CVE-2017-1000408 | CWE-772 | raesene/bwapp:latest (ubuntu 14.04) |
| 301 | 40.2 | P3 | 168h | appsec-web | juice_shop | node-jws: auth0/node-jws: Improper signature verification in | CVE-2025-65945 | CWE-347 | Node.js |
| 302 | 40.1 | P3 | 168h | appsec-legacy | bwapp | openssh: missing sanitisation of input for X11 forwarding | CVE-2016-3115 | CWE-93 | raesene/bwapp:latest (ubuntu 14.04) |
| 303 | 40.0 | P3 | 168h | appsec-legacy | bwapp | libxml2: Heap-based buffer-overread in xmlNextChar | CVE-2016-1762 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 304 | 40.0 | P3 | 168h | appsec-web | juice_shop | glibc: glibc: Application crash or uninitialized memory read | CVE-2026-6238 | CWE-126 | bkimminich/juice-shop:latest (debian 13.6) |
| 305 | 39.9 | P4 | 720h | appsec-web | juice_shop | multer: Multer Denial of Service | CVE-2025-7338 | CWE-248 | Node.js |
| 306 | 39.8 | P4 | 720h | appsec-node | nodegoat | marked: regular expression block.def may lead Denial of Serv | CVE-2022-21680 | CWE-400 | Node.js |
| 307 | 39.8 | P4 | 720h | appsec-node | nodegoat | nodejs-debug: Regular expression Denial of Service | CVE-2017-16137 | CWE-400 | Node.js |
| 308 | 39.8 | P4 | 720h | appsec-node | nodegoat | Marked prior to version 0.3.17 is vulnerable to a Regular Ex | CVE-2018-25110 | CWE-1333 | Node.js |
| 309 | 39.7 | P4 | 720h | appsec-legacy | bwapp | CGIHandler: sets environmental variable based on user suppli | CVE-2016-1000110 | CWE-601 | raesene/bwapp:latest (ubuntu 14.04) |
| 310 | 39.7 | P4 | 720h | appsec-node | nodegoat | marked: regular expression inline.reflinkSearch may lead Den | CVE-2022-21681 | CWE-400 | Node.js |
| 311 | 39.7 | P4 | 720h | appsec-node | nodegoat | form-data: form-data: Form field override via CRLF injection | CVE-2026-12143 | CWE-93 | Node.js |
| 312 | 39.6 | P4 | 720h | appsec-legacy | bwapp | openssh: Bounds check can be evaded in the shared memory man | CVE-2016-10012 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 313 | 39.6 | P4 | 720h | appsec-node | nodegoat | minimatch: minimatch: Denial of Service via specially crafte | CVE-2026-26996 | CWE-1333 | Node.js |
| 314 | 39.5 | P4 | 720h | appsec-legacy | bwapp | pam: path traversal issue in pam_timestamp's format_timestam | CVE-2014-2583 | CWE-22 | raesene/bwapp:latest (ubuntu 14.04) |
| 315 | 39.5 | P4 | 720h | appsec-legacy | bwapp | curl: Heap-based buffer over-read in the curl tool warning f | CVE-2018-16842 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 316 | 39.5 | P4 | 720h | appsec-legacy | bwapp | ntp: Privilege escalation via cronjob | CVE-2016-0727 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 317 | 39.5 | P4 | 720h | appsec-web | juice_shop | Authorization bypass in express-jwt | CVE-2020-15084 | CWE-285 | Node.js |
| 318 | 39.5 | P4 | 720h | appsec-web | juice_shop | Out-of-bounds Read | NSWG-ECO-428 |  | Node.js |
| 319 | 39.5 | P4 | 720h | appsec-web | juice_shop | Verification Bypass | NSWG-ECO-17 |  | Node.js |
| 320 | 39.4 | P4 | 720h | appsec-node | nodegoat | form-data: Unsafe random function in form-data | CVE-2025-7783 | CWE-330 | Node.js |
| 321 | 39.3 | P4 | 720h | appsec-node | nodegoat | nodejs-kind-of: ctorName in index.js allows external user in | CVE-2019-20149 | CWE-668 | Node.js |
| 322 | 39.3 | P4 | 720h | appsec-node | nodegoat | nodejs-got: missing verification of requested URLs allows re | CVE-2022-33987 |  | Node.js |
| 323 | 39.3 | P4 | 720h | appsec-node | nodegoat | node-tar: denial of service while parsing a tar file due to  | CVE-2024-28863 | CWE-400 | Node.js |
| 324 | 39.3 | P4 | 720h | appsec-node | nodegoat | ajv: ReDoS via $data reference | CVE-2025-69873 | CWE-1333 | Node.js |
| 325 | 39.2 | P4 | 720h | appsec-legacy | bwapp | ntp: replay attack on authenticated broadcast mode | CVE-2015-7973 | CWE-254 | raesene/bwapp:latest (ubuntu 14.04) |
| 326 | 39.1 | P4 | 720h | appsec-legacy | bwapp | PHP: sets environmental variable based on user supplied Prox | CVE-2016-5385 | CWE-601 | raesene/bwapp:latest (ubuntu 14.04) |
| 327 | 39.1 | P4 | 720h | appsec-legacy | bwapp | mysql: Incorrect input validation allowing code execution vi | CVE-2017-3600 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 328 | 39.0 | P4 | 720h | appsec-legacy | bwapp | openssh: User enumeration via malformed packets in authentic | CVE-2018-15473 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 329 | 39.0 | P4 | 720h | appsec-legacy | bwapp | SSL/TLS: Birthday attack against 64-bit block ciphers (SWEET | CVE-2016-2183 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 330 | 39.0 | P4 | 720h | appsec-legacy | bwapp | httpd: Use-after-free by limiting unregistered HTTP method ( | CVE-2017-9798 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 331 | 38.9 | P4 | 720h | appsec-legacy | bwapp | dhcp: omapi code doesn't free socket descriptors when empty  | CVE-2017-3144 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 332 | 38.9 | P4 | 720h | appsec-legacy | bwapp | httpd: Out of bounds read in mod_cache_socache can allow a r | CVE-2018-1303 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 333 | 38.8 | P4 | 720h | appsec-legacy | bwapp | openssl: Truncated packet could crash via OOB read | CVE-2017-3731 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 334 | 38.8 | P4 | 720h | appsec-legacy | bwapp | httpd: ap_find_token() buffer overread | CVE-2017-7668 | CWE-126 | raesene/bwapp:latest (ubuntu 14.04) |
| 335 | 38.8 | P4 | 720h | appsec-legacy | bwapp | openssl: Malicious server can send large prime to client dur | CVE-2018-0732 | CWE-320 | raesene/bwapp:latest (ubuntu 14.04) |
| 336 | 38.8 | P4 | 720h | appsec-legacy | bwapp | httpd: Padding Oracle in Apache mod_session_crypto | CVE-2016-0736 | CWE-310 | raesene/bwapp:latest (ubuntu 14.04) |
| 337 | 38.8 | P4 | 720h | appsec-legacy | bwapp | php: Unserialize Exception object can lead to infinite loop | CVE-2016-7478 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 338 | 38.8 | P4 | 720h | appsec-legacy | bwapp | SSL/TLS: Malformed plain-text ALERT packets could cause remo | CVE-2016-8610 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 339 | 38.8 | P4 | 720h | appsec-legacy | bwapp | openssl: EVP_EncodeUpdate overflow | CVE-2016-2105 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 340 | 38.8 | P4 | 720h | appsec-legacy | bwapp | pt_chown in the glibc package before 2.19-18+deb8u4 on Debia | CVE-2016-2856 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 341 | 38.8 | P4 | 720h | appsec-web | juice_shop | node-tar: tar: node-tar: Arbitrary file overwrite and symlin | CVE-2026-23745 | CWE-22 | Node.js |
| 342 | 38.7 | P4 | 720h | appsec-legacy | bwapp | OpenSSL: OOB read in TS_OBJ_print_bio() | CVE-2016-2180 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 343 | 38.7 | P4 | 720h | appsec-legacy | bwapp | openssl: EVP_EncryptUpdate overflow | CVE-2016-2106 | CWE-189 | raesene/bwapp:latest (ubuntu 14.04) |
| 344 | 38.7 | P4 | 720h | appsec-legacy | bwapp | OpenSSL: BN_hex2bn/BN_dec2bn NULL pointer deref/heap corrupt | CVE-2016-0797 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 345 | 38.7 | P4 | 720h | appsec-legacy | bwapp | openssl: DTLS memory exhaustion DoS when messages are not re | CVE-2016-2179 | CWE-399 | raesene/bwapp:latest (ubuntu 14.04) |
| 346 | 38.7 | P4 | 720h | appsec-legacy | bwapp | openssl: Insufficient TLS session ticket HMAC length checks | CVE-2016-6302 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 347 | 38.7 | P4 | 720h | appsec-legacy | bwapp | php: Out-of-bound read in timelib_meridian() | CVE-2017-16642 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 348 | 38.7 | P4 | 720h | appsec-legacy | bwapp | pam: DoS/user enumeration due to blocking pipe in pam_unix m | CVE-2015-3238 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 349 | 38.7 | P4 | 720h | appsec-node | nodegoat | openssl: Invalid certificate policies in leaf certificates a | CVE-2023-0465 | CWE-295 | nodegoat-web:latest (alpine 3.15.4) |
| 350 | 38.7 | P4 | 720h | appsec-node | nodegoat | brace-expansion: brace-expansion: Denial of Service via zero | CVE-2026-33750 | CWE-400 | Node.js |
| 351 | 38.6 | P4 | 720h | appsec-legacy | bwapp | openssl: DTLS replay protection bypass allows DoS against DT | CVE-2016-2181 | CWE-189 | raesene/bwapp:latest (ubuntu 14.04) |
| 352 | 38.6 | P4 | 720h | appsec-legacy | bwapp | httpd: DoS vulnerability in mod_auth_digest | CVE-2016-2161 | CWE-823 | raesene/bwapp:latest (ubuntu 14.04) |
| 353 | 38.6 | P4 | 720h | appsec-legacy | bwapp | httpd: mod_session_cookie does not respect expiry time | CVE-2018-17199 | CWE-384 | raesene/bwapp:latest (ubuntu 14.04) |
| 354 | 38.6 | P4 | 720h | appsec-legacy | bwapp | dhcp: Reference count overflow in dhcpd allows denial of ser | CVE-2018-5733 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 355 | 38.6 | P4 | 720h | appsec-legacy | bwapp | glibc: Buffer overflow triggerable via LD_LIBRARY_PATH | CVE-2017-1000409 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 356 | 38.6 | P4 | 720h | appsec-node | nodegoat | tar: node-tar: Denial of Service via crafted gzip bomb | CVE-2026-59873 | CWE-770 | Node.js |
| 357 | 38.6 | P4 | 720h | appsec-web | juice_shop | decompress: Decompress: File disclosure and corruption via a | CVE-2026-39243 | CWE-59 | Node.js |
| 358 | 38.5 | P4 | 720h | appsec-legacy | bwapp | httpd: URL normalization inconsistency | CVE-2019-0220 | CWE-706 | raesene/bwapp:latest (ubuntu 14.04) |
| 359 | 38.5 | P4 | 720h | appsec-legacy | bwapp | httpd: Out of bounds write in mod_authnz_ldap when using too | CVE-2017-15710 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 360 | 38.5 | P4 | 720h | appsec-legacy | bwapp | openssl: Malformed X.509 IPAdressFamily could cause OOB read | CVE-2017-3735 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 361 | 38.5 | P4 | 720h | appsec-legacy | bwapp | ntp: broadcast interleave (incomplete fix for CVE-2016-1548) | CVE-2016-4956 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 362 | 38.5 | P4 | 720h | appsec-legacy | bwapp | curl: TLS session resumption client cert bypass | CVE-2016-5419 | CWE-310 | raesene/bwapp:latest (ubuntu 14.04) |
| 363 | 38.5 | P4 | 720h | appsec-legacy | bwapp | openssh: Out of sequence NEWKEYS message can allow remote at | CVE-2016-10708 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 364 | 38.5 | P4 | 720h | appsec-legacy | bwapp | tar: Bypassing the extract path name | CVE-2016-6321 | CWE-22 | raesene/bwapp:latest (ubuntu 14.04) |
| 365 | 38.5 | P4 | 720h | appsec-legacy | bwapp | ntp: out-of-bounds references on crafted packet | CVE-2016-2518 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 366 | 38.5 | P4 | 720h | appsec-legacy | bwapp | curl: Re-using connection with wrong client cert | CVE-2016-5420 | CWE-285 | raesene/bwapp:latest (ubuntu 14.04) |
| 367 | 38.5 | P4 | 720h | appsec-web | juice_shop | XSS - Sanitization not applied recursively | CVE-2016-1000237 | CWE-79 | Node.js |
| 368 | 38.5 | P4 | 720h | appsec-node | nodegoat | tar: Node-tar: Denial of Service via malformed tar archive h | CVE-2026-59874 | CWE-835 | Node.js |
| 369 | 38.5 | P4 | 720h | appsec-node | nodegoat | qs: qs: Denial of Service via improper input validation in a | CVE-2025-15284 | CWE-20 | Node.js |
| 370 | 38.4 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap-based buffer underreads due to xmlParseName | CVE-2016-4447 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 371 | 38.4 | P4 | 720h | appsec-legacy | bwapp | php: Out-of-bounds heap read on unserialize in finish_nested | CVE-2016-10161 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 372 | 38.4 | P4 | 720h | appsec-legacy | bwapp | httpd: Apache HTTP Request Parsing Whitespace Defects | CVE-2016-8743 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 373 | 38.4 | P4 | 720h | appsec-legacy | bwapp | ntp: partial processing of spoofed packets | CVE-2016-4954 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 374 | 38.4 | P4 | 720h | appsec-legacy | bwapp | ntp: off-path denial of service on authenticated broadcast m | CVE-2015-7979 | CWE-19 | raesene/bwapp:latest (ubuntu 14.04) |
| 375 | 38.4 | P4 | 720h | appsec-node | nodegoat | The marked module is vulnerable to a regular expression deni | CVE-2017-16114 | CWE-400 | Node.js |
| 376 | 38.4 | P4 | 720h | appsec-node | nodegoat | nconf: Prototype pollution in memory store | CVE-2022-21803 | CWE-1321 | Node.js |
| 377 | 38.4 | P4 | 720h | appsec-node | nodegoat | brace-expansion: DoS via unbounded intermediate arrays, bypa | CVE-2026-69152 | CWE-400 | Node.js |
| 378 | 38.4 | P4 | 720h | appsec-node | nodegoat | node-tar: node-tar: Denial of Service due to incorrect PAX p | CVE-2026-59871 | CWE-704 | Node.js |
| 379 | 38.3 | P4 | 720h | appsec-legacy | bwapp | php: Null pointer dereference in php_wddx_push_element | CVE-2016-7418 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 380 | 38.3 | P4 | 720h | appsec-legacy | bwapp | python: Missing salt initialization in _elementtree.c module | CVE-2018-14647 | CWE-335 | raesene/bwapp:latest (ubuntu 14.04) |
| 381 | 38.3 | P4 | 720h | appsec-legacy | bwapp | php: Infinite loop in ext/iconv/iconv.c when using stream fi | CVE-2018-10546 | CWE-835 | raesene/bwapp:latest (ubuntu 14.04) |
| 382 | 38.3 | P4 | 720h | appsec-legacy | bwapp | ntp: stack exhaustion in recursive traversal of restriction  | CVE-2015-7978 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 383 | 38.3 | P4 | 720h | appsec-node | nodegoat | micromatch: vulnerable to Regular Expression Denial of Servi | CVE-2024-4067 | CWE-1333 | Node.js |
| 384 | 38.3 | P4 | 720h | appsec-web | juice_shop | undici: Undici: HTTP header injection and request smuggling  | CVE-2026-1527 | CWE-93 | Node.js |
| 385 | 38.2 | P4 | 720h | appsec-legacy | bwapp | curl: LDAP NULL pointer dereference | CVE-2018-1000121 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 386 | 38.2 | P4 | 720h | appsec-legacy | bwapp | procps: denial of service in ps via mmap buffer overflow | CVE-2018-1123 | CWE-122 | raesene/bwapp:latest (ubuntu 14.04) |
| 387 | 38.2 | P4 | 720h | appsec-legacy | bwapp | expat: Inifinite loop due to invalid XML in external entity | CVE-2017-9233 | CWE-611 | raesene/bwapp:latest (ubuntu 14.04) |
| 388 | 38.2 | P4 | 720h | appsec-legacy | bwapp | perl: ambiguous environment variables handling | CVE-2016-2381 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 389 | 38.2 | P4 | 720h | appsec-legacy | bwapp | ntp: Unauthenticated packet can reset authenticated interlea | CVE-2018-7185 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 390 | 38.2 | P4 | 720h | appsec-legacy | bwapp | php: exif: integer overflow leading to out-of-bound buffer r | CVE-2018-14883 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 391 | 38.2 | P4 | 720h | appsec-legacy | bwapp | php: wddx_deserialize null dereference with invalid xml | CVE-2016-7131 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 392 | 38.2 | P4 | 720h | appsec-legacy | bwapp | php: wddx_deserialize null dereference in php_wddx_pop_eleme | CVE-2016-7132 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 393 | 38.2 | P4 | 720h | appsec-legacy | bwapp | php: NULL pointer dereference due to mishandling of ldap_get | CVE-2018-10548 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 394 | 38.2 | P4 | 720h | appsec-legacy | bwapp | gnupg2: Improper sanitization of filenames allows for the di | CVE-2018-12020 | CWE-706 | raesene/bwapp:latest (ubuntu 14.04) |
| 395 | 38.2 | P4 | 720h | appsec-legacy | bwapp | curl: FTP PWD response parser out of bounds read | CVE-2017-1000254 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 396 | 38.2 | P4 | 720h | appsec-legacy | bwapp | patch: NULL pointer dereference in pch.c:intuit_diff_type()  | CVE-2018-6951 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 397 | 38.2 | P4 | 720h | appsec-legacy | bwapp | curl: Incorrect reuse of client certificates | CVE-2016-7141 | CWE-287 | raesene/bwapp:latest (ubuntu 14.04) |
| 398 | 38.2 | P4 | 720h | appsec-legacy | bwapp | php: Uninitialized read in exif_process_IFD_in_MAKERNOTE | CVE-2019-9639 | CWE-908 | raesene/bwapp:latest (ubuntu 14.04) |
| 399 | 38.1 | P4 | 720h | appsec-legacy | bwapp | sqlite: NULL pointer dereference with databases with schema  | CVE-2018-8740 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 400 | 38.1 | P4 | 720h | appsec-legacy | bwapp | curl: HTTP authentication leak in redirects | CVE-2018-1000007 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 401 | 38.1 | P4 | 720h | appsec-legacy | bwapp | gnutls: Out of memory while parsing crafted OpenPGP certific | CVE-2017-5335 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 402 | 38.1 | P4 | 720h | appsec-legacy | bwapp | php: Wrong calculation in exif_convert_any_to_int function | CVE-2016-10158 | CWE-189 | raesene/bwapp:latest (ubuntu 14.04) |
| 403 | 38.1 | P4 | 720h | appsec-legacy | bwapp | php: Memory Leakage In exif_process_IFD_in_TIFF | CVE-2016-7128 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 404 | 38.1 | P4 | 720h | appsec-legacy | bwapp | busybox: Out of bounds read in udhcp components resulting in | CVE-2018-20679 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 405 | 38.1 | P4 | 720h | appsec-legacy | bwapp | php: Integer overflow in phar_parse_pharfile | CVE-2016-10159 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 406 | 38.1 | P4 | 720h | appsec-legacy | bwapp | busybox: out of bounds write (heap) due to integer underflow | CVE-2016-2147 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 407 | 38.1 | P4 | 720h | appsec-legacy | bwapp | glibc: Stack overflow in nss_dns_getnetbyname_r | CVE-2016-3075 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 408 | 38.1 | P4 | 720h | appsec-legacy | bwapp | php: File rename across filesystems may allow unwanted acces | CVE-2019-9637 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 409 | 38.1 | P4 | 720h | appsec-legacy | bwapp | busybox: Path traversal via crafted tar file containing syml | CVE-2011-5325 | CWE-22 | raesene/bwapp:latest (ubuntu 14.04) |
| 410 | 38.1 | P4 | 720h | appsec-legacy | bwapp | php: Out-of-bounds read in base64_decode_xmlrpc in ext/xmlrp | CVE-2019-9024 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 411 | 38.1 | P4 | 720h | appsec-web | juice_shop | glibc: glibc: Heap Buffer Overflow in `scanf` with `%mc` for | CVE-2026-5450 | CWE-122 | bkimminich/juice-shop:latest (debian 13.6) |
| 412 | 38.0 | P4 | 720h | appsec-legacy | bwapp | libxml2: stack exhaustion while parsing xml files in recover | CVE-2016-3627 | CWE-674 | raesene/bwapp:latest (ubuntu 14.04) |
| 413 | 38.0 | P4 | 720h | appsec-legacy | bwapp | php: Incorrect WDDX deserialization of boolean parameters le | CVE-2017-11143 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 414 | 38.0 | P4 | 720h | appsec-legacy | bwapp | php: NULL Pointer Dereference in WDDX Packet Deserialization | CVE-2016-9934 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 415 | 38.0 | P4 | 720h | appsec-legacy | bwapp | libidn: Out-of-bounds read due to use of fgets with fixed-si | CVE-2015-8948 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 416 | 38.0 | P4 | 720h | appsec-legacy | bwapp | php: Uninitialized read in exif_process_IFD_in_MAKERNOTE | CVE-2019-9638 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 417 | 38.0 | P4 | 720h | appsec-legacy | bwapp | php: Stack based buffer overflow in msgfmt_format_message | CVE-2016-7416 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 418 | 38.0 | P4 | 720h | appsec-legacy | bwapp | php: wddx_deserialize null dereference | CVE-2016-7130 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 419 | 38.0 | P4 | 720h | appsec-legacy | bwapp | libidn: Out-of-bounds read when reading zero byte as input | CVE-2016-6262 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 420 | 38.0 | P4 | 720h | appsec-legacy | bwapp | rsync: sanitization bypass in parse_argument in options.c | CVE-2018-5764 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 421 | 37.9 | P4 | 720h | appsec-legacy | bwapp | ntp: missing check for zero originate timestamp | CVE-2015-8138 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 422 | 37.9 | P4 | 720h | appsec-legacy | bwapp | curl: Invalid URL parsing with '#' | CVE-2016-8624 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 423 | 37.9 | P4 | 720h | appsec-legacy | bwapp | perl: Heap buffer overflow in regular expression compiler | CVE-2017-12837 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 424 | 37.9 | P4 | 720h | appsec-legacy | bwapp | php: Invalid read in exif_process_SOFn() | CVE-2019-9640 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 425 | 37.9 | P4 | 720h | appsec-legacy | bwapp | libxml2: out-of-bounds read | CVE-2016-4483 | CWE-502 | raesene/bwapp:latest (ubuntu 14.04) |
| 426 | 37.9 | P4 | 720h | appsec-legacy | bwapp | php: Incorrect return value check of OpenSSL sealing functio | CVE-2017-11144 | CWE-754 | raesene/bwapp:latest (ubuntu 14.04) |
| 427 | 37.9 | P4 | 720h | appsec-legacy | bwapp | libxml2: Infinite recursion in parameter entities | CVE-2017-16932 | CWE-835 | raesene/bwapp:latest (ubuntu 14.04) |
| 428 | 37.9 | P4 | 720h | appsec-legacy | bwapp | glibc: stack (frame) overflow in getaddrinfo() when called w | CVE-2016-3706 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 429 | 37.9 | P4 | 720h | appsec-legacy | bwapp | php: Session Data Injection Vulnerability | CVE-2016-7125 | CWE-74 | raesene/bwapp:latest (ubuntu 14.04) |
| 430 | 37.9 | P4 | 720h | appsec-legacy | bwapp | php: Integer overflow in php_raw_url_encode | CVE-2016-4070 | CWE-189 | raesene/bwapp:latest (ubuntu 14.04) |
| 431 | 37.8 | P4 | 720h | appsec-legacy | bwapp | glibc: Unexpected closing of nss_files databases after looku | CVE-2014-8121 | CWE-17 | raesene/bwapp:latest (ubuntu 14.04) |
| 432 | 37.8 | P4 | 720h | appsec-legacy | bwapp | libpng: NULL pointer dereference in png_set_text_2() | CVE-2016-10087 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 433 | 37.8 | P4 | 720h | appsec-legacy | bwapp | curl: curl_getdate out-of-bounds read | CVE-2016-8621 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 434 | 37.8 | P4 | 720h | appsec-legacy | bwapp | glibc: Stack-based buffer overflow in glob with GLOB_ALTDIRF | CVE-2016-1234 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 435 | 37.8 | P4 | 720h | appsec-legacy | bwapp | oniguruma: Invalid pointer dereference in left_adjust_char_h | CVE-2017-9229 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 436 | 37.8 | P4 | 720h | appsec-node | nodegoat | Underscore.js: Underscore.js: Denial of Service via recursiv | CVE-2026-27601 | CWE-770 | Node.js |
| 437 | 37.7 | P4 | 720h | appsec-legacy | bwapp | ntp: crypto-NAK preemptable association denial of service | CVE-2016-1547 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 438 | 37.7 | P4 | 720h | appsec-legacy | bwapp | python: DOS via regular expression catastrophic backtracking | CVE-2018-1060 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 439 | 37.7 | P4 | 720h | appsec-legacy | bwapp | libxml2: stack overflow before detecting invalid XML file | CVE-2016-3705 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 440 | 37.7 | P4 | 720h | appsec-legacy | bwapp | libtasn1: NULL pointer dereference in the _asn1_check_identi | CVE-2017-10790 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 441 | 37.7 | P4 | 720h | appsec-legacy | bwapp | python: DOS via regular expression backtracking in difflib.I | CVE-2018-1061 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 442 | 37.7 | P4 | 720h | appsec-legacy | bwapp | libxml2: heap-buffer overread in dict.c | CVE-2015-8806 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 443 | 37.7 | P4 | 720h | appsec-legacy | bwapp | dhcp: Buffer overflow in dhclient possibly allowing code exe | CVE-2018-5732 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 444 | 37.7 | P4 | 720h | appsec-legacy | bwapp | mysql: prepared statement handle use-after-free after discon | CVE-2017-3302 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 445 | 37.7 | P4 | 720h | appsec-legacy | bwapp | libxml2: Stack-based buffer overflow in function xmlSnprintf | CVE-2017-9048 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 446 | 37.7 | P4 | 720h | appsec-legacy | bwapp | php: wddx_deserialize() heap out-of-bound read via php_parse | CVE-2017-11145 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 447 | 37.7 | P4 | 720h | appsec-legacy | bwapp | curl: Cookie injection for other servers | CVE-2016-8615 | CWE-99 | raesene/bwapp:latest (ubuntu 14.04) |
| 448 | 37.7 | P4 | 720h | appsec-legacy | bwapp | mysql: incorrect enforcement of ssl-mode=REQUIRED in MySQL 5 | CVE-2017-3305 | CWE-319 | raesene/bwapp:latest (ubuntu 14.04) |
| 449 | 37.7 | P4 | 720h | appsec-node | nodegoat | express: cause malformed URLs to be evaluated | CVE-2024-29041 | CWE-601 | Node.js |
| 450 | 37.6 | P4 | 720h | appsec-legacy | bwapp | file: limit the number of ELF notes processed | CVE-2014-9620 | CWE-399 | raesene/bwapp:latest (ubuntu 14.04) |
| 451 | 37.6 | P4 | 720h | appsec-legacy | bwapp | busybox: Out of bounds read in udhcp components resulting in | CVE-2019-5747 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 452 | 37.6 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap-based buffer over-read in function xmlDictComp | CVE-2017-9049 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 453 | 37.6 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap-based buffer over-read in function xmlDictAddS | CVE-2017-9050 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 454 | 37.6 | P4 | 720h | appsec-legacy | bwapp | git: path sanity check in is_ntfs_dotgit() can read arbitrar | CVE-2018-11233 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 455 | 37.6 | P4 | 720h | appsec-legacy | bwapp | pcre: pcregrep -q is not always quiet (8.38/28) | CVE-2015-8393 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 456 | 37.6 | P4 | 720h | appsec-legacy | bwapp | php: openssl_random_pseudo_bytes() is not cryptographically  | CVE-2015-8867 | CWE-310 | raesene/bwapp:latest (ubuntu 14.04) |
| 457 | 37.6 | P4 | 720h | appsec-web | juice_shop | sanitize-html: sanitize-html cross site scripting | CVE-2019-25225 | CWE-79 | Node.js |
| 458 | 37.5 | P4 | 720h | appsec-legacy | bwapp | krb5: krb5 doesn't check for null policy when KADM5_POLICY i | CVE-2015-8630 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 459 | 37.5 | P4 | 720h | appsec-legacy | bwapp | curl: SMTP end-of-response out-of-bounds read | CVE-2019-3823 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 460 | 37.5 | P4 | 720h | appsec-legacy | bwapp | libX11: Crash on invalid reply in XListExtensions in ListExt | CVE-2018-14598 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 461 | 37.5 | P4 | 720h | appsec-legacy | bwapp | php: memcpy with negative length via crafted DNS response | CVE-2019-9022 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 462 | 37.5 | P4 | 720h | appsec-legacy | bwapp | perl-DBD-MySQL: Buffer overflow triggered by user supplied d | CVE-2016-1246 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 463 | 37.5 | P4 | 720h | appsec-legacy | bwapp | krb5: DN container check bypass by supplying special crafted | CVE-2018-5730 | CWE-90 | raesene/bwapp:latest (ubuntu 14.04) |
| 464 | 37.5 | P4 | 720h | appsec-node | nodegoat | brace-expansion: Brace-expansion: Denial of Service due to e | CVE-2026-13149 | CWE-400 | Node.js |
| 465 | 37.4 | P4 | 720h | appsec-legacy | bwapp | php: Stack consumption vulnerability in Zend/zend_exceptions | CVE-2015-8873 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 466 | 37.4 | P4 | 720h | appsec-legacy | bwapp | libidn: Out of bounds stack read in idna_to_ascii_4i | CVE-2016-6261 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 467 | 37.4 | P4 | 720h | appsec-legacy | bwapp | libidn: Crash when given invalid UTF-8 data on input | CVE-2016-6263 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 468 | 37.4 | P4 | 720h | appsec-legacy | bwapp | glibc: Missing unwind info in __startcontext causes infinite | CVE-2016-6323 | CWE-284 | raesene/bwapp:latest (ubuntu 14.04) |
| 469 | 37.4 | P4 | 720h | appsec-web | juice_shop | multer: Multer vulnerable to Denial of Service via unhandled | CVE-2025-48997 | CWE-248 | Node.js |
| 470 | 37.3 | P4 | 720h | appsec-legacy | bwapp | openssh: User enumeration via covert timing channel | CVE-2016-6210 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 471 | 37.3 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Thread Pooling unspecified vulnerability (CPU | CVE-2017-3329 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 472 | 37.3 | P4 | 720h | appsec-legacy | bwapp | libxml2: NULL pointer dereference in xmlXPathCompOpEval() fu | CVE-2018-14404 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 473 | 37.3 | P4 | 720h | appsec-legacy | bwapp | ntp: libntp message digest disclosure | CVE-2016-1550 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 474 | 37.3 | P4 | 720h | appsec-legacy | bwapp | libgcrypt: PRNG output is predictable | CVE-2016-6313 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 475 | 37.3 | P4 | 720h | appsec-node | nodegoat | request: bypass of SSRF mitigations when following a cross-p | CVE-2023-28155 | CWE-918 | Node.js |
| 476 | 37.3 | P4 | 720h | appsec-node | nodegoat | brace-expansion: Brace-expansion: Denial of Service via memo | CVE-2026-14257 | CWE-400 | Node.js |
| 477 | 37.3 | P4 | 720h | appsec-node | nodegoat | uuid: uuid: Out-of-bounds write vulnerability impacts data i | CVE-2026-41907 | CWE-787 | Node.js |
| 478 | 37.2 | P4 | 720h | appsec-legacy | bwapp | php: Reflected XSS on PHAR 404 page | CVE-2018-5712 | CWE-79 | raesene/bwapp:latest (ubuntu 14.04) |
| 479 | 37.2 | P4 | 720h | appsec-legacy | bwapp | openssh: Improper write operations in readonly mode allow fo | CVE-2017-15906 | CWE-732 | raesene/bwapp:latest (ubuntu 14.04) |
| 480 | 37.2 | P4 | 720h | appsec-legacy | bwapp | libxml2: Inappropriate fetch of entities content | CVE-2016-4449 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 481 | 37.1 | P4 | 720h | appsec-legacy | bwapp | openssl: certificate message OOB reads | CVE-2016-6306 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 482 | 37.0 | P4 | 720h | appsec-legacy | bwapp | libtasn1: infinite loop while parsing DER certificates | CVE-2016-4008 | CWE-399 | raesene/bwapp:latest (ubuntu 14.04) |
| 483 | 37.0 | P4 | 720h | appsec-legacy | bwapp | libxml2: Buffer overflow in function xmlSnprintfElementConte | CVE-2017-9047 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 484 | 37.0 | P4 | 720h | appsec-legacy | bwapp | The AMF3ReadString function in amf.c in RTMPDump 2.4 allows  | CVE-2015-8270 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 485 | 36.9 | P4 | 720h | appsec-legacy | bwapp | httpd: CRLF injection allowing HTTP response splitting attac | CVE-2016-4975 | CWE-93 | raesene/bwapp:latest (ubuntu 14.04) |
| 486 | 36.9 | P4 | 720h | appsec-legacy | bwapp | openssl: Handling of crafted recursive ASN.1 structures can  | CVE-2018-0739 | CWE-674 | raesene/bwapp:latest (ubuntu 14.04) |
| 487 | 36.9 | P4 | 720h | appsec-legacy | bwapp | file: limit string printing to 100 chars | CVE-2014-9621 | CWE-399 | raesene/bwapp:latest (ubuntu 14.04) |
| 488 | 36.9 | P4 | 720h | appsec-node | nodegoat | inflect vulnerable to Inefficient Regular Expression Complex | CVE-2021-3820 | CWE-1333 | Node.js |
| 489 | 36.9 | P4 | 720h | appsec-web | juice_shop | undici: undici vulnerable to HTTP header injection via Set-C | CVE-2026-9679 | CWE-93 | Node.js |
| 490 | 36.8 | P4 | 720h | appsec-legacy | bwapp | httpd: Out of bounds access after failure in reading the HTT | CVE-2018-1301 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 491 | 36.8 | P4 | 720h | appsec-legacy | bwapp | gnutls: Out-of-bounds write related to the cdk_pkt_read func | CVE-2017-7869 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 492 | 36.8 | P4 | 720h | appsec-web | juice_shop | undici: undici: Response desynchronization via retry interce | CVE-2026-16728 | CWE-444 | Node.js |
| 493 | 36.7 | P4 | 720h | appsec-legacy | bwapp | ntp: Client rate limiting and server responses | CVE-2016-7426 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 494 | 36.7 | P4 | 720h | appsec-legacy | bwapp | openssl: timing side channel attack in the DSA signature alg | CVE-2018-0734 | CWE-327 | raesene/bwapp:latest (ubuntu 14.04) |
| 495 | 36.7 | P4 | 720h | appsec-legacy | bwapp | openssl: RSA key generation cache timing vulnerability in cr | CVE-2018-0737 | CWE-327 | raesene/bwapp:latest (ubuntu 14.04) |
| 496 | 36.7 | P4 | 720h | appsec-legacy | bwapp | curl: Use-after-free via shared cookies | CVE-2016-8623 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 497 | 36.7 | P4 | 720h | appsec-node | nodegoat | Incorrect parsing of certain JSON input may result in js-bso | CVE-2019-2391 | CWE-502 | Node.js |
| 498 | 36.7 | P4 | 720h | appsec-web | juice_shop | undici: Undici: Cookie attribute injection allows bypassing  | CVE-2026-16729 | CWE-74 | Node.js |
| 499 | 36.6 | P4 | 720h | appsec-legacy | bwapp | python: http protocol steam injection attack | CVE-2016-5699 | CWE-113 | raesene/bwapp:latest (ubuntu 14.04) |
| 500 | 36.6 | P4 | 720h | appsec-legacy | bwapp | perl: regexp matching hangs indefinitely on illegal UTF-8 in | CVE-2015-8853 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 501 | 36.6 | P4 | 720h | appsec-node | nodegoat | Vercel ms Inefficient Regular Expression Complexity vulnerab | CVE-2017-20162 | CWE-1333 | Node.js |
| 502 | 36.5 | P4 | 720h | appsec-legacy | bwapp | ntp: autokey association reset | CVE-2016-4955 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 503 | 36.5 | P4 | 720h | appsec-web | juice_shop | cookie: cookie accepts cookie name, path, and domain with ou | CVE-2024-47764 | CWE-74 | Node.js |
| 504 | 36.5 | P4 | 720h | appsec-node | nodegoat | minimatch: Minimatch: Denial of Service via catastrophic bac | CVE-2026-27904 | CWE-1333 | Node.js |
| 505 | 36.5 | P4 | 720h | appsec-web | juice_shop | glibc: glibc: Information disclosure or denial of service vi | CVE-2026-5928 | CWE-127 | bkimminich/juice-shop:latest (debian 13.6) |
| 506 | 36.5 | P4 | 720h | appsec-web | juice_shop | file-type: file-type: Denial of Service due to infinite loop | CVE-2026-31808 | CWE-835 | Node.js |
| 507 | 36.5 | P4 | 720h | appsec-web | juice_shop | glibc: glibc: Out-of-bounds write via TSIG record processing | CVE-2026-5435 | CWE-787 | bkimminich/juice-shop:latest (debian 13.6) |
| 508 | 36.4 | P4 | 720h | appsec-legacy | bwapp | ntp: potential infinite loop in ntpq | CVE-2015-8158 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 509 | 36.4 | P4 | 720h | appsec-legacy | bwapp | ntp: Attack on interface selection | CVE-2016-7429 | CWE-18 | raesene/bwapp:latest (ubuntu 14.04) |
| 510 | 36.4 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap-based buffer overread in xmlDictAddString | CVE-2016-1839 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 511 | 36.4 | P4 | 720h | appsec-legacy | bwapp | The apt package in Debian jessie before 1.0.9.8.4, in Debian | CVE-2016-1252 | CWE-295 | raesene/bwapp:latest (ubuntu 14.04) |
| 512 | 36.4 | P4 | 720h | appsec-legacy | bwapp | systemd: automount: access to automounted volumes can lock u | CVE-2018-1049 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 513 | 36.4 | P4 | 720h | appsec-node | nodegoat | path-to-regexp: Backtracking regular expressions cause ReDoS | CVE-2024-45296 | CWE-1333 | Node.js |
| 514 | 36.4 | P4 | 720h | appsec-legacy | bwapp | openssh: privilege escalation via user's PAM environment and | CVE-2015-8325 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 515 | 36.4 | P4 | 720h | appsec-web | juice_shop | lodash: Lodash: Prototype pollution allows deletion of built | CVE-2026-2950 | CWE-1321 | Node.js |
| 516 | 36.3 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap-based buffer overread in xmlPArserPrintFileCon | CVE-2016-1838 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 517 | 36.3 | P4 | 720h | appsec-legacy | bwapp | ntp: restriction list NULL pointer dereference | CVE-2015-7977 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 518 | 36.3 | P4 | 720h | appsec-legacy | bwapp | glibc: data corruption while reading the NSS files database | CVE-2015-5277 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 519 | 36.3 | P4 | 720h | appsec-web | juice_shop | node-tar: tar: node-tar: Arbitrary file overwrite via Unicod | CVE-2026-23950 | CWE-176 | Node.js |
| 520 | 36.2 | P4 | 720h | appsec-legacy | bwapp | mysql: Client programs unspecified vulnerability (CPU Jul 20 | CVE-2018-3081 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 521 | 36.2 | P4 | 720h | appsec-legacy | bwapp | php: Output of stream_get_meta_data can be falsified by its  | CVE-2016-10712 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 522 | 36.2 | P4 | 720h | appsec-legacy | bwapp | procps: stack buffer overflow in pgrep | CVE-2018-1125 | CWE-121 | raesene/bwapp:latest (ubuntu 14.04) |
| 523 | 36.2 | P4 | 720h | appsec-legacy | bwapp | bash: Specially crafted SHELLOPTS+PS4 variables allows comma | CVE-2016-7543 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 524 | 36.1 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: DM | CVE-2016-3615 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 525 | 36.1 | P4 | 720h | appsec-legacy | bwapp | cpio: out of bounds write | CVE-2016-2037 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 526 | 36.1 | P4 | 720h | appsec-node | nodegoat | marked version 0.3.6 and earlier is vulnerable to an XSS att | CVE-2017-1000427 | CWE-79 | Node.js |
| 527 | 36.0 | P4 | 720h | appsec-legacy | bwapp | mysql: race condition while setting stats during MyISAM tabl | CVE-2016-6663 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 528 | 36.0 | P4 | 720h | appsec-node | nodegoat | marked is an application that is meant to parse and compile  | CVE-2016-10531 | CWE-79 | Node.js |
| 529 | 36.0 | P4 | 720h | appsec-web | juice_shop | node-tar: node-tar: Denial of Service via crafted archive wi | CVE-2026-59875 | CWE-248 | Node.js |
| 530 | 36.0 | P4 | 720h | appsec-web | juice_shop | glibc: Glibc: Denial of Service via stack exhaustion during  | CVE-2026-6791 | CWE-121 | bkimminich/juice-shop:latest (debian 13.6) |
| 531 | 35.9 | P4 | 720h | appsec-legacy | bwapp | php: ZipArchive:: extractTo allows for directory traversal w | CVE-2014-9767 | CWE-22 | raesene/bwapp:latest (ubuntu 14.04) |
| 532 | 35.9 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap use-after-free in htmlPArsePubidLiteral and ht | CVE-2016-1837 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 533 | 35.8 | P4 | 720h | appsec-legacy | bwapp | php: exif: Buffer over-read in exif_process_IFD_in_MAKERNOTE | CVE-2018-14851 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 534 | 35.8 | P4 | 720h | appsec-legacy | bwapp | libxml2: Infinite loop caused by incorrect error detection d | CVE-2018-14567 | CWE-835 | raesene/bwapp:latest (ubuntu 14.04) |
| 535 | 35.8 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap use-after-free in xmlDictComputeFastKey | CVE-2016-1836 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 536 | 35.8 | P4 | 720h | appsec-legacy | bwapp | php: Cross-site scripting (XSS) flaw in Apache2 component vi | CVE-2018-17082 | CWE-79 | raesene/bwapp:latest (ubuntu 14.04) |
| 537 | 35.8 | P4 | 720h | appsec-legacy | bwapp | mysql: Client programs unspecified vulnerability (CPU Apr 20 | CVE-2018-2761 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 538 | 35.8 | P4 | 720h | appsec-web | juice_shop | tar: tar: File overwrite via drive-relative symlink traversa | CVE-2026-31802 | CWE-22 | Node.js |
| 539 | 35.7 | P4 | 720h | appsec-legacy | bwapp | curl: TFTP sends more than buffer size | CVE-2017-1000100 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 540 | 35.7 | P4 | 720h | appsec-legacy | bwapp | glibc: libtirpc: stack (frame) overflow in Sun RPC clntudp_c | CVE-2016-4429 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 541 | 35.7 | P4 | 720h | appsec-legacy | bwapp | php: Null pointer dereference in exif_process_user_comment | CVE-2016-6292 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 542 | 35.7 | P4 | 720h | appsec-legacy | bwapp | libgcrypt: Use of left-to-right sliding window method allows | CVE-2017-7526 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 543 | 35.7 | P4 | 720h | appsec-legacy | bwapp | curl: URL globbing out of bounds read | CVE-2017-1000101 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 544 | 35.7 | P4 | 720h | appsec-legacy | bwapp | php: Incorrect handling of URI components in URL parser | CVE-2016-10397 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 545 | 35.7 | P4 | 720h | appsec-node | nodegoat | path-to-regexp: path-to-regexp Unpatched `path-to-regexp` Re | CVE-2024-52798 | CWE-1333 | Node.js |
| 546 | 35.6 | P4 | 720h | appsec-legacy | bwapp | openldap: Double free vulnerability in servers/slapd/back-md | CVE-2017-9287 | CWE-415 | raesene/bwapp:latest (ubuntu 14.04) |
| 547 | 35.6 | P4 | 720h | appsec-legacy | bwapp | mysql: ssl-validate-cert incorrect hostname check | CVE-2016-2047 | CWE-254 | raesene/bwapp:latest (ubuntu 14.04) |
| 548 | 35.6 | P4 | 720h | appsec-legacy | bwapp | php: Reflected XSS vulnerability on PHAR 403 and 404 error p | CVE-2018-10547 | CWE-79 | raesene/bwapp:latest (ubuntu 14.04) |
| 549 | 35.5 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Ty | CVE-2016-8283 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 550 | 35.5 | P4 | 720h | appsec-legacy | bwapp | curl: Case insensitive password comparison | CVE-2016-8616 | CWE-592 | raesene/bwapp:latest (ubuntu 14.04) |
| 551 | 35.5 | P4 | 720h | appsec-legacy | bwapp | file: out-of-bounds read via a crafted ELF file | CVE-2018-10360 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 552 | 35.5 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Options unspecified vulnerability (CPU Jul 20 | CVE-2018-3066 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 553 | 35.5 | P4 | 720h | appsec-node | nodegoat | minimatch: minimatch: Denial of Service due to unbounded rec | CVE-2026-27903 | CWE-407 | Node.js |
| 554 | 35.5 | P4 | 720h | appsec-node | nodegoat | node-tar: node-tar: Arbitrary file read/write via malicious  | CVE-2026-26960 | CWE-22 | Node.js |
| 555 | 35.4 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: GI | CVE-2016-5626 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 556 | 35.4 | P4 | 720h | appsec-node | nodegoat | node-tar: hardlink path traversal via drive-relative linkpat | CVE-2026-29786 | CWE-22 | Node.js |
| 557 | 35.3 | P4 | 720h | appsec-legacy | bwapp | ntp: missing key check allows impersonation between authenti | CVE-2015-7974 | CWE-287 | raesene/bwapp:latest (ubuntu 14.04) |
| 558 | 35.3 | P4 | 720h | appsec-legacy | bwapp | ntp: Authenticated DoS via Malicious Config Option | CVE-2017-6463 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 559 | 35.3 | P4 | 720h | appsec-legacy | bwapp | dmcrypt-get-device, as shipped in the eject package of Debia | CVE-2017-6964 | CWE-252 | raesene/bwapp:latest (ubuntu 14.04) |
| 560 | 35.2 | P4 | 720h | appsec-legacy | bwapp | ntp: Denial of Service via Malformed Config | CVE-2017-6464 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 561 | 35.2 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Jan  | CVE-2017-3238 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 562 | 35.2 | P4 | 720h | appsec-legacy | bwapp | php: HTTP response splitting in header() function | CVE-2015-8935 | CWE-79 | raesene/bwapp:latest (ubuntu 14.04) |
| 563 | 35.2 | P4 | 720h | appsec-legacy | bwapp | libxml2: XML External Entity vulnerability | CVE-2016-9318 | CWE-611 | raesene/bwapp:latest (ubuntu 14.04) |
| 564 | 35.2 | P4 | 720h | appsec-web | juice_shop | zlib: zlib: Denial of Service via infinite loop in CRC32 com | CVE-2026-27171 | CWE-1284 | bkimminich/juice-shop:latest (debian 13.6) |
| 565 | 35.1 | P4 | 720h | appsec-legacy | bwapp | krb5: null pointer dereference in kadmin | CVE-2016-3119 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 566 | 35.1 | P4 | 720h | appsec-legacy | bwapp | krb5: Memory leak caused by supplying a null principal name  | CVE-2015-8631 | CWE-772 | raesene/bwapp:latest (ubuntu 14.04) |
| 567 | 35.1 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: DM | CVE-2016-5624 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 568 | 35.1 | P4 | 720h | appsec-legacy | bwapp | krb5: S4U2Self KDC crash when anon is restricted | CVE-2016-3120 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 569 | 35.0 | P4 | 720h | appsec-legacy | bwapp | RTMPDump 2.4 allows remote attackers to trigger a denial of  | CVE-2015-8272 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 570 | 35.0 | P4 | 720h | appsec-legacy | bwapp | libxml2: Unrestricted memory usage in xz_head() function in  | CVE-2017-18258 | CWE-770 | raesene/bwapp:latest (ubuntu 14.04) |
| 571 | 34.9 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Storage Engines unspecified vulnerability (CP | CVE-2018-3282 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 572 | 34.9 | P4 | 720h | appsec-legacy | bwapp | openssh: Missing character encoding in progress display allo | CVE-2019-6109 | CWE-116 | raesene/bwapp:latest (ubuntu 14.04) |
| 573 | 34.9 | P4 | 720h | appsec-legacy | bwapp | libxml2: Heap-based buffer overread in htmlCurrentChar | CVE-2016-1833 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 574 | 34.8 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: RB | CVE-2016-5440 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 575 | 34.8 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DML unspecified vulnerability (CPU Jan 2017) | CVE-2017-3244 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 576 | 34.8 | P4 | 720h | appsec-legacy | bwapp | mysql: Client mysqldump unspecified vulnerability (CPU Jul 2 | CVE-2018-3070 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 577 | 34.8 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Security: Privileges unspecified vulnerabilit | CVE-2018-2818 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 578 | 34.8 | P4 | 720h | appsec-legacy | bwapp | pam: pam_userdb case insensitive password hash comparison | CVE-2013-7041 | CWE-310 | raesene/bwapp:latest (ubuntu 14.04) |
| 579 | 34.8 | P4 | 720h | appsec-legacy | bwapp | libffi: Requests an executable stack | CVE-2017-1000376 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 580 | 34.7 | P4 | 720h | appsec-legacy | bwapp | ntp: 'ntpq saveconfig' command allows dangerous characters i | CVE-2015-7976 | CWE-254 | raesene/bwapp:latest (ubuntu 14.04) |
| 581 | 34.7 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: DM | CVE-2016-5612 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 582 | 34.7 | P4 | 720h | appsec-legacy | bwapp | glibc: potential denial of service in internal_fnmatch() | CVE-2015-8984 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 583 | 34.7 | P4 | 720h | appsec-legacy | bwapp | expat: Using XML_Parse before rand() results into non-random | CVE-2012-6702 | CWE-310 | raesene/bwapp:latest (ubuntu 14.04) |
| 584 | 34.7 | P4 | 720h | appsec-legacy | bwapp | busybox: Segmentation fault when unzipping specially crafted | CVE-2015-9261 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 585 | 34.6 | P4 | 720h | appsec-legacy | bwapp | httpd: Improper handling of headers in mod_session can allow | CVE-2018-1283 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 586 | 34.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Apr  | CVE-2018-2781 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 587 | 34.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Oct  | CVE-2017-10378 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 588 | 34.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Security: Privileges unspecified vulnerabilit | CVE-2018-3063 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 589 | 34.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DML unspecified vulnerability (CPU Jul 2017) | CVE-2017-3641 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 590 | 34.6 | P4 | 720h | appsec-legacy | bwapp | perl-File-Path: rmtree/remove_tree race condition | CVE-2017-6512 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |
| 591 | 34.6 | P4 | 720h | appsec-legacy | bwapp | libxml2: out-of-bounds read in htmlParseNameComplex() | CVE-2016-2073 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 592 | 34.6 | P4 | 720h | appsec-legacy | bwapp | procps: Integer overflows leading to heap overflow in file2s | CVE-2018-1124 | CWE-122 | raesene/bwapp:latest (ubuntu 14.04) |
| 593 | 34.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Jul 2017) | CVE-2017-3652 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 594 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Apr 2018) | CVE-2018-2817 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 595 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: InnoDB unspecified vulnerability (CPU Apr 2018) | CVE-2018-2819 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 596 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Fe | CVE-2016-5629 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 597 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Jan 2017) | CVE-2017-3258 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 598 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DML unspecified vulnerability (CPU Apr 2017) | CVE-2017-3308 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 599 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Oct 2017) | CVE-2017-10384 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 600 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Apr  | CVE-2017-3309 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 601 | 34.5 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Optimizer unspecified vulnerability (CPU Apr  | CVE-2017-3453 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 602 | 34.5 | P4 | 720h | appsec-web | juice_shop | Out-of-bounds Read in base64url | GHSA-rvg8-pwq2-xj7q |  | Node.js |
| 603 | 34.5 | P4 | 720h | appsec-web | juice_shop | Cross Site Scripting | NSWG-ECO-154 |  | Node.js |
| 604 | 34.5 | P4 | 720h | appsec-node | nodegoat | Denial of Service in mongodb | GHSA-mh5c-679w-hh4r |  | Node.js |
| 605 | 34.5 | P4 | 720h | appsec-node | nodegoat | Cleartext Submission of Password: Password field password se |  | CWE-319 | /login |
| 606 | 34.5 | P4 | 720h | appsec-node | nodegoat | Cleartext Submission of Password: Password field password se |  | CWE-319 | /signup |
| 607 | 34.5 | P4 | 720h | appsec-node | nodegoat | Cleartext Submission of Password: Password field verify sent |  | CWE-319 | /signup |
| 608 | 34.4 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DML unspecified vulnerability (CPU Apr 2017) | CVE-2017-3456 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 609 | 34.4 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Parser unspecified vulnerability (CPU Oct 201 | CVE-2018-3133 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 610 | 34.4 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: DM | CVE-2016-0640 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 611 | 34.3 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Security: Privileges unspecified vulnerabilit | CVE-2017-3462 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 612 | 34.3 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Security: Privileges unspecified vulnerabilit | CVE-2017-3461 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 613 | 34.3 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Security: Privileges unspecified vulnerabilit | CVE-2017-3463 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 614 | 34.3 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Charsets unspecified vulnerability (CPU Jul 2 | CVE-2017-3648 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 615 | 34.3 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: My | CVE-2016-0641 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 616 | 34.2 | P4 | 720h | appsec-legacy | bwapp | mysql: unsafe chmod/chown use in init script (CPU Jan 2017) | CVE-2017-3265 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 617 | 34.1 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Apr 2018) | CVE-2018-2813 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 618 | 33.9 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Charsets unspecified vulnerability (CPU Jan 2 | CVE-2017-3243 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 619 | 33.9 | P4 | 720h | appsec-legacy | bwapp | mysql: MyISAM unspecified vulnerability (CPU Jul 2018) | CVE-2018-3058 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 620 | 33.9 | P4 | 720h | appsec-legacy | bwapp | krb5: Invalid S4U2Self or S4U2Proxy request causes assertion | CVE-2017-11368 | CWE-617 | raesene/bwapp:latest (ubuntu 14.04) |
| 621 | 33.9 | P4 | 720h | appsec-node | nodegoat | cross-spawn: regular expression denial of service | CVE-2024-21538 | CWE-1333 | Node.js |
| 622 | 33.9 | P4 | 720h | appsec-web | juice_shop | node-tar: node-tar: File smuggling due to inconsistent tar a | CVE-2026-53655 | CWE-436 | Node.js |
| 623 | 33.8 | P4 | 720h | appsec-legacy | bwapp | rsync: recv_files function metadata handling allows for acce | CVE-2017-17433 | CWE-862 | raesene/bwapp:latest (ubuntu 14.04) |
| 624 | 33.8 | P4 | 720h | appsec-node | nodegoat | node-tar: tar: node-tar: Arbitrary file overwrite and symlin | CVE-2026-23745 | CWE-22 | Node.js |
| 625 | 33.8 | P4 | 720h | appsec-web | juice_shop | undici: undici: HTTP header injection via unvalidated blob-l | CVE-2026-15157 | CWE-93 | Node.js |
| 626 | 33.7 | P4 | 720h | appsec-legacy | bwapp | mysql: Client programs unspecified vulnerability (CPU Oct 20 | CVE-2017-10379 | CWE-863 | raesene/bwapp:latest (ubuntu 14.04) |
| 627 | 33.7 | P4 | 720h | appsec-legacy | bwapp | php: mysqlnd interface vulnerable to BACKRONYM | CVE-2015-8838 | CWE-284 | raesene/bwapp:latest (ubuntu 14.04) |
| 628 | 33.7 | P4 | 720h | appsec-node | nodegoat | path-to-regexp: path-to-regexp: Denial of Service via catast | CVE-2026-4867 | CWE-1333 | Node.js |
| 629 | 33.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Locking unspecified vulnerability (CPU Apr 20 | CVE-2018-2771 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 630 | 33.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Apr 2017) | CVE-2017-3464 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 631 | 33.5 | P4 | 720h | appsec-legacy | bwapp | git: Mishandling layers of tree objects | CVE-2017-15298 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 632 | 33.5 | P4 | 720h | appsec-web | juice_shop | glibc: glibc: Process abort due to invalid memory in wordexp | CVE-2026-6368 | CWE-908 | bkimminich/juice-shop:latest (debian 13.6) |
| 633 | 33.4 | P4 | 720h | appsec-legacy | bwapp | mysql: Client mysqldump unspecified vulnerability (CPU Jul 2 | CVE-2017-3651 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 634 | 33.3 | P4 | 720h | appsec-legacy | bwapp | patch: Out-of-bounds access in pch_write_line function in pc | CVE-2016-10713 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 635 | 33.1 | P4 | 720h | appsec-legacy | bwapp | ntp: Broadcast Mode Replay Prevention DoS | CVE-2016-7427 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 636 | 33.1 | P4 | 720h | appsec-legacy | bwapp | ntp: Broadcast Mode Poll Interval Enforcement DoS | CVE-2016-7428 | CWE-400 | raesene/bwapp:latest (ubuntu 14.04) |
| 637 | 33.1 | P4 | 720h | appsec-node | nodegoat | serve-static: Improper Sanitization in serve-static | CVE-2024-43800 | CWE-79 | Node.js |
| 638 | 33.0 | P4 | 720h | appsec-legacy | bwapp | openssl: Padding oracle in AES-NI CBC MAC check | CVE-2016-2107 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 639 | 33.0 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: DM | CVE-2016-0643 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 640 | 33.0 | P4 | 720h | appsec-legacy | bwapp | krb5: null pointer deference in strlen function in plugins/k | CVE-2018-5710 | CWE-476 | raesene/bwapp:latest (ubuntu 14.04) |
| 641 | 32.8 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: FT | CVE-2016-0647 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 642 | 32.8 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: PS | CVE-2016-0648 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 643 | 32.8 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: DM | CVE-2016-0646 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 644 | 32.7 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: DD | CVE-2016-0644 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 645 | 32.7 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: PS | CVE-2016-0649 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 646 | 32.7 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Re | CVE-2016-0650 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 647 | 32.7 | P4 | 720h | appsec-legacy | bwapp | procps: Local privilege escalation in top | CVE-2018-1122 | CWE-829 | raesene/bwapp:latest (ubuntu 14.04) |
| 648 | 32.7 | P4 | 720h | appsec-web | juice_shop | node-tar: Uncontrolled recursion in mapHas/filesFilter allow | GHSA-r292-9mhp-454m |  | Node.js |
| 649 | 32.5 | P4 | 720h | appsec-legacy | bwapp | busybox: Integer overflow in the get_next_block function | CVE-2017-15873 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 650 | 32.5 | P4 | 720h | appsec-node | nodegoat | send: Code Execution Vulnerability in Send Library | CVE-2024-43799 | CWE-79 | Node.js |
| 651 | 32.4 | P4 | 720h | appsec-legacy | bwapp | systemd: Spoofing of XDG_SEAT allows for actions to be check | CVE-2019-3842 | CWE-285 | raesene/bwapp:latest (ubuntu 14.04) |
| 652 | 32.2 | P4 | 720h | appsec-legacy | bwapp | mysql: C API unspecified vulnerability (CPU Jul 2017) | CVE-2017-3635 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 653 | 32.2 | P4 | 720h | appsec-node | nodegoat | body-parser: body-parser: Denial of Service via invalid limi | CVE-2026-12590 | CWE-770 | Node.js |
| 654 | 32.1 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Fe | CVE-2016-0642 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 655 | 32.0 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: DDL unspecified vulnerability (CPU Jul 2017) | CVE-2017-3653 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 656 | 32.0 | P4 | 720h | appsec-node | nodegoat | express: Improper Input Handling in Express Redirects | CVE-2024-43796 | CWE-79 | Node.js |
| 657 | 31.5 | P4 | 720h | appsec-node | nodegoat | cookie: cookie accepts cookie name, path, and domain with ou | CVE-2024-47764 | CWE-74 | Node.js |
| 658 | 31.4 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Se | CVE-2016-0666 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 659 | 31.3 | P4 | 720h | appsec-legacy | bwapp | openssh: scp client improper directory name validation | CVE-2018-20685 | CWE-863 | raesene/bwapp:latest (ubuntu 14.04) |
| 660 | 31.3 | P4 | 720h | appsec-node | nodegoat | node-tar: tar: node-tar: Arbitrary file overwrite via Unicod | CVE-2026-23950 | CWE-176 | Node.js |
| 661 | 31.2 | P4 | 720h | appsec-legacy | bwapp | mysql: use of SSL/TLS not enforced in libmysqld (Return of B | CVE-2018-2767 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 662 | 31.1 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Se | CVE-2016-5584 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 663 | 31.0 | P4 | 720h | appsec-legacy | bwapp | perl: XSLoader loads relative paths not included in @INC | CVE-2016-6185 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 664 | 31.0 | P4 | 720h | appsec-node | nodegoat | node-tar: node-tar: Denial of Service via crafted archive wi | CVE-2026-59875 | CWE-248 | Node.js |
| 665 | 31.0 | P4 | 720h | appsec-web | juice_shop | undici: undici: Weakening of cookie SameSite policy due to i | CVE-2026-11525 | CWE-183 | Node.js |
| 666 | 30.8 | P4 | 720h | appsec-node | nodegoat | tar: tar: File overwrite via drive-relative symlink traversa | CVE-2026-31802 | CWE-22 | Node.js |
| 667 | 30.6 | P4 | 720h | appsec-web | juice_shop | undici: Undici: Response queue poisoning on reused keep-aliv | CVE-2026-6733 | CWE-367 | Node.js |
| 668 | 30.1 | P4 | 720h | appsec-legacy | bwapp | krb5: xdr_nullstring() doesn't check for terminating null ch | CVE-2015-8629 | CWE-125 | raesene/bwapp:latest (ubuntu 14.04) |
| 669 | 29.7 | P4 | 720h | appsec-legacy | bwapp | python: Heap-Buffer-Overflow and Heap-Use-After-Free in Obje | CVE-2018-1000030 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 670 | 29.7 | P4 | 720h | appsec-web | juice_shop | @tootallnate/once: @tootallnate/once: Denial of Service due  | CVE-2026-3449 | CWE-705 | Node.js |
| 671 | 29.6 | P4 | 720h | appsec-legacy | bwapp | libdb: Reads DB_CONFIG from the current working directory | CVE-2017-10140 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 672 | 29.5 | P4 | 720h | appsec-legacy | bwapp | openssl: Side-channel vulnerability on SMT/Hyper-Threading a | CVE-2018-5407 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 673 | 29.5 | P4 | 720h | appsec-node | nodegoat | Sanitization bypass using HTML Entities | NSWG-ECO-101 |  | Node.js |
| 674 | 29.5 | P4 | 720h | appsec-node | nodegoat | Unencrypted Channels: Sensitive data (POST data) was sent ov |  |  | /login |
| 675 | 29.5 | P4 | 720h | appsec-node | nodegoat | Reflected Cross Site Scripting: Reflected Cross Site Scripti |  | CWE-79 | /login |
| 676 | 29.5 | P4 | 720h | appsec-node | nodegoat | Source Code Disclosure - SQL |  | CWE-540 | http://nodegoat:4000 |
| 677 | 29.5 | P4 | 720h | appsec-node | nodegoat | Vulnerable JS Library |  | CWE-1395 | http://nodegoat:4000 |
| 678 | 29.3 | P4 | 720h | appsec-legacy | bwapp | curl: Out-of-bounds write via unchecked multiplication | CVE-2016-8617 | CWE-787 | raesene/bwapp:latest (ubuntu 14.04) |
| 679 | 29.2 | P4 | 720h | appsec-legacy | bwapp | cpio: directory traversal through symlinks | CVE-2015-1197 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 680 | 29.0 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Replication unspecified vulnerability (CPU Ap | CVE-2018-2755 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 681 | 29.0 | P4 | 720h | appsec-legacy | bwapp | ntp: Buffer Overflow in DPTS Clock | CVE-2017-6462 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 682 | 28.9 | P4 | 720h | appsec-node | nodegoat | node-tar: node-tar: File smuggling due to inconsistent tar a | CVE-2026-53655 | CWE-436 | Node.js |
| 683 | 28.4 | P4 | 720h | appsec-node | nodegoat | brace-expansion: juliangruber brace-expansion index.js expan | CVE-2025-5889 | CWE-400 | Node.js |
| 684 | 28.4 | P4 | 720h | appsec-legacy | bwapp | mysql: Client programs unspecified vulnerability (CPU Jul 20 | CVE-2017-3636 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 685 | 28.3 | P4 | 720h | appsec-web | juice_shop | messageformat has a prototype pollution vulnerability | CVE-2025-57349 | CWE-1321 | Node.js |
| 686 | 28.3 | P4 | 720h | appsec-web | juice_shop | Unencrypted Channels: No HTTPS redirection for this host. Al |  |  | / |
| 687 | 28.3 | P4 | 720h | appsec-web | juice_shop | Dangerous JS Functions |  | CWE-749 | http://juice-shop:3000 |
| 688 | 28.3 | P4 | 720h | appsec-web | juice_shop | Deprecated Feature Policy Header Set |  | CWE-16 | http://juice-shop:3000 |
| 689 | 28.3 | P4 | 720h | appsec-web | juice_shop | Timestamp Disclosure - Unix |  | CWE-497 | http://juice-shop:3000 |
| 690 | 28.1 | P4 | 720h | appsec-legacy | bwapp | shadow-utils: Incorrect integer handling results in LPE | CVE-2016-6252 | CWE-190 | raesene/bwapp:latest (ubuntu 14.04) |
| 691 | 28.0 | P4 | 720h | appsec-legacy | bwapp | OpenSSL: Side channel attack on modular exponentiation | CVE-2016-0702 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 692 | 27.7 | P4 | 720h | appsec-node | nodegoat | node-tar: Uncontrolled recursion in mapHas/filesFilter allow | GHSA-r292-9mhp-454m |  | Node.js |
| 693 | 27.5 | P4 | 720h | appsec-legacy | bwapp | mysql: unspecified vulnerability in subcomponent: Server: Pa | CVE-2016-3477 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 694 | 26.5 | P4 | 720h | appsec-legacy | bwapp | openssl: Non-constant time codepath followed for certain ope | CVE-2016-2178 | CWE-203 | raesene/bwapp:latest (ubuntu 14.04) |
| 695 | 26.5 | P4 | 720h | appsec-legacy | bwapp | Application Error Disclosure |  | CWE-550 | http://bwapp |
| 696 | 26.4 | P4 | 720h | appsec-legacy | bwapp | util-linux: Sending SIGKILL to other processes with root pri | CVE-2017-2616 | CWE-267 | raesene/bwapp:latest (ubuntu 14.04) |
| 697 | 26.2 | P4 | 720h | appsec-legacy | bwapp | openssh: Leak of host private key material to privilege-sepa | CVE-2016-10011 | CWE-320 | raesene/bwapp:latest (ubuntu 14.04) |
| 698 | 25.9 | P4 | 720h | appsec-legacy | bwapp | mysql: insecure error log file handling in mysqld_safe, inco | CVE-2017-3312 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 699 | 25.8 | P4 | 720h | appsec-legacy | bwapp | mysql: unrestricted mysqld_safe's ledir (CPU Jan 2017) | CVE-2017-3291 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 700 | 24.7 | P4 | 720h | appsec-legacy | bwapp | ROHNP: Key Extraction Side Channel in Multiple Crypto Librar | CVE-2018-0495 | CWE-203 | raesene/bwapp:latest (ubuntu 14.04) |
| 701 | 24.5 | P4 | 720h | appsec-legacy | bwapp | php: Dumpable FPM child processes allow bypassing opcache ac | CVE-2018-10545 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 702 | 24.4 | P4 | 720h | appsec-legacy | bwapp | mysql: Init script calling kill with root privileges using p | CVE-2018-3174 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 703 | 24.1 | P4 | 720h | appsec-node | nodegoat | on-headers: on-headers vulnerable to http response header ma | CVE-2025-7339 | CWE-241 | Node.js |
| 704 | 23.9 | P4 | 720h | appsec-legacy | bwapp | busybox: unprivileged arbitrary module load via basename abu | CVE-2014-9645 | CWE-20 | raesene/bwapp:latest (ubuntu 14.04) |
| 705 | 23.6 | P4 | 720h | appsec-legacy | bwapp | openssl: ECDSA P-256 timing attack key recovery | CVE-2016-7056 | CWE-385 | raesene/bwapp:latest (ubuntu 14.04) |
| 706 | 23.5 | P4 | 720h | appsec-legacy | bwapp | curl: --write-out out of bounds read | CVE-2017-7407 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 707 | 23.5 | P4 | 720h | appsec-legacy | bwapp | glibc: LD_POINTER_GUARD in the environment is not sanitized | CVE-2015-8777 | CWE-254 | raesene/bwapp:latest (ubuntu 14.04) |
| 708 | 23.3 | P4 | 720h | appsec-legacy | bwapp | perl-Data-Dumper: deep recursion stack overflow | CVE-2014-4330 | CWE-119 | raesene/bwapp:latest (ubuntu 14.04) |
| 709 | 23.3 | P4 | 720h | appsec-node | nodegoat | Out-of-bounds Read | NSWG-ECO-445 |  | Node.js |
| 710 | 23.3 | P4 | 720h | appsec-node | nodegoat | Unencrypted Channels: Sensitive data (cookie in the response |  |  | / |
| 711 | 23.3 | P4 | 720h | appsec-node | nodegoat | Unencrypted Channels: No HTTPS redirection for this host. Al |  |  | /login |
| 712 | 23.3 | P4 | 720h | appsec-node | nodegoat | Secure Flag cookie: Secure flag is not set on the cookie: 'c |  |  | / |
| 713 | 23.3 | P4 | 720h | appsec-node | nodegoat | Cookie without SameSite Attribute |  | CWE-1275 | http://nodegoat:4000 |
| 714 | 23.3 | P4 | 720h | appsec-node | nodegoat | Dangerous JS Functions |  | CWE-749 | http://nodegoat:4000 |
| 715 | 23.3 | P4 | 720h | appsec-node | nodegoat | Server Leaks Information via "X-Powered-By" HTTP Response He |  | CWE-497 | http://nodegoat:4000 |
| 716 | 22.8 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Replication unspecified vulnerability (CPU Oc | CVE-2017-10268 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 717 | 22.5 | P4 | 720h | appsec-legacy | bwapp | mysql: pid file can be created in a world-writeable director | CVE-2018-2773 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 718 | 22.2 | P4 | 720h | appsec-legacy | bwapp | (pt_chown): Improper pseudotty ownership and permissions cha | CVE-2013-2207 | CWE-264 | raesene/bwapp:latest (ubuntu 14.04) |
| 719 | 22.1 | P4 | 720h | appsec-legacy | bwapp | bash: popd controlled free | CVE-2016-9401 | CWE-416 | raesene/bwapp:latest (ubuntu 14.04) |
| 720 | 21.7 | P4 | 720h | appsec-legacy | bwapp | libgcrypt: side-channel attack on ECDH with Weierstrass curv | CVE-2015-7511 | CWE-200 | raesene/bwapp:latest (ubuntu 14.04) |
| 721 | 20.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: MyISAM unspecified vulnerability (CPU Jan 201 | CVE-2017-3313 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 722 | 20.3 | P4 | 720h | appsec-legacy | bwapp | yaSSL: AES key leak via cache-bank timing side channel attac | CVE-2016-7440 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 723 | 20.3 | P4 | 720h | appsec-legacy | bwapp | PHPinfo Page - Detect |  | cwe-200 | http://bwapp:80/phpinfo.php |
| 724 | 20.3 | P4 | 720h | appsec-legacy | bwapp | HttpOnly Flag cookie: HttpOnly flag is not set on the cookie |  |  | /portal.php |
| 725 | 20.3 | P4 | 720h | appsec-legacy | bwapp | Unencrypted Channels: No HTTPS redirection for this host. Al |  |  | / |
| 726 | 20.3 | P4 | 720h | appsec-legacy | bwapp | Unencrypted Channels: Sensitive data (cookie in the response |  |  | /portal.php |
| 727 | 20.3 | P4 | 720h | appsec-legacy | bwapp | Server Leaks Information via "X-Powered-By" HTTP Response He |  | CWE-497 | http://bwapp |
| 728 | 20.2 | P4 | 720h | appsec-legacy | bwapp | mysql: Logging unspecified vulnerability (CPU Jan 2017) | CVE-2017-3317 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 729 | 19.6 | P4 | 720h | appsec-legacy | bwapp | mysql: Server: Error Handling unspecified vulnerability (CPU | CVE-2017-3318 |  | raesene/bwapp:latest (ubuntu 14.04) |
| 730 | 19.3 | P4 | 720h | appsec-legacy | bwapp | dbus: denial of service in dbus systemd activation | CVE-2015-0245 | CWE-362 | raesene/bwapp:latest (ubuntu 14.04) |

## Score breakdown (top 10)

**#1 · 53.5 — zlib: heap-based buffer over-read and overflow in inflate() in inflate**
- cvss=24.5, epss=14.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5
- Drivers: EPSS percentile 0.969

**#2 · 53.3 — moment.js: regular expression denial of service**
- cvss=19.5, epss=14.3, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0
- Drivers: EPSS percentile 0.952

**#3 · 53.2 — node-ip: Incomplete fix for CVE-2023-42282**
- cvss=24.5, epss=14.2, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5
- Drivers: EPSS percentile 0.944

**#4 · 52.5 — nodejs-jsonwebtoken: verification step bypass with an altered token**
- cvss=18.8, epss=14.2, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0
- Drivers: EPSS percentile 0.946

**#5 · 51.5 — tough-cookie: prototype pollution in cookie memstore**
- cvss=24.5, epss=12.5, kev=0.0, exploit=0.0, asset=6.0, business=6.0, exposure=4.0, controls=-1.5
- Drivers: EPSS percentile 0.836

**#6 · 51.4 — openssl: Memory corruption in the ASN.1 encoder**
- cvss=25.0, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0
- Drivers: EPSS percentile 0.995

**#7 · 51.4 — mysql: general_log can write to configuration files, leading to privil**
- cvss=25.0, epss=14.9, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0
- Drivers: EPSS percentile 0.993

**#8 · 51.4 — glibc: stack guard protection bypass**
- cvss=18.8, epss=13.1, kev=0.0, exploit=0.0, asset=8.0, business=8.0, exposure=4.5, controls=-1.0
- Drivers: EPSS percentile 0.872

**#9 · 51.3 — openssl: doapr_outch function does not verify that certain memory allo**
- cvss=25.0, epss=14.8, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0
- Drivers: EPSS percentile 0.989

**#10 · 51.2 — OpenSSL: Fix memory issues in BIO_*printf functions**
- cvss=25.0, epss=14.7, kev=0.0, exploit=0.0, asset=5.0, business=5.0, exposure=3.5, controls=-2.0
- Drivers: EPSS percentile 0.982
