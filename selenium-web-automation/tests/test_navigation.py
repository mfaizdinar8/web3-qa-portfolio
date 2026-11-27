"""Navigation tests — TC-06 to TC-10."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base import BASE_URL, EthereumTestCase


class TestNavigation(EthereumTestCase):
    def _open_and_check_h1(self, path):
        self.driver.get(BASE_URL + path)
        self.assertTrue(self.driver.current_url.startswith(BASE_URL + path))
        h1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertTrue(h1.text.strip(), "H1 must not be empty")

    def test_tc06_learn_page_loads(self):
        """TC-06: /learn/ loads with a non-empty H1."""
        self._open_and_check_h1("/learn/")

    def test_tc07_developers_page_loads(self):
        """TC-07: /developers/ loads with a non-empty H1."""
        self._open_and_check_h1("/developers/")

    def test_tc08_what_is_ethereum_page_loads(self):
        """TC-08: /what-is-ethereum/ loads with a non-empty H1."""
        self._open_and_check_h1("/what-is-ethereum/")

    def test_tc09_browser_back_returns_home(self):
        """TC-09: browser Back from /learn/ returns to the homepage."""
        self.driver.get(BASE_URL)
        self.driver.get(BASE_URL + "/learn/")
        self.driver.back()
        WebDriverWait(self.driver, 15).until(EC.url_to_be(BASE_URL + "/"))
        self.assertEqual(self.driver.current_url, BASE_URL + "/")

    def test_tc10_refresh_keeps_homepage(self):
        """TC-10: refreshing the homepage keeps the Ethereum title."""
        self.driver.get(BASE_URL)
        self.driver.refresh()
        WebDriverWait(self.driver, 15).until(EC.title_contains("Ethereum"))
        self.assertIn("Ethereum", self.driver.title)
