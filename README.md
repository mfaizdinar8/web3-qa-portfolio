# Web3 QA Portfolio

## About Me

I am an aspiring Web3 QA tester learning manual quality assurance by testing real Web3 applications. This portfolio documents my hands-on practice: structured test cases, recorded results, and honest observations — including what I could not test and why.

## Skills

- Manual Testing
- Test Case Design
- Functional Testing
- Exploratory Testing
- Bug Reporting
- API Testing (Postman)
- Web3 dApp Familiarity

## Featured Projects

### Project 01 — Ethereum.org Manual QA

A manual QA session on [ethereum.org](https://ethereum.org), covering the homepage, navigation, page refresh, browser back button, page title consistency, external links, layout consistency, search behavior, and error messages. No wallet connection and no transactions were used.

**Test results (24 November 2026):** 15 test cases — **14 Passed, 1 Blocked, 0 Failed**. One test (mobile layout) was blocked by a browser limitation, and one observation about empty-search feedback is still open for further investigation.

**Scope:** Website QA, navigation, search, error handling, layout consistency.
**Testing type:** Manual.
**Disclaimer:** Independent practice project, not officially affiliated with the Ethereum Foundation.

#### Project Files

- [README](ethereum-org-manual-qa/README.md) — project overview and results summary
- [Test Cases](ethereum-org-manual-qa/test-cases.md) — full test case list (TC001–TC015)
- [Test Session 01](ethereum-org-manual-qa/test-session-01.md) — session log with verified observations
- [Final QA Report](ethereum-org-manual-qa/final-qa-report.md) — full test results and conclusion
- [Bug Observations](ethereum-org-manual-qa/bug-observations.md) — open observation and testing limitations

### Project 02 — Etherscan Manual QA

A manual, read-only QA session on [Etherscan](https://etherscan.io), the Ethereum block explorer, covering the homepage, search, transaction and block pages, the USDT token page, smart contract Read Contract functions, and token transfers. No wallet connection and no transactions were used.

**Test results (24 November 2026):** 15 test cases — **14 Passed, 1 Blocked, 0 Failed**. One test (token transfers pagination) was blocked because the Next button was not available.

**Scope:** Blockchain explorer, wallet address search, transaction details, block search, token pages, smart contract Read Contract.
**Testing type:** Manual, read-only.
**Disclaimer:** Independent practice project, not officially affiliated with Etherscan.

#### Project Files

- [README](etherscan-manual-qa/README.md) — project overview and results summary
- [Test Cases](etherscan-manual-qa/test-cases.md) — full test case list (TC001–TC015)
- [Test Session 01](etherscan-manual-qa/test-session-01.md) — session log with verified observations
- [Final QA Report](etherscan-manual-qa/final-qa-report.md) — full test results and conclusion
- [Bug Observations](etherscan-manual-qa/bug-observations.md) — open observation and testing notes

### Project 03 — REST API Testing with Postman

An API testing session on [JSONPlaceholder](https://jsonplaceholder.typicode.com), a free fake REST API, covering all five HTTP methods (GET, POST, PUT, PATCH, DELETE) plus negative testing. The Postman collection runs 15 test cases with 48 automated assertions via Postman CLI — no login or API key needed.

**Test results (27 November 2026):** 15 test cases, 48 assertions — **48 Passed, 0 Failed**. Two API behavior observations were documented: POST accepts an empty/incomplete body without validation, and DELETE of a nonexistent resource returns 200 instead of 404 (no published API contract exists, so these are deviations from common REST conventions, not confirmed defects).

**Scope:** REST API testing, positive and negative testing, automated assertions.
**Testing type:** Manual test design + automated execution (Postman CLI).
**Disclaimer:** Independent practice project. JSONPlaceholder is a mock API by design — it does not persist data and intentionally skips validation, so the findings are documented observations, not production defects.

#### Project Files

- [README](api-testing-postman/README.md) — project overview and results summary
- [Collection](api-testing-postman/collection/api-tests.json) — Postman collection (15 requests + test scripts)
- [Test Cases](api-testing-postman/test-cases.md) — full test case list (TC-01–TC-15)
- [Test Results](api-testing-postman/test-results.md) — real execution results (48/48 PASS)
- [Bug Report](api-testing-postman/bug-report.md) — 2 findings with reproduction steps
- [Final QA Report](api-testing-postman/final-qa-report.md) — full test results and conclusion

## Tools

- Browser (Muse Browser)
- Postman CLI
- GitHub
- Markdown

## Disclaimer

This is an independent practice project created for learning and portfolio purposes. It is not official work for the Ethereum Foundation or Etherscan, and I am not affiliated with or endorsed by either.
