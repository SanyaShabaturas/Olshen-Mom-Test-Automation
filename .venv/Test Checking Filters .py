import datetime
import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import (Service)
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://olshen-mom.com.ua/"
driver.get(url)
driver.maximize_window()

for_pregnant_nursing_mothers = driver.find_element(By.XPATH, "//span[@class='productsMenu-submenu-t']")
actions = ActionChains(driver)
actions.move_to_element(for_pregnant_nursing_mothers).perform()
print("Place the cursor on the inscription 'For pregnant and nursing mothers'")

Sets_for_the_maternity_hospital = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='productsMenu-submenu-t']")))
Sets_for_the_maternity_hospital.click()
print("Click on the filter 'Sets for the maternity hospital'")

Sets_for_the_maternity_hospital_text = "Комплекти до пологового будинку"
text_test_sets = driver.find_element(By.XPATH, "//*[@id='j-catalog-header']")
value_text_test_sets = text_test_sets.text
assert value_text_test_sets == Sets_for_the_maternity_hospital_text, f"The test failed, here's what it found {value_text_test_sets}"

filter_popular = driver.find_element(By.CSS_SELECTOR, "div[class*=catalog-sorting__selected]")
actions = ActionChains(driver)
actions.move_to_element(filter_popular).perform()
print("Hover over the set filter")

popular = driver.find_element(By.CSS_SELECTOR, "span[class*='catalog-sorting__item']")
popular.click()
print("Click on 'By popularity'")
popular_text = "за популярністю"
value_popular = popular.text
assert value_popular == popular_text, f"The test failed, here's what it found {value_popular}"
print("Open filter 'for popularity'")

Size_chart_action = driver.find_element(By.XPATH, "//div[@class='filter__name j-filter-dropdown-trigger' and contains(text(), 'Розмірна сітка')]")
actions = ActionChains(driver)
actions.move_to_element(Size_chart_action).perform()
print("Hover over the 'Dimensional Grid' filter")
Size_chart = driver.find_element(By.XPATH, "//span[@class='checkbox-text' and contains(text(), '50-52')]")
Size_chart.click()
print("Select size '50-52'")

Expected_result = WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.XPATH, "//h1[@id='j-catalog-header']"), 'Комплекти до пологового будинку Розмірна сітка: 50-52'))
print(f"{Expected_result} - is result test")

time.sleep(1)
# while True:
#     pass

