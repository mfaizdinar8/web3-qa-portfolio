# Final QA Report — Project 03: REST API Testing with Postman

**Project:** API Testing with Postman (JSONPlaceholder)
**Tester:** M Faiz Dinar (Junior QA portfolio)
**Date:** 27 Nov 2026
**Target:** `https://jsonplaceholder.typicode.com`
**Tool:** Postman CLI 1.94.0 (`npm install -g postman-cli`)

## 1. Objective

Demonstrate manual + automated REST API testing: build a Postman collection
covering all 5 HTTP methods plus negative testing, execute it for real, and
document results, bugs, and a QA conclusion — as recruiter-visible evidence.

## 2. Scope

- 15 test cases (9 positive, 6 negative), 48 assertions.
- Methods: GET, POST, PUT, PATCH, DELETE.
- Endpoints: `/posts`, `/posts/:id`, `/posts/:id/comments`, `/users/:id`.
- Out of scope: authentication (API is public, no auth), performance/load
  testing, data persistence (mock API does not persist).

## 3. Results

| Metric | Value |
| --- | --- |
| Test cases executed | 15 |
| Assertions | 48 |
| Passed | 48 |
| Failed | 0 |
| Bugs found | 2 (1 Medium, 1 Low) |

All 15 test cases passed against their documented expected behavior. Response
times were stable (avg ~1.4 s, max 1.9 s).

## 4. Bugs found

| ID | Summary | Severity |
| --- | --- | --- |
| BUG-01 | `POST /posts` accepts empty / incomplete body, returns `201` — no server-side validation | Medium |
| BUG-02 | `DELETE /posts/999` returns `200` instead of `404` — inconsistent with `GET` | Low |

Details, reproduction steps, and evidence: `bug-report.md`.

## 5. Process notes

- Behavior of every endpoint was probed with `curl` before writing test
  expectations, so assertions describe real behavior.
- The first collection run had 1 failure (TC-15.2) caused by a wrong test
  expectation (404 body is `{}`, not empty text). The expectation was fixed
  and the collection re-run to 48/48. The failure and the fix are recorded
  in `test-results.md`.
- No result in this report was fabricated; all PASS/FAIL values come from
  real Postman CLI executions.

## 6. Conclusion

The API is functionally sound for its purpose as a mock service: reads,
creates, full/partial updates, deletes, and error handling for unknown
resources and routes all behave as expected, with two deviations worth
reporting (missing input validation on POST, inconsistent DELETE status).
Given it is a mock API by design, both findings are acceptable as documented
observations rather than release blockers.

**Verdict: PASS with 2 documented observations. Portfolio-ready.**
