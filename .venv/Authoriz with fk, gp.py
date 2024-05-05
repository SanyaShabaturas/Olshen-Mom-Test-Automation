import datetime
import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import (Service)
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.service = Service(executable_path='./chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.url = "https://olshen-mom.com.ua/"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    @classmethod
    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

class Test_Olshen_Mom_site(BaseTest):
    def test_authorize_fk(self):
        button_register = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_register.click()
        button_fb = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[class*='icon--fb']")))
        button_fb.click()
        new_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
        text_name = self.driver.find_element(By.CSS_SELECTOR, "i[class*='fb_logo']")
        text_name_assert = text_name.text
        Expected_result = "Facebook"
        time.sleep(2)
        assert text_name_assert == Expected_result, f"we looked for the '{Expected_result}' but we found '{text_name_assert}'"

    def test_authorize_google(self):
        button_register2 = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_register2.click()
        button_gp = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[class*='icon--gp']")))
        button_gp.click()
        new_window_handle1 = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window_handle1)
        url_googl = self.driver.current_url
        Exprcted_domain = "accounts.google.com"
        self.assertTrue(Exprcted_domain in url_googl), f"'{Exprcted_domain}'not contained in '{url_googl}'"

if __name__ == "__main__":
        suite = unittest.TestSuite()
        suite.addTest(Test_Olshen_Mom_site('test_authorize_fk'))
        suite.addTest(Test_Olshen_Mom_site('test_authorize_google'))

        runner = unittest.TextTestRunner()
        runner.run(suite)
        # unittest.main()




