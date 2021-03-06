# Import the 'modules' that are required for execution for Selenium test automation

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


@pytest.mark.usefixtures("driver_init","app_url")
class BasicTest:
    pass

class Test_URL_Chrome(BasicTest):
    def test_open_url(self,app_url):
        # Step 2) Navigate to OrangeHRM
        self.driver.get(app_url)
        # Step 3) Enter the Username & Enter Password
        username = self.driver.find_element_by_name("txtUsername")
        password = self.driver.find_element_by_name("txtPassword")
        submit = self.driver.find_element_by_name("Submit")
        username.send_keys("Admin")
        password.send_keys("admin123")
        # Step 4) Click Login
        submit.click()
        time.sleep(3)
        #Logout from application
        self.driver.find_element_by_id("welcome").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)