# Test Results — Project 03 (JSONPlaceholder)

Run with: `postman collection run collection/api-tests.json`
Tool: Postman CLI 1.94.0. Target: `https://jsonplaceholder.typicode.com`

## Final run — 27 Nov 2026 (after fixing one wrong test expectation)

| Metric | Value |
| --- | --- |
| Requests | 15 |
| Test scripts | 15 |
| Assertions | 48 |
| Passed | **48** |
| Failed | **0** |
| Total run duration | 21.2 s |
| Data received | 9.36 KB |
| Avg response time | 1,400 ms (min 1,242 ms, max 1,871 ms) |

## Per-request results

| ID | Request | Status | Time | Assertions | Result |
| --- | --- | --- | --- | --- | --- |
| TC-01 | GET /posts/1 | 200 OK | 1,243 ms | 6 | PASS |
| TC-02 | GET /posts | 200 OK | 1,292 ms | 4 | PASS |
| TC-03 | GET /posts?userId=1 | 200 OK | 1,871 ms | 3 | PASS |
| TC-04 | GET /posts/1/comments | 200 OK | 1,340 ms | 3 | PASS |
| TC-05 | GET /users/1 | 200 OK | 1,242 ms | 4 | PASS |
| TC-06 | POST /posts (valid) | 201 Created | 1,312 ms | 4 | PASS |
| TC-07 | POST /posts (no title) | 201 Created | 1,339 ms | 3 | PASS |
| TC-08 | POST /posts (empty {}) | 201 Created | 1,415 ms | 3 | PASS |
| TC-09 | PUT /posts/1 | 200 OK | 1,442 ms | 4 | PASS |
| TC-10 | PATCH /posts/1 | 200 OK | 1,315 ms | 4 | PASS |
| TC-11 | DELETE /posts/1 | 200 OK | 1,557 ms | 2 | PASS |
| TC-12 | DELETE /posts/999 | 200 OK | 1,678 ms | 2 | PASS |
| TC-13 | GET /posts/999 | 404 Not Found | 1,365 ms | 2 | PASS |
| TC-14 | GET /posts/abc | 404 Not Found | 1,269 ms | 2 | PASS |
| TC-15 | GET /invalid-endpoint | 404 Not Found | 1,329 ms | 2 | PASS |

"PASS" here means the response matched the documented expected behavior in
`test-cases.md`. For TC-07, TC-08 and TC-12 the expected behavior was written
to document the real (non-validating / inconsistent) behavior — the underlying
findings are reported as bugs in `bug-report.md`.

## First run — 27 Nov 2026 (before the fix)

48 assertions, **47 passed, 1 failed**:

- **TC-15.2 FAIL:** `AssertionError: expected '{}' to be empty` — my test
  asserted `pm.response.text()` is empty, but the 404 response body is the
  JSON object `{}`. The API was behaving correctly; the test expectation was
  wrong. Fixed TC-15.2 to assert an empty object (same as TC-13.2/TC-14.2)
  and re-ran the full collection → 48/48 PASS.

This correction is recorded here on purpose: the first run's failure was a
test-design mistake, not an API defect.
