import datetime
import random
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
        self.wait = WebDriverWait(self.driver, 5)
        self.fake = Faker()
        self.random_email = self.fake.email()
        self.random_name = self.fake.name()
        self.random_last_name = self.fake.last_name()


    @classmethod
    def tearDown(self):
        self.driver.quit()

class Password_value_tests(auto_values):
    def test_1_register_user_with_valid_data(self):
        self.random_email = self.fake.email()
        self.random_password = self.fake.password(length=8)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[starts-with(text(), 'Реєстрація')]")))
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
        print("test_1_register_user_with_valid_data", {expected_result})
        assert factual_error_text == expected_result, f"expected {expected_result} and got this {factual_error_text}"

    def test_2_register_user_with_invalid_email(self):
        self.random_email = self.fake.email().replace('@', '@@')
        self.random_password = self.fake.password(length=8)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[starts-with(text(), 'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[title]']")
        input_name.send_keys(self.random_name, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password)
        input_password.send_keys(Keys.RETURN)
        factual_error_lok = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=form-error-box]")))
        factual_error = factual_error_lok.text
        expected_error = "Некоректна адреса електронної пошти"
        print("test_2_register_user_with_invalid_email", {expected_error})
        assert expected_error == factual_error, f"expected {expected_error} and got this {factual_error}"

    def test_3_register_user_with_invalid_password(self):
        self.random_email = self.fake.email()
        self.random_password = self.fake.password(length=8)
        self.random_password_with_space = ' ' + self.random_password
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[starts-with(text(), 'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[title]']")
        input_name.send_keys(self.random_name, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password_with_space)
        input_password.send_keys(Keys.RETURN)
        factual_error_lok = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=form-error-box]")))
        factual_error = factual_error_lok.text
        expected_error = "Пароль не повинен містити пробіли"
        print("test_3_register_user_with_invalid_password", {expected_error})
        assert expected_error == factual_error, f"expected {expected_error} and got this {factual_error}"

    def test_4_register_user_with_invalid_password_and_email(self):
        self.random_email = self.fake.email().replace('@', '@@')
        self.random_password = self.fake.password(length=8)
        self.random_password_with_space = ' ' + self.random_password
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[starts-with(text(), 'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[title]']")
        input_name.send_keys(self.random_name, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password_with_space)
        input_password.send_keys(Keys.RETURN)
        factual_error_lok = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[starts-with(text(), 'Пароль')]")))
        factual_error = factual_error_lok.text
        expected_error = "Пароль не повинен містити пробіли"
        assert expected_error == factual_error, f"expected {expected_error} and got this {factual_error}"
        factual_error_lok1 = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[starts-with(text(), 'Некоректна')]")))
        factual_error1 = factual_error_lok1.text
        expected_error2 = "Некоректна адреса електронної пошти"
        print("test_4_register_user_with_invalid_password_and_email", {factual_error}, {expected_error2})
        assert expected_error2 == factual_error1, f"expected {expected_error2} and got this {factual_error1}"

    def test_5_register_user_with_invalid_name(self):
        self.random_name = self.fake.name()
        invalid_chars = '#'
        invalid_char = random.choice(invalid_chars)
        self.random_name_with_invalid_char = self.random_name + invalid_char
        self.random_password = self.fake.password(length=8)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class,'login-tabs-txt') and contains(text(),'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='user[title]']")
        input_name.send_keys(self.random_name_with_invalid_char, self.random_last_name)
        input_name.send_keys(Keys.RETURN)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password)
        input_password.send_keys(Keys.RETURN)
        factual_error = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[class*=form-error-box]")))
        factual_error_text = factual_error.text
        expected_result = "Ви ввели недопустимі символи"
        print("test_5_register_user_with_invalid_name", {expected_result})
        assert factual_error_text == expected_result, f"expected {expected_result} and got this {factual_error_text}"

    def test_6_register_user_with_invalid_name_and_password(self):
        self.random_name = self.fake.name()
        invalid_chars = '#'
        invalid_char = random.choice(invalid_chars)
        self.random_name_with_invalid_char = self.random_name + invalid_char
        self.random_password = self.fake.password(length=6)
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[starts-with(text(), 'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='user[title]']")
        input_name.send_keys(self.random_name_with_invalid_char, self.random_last_name)
        input_name.send_keys(Keys.RETURN)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password)
        input_password.send_keys(Keys.RETURN)
        factual_error_name = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[class*=form-error-box]")))
        factual_1_error_text = factual_error_name.text
        expected_result_1 = "Ви ввели недопустимі символи"
        factual_error_password = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[starts-with(text(), 'Довжина')]")))
        factual_2_error_text = factual_error_password.text
        print("test_6_register_user_with_invalid_name_and_password", {factual_2_error_text}, {factual_1_error_text})
        assert expected_result_1 == factual_1_error_text, f"expected {expected_result_1} and got this {factual_error_text}"

    def test_7_register_user_with_invalid_name_and_password_and_email(self):
        self.random_name = self.fake.name()
        invalid_chars = '#'
        invalid_char = random.choice(invalid_chars)
        self.random_name_invalid = self.random_name + invalid_char
        self.random_password_invalid = self.fake.password(length=6)
        self.random_email_invalid = self.fake.email().replace('@', '@@')
        button_authorization = self.driver.find_element(By.CSS_SELECTOR, "svg[class*='icon--user']")
        button_authorization.click()
        button_register = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[starts-with(text(), 'Реєстрація')]")))
        button_register.click()
        input_name = self.driver.find_element(By.XPATH, "//input[@type='text' and @name='user[title]']")
        input_name.send_keys(self.random_name_invalid, self.random_last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='user[email]']")
        input_email.send_keys(self.random_email_invalid)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='signup-form']/dl/dd[3]/input")
        input_password.send_keys(self.random_password_invalid)
        input_password.send_keys(Keys.RETURN)
        factual_error_name = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[class*=form-error-box]")))
        factual_1_error_name = factual_error_name.text
        expected_result_1 = "Ви ввели недопустимі символи"
        factual_error_password = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[starts-with(text(), 'Довжина')]")))
        factual_2_error_pass = factual_error_password.text
        factual_error_email = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[starts-with(text(), 'Некоректна')]")))
        factual_error_email_text = factual_error_email.text
        print("test_7_register_user_with_invalid_name_and_password_and_email", {factual_2_error_pass}, {factual_1_error_name}, {factual_error_email_text})
        assert expected_result_1 == factual_1_error_name, f"expected {expected_result_1} and got this {factual_1_error_name}"










if __name__ == "__main__":
        suite = unittest.TestSuite()
        suite.addTest(Password_value_tests('test_1_register_user_with_valid_data'))
        suite.addTest(Password_value_tests('test_2_register_user_with_invalid_email'))
        suite.addTest(Password_value_tests('test_3_register_user_with_invalid_password'))
        suite.addTest(Password_value_tests('test_4_register_user_with_invalid_password_and_email'))
        suite.addTest(Password_value_tests('test_5_register_user_with_invalid_name'))
        suite.addTest(Password_value_tests('test_6_register_user_with_invalid_name_and_password'))
        suite.addTest(Password_value_tests('test_7_register_user_with_invalid_name_and_password_and_email'))
        runner = unittest.TextTestRunner()
        runner.run(suite)

# if __name__ == "__main__":
#     unittest.main()

