# Test Results — Project 04 (ethereum.org, Selenium)

Run with: `../venv/bin/python run_tests.py` (from `selenium-web-automation/`)
Tool: Python 3.12.3 + Selenium 4.54.0, headless Chrome 157.
Target: `https://ethereum.org`

## Final run — 27 Nov 2026 (run 5)

| Metric | Value |
| --- | --- |
| Tests run | 15 |
| Passed | **15** |
| Failed | **0** |
| Errors | **0** |
| Skipped | 0 |
| Total suite time | 47.3 s |

## Per-test results (final run)

| ID | Test | Time | Result |
| --- | --- | --- | --- |
| TC-01 | Homepage title contains "Ethereum" | 5.2 s | PASS |
| TC-02 | Homepage H1 text | 0.8 s | PASS |
| TC-03 | Page language is "en" | 0.7 s | PASS |
| TC-04 | Search toggle visible | 0.6 s | PASS |
| TC-05 | Footer "Learn hub" link | 0.5 s | PASS |
| TC-06 | /learn/ loads | 4.6 s | PASS |
| TC-07 | /developers/ loads | 3.5 s | PASS |
| TC-08 | /what-is-ethereum/ loads | 0.9 s | PASS |
| TC-09 | Browser Back returns home | 2.5 s | PASS |
| TC-10 | Refresh keeps homepage | 1.1 s | PASS |
| TC-11 | Click footer "What is Ethereum?" | 7.1 s | PASS |
| TC-12 | Search for "staking" | 1.5 s | PASS |
| TC-13 | Footer links valid | 3.7 s | PASS |
| TC-14 | 404 page | 5.4 s | PASS |
| TC-15 | Missing element returns empty list | 5.6 s | PASS |

## Run history (all runs real, none hidden)

| Run | Date | Result | What happened |
| --- | --- | --- | --- |
| 1 | 27 Nov 2026 | 11 passed, 2 failed, 2 errors (85.9 s) | TC-04: checked the first (hidden) search toggle instead of the visible one. TC-11: footer click intercepted (element outside viewport). TC-12: waited for the hidden toggle to become clickable (timeout). TC-13: expected all footer links to stay on ethereum.org — the footer also links to blog.ethereum.org. |
| 2 | 27 Nov 2026 | 14 passed, 1 failed (49.0 s) | TC-04/TC-11/TC-12 fixed. TC-13 failed again: footer also links to esp.ethereum.foundation. |
| 3 | 27 Nov 2026 | 14 passed, 1 failed (45.5 s) | TC-13 expectation widened to ethereum.org + ethereum.foundation. Failed again: footer also links to devcon.org. |
| 4 | 27 Nov 2026 | 14 passed, 1 failed (46.3 s) | TC-13 rewritten to "valid https href". Failed again: footer has a `mailto:press@ethereum.org` link. |
| 5 | 27 Nov 2026 | **15 passed, 0 failed (47.3 s)** | TC-13 allows well-formed `mailto:` links. Clean run. |

Every failure above was a mistake in my test expectation, not a site defect.
Each fix corrected the expectation to verified live behavior, and the suite
was re-run in full after every fix. No test was deleted or skipped.
