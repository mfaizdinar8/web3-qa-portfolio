"""Shared base for Project 04 Selenium tests (ethereum.org).

One headless Chrome per test class (RAM is tight on this VM).
Flags mirror the working smoke test: headless, no-sandbox, VM egress proxy,
ignore-certificate-errors (the proxy does MITM).
"""
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://ethereum.org"


def make_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-vulkan")
    options.add_argument("--disable-features=Vulkan")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--proxy-server=http://127.0.0.1:8899")
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(5)
    return driver


class EthereumTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
