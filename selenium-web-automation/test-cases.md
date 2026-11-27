# Test Cases — Project 04 (ethereum.org, Selenium)

Target: `https://ethereum.org`
Tool: Python 3.12.3 + Selenium 4.54.0, headless Chrome 157.
Runner: `run_tests.py` (unittest). Each test case is one test method; file
locations are in `tests/`.

## Homepage (test_homepage.py)

| ID | Action | Expected result |
| --- | --- | --- |
| TC-01 | Open `/` | Title contains "Ethereum" |
| TC-02 | Open `/` | H1 text is "The internet that belongs to you" |
| TC-03 | Open `/` | `html lang` attribute is "en" |
| TC-04 | Open `/` | At least one search toggle button (`aria-label='Toggle search button'`) is visible |
| TC-05 | Open `/` | Footer contains a "Learn hub" link to `https://ethereum.org/learn/` |

## Navigation (test_navigation.py)

| ID | Action | Expected result |
| --- | --- | --- |
| TC-06 | Open `/learn/` | URL starts with `https://ethereum.org/learn/`; H1 present and non-empty |
| TC-07 | Open `/developers/` | URL starts with `https://ethereum.org/developers/`; H1 present and non-empty |
| TC-08 | Open `/what-is-ethereum/` | URL starts with `https://ethereum.org/what-is-ethereum/`; H1 present and non-empty |
| TC-09 | Open `/`, open `/learn/`, browser Back | URL returns to `https://ethereum.org/` |
| TC-10 | Open `/`, refresh | Title still contains "Ethereum" |

## Interaction (test_interaction.py)

| ID | Action | Expected result |
| --- | --- | --- |
| TC-11 | Open `/`, click footer link "What is Ethereum?" | Lands on `https://ethereum.org/what-is-ethereum/` |
| TC-12 | Open `/`, click visible search toggle, type "staking" | At least 1 search result link containing "staking" appears |
| TC-13 | Open `/`, read all footer links with text | >= 5 links; every href is a valid `https://` URL, or a well-formed `mailto:` address |

## Negative (test_negative.py)

| ID | Action | Expected result |
| --- | --- | --- |
| TC-14 | Open `/this-page-does-not-exist-xyz/` | Title is "Page not found"; H1 is "We couldn't find that page" |
| TC-15 | Open `/`, search for element id `no-such-element-xyz` | `find_elements` returns an empty list (no exception) |

## Coverage

- Homepage: 5 cases (TC-01–05)
- Navigation: 5 cases (TC-06–10)
- Interaction: 3 cases (TC-11–13)
- Negative: 2 cases (TC-14–15)
- Total: **15 test cases**
- Locators used: tag name, CSS selector, link text, XPath, aria-label
- Interactions: navigation, Back, refresh, click, text input, explicit waits
