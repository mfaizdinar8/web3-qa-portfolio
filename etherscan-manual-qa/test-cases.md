# Etherscan Manual QA Test Cases

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC001 | Open homepage | Homepage loads | Homepage loaded normally | Passed |
| TC002 | Search wallet address (zero address) | Address page loads | Zero address page loaded normally | Passed |
| TC003 | Search valid transaction hash | Transaction page loads | Transaction page loaded normally | Passed |
| TC004 | View transaction details | Transaction details display correctly | Transaction details displayed correctly | Passed |
| TC005 | Search block number 19000000 | Block page loads | Block 19000000 page loaded normally | Passed |
| TC006 | Open USDT token page | Token page loads | USDT token page loaded normally | Passed |
| TC007 | Navigate to Contract Address | Contract address page loads | Contract address page opened normally | Passed |
| TC008 | Open Read Contract tab | Read Contract tab displays | Read Contract tab displayed | Passed |
| TC009 | Read Contract name query | Name returns "Tether USD" | Name query returned "Tether USD" | Passed |
| TC010 | Read Contract symbol query | Symbol returns "USDT" | Symbol query returned "USDT" | Passed |
| TC011 | Read Contract totalSupply query | Total supply value is returned | Total supply query returned a value | Passed |
| TC012 | Open Token Transfers | Token transfers list displays | Token transfers displayed | Passed |
| TC013 | Token Transfers pagination | Next page loads | Next button was not available; pagination could not be tested | Blocked |
| TC014 | Search invalid input | No records message and suggestions display | No records message and suggestions displayed | Passed |
| TC015 | Refresh homepage | Page reloads correctly | Homepage refreshed successfully | Passed |
