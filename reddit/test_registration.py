import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

class TestReddit(unittest.TestCase):

    def test_registration(self):
        self.driver.get("https://reddit.com")
        self.assertEqual("reddit: the front page of the internet", self.driver.title)

        sign_up_link=self.driver.find_element_by_xpath("//a[contains(text(), 'sign up')]")
        sign_up_link.click()

        self.driver.switch_to.frame(1)
        email_box=self.driver.find_element_by_id("regEmail")
        email_box.send_keys("foobar@gmail.com")
        next_button=self.driver.find_element_by_tag_name("button")
        next_button.click()

        username_box = self.driver.find_element_by_id("regUsername").click()
        ActionChains(self.driver).move_to_element(username_box).send_keys("warolide!%u5f6u")

        password_box = self.driver.find_element_by_id("regPassword").click()
        ActionChains(self.driver).move_to_element(password_box).send_keys("12Wejdokfme")

        self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".SignupButton").click()


    def setUp(self):
        self.driver=webdriver.Firefox()


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
