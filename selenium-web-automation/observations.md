# Observations — Project 04 (ethereum.org, Selenium)

Date: 27 Nov 2026. Target: `https://ethereum.org`.
No site defects were found. The items below are things the test runs taught
me about the site and the environment — each one corrected a wrong assumption
in my own tests.

## OBS-01 — The page has two search toggle buttons; only one is visible

- **Test cases:** TC-04, TC-12
- **Observed:** `document` contains two buttons with
  `aria-label='Toggle search button'` (desktop + mobile variants). At desktop
  width (1280px) the first match in the DOM is hidden (`is_displayed()` is
  false), so asserting on the first match fails and waiting for it to become
  clickable times out.
- **Fix:** collect all matching buttons and use the one that is displayed.
- **Lesson:** with responsive sites, never assume a locator matches exactly
  one visible element — check visibility across all matches.

## OBS-02 — Footer click needs a real scroll into view

- **Test case:** TC-11
- **Observed:** a plain `scrollIntoView({block: 'center'})` + `click()` on the
  footer link threw `ElementClickInterceptedException` — the element sits near
  the bottom of a ~8,000 px page and the click point was outside the viewport.
- **Fix:** `ActionChains.move_to_element(link).click()` — moves to the element
  (scrolling it into view) and clicks in one action.
- **Lesson:** for elements far down a long page, drive the scroll through the
  same action chain as the click.

## OBS-03 — The footer links out to several official Ethereum properties

- **Test case:** TC-13
- **Observed:** the footer does not stay on ethereum.org. Across runs 1–4 it
  linked to `blog.ethereum.org`, `esp.ethereum.foundation`, `devcon.org`, and
  a `mailto:press@ethereum.org` address — all legitimate official Ethereum
  destinations. Each run exposed one more, because my expectation kept
  assuming "same domain".
- **Fix:** the final expectation is that every footer link with text has a
  valid `https://` href, or a well-formed `mailto:` address.
- **Lesson:** do not write an allowlist from assumption — probe the real
  destinations first, or assert the property that actually matters (valid href).

## OBS-04 — System pip cannot install Selenium on this VM

- **Observed:** `pip install selenium` (system pip) fails with
  `ERROR: Cannot uninstall urllib3 2.0.7, RECORD file not found` — urllib3 is
  a Debian-managed package and pip cannot upgrade it in place.
- **Fix:** install into a venv (`python3 -m venv venv`, then
  `venv/bin/pip install selenium`). Selenium 4.54.0 installed cleanly there.
- **Lesson:** on Debian-based systems, always use a venv for Python test
  dependencies instead of fighting the system packages.

## Environment notes

- Headless Chrome needs `--ignore-certificate-errors` on this VM because the
  egress proxy does MITM on TLS, plus the usual `--no-sandbox`,
  `--disable-dev-shm-usage`, and `--proxy-server=http://127.0.0.1:8899` flags.
- Page loads through the proxy take 1–7 s each; the suite total is ~47 s for
  15 tests. Explicit waits (up to 15 s) are used instead of fixed sleeps.
