# Web3 QA Test Cases

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC001 | Open homepage | Homepage loads | Homepage loaded normally; title, navigation, search, language selector and main content visible | Passed |
| TC002 | Check navigation | Links work correctly | Learn, Use and Build navigation links opened their intended pages; URLs and content were correct, with no visible errors | Passed |
| TC003 | Refresh page | Page reloads correctly | Homepage refreshed successfully and content remained visible without errors | Passed |
| TC004 | Navigate back from Learn page | Browser back button returns the user to the homepage | Browser back button successfully returned to the homepage from the Learn page | Passed |
| TC005 | Open mobile layout | Mobile viewport displays content correctly | Not tested — browser limitation | Blocked |

| TC006 | Check page title | Correct title displayed | Page title remained consistent and displayed correctly as "Ethereum - The complete guide from ethereum.org" | Passed |
| TC007 | Check external links | Links open correct destinations | External link opened the correct destination successfully | Passed |
| TC008 | Navigate between pages | Pages load correctly | Research page opened and displayed normally | Passed |
| TC009 | Check browser back button | Previous page is restored | Browser returned to the previous page successfully | Passed |
| TC010 | UI elements display consistently | Header and navigation are consistent across Home, Learn and Research | Consistent appearance observed | Passed |
| TC011 | Search for a known topic | Search returns a relevant result for a valid topic | Searching for "Ethereum" generated an AI answer with source references | Passed |
| TC012 | Check valid input | Search returns relevant results | Smart Contracts generated a relevant AI answer | Passed |
| TC013 | Check duplicate submission | Duplicate searches are handled correctly | Repeated Ethereum search returned results normally | Passed |
| TC014 | Check loading indicator | Loading state is visible when needed | Loading indicator appeared before search results | Passed |
| TC015 | Check error messages | Errors are understandable and recoverable | No results message and alternative search suggestions displayed | Passed |
