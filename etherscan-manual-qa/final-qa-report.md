# Final QA Report — Test Session 01: Etherscan

## Summary

| Item | Detail |
|---|---|
| Project | Etherscan (https://etherscan.io) |
| Date | 24 November 2026 |
| Testing type | Manual QA |
| Environment | Muse Browser |
| Wallet connection | Not used |
| Transactions | None (read-only testing) |
| Total test cases | 15 |
| Passed | 14 |
| Blocked | 1 |
| Failed | 0 |

Pass rate: 14 of 15 cases passed. All 14 executable cases passed; 1 case was blocked because the Next button was not available.

## Scope

Tested:
- Homepage load and refresh
- Search: wallet address (zero address), valid transaction hash, block number 19000000, invalid input
- Transaction details
- USDT token page
- Contract address navigation and Read Contract tab
- Read Contract queries: name, symbol, totalSupply
- Token transfers and pagination

Out of scope:
- Wallet connection and on-chain transactions (testing was read-only)
- Token transfers pagination (blocked — see TC013)

## Results

| Test ID | Actual Result | Status | Evidence |
|---|---|---|---|
| TC001 | Homepage loaded normally | Passed | Browser observation |
| TC002 | Zero address page loaded normally | Passed | Browser observation |
| TC003 | Transaction page loaded normally | Passed | Browser observation |
| TC004 | Transaction details displayed correctly | Passed | Browser observation |
| TC005 | Block 19000000 page loaded normally | Passed | Browser observation |
| TC006 | USDT token page loaded normally | Passed | Browser observation |
| TC007 | Contract address page opened normally | Passed | Browser observation |
| TC008 | Read Contract tab displayed | Passed | Browser observation |
| TC009 | Name query returned "Tether USD" | Passed | Browser observation |
| TC010 | Symbol query returned "USDT" | Passed | Browser observation |
| TC011 | Total supply query returned a value | Passed | Browser observation |
| TC012 | Token transfers displayed | Passed | Browser observation |
| TC013 | Next button was not available; pagination could not be tested | Blocked | Browser observation |
| TC014 | No records message and suggestions displayed | Passed | Browser observation |
| TC015 | Homepage refreshed successfully | Passed | Browser observation |

## Key Findings

- All executable checks passed. No defects were confirmed.
- Search works for addresses, transaction hashes, and block numbers; an invalid search shows a "No records" message with suggestions.
- The USDT contract read functions returned the expected values: name "Tether USD" and symbol "USDT".
- One blocked test: token transfers pagination (TC013) could not be tested because the Next button was not available. See [bug-observations.md](bug-observations.md) (OBS-01). This is a testing limitation, not a confirmed bug.
- One testing note: the first transaction hash test used invalid sample data. The test was repeated with a valid transaction hash found on the site and passed. The first attempt is not counted as a separate test case.

## Limitations

- Manual browser observation only; no automated tests were run.
- No screenshots were captured in this session; evidence is recorded browser observation.
- Token transfers pagination was not verified.
- Only public pages were covered; no wallet connection or on-chain interaction was tested.

## Conclusion

Etherscan passed every executable manual QA check in this session (14/14). The only open items are one blocked pagination test and one testing note about the repeated transaction hash test, both documented in [bug-observations.md](bug-observations.md).

## Disclaimer

This is an independent practice project created for learning and portfolio purposes. It is not official work for Etherscan, and I am not affiliated with or endorsed by Etherscan.

## Related Files

- [Test Cases](test-cases.md)
- [Test Session 01](test-session-01.md)
- [Bug Observations](bug-observations.md)
