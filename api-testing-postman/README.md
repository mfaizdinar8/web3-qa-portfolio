# Project 03 — REST API Testing with Postman

Manual + automated API testing of the free fake REST API
[JSONPlaceholder](https://jsonplaceholder.typicode.com) (`https://jsonplaceholder.typicode.com`),
built as portfolio evidence for a Junior QA role.

## What was tested

| Area | Coverage |
| --- | --- |
| GET | Single post, all posts, filtered posts (`?userId=1`), post comments, single user |
| POST | Valid create, missing title, empty body |
| PUT | Full update of a post |
| PATCH | Partial update (title only) |
| DELETE | Existing post, nonexistent post |
| Negative | Nonexistent resource, invalid id, invalid endpoint |

**15 test cases, 48 assertions — 48/48 PASS** (final run, 27 Nov 2026).

## Structure

```text
api-testing-postman/
├── README.md
├── collection/
│   └── api-tests.json      # Postman collection (15 requests + test scripts)
├── test-cases.md           # Test case specifications
├── test-results.md         # Real execution results
├── bug-report.md           # Bugs found (2)
└── final-qa-report.md      # QA summary & conclusion
```

## How to run

Requires [Postman CLI](https://learning.postman.com/docs/postman-cli/) (`npm install -g postman-cli`).

```bash
postman collection run collection/api-tests.json
```

No login, API key, or environment file needed — the collection is self-contained
and hits the public JSONPlaceholder API.

## Environment

- Postman CLI 1.94.0 (Node v24.22.1, npm 10.9.4)
- Run date: 27 Nov 2026, Muse VM (Linux)
- Target: `https://jsonplaceholder.typicode.com`
- Average response time in final run: ~1,400 ms (min 1,242 ms, max 1,871 ms)
- Total run duration: 21.2 s; data received: 9.36 KB

## Results summary

| Metric | Value |
| --- | --- |
| Test cases | 15 |
| Assertions | 48 |
| Passed | 48 |
| Failed | 0 |

Two real findings are documented in `bug-report.md`:
1. **BUG-01 (Medium):** `POST /posts` accepts an empty body / missing fields and still returns `201 Created` — no server-side validation.
2. **BUG-02 (Low):** `DELETE /posts/999` (nonexistent) returns `200 OK` instead of `404` — inconsistent with `GET /posts/999`, which correctly returns `404`.

> Note: JSONPlaceholder is a mock API by design — it does not persist data and
> intentionally skips validation. The findings above are real observed behavior,
> reported as deviations from expected REST behavior, not as production defects.

## Notes on honesty

- Every PASS/FAIL in `test-results.md` comes from a real Postman CLI run.
  The first run had 1 failure (TC-15.2 — my own test expectation was wrong:
  the 404 body is `{}`, not empty); the expectation was corrected and the
  collection was re-run to a clean 48/48. Both runs are recorded.
- No result was fabricated.
