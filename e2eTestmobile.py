import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class testOne:

    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # //a[@href='/angularpractice/shop'] , //a[contains(@href,'shop')] ,a[href*= 'shop']
    driver.find_element(By.CSS_SELECTOR, "a[href*= 'shop']").click()
    #find products in elements , chaining
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for product in products:
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("India")
    # use Explicit wait
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(success_message)
    assert "Success" in success_message, "message content has changed "

    time.sleep(5)
    driver.close()

    print("this is github commit example 1")
    print("this is github commit example 2")
