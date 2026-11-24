# Test Session 01

Project: Etherscan
Testing Type: Manual QA
Environment: Muse Browser
Wallet Connection: Not used
Transactions: None (read-only testing)

## Test Results

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

## Notes

- Only verified observations are recorded.
- TC003: the first transaction hash test used invalid sample data. The test was repeated with a valid transaction hash found on the site and passed. The first attempt is not counted as a separate test case.
- TC013: pagination could not be tested because the Next button was not available. This is recorded as Blocked, not as a confirmed bug.
