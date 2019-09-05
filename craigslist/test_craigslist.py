import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCraigslist(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        SEARCH_CRITERIA="ford"
        self.driver.get("https://atlanta.craigslist.org")
        self.assertEqual("craigslist: atlanta, GA jobs, apartments, for sale, services, community, and events",
                         self.driver.title)
        query_box=self.driver.find_element_by_id("query")
        query_box.send_keys(SEARCH_CRITERIA)
        query_box.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.title_is(f'atlanta for sale "{SEARCH_CRITERIA}" - craigslist')
        )


if __name__ == '__main__':
    unittest.main()
