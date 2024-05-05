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
from faker import Faker
from selenium.webdriver import Keys

class auto_values(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.service = Service(executable_path='./chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.url = "https://olshen-mom.com.ua/"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.fake = Faker()
        self.random_email = self.fake.email()
        self.random_name = self.fake.name()
        self.random_last_name = self.fake.last_name()

    @classmethod
    def tearDown(self):
        self.driver.quit()

class Password_value_tests(auto_values):
    def test_password_7_characters_long(self):
        self.random_password = self.fake.password(length=7)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class,'login-tabs-txt') and contains(text(),'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='user[title]']")
        input_name.send_keys(self.random_name, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password)
        input_password.send_keys(Keys.RETURN)
        factual_error_lok = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='signup-form']/dl/dd[3]/div/div")))
        factual_error = factual_error_lok.text
        expected_error = "Довжина пароля повинна бути не менше 8 і не більше 15 символів."
        assert expected_error == factual_error, f"expected {expected_error} and got this {factual_error}"

    def test_password_8_characters_long(self):
        self.random_password = self.fake.password(length=8)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class,'login-tabs-txt') and contains(text(),'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='user[title]']")
        input_name.send_keys(self.random_name, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password)
        input_password.send_keys(Keys.RETURN)
        factual_error = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Дякуємо') and contains(@class, 'popup-title')]")))
        factual_error_text = factual_error.text
        expected_result = "Дякуємо за реєстрацію"
        assert factual_error_text == expected_result, f"expected {expected_result} and got this {factual_error_text}"

    def test_password_15_characters_long(self):
        self.random_password = self.fake.password(length=15)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class,'login-tabs-txt') and contains(text(),'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='user[title]']")
        input_name.send_keys(self.random_name, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password)
        input_password.send_keys(Keys.RETURN)
        factual_error = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Дякуємо') and contains(@class, 'popup-title')]")))
        factual_error_text = factual_error.text
        expected_result = "Дякуємо за реєстрацію"
        assert factual_error_text == expected_result, f"expected {expected_result} and got this {factual_error_text}"

    def test_password_16_characters_long(self):
        self.random_password = self.fake.password(length=16)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class,'login-tabs-txt') and contains(text(),'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='user[title]']")
        input_name.send_keys(self.random_name, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password)
        input_password.send_keys(Keys.RETURN)
        factual_error_lok = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='signup-form']/dl/dd[3]/div/div")))
        factual_error = factual_error_lok.text
        expected_error = "Довжина пароля повинна бути не менше 8 і не більше 15 символів."
        assert expected_error == factual_error, f"expected {expected_error} and got this {factual_error}"





if __name__ == "__main__":
    unittest.main()

