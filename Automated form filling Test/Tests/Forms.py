import time

import HtmlTestRunner
from selenium import webdriver
import unittest
from Project_05.Pages.test_Pages import TestPages
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class TestForms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/jackdaniel/PycharmProjects/selenium/Project_05/Driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_form_filling(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form/")

        homepage = TestPages(driver)
        homepage.enter_firstname("A")
        homepage.enter_last_name("Daniel")
        homepage.enter_email("daniel@gmail.com")
        homepage.click_gender()
        homepage.enter_mobile_number("8946087040")
        homepage.click_date()
        homepage.click_hobbies()
        homepage.enter_address("rc-street Ramagiri")
        homepage.click_submit()
        homepage.click_close()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/home/jackdaniel/PycharmProjects/selenium/Project_05/Reports"))
