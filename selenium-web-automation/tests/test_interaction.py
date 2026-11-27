"""Interaction tests — TC-11 to TC-13 (clicks, search, link validation)."""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base import BASE_URL, EthereumTestCase


class TestInteraction(EthereumTestCase):
    def test_tc11_click_footer_what_is_ethereum(self):
        """TC-11: clicking the footer 'What is Ethereum?' link lands on /what-is-ethereum/."""
        self.driver.get(BASE_URL)
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        link = footer.find_element(By.LINK_TEXT, "What is Ethereum?")
        ActionChains(self.driver).move_to_element(link).click().perform()
        WebDriverWait(self.driver, 15).until(
            EC.url_to_be(BASE_URL + "/what-is-ethereum/")
        )
        self.assertEqual(
            self.driver.current_url, BASE_URL + "/what-is-ethereum/"
        )

    def test_tc12_search_for_staking(self):
        """TC-12: site search for 'staking' shows at least one matching result.

        The page ships two toggle buttons (desktop + mobile); only the one
        matching the current viewport is displayed, so we click the visible one.
        """
        self.driver.get(BASE_URL)
        toggles = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[aria-label='Toggle search button']")
            )
        )
        visible = [t for t in toggles if t.is_displayed()]
        self.assertGreaterEqual(
            len(visible), 1, "expected >= 1 visible search toggle button"
        )
        visible[0].click()
        search_input = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "input[type='search'], input[placeholder*='Search' i]",
                )
            )
        )
        search_input.send_keys("staking")
        results = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    " 'abcdefghijklmnopqrstuvwxyz'), 'staking')]",
                )
            )
        )
        self.assertGreaterEqual(len(results), 1, "expected >= 1 staking result")

    def test_tc13_footer_learn_links_valid(self):
        """TC-13: footer links (>= 5) all have a valid https href.

        Note: the live footer links out to several official Ethereum
        properties (ethereum.org, blog.ethereum.org, esp.ethereum.foundation,
        devcon.org), so the check is 'valid https href', not 'same domain'.
        """
        self.driver.get(BASE_URL)
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        links = [
            a for a in footer.find_elements(By.TAG_NAME, "a") if (a.text or "").strip()
        ]
        self.assertGreaterEqual(len(links), 5, "expected >= 5 footer links")
        for a in links:
            href = a.get_attribute("href") or ""
            if href.startswith("mailto:"):
                self.assertIn(
                    "@",
                    href,
                    f"footer link {a.text!r} has a malformed mailto href: {href!r}",
                )
            else:
                self.assertTrue(
                    href.startswith("https://"),
                    f"footer link {a.text!r} has no valid https href: {href!r}",
                )
