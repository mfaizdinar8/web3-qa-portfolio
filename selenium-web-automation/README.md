# Project 04 — Selenium Web Automation (ethereum.org)

Automated browser tests for [ethereum.org](https://ethereum.org) using
Python + Selenium WebDriver, built as portfolio evidence for a Junior QA role
— the automation step after manual QA (Project 01) and API testing (Project 03).

## What was tested

| Area | Coverage |
| --- | --- |
| Homepage | Title, H1 text, page language, search toggle, footer link |
| Navigation | /learn/, /developers/, /what-is-ethereum/, browser Back, refresh |
| Interaction | Footer link click, site search, footer link validation |
| Negative | Unknown URL (404 page), non-existent element lookup |

**15 test cases — 15/15 PASS** (final run, 27 Nov 2026, 47.3 s).

## Structure

```text
selenium-web-automation/
├── README.md
├── requirements.txt
├── run_tests.py            # test runner (unittest + per-test timings)
├── tests/
│   ├── base.py             # shared driver setup (headless Chrome)
│   ├── test_homepage.py    # TC-01–TC-05
│   ├── test_navigation.py  # TC-06–TC-10
│   ├── test_interaction.py # TC-11–TC-13
│   └── test_negative.py    # TC-14–TC-15
├── test-cases.md           # test case specifications
├── test-results.md         # real execution results
├── observations.md         # findings from the runs (test-design fixes)
└── final-qa-report.md      # QA summary & conclusion
```

## How to run

Requires Python 3.12+ and Google Chrome.

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
cd selenium-web-automation
../venv/bin/python run_tests.py
```

No login, API key, or test account needed — the tests run against the public
ethereum.org site in headless Chrome. Selenium Manager downloads the matching
ChromeDriver automatically on first run.

## Environment

- Python 3.12.3, Selenium 4.54.0 (in a venv — system pip cannot install it:
  the Debian-managed urllib3 cannot be uninstalled, see `observations.md`)
- Google Chrome 157.0.8103.38, headless
- Run date: 27 Nov 2026, Muse VM (Linux)
- Target: `https://ethereum.org`
- Total suite time (final run): 47.3 s for 15 tests

## Results summary

| Metric | Value |
| --- | --- |
| Test cases | 15 |
| Passed | 15 |
| Failed | 0 |
| Errors | 0 |

No site defects were found. All four failures across the earlier runs were
mistakes in my own test expectations (see `test-results.md` run history and
`observations.md`) — each was fixed and the suite re-run to a clean 15/15.

## Notes on honesty

- Every PASS/FAIL in `test-results.md` comes from real suite executions.
- No result was fabricated, and no failing test was deleted or skipped to
  reach 15/15 — the expectations were corrected to match verified site
  behavior, with the corrections recorded.
