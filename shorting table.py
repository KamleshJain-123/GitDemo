import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#take browser shorted list
browser_shorted_list = []
browser_shorted = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
for product in browser_shorted:
    browser_shorted_list.append(product.text)
#copy orignal sorted lis
original_browser_shorted_list = browser_shorted_list.copy()
print("original_browser_shorted_list", original_browser_shorted_list)
# browser_shorted_list sort through sort() function
browser_shorted_list.sort()
print("browser_shorted_list", browser_shorted_list)

# very through assertion browser_shorted_list and original_browser_shorted_list equal or not
assert browser_shorted_list == original_browser_shorted_list
time.sleep(5)