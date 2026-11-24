# Etherscan Manual QA

## About

Manual QA practice on [Etherscan](https://etherscan.io), the Ethereum block explorer. Testing covered the homepage, search, transaction and block pages, the USDT token page, contract read functions, and token transfers. All testing was manual and read-only.

## Results — Test Session 01 (24 November 2026)

- 15 test cases: **14 Passed, 1 Blocked, 0 Failed**
- Manual, read-only testing; no wallet connection, no transactions
- No defects confirmed; 1 open observation (token transfers pagination could not be tested)

### Reports

- [Test Cases](test-cases.md) — full test case list (TC001–TC015)
- [Test Session 01](test-session-01.md) — session log with verified observations
- [Final QA Report](final-qa-report.md) — full test results and conclusion
- [Bug Observations](bug-observations.md) — open observation and testing notes

## Testing Scope

- Homepage load and refresh
- Search: wallet address, transaction hash, block number, invalid input
- Transaction details
- USDT token page and contract read functions (name, symbol, totalSupply)
- Token transfers and pagination

## Evidence

Browser observations recorded per test case in the session log and final report. No screenshots were captured in Session 01.

## Tools

- Browser (Muse Browser)
- GitHub
- Markdown

## Limitations

- Manual testing only; no automated tests.
- Token transfers pagination (TC013) could not be tested because the Next button was not available.

## Disclaimer

This is an independent practice project created for learning and portfolio purposes. It is not official work for Etherscan, and I am not affiliated with or endorsed by Etherscan.
