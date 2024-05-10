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
        self.wait = WebDriverWait(self.driver, 10)
        self.fake = Faker()



    @classmethod
    def tearDown(self):
        self.driver.quit()

class filter_for_regnant_and_nursing_mothers(auto_values):
    def test_1_sets_for_the_maternity_hospital(self):
        filter_for_regnant_and_nursing = self.driver.find_element(
            By.CSS_SELECTOR, "a[class*='products'][href*='/dlia-v']")
        action = ActionChains(self.driver)
        action.move_to_element(filter_for_regnant_and_nursing).perform()
        filter_for_maternity_kits = self.driver.find_element(
            By.XPATH, "//span[contains(@class,'products') and contains(text(), 'пологового')]")
        filter_for_maternity_kits.click()
        check_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "h1[class*='main-h']")))
        check_text_assert = check_text.text
        assert_1 = "Комплекти до пологового будинку"
        assert check_text_assert == assert_1, f"expected {assert_1} got {check_text_assert}"
        print("filter_for_regnant_and_nursing_mothers", {check_text_assert})

    def test_2_sets_for_newborns(self):
        filter_sets_for_newborns = self.driver.find_element(
            By.CSS_SELECTOR, "a[class*='products'][href*='/dlia-n']")
        action = ActionChains(self.driver)
        action.move_to_element(filter_sets_for_newborns).perform()
        filter_swaddles = self.driver.find_element(
            By.XPATH, "//span[contains(@class, 'products')and contains(text(), 'Пелюшки')]")
        filter_swaddles.click()
        check_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "h1[id*='j-catalog']")))
        check_text_assert = check_text.text
        assert_2 = "Пелюшки"
        assert check_text_assert == assert_2, f"expected {assert_2} got {check_text_assert}"
        print("test_2_sets_for_newborns", {check_text_assert})

    def test_3_sets_for_kids(self):
        filter_sets_for_kids = self.driver.find_element(
            By.CSS_SELECTOR, "a[class*='products'][href*='/odiah']")
        action = ActionChains(self.driver)
        action.move_to_element(filter_sets_for_kids).perform()
        filter_suit = self.driver.find_element(
            By.XPATH, "//span[contains(@class, 'products')and contains(text(), 'Костюмчики ')]")
        filter_suit.click()
        check_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "h1[id*='j-catalog']")))
        check_text_assert = check_text.text
        assert_3 = "Костюмчики"
        assert check_text_assert == assert_3, f"expected {assert_3} got {check_text_assert}"
        print("test_3_sets_for_kids", {check_text_assert})

    def test_4_seasonal_sale(self):
        seasonal_sale_button = self.driver.find_element(
        By.CSS_SELECTOR, "a[class*='products'][href*='kataloh']")
        seasonal_sale_button.click()
        check_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "h1[class*='main-h']")))
        check_text_assert = check_text.text
        assert_4 = "Каталог Розпродаж"
        assert check_text_assert == assert_4, f"expected {assert_4} got {check_text_assert}"
        print("test_4_seasonal_sale", {check_text_assert})

class input_search(auto_values):
    def test_5_filter_nursing_bra(self):
        input_search_click = self.driver.find_element(
            By.CSS_SELECTOR, "input[class*='search__input']")
        input_search_click.click()
        input_search_click.send_keys("Бюстгальтер для годування")
        time.sleep(1)
        input_search_click.send_keys(Keys.ENTER)
        check_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "h1[id*='j-catalog-header']")))
        check_text_assert = check_text.text
        assert_5 = "Результати пошуку «Бюстгальтер для годування»"
        assert check_text_assert == assert_5, f"expected {assert_5} got {check_text_assert}"
        print("test_5_seasonal_sale", {check_text_assert})

    def test_6_language(self):
        button_language = self.driver.find_element(
            By.CSS_SELECTOR, "div[class*='lang-menu__button']")
        action = ActionChains(self.driver)
        action.move_to_element(button_language).perform()
        button_language = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "a[href='/ru/']")))
        button_language.click()
        check_text = self.driver.find_element(By.CSS_SELECTOR, "div[class*='h2']")
        check_text_assert = check_text.text
        assert_6 = "Популярные категории"
        assert check_text_assert == assert_6, f"expected {assert_6} got {check_text_assert}"
        print("test_6_seasonal_sale (expected ru - language) - ", {check_text_assert})










if __name__ == "__main__":
        suite = unittest.TestSuite()
        suite.addTest(filter_for_regnant_and_nursing_mothers('test_1_sets_for_the_maternity_hospital'))
        suite.addTest(filter_for_regnant_and_nursing_mothers('test_2_sets_for_newborns'))
        suite.addTest(filter_for_regnant_and_nursing_mothers('test_3_sets_for_kids'))
        suite.addTest(filter_for_regnant_and_nursing_mothers('test_4_seasonal_sale'))
        suite.addTest(input_search('test_5_filter_nursing_bra'))
        suite.addTest(input_search('test_6_language'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

# if __name__ == "__main__":
#     unittest.main()

