# Test Cases — Project 03 (JSONPlaceholder)

Target: `https://jsonplaceholder.typicode.com`
Tool: Postman CLI 1.94.0. Each test case is one request in
`collection/api-tests.json` with automated assertions.

## Positive — GET

| ID | Request | Expected result |
| --- | --- | --- |
| TC-01 | `GET /posts/1` | 200; JSON; `Content-Type: application/json`; `id` = 1; `userId` = 1; `body` not empty |
| TC-02 | `GET /posts` | 200; JSON array; 100 posts; every post has `userId`, `id`, `title`, `body` |
| TC-03 | `GET /posts?userId=1` | 200; 10 posts; all `userId` = 1 |
| TC-04 | `GET /posts/1/comments` | 200; 5 comments; all `postId` = 1 |
| TC-05 | `GET /users/1` | 200; `id` = 1; has `name`, `username`, `email`; email contains `@` |

## Positive — POST / PUT / PATCH / DELETE

| ID | Request | Body | Expected result |
| --- | --- | --- | --- |
| TC-06 | `POST /posts` | `{"title":"QA Test Post","body":"Created by Postman CLI test","userId":1}` | 201; `id` = 101; echoes `title`, `body`, `userId` |
| TC-09 | `PUT /posts/1` | `{"id":1,"title":"updated title","body":"updated body","userId":1}` | 200; `id` stays 1; `title`, `body`, `userId` fully replaced |
| TC-10 | `PATCH /posts/1` | `{"title":"patched title"}` | 200; `id` stays 1; `title` patched; `userId` still 1; `body` equals the value read before PATCH (pre-request GET saved to a collection variable) |
| TC-11 | `DELETE /posts/1` | — | 200; response body is `{}` |

## Negative

| ID | Request | Expected result | Note |
| --- | --- | --- | --- |
| TC-07 | `POST /posts` (no `title`) | 201; `id` = 101; `title` missing in response | Documents missing server-side validation → OBS-01 |
| TC-08 | `POST /posts` (empty `{}`) | 201; `id` = 101; response contains only `id` | Documents missing server-side validation → OBS-01 |
| TC-12 | `DELETE /posts/999` | 200; response body is `{}` | Inconsistent with GET 404 for the same id → OBS-02 |
| TC-13 | `GET /posts/999` | 404; response body is `{}` | Correct REST behavior |
| TC-14 | `GET /posts/abc` | 404; response body is `{}` | Invalid id handled correctly |
| TC-15 | `GET /invalid-endpoint` | 404; response body is `{}` | Unknown route handled correctly |

## Coverage

- Methods: GET, POST, PUT, PATCH, DELETE (all 5 covered)
- Positive: 9 cases (TC-01–06, TC-09–11)
- Negative: 6 cases (TC-07, TC-08, TC-12–15)
- Total: **15 test cases, 48 assertions**
