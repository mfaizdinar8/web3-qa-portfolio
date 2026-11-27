# API Behavior Observations — Project 03 (JSONPlaceholder)

Target: `https://jsonplaceholder.typicode.com`
Date observed: 27 Nov 2026. Observed by: Postman CLI collection run (`collection/api-tests.json`).
Environment: Postman CLI 1.94.0, Muse VM (Linux).

> Context: JSONPlaceholder is a mock API by design — it does not persist data
> and intentionally skips validation. **There is no published API contract or
> specification for JSONPlaceholder**, so the items below are *observed API
> behavior / API contract inconsistencies* measured against common REST
> conventions — not confirmed defects against a spec, and not production bugs.

## OBS-01 — POST /posts accepts empty / incomplete body (no validation)

- **Significance:** Medium (as a contract inconsistency)
- **Test cases:** TC-07, TC-08
- **Steps to reproduce:**
  1. `POST /posts` with body `{"body": "test body", "userId": 1}` (no `title`)
  2. `POST /posts` with body `{}`
- **Expected (by common REST convention — no published contract):** `400 Bad Request` (or `422`) — required field `title` is missing.
- **Actual:** `201 Created` in both cases. Missing-title request returns
  `{"body": "test body", "userId": 1, "id": 101}`; empty-body request returns
  `{"id": 101}`.
- **Impact:** In a real API, clients could not rely on the server to reject invalid payloads, and incomplete records could be created silently. Here the API is a mock that stores nothing, so the impact is limited to the contract inconsistency itself.

## OBS-02 — DELETE nonexistent resource returns 200 instead of 404

- **Significance:** Low (as a contract inconsistency)
- **Test cases:** TC-12 (vs TC-13)
- **Steps to reproduce:**
  1. `DELETE /posts/999` (id 999 does not exist)
  2. `GET /posts/999` for comparison
- **Expected (by common REST convention — no published contract):** `404 Not Found` for the DELETE, consistent with the GET.
- **Actual:** `DELETE /posts/999` returns `200 OK` with `{}`; `GET /posts/999`
  correctly returns `404 Not Found` with `{}`.
- **Impact:** Inconsistent error handling across methods — a client cannot tell
  from the DELETE response whether anything was actually deleted.

## What works correctly (verified, no observation)

- `GET /posts/999` and `GET /posts/abc` correctly return `404` (TC-13, TC-14).
- Unknown routes correctly return `404` (TC-15).
- `PATCH` preserves unmentioned fields (TC-10); `PUT` fully replaces the
  resource (TC-09); `POST` with a valid body returns `201` with `id` 101 (TC-06).
- `GET /posts` returns exactly 100 posts; `GET /posts?userId=1` returns 10,
  all belonging to user 1; `GET /posts/1/comments` returns 5, all `postId` 1.
