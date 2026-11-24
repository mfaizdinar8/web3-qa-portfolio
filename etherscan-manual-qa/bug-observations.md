# Bug Observations — Test Session 01: Etherscan

Date: 24 November 2026
Environment: Muse Browser
Source session: [test-session-01.md](test-session-01.md)

## OBS-01: Token Transfers pagination could not be tested

- Related test case: TC013
- Type: Testing limitation, not a confirmed bug
- Status: Blocked

### Detail

The Next button was not available on the Token Transfers list, so pagination could not be tested. No defect is confirmed; the reason the button was unavailable was not established.

## OBS-02: First transaction hash test used invalid sample data

- Related test case: TC003 (testing note)
- Type: Testing note, not a defect
- Status: Closed (retested)

### Detail

The first attempt used sample data that was not a valid transaction hash. The test was repeated with a valid transaction hash found on the site and passed. The first attempt is not counted as a separate test case.

## Summary

| Item | Count |
|---|---|
| Open observations | 1 (OBS-01) |
| Blocked tests | 1 (TC013) |
| Confirmed defects | 0 |
