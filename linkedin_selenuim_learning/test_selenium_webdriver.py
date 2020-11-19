import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestLinkedin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()  ### you can use any of the browser to start the testing-Chrome,Safari

    # def tearDown(self):
    #     self.driver.close()

    def test_01_03(self):
        self.driver.get("http://google.com")
        self.assertEqual("Google", self.driver.title)

        query_box=self.driver.find_element_by_name('q')

        query_box.send_keys("Hello WebDriver!")
        query_box.send_keys(Keys.ENTER)

    def test_login(self):
        self.driver.get("https://selenium-blog.herokuapp.com/signup")
        self.assertEqual("AlphaBlog", self.driver.title)

        ts=time.time()
        user_name= f"Test@22 {ts}"
        username_box=self.driver.find_element_by_id("user_username")
        username_box.send_keys(user_name)

        email= f"{ts}test@sgintl.com"
        email_box=self.driver.find_element_by_id("user_email")
        email_box.send_keys(email)

        password_box=self.driver.find_element_by_id("user_password")
        password_box.send_keys("Test123!")

        signup_button=self.driver.find_element_by_id("submit")
        signup_button.click()

        banner_box=self.driver.find_element_by_id('flash_success')

        self.assertEqual("Welcome to the alpha blog " + user_name, banner_box.text)

    def test_create_article(self):
        ''''
        this test creates new article for the Selenium blog page after being able
        to successfully login to the this page from the above test
         '''

