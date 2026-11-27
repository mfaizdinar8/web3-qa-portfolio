# Test Results — Project 03 (JSONPlaceholder)

Run with: `postman collection run collection/api-tests.json`
Tool: Postman CLI 1.94.0. Target: `https://jsonplaceholder.typicode.com`

## Final run — 27 Nov 2026 (after TC-10 strengthening; second consecutive 48/48 run)

| Metric | Value |
| --- | --- |
| Requests | 15 |
| Test scripts | 15 |
| Assertions | 48 |
| Passed | **48** |
| Failed | **0** |
| Total run duration | 23.7 s |
| Data received | 9.55 KB |
| Avg response time | 1,468 ms (min 1,312 ms, max 1,727 ms) |

## Per-request results

| ID | Request | Status | Time | Assertions | Result |
| --- | --- | --- | --- | --- | --- |
| TC-01 | GET /posts/1 | 200 OK | 1,312 ms | 6 | PASS |
| TC-02 | GET /posts | 200 OK | 1,371 ms | 4 | PASS |
| TC-03 | GET /posts?userId=1 | 200 OK | 1,517 ms | 3 | PASS |
| TC-04 | GET /posts/1/comments | 200 OK | 1,507 ms | 3 | PASS |
| TC-05 | GET /users/1 | 200 OK | 1,333 ms | 4 | PASS |
| TC-06 | POST /posts (valid) | 201 Created | 1,647 ms | 4 | PASS |
| TC-07 | POST /posts (no title) | 201 Created | 1,727 ms | 3 | PASS |
| TC-08 | POST /posts (empty {}) | 201 Created | 1,396 ms | 3 | PASS |
| TC-09 | PUT /posts/1 | 200 OK | 1,412 ms | 4 | PASS |
| TC-10 | PATCH /posts/1 | 200 OK | 1,455 ms | 4 | PASS |
| TC-11 | DELETE /posts/1 | 200 OK | 1,320 ms | 2 | PASS |
| TC-12 | DELETE /posts/999 | 200 OK | 1,547 ms | 2 | PASS |
| TC-13 | GET /posts/999 | 404 Not Found | 1,608 ms | 2 | PASS |
| TC-14 | GET /posts/abc | 404 Not Found | 1,494 ms | 2 | PASS |
| TC-15 | GET /invalid-endpoint | 404 Not Found | 1,512 ms | 2 | PASS |

TC-10's pre-request GET (reads the original body before patching) took 1,343 ms and is not counted among the 15 collection requests.

"PASS" here means the response matched the documented expected behavior in
`test-cases.md`. For TC-07, TC-08 and TC-12 the expected behavior was written
to document the real (non-validating / inconsistent) behavior — the underlying
findings are reported as API behavior observations in `bug-report.md`.

## Run history

- **First run (27 Nov 2026):** 48 assertions, 47 passed, 1 failed (TC-15.2 — see below).
- **Second run (27 Nov 2026):** 48/48 PASS in 21.2 s (avg 1,400 ms) — after fixing the TC-15.2 expectation.
- **Third and fourth runs (27 Nov 2026):** 48/48 PASS twice in a row after strengthening TC-10 (explicit before/after body comparison). The fourth run's numbers are recorded as the final run above.

## First run — 27 Nov 2026 (before the fix)

48 assertions, **47 passed, 1 failed**:

- **TC-15.2 FAIL:** `AssertionError: expected '{}' to be empty` — my test
  asserted `pm.response.text()` is empty, but the 404 response body is the
  JSON object `{}`. The API was behaving correctly; the test expectation was
  wrong. Fixed TC-15.2 to assert an empty object (same as TC-13.2/TC-14.2)
  and re-ran the full collection → 48/48 PASS.

This correction is recorded here on purpose: the first run's failure was a
test-design mistake, not an API defect.
