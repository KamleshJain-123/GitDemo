import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
action.context_click(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
driver.find_element(By.LINK_TEXT, "Reload").click()


time.sleep(5)



