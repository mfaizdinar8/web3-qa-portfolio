# Final QA Report — Project 04: Selenium Web Automation (ethereum.org)

**Project:** Selenium Web Automation (ethereum.org)
**Tester:** M Faiz Dinar (Junior QA portfolio)
**Date:** 27 Nov 2026
**Target:** `https://ethereum.org`
**Tool:** Python 3.12.3 + Selenium 4.54.0, headless Chrome 157

## 1. Objective

Demonstrate browser test automation: build a Selenium suite covering
homepage checks, navigation, element interaction, and negative cases —
executed for real in headless Chrome, with results, observations, and a QA
conclusion, as recruiter-visible evidence. This is the automation step after
manual QA (Project 01) and API testing (Project 03).

## 2. Scope

- 15 test cases (5 homepage, 5 navigation, 3 interaction, 2 negative).
- Locators: tag name, CSS selector, link text, XPath, aria-label.
- Interactions: navigation, browser Back, refresh, click, text input,
  explicit waits, ActionChains.
- Out of scope: login/authentication (site is public, no login), visual
  regression, cross-browser runs (Chrome only), performance/load testing.

## 3. Results

| Metric | Value |
| --- | --- |
| Test cases executed | 15 |
| Passed | 15 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Total suite time | 47.3 s |

All 15 test cases passed. Response behavior was stable across 5 runs.

## 4. Observations

| ID | Summary |
| --- | --- |
| OBS-01 | Two search toggle buttons exist (desktop + mobile); only the visible one can be used |
| OBS-02 | Footer click needs ActionChains scrolling on a very long page |
| OBS-03 | Footer links out to blog.ethereum.org, esp.ethereum.foundation, devcon.org, and a mailto: address — all official Ethereum destinations |
| OBS-04 | System pip cannot install Selenium (Debian-managed urllib3); a venv is required |

Details: `observations.md`. No site defects were found.

## 5. Process notes

- The site's real structure was probed with Selenium before writing the
  tests (title, H1, language, footer links, 404 page), so expectations were
  based on verified behavior.
- Four runs failed before the clean one — every failure was a mistake in my
  own test expectation (hidden toggle, intercepted click, too-narrow footer
  domain assumption, mailto: link). Each was fixed and the full suite re-run.
  The failures and fixes are recorded in `test-results.md`.
- No result in this report was fabricated; all PASS/FAIL values come from
  real suite executions. No test was deleted or skipped to reach 15/15.

## 6. Conclusion

The site behaves correctly across everything the suite covers: the homepage
renders with the expected title, heading, and language; the main sections
load; footer navigation and site search work; the 404 page is handled
gracefully; and missing elements are reported as empty results rather than
crashes.

**Verdict: PASS, 0 defects. Portfolio-ready.**
