# Bug Observations — Test Session 01: Ethereum.org

Date: 24 November 2026
Environment: Muse Browser (cloud, B1 profile)
Source session: [test-session-01.md](test-session-01.md)

## OBS-01: Empty search submission shows no response or validation

- Related test case: TC011 (additional observation)
- Severity: Low — observation, not a confirmed defect
- Status: Open — needs further investigation

### Steps to reproduce

1. Open https://ethereum.org.
2. Open the site search.
3. Submit the search with an empty input.

### Expected

A validation message or other visible feedback indicating that a search term is required.

### Actual

No visible response or validation message appeared.

### Notes

- Valid searches work correctly: searching for "Ethereum" generated an AI answer with source references, and "Smart Contracts" returned a relevant AI answer.
- An invalid query behaves correctly too: it shows a "No results" message with alternative search suggestions.
- Only the empty submission is silent. This needs a retest to confirm whether the submit is intentionally ignored or a validation message is missing.

## OBS-02: Mobile layout could not be tested

- Related test case: TC005
- Type: Testing limitation, not a product defect
- Status: Blocked

### Detail

Muse Browser provides no mobile or responsive viewport mode, so responsive behavior and mobile layout could not be verified in this session. Recommend retesting on a real mobile device or in a browser with device emulation before drawing any conclusion about mobile layout.

## Summary

| Item | Count |
|---|---|
| Open observations | 1 (OBS-01) |
| Blocked tests | 1 (TC005) |
| Confirmed defects | 0 |
