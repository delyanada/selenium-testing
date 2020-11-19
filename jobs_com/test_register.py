"""
Testing registration on jobs.com.
Successful test with new user.
Failing.....
"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_register_new_user_bad_email(self):
        """ Invalid email format should fail registration """

        self.driver.get("https://www.kroger.com/signin")
        email_input=self.driver.find_element_by_id("SignIn-emailInput")
        email_input.send_keys("foobar.com")
        password_input=self.driver.find_element_by_id("SignIn-passwordInput")
        password_input.send_keys('didka123')
        submit_button=self.driver.find_element_by_id("SignIn-submitButton")
        submit_button.click()

        self.assertEqual("https://www.kroger.com/signin", self.driver.current_url)
        self.assertIsNone(self.driver.find_element_by_xpath("//span[text()='Please enter a valid email address']"))

