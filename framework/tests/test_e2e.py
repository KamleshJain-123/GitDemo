import pytest
import time

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.utilities.BaseClass import BaseClass


class testOne(BaseClass):
        def __init__(self):
                self.driver = None

        def test_e2e(self):
                # //a[@href='/angularpractice/shop'] , //a[contains(@href,'shop')] ,a[href*= 'shop']
                self.driver.find_element(By.CSS_SELECTOR, "a[href*= 'shop']").click()
                # find products in elements , chaining
                products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
                for product in products:
                        productName = product.find_element(By.XPATH, "div/h4/a").text
                        if productName == "Blackberry":
                                product.find_element(By.XPATH, "div/button").click()
                self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
                self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
                self.driver.find_element(By.ID, "country").send_keys("India")
                # use Explicit wait
                wait = WebDriverWait(self.driver, 10)
                wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
                self.driver.find_element(By.LINK_TEXT, "India").click()
                self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
                self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
                success_message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
                print(success_message)
                assert "Success" in success_message, "message content has changed "

                time.sleep(5)
