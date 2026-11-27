"""Negative tests — TC-14 to TC-15."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base import BASE_URL, EthereumTestCase


class TestNegative(EthereumTestCase):
    def test_tc14_404_page(self):
        """TC-14: unknown URL shows the 'Page not found' page.

        Verified live: title 'Page not found', H1 "We couldn't find that page".
        """
        self.driver.get(BASE_URL + "/this-page-does-not-exist-xyz/")
        WebDriverWait(self.driver, 15).until(EC.title_is("Page not found"))
        self.assertEqual(self.driver.title, "Page not found")
        h1 = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1.text, "We couldn't find that page")

    def test_tc15_missing_element_returns_empty(self):
        """TC-15: searching for a non-existent element returns an empty list
        (no exception) — correct 'not found' handling."""
        self.driver.get(BASE_URL)
        found = self.driver.find_elements(By.ID, "no-such-element-xyz")
        self.assertEqual(found, [])
