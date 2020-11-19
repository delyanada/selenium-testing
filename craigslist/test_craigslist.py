import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from weblib.selenium_tools import click

SEARCH_CRITERIA="ford"


class TestCraigslist(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_main_search_box(self):
        """ Testing basic search"""

        self.driver.get("https://atlanta.craigslist.org")
        self.assertEqual("craigslist: atlanta, GA jobs, apartments, for sale, services, community, and events",
                         self.driver.title)
        query_box=self.driver.find_element_by_id("query")
        query_box.send_keys(SEARCH_CRITERIA)
        query_box.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.title_is(f'atlanta for sale "{SEARCH_CRITERIA}" - craigslist')
        )
    #
    # def test_search_additional_criteria(self):
    #     PRICE=5000
    #
    #     self.driver.get("https://atlanta.craigslist.org")
    #     query_box=self.driver.find_element_by_id("query")
    #     query_box.send_keys(SEARCH_CRITERIA)
    #     query_box.send_keys(Keys.ENTER)
    #     WebDriverWait(self.driver, 10).until(
    #         EC.title_is(f'atlanta for sale "{SEARCH_CRITERIA}" - craigslist'))
    #
    #     price_box = self.driver.find_element_by_name("max_price")
    #     price_box = WebDriverWait(self.driver,10).until(
    #         EC.element_to_be_clickable((By.NAME, "max_price"))
    #     )
    #
    #     price_box.send_keys(PRICE)
    #     price_box.send_keys(Keys.ENTER)
    #
    #     url= f"/search/cta?auto_make_model={SEARCH_CRITERIA}&hints=makemodel&max_price={PRICE}"
    #
    #     WebDriverWait(self.driver,10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//a[@href="' + url + '"]'))
    #     )
    #
    #     model_box = WebDriverWait(self.driver,10).until(
    #         EC.element_to_be_clickable((By.NAME, "max_auto_year"))
    #     )
    #     model_box.send_keys(2005)
    #     model_box.send_keys(Keys.ENTER)
    #
    #     miles_box = WebDriverWait(self.driver,10).until(
    #         EC.element_to_be_clickable((By.NAME, "max_auto_miles"))
    #     )
    #     miles_box.send_keys(70000)
    #     miles_box.send_keys(Keys.ENTER)
    #     self.driver.refresh()
    #     check_box = WebDriverWait(self.driver,10).until(
    #         EC.element_to_be_clickable((By.NAME, "srchType"))
    #     )
    #     check_box.click()


if __name__ == '__main__':
    unittest.main()
