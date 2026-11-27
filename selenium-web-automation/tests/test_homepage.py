"""Homepage tests — TC-01 to TC-05. All values verified live on 27 Nov 2026."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base import BASE_URL, EthereumTestCase


class TestHomepage(EthereumTestCase):
    def test_tc01_title_contains_ethereum(self):
        """TC-01: homepage title contains 'Ethereum'."""
        self.driver.get(BASE_URL)
        self.assertIn("Ethereum", self.driver.title)

    def test_tc02_h1_text(self):
        """TC-02: homepage H1 is 'The internet that belongs to you'."""
        self.driver.get(BASE_URL)
        h1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertEqual(h1.text, "The internet that belongs to you")

    def test_tc03_html_lang_is_en(self):
        """TC-03: page language is English (html lang='en')."""
        self.driver.get(BASE_URL)
        lang = self.driver.find_element(By.TAG_NAME, "html").get_attribute("lang")
        self.assertEqual(lang, "en")

    def test_tc04_search_toggle_present(self):
        """TC-04: at least one search toggle button is present and visible.

        The page ships two toggle buttons (desktop + mobile); only the one
        matching the current viewport is displayed, so we check all of them.
        """
        self.driver.get(BASE_URL)
        btns = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[aria-label='Toggle search button']")
            )
        )
        visible = [b for b in btns if b.is_displayed()]
        self.assertGreaterEqual(
            len(visible), 1, "expected >= 1 visible search toggle button"
        )

    def test_tc05_footer_learn_hub_link(self):
        """TC-05: footer contains a 'Learn hub' link to /learn/."""
        self.driver.get(BASE_URL)
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        link = footer.find_element(By.LINK_TEXT, "Learn hub")
        self.assertEqual(link.get_attribute("href"), BASE_URL + "/learn/")
