import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_option)
expected_products_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_products_list = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)
product_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(product_list)
assert count > 0
time.sleep(5)
# Items add to cart
for product in product_list:
    actual_products_list.append(product.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH, "div/button").click()
    time.sleep(5)
assert expected_products_list == actual_products_list, "actual_products_list and actual_products_list is not equal"
print(actual_products_list)

# go to cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#products price or summery page and calculate tptal price
actual_price = 0
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
for price in prices:
    act_price = float(price.text)
    actual_price = actual_price + act_price
# find expected price
expected_price = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
if actual_price == expected_price:
    print("actual_price == expected_price")
else:
    print("actual_price != expected_price")

assert actual_price == expected_price

#apply promocode
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
#verify discount amount is correct after discount

discount_percentage_string = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
discount_percentage = float(discount_percentage_string.strip('%'))
actual_discount_amount = (expected_price * discount_percentage) / 100

actual_Total_After_Discount = expected_price - actual_discount_amount
print("actual_Total_After_Discount", actual_Total_After_Discount)

Expected_Total_After_Discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
if Expected_Total_After_Discount == actual_Total_After_Discount:
    print("Expected_Total_After_Discount == actual_Total_After_Discount")
else:
    print("Expected_Total_After_Discount != actual_Total_After_Discount")
assert actual_price > actual_Total_After_Discount, "actual_price is not greater than actual_Total_After_Discount price"

assert Expected_Total_After_Discount == actual_Total_After_Discount
assert Expected_Total_After_Discount < expected_price
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

# select country
countries_dropdown = Select(driver.find_element(By.XPATH, "//div/select"))
countries_dropdown.select_by_value("India")
driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
order_placed = driver.find_element(By.XPATH, "//div[@class='wrapperTwo']/span").text
print(order_placed)

assert "successfully" in order_placed
time.sleep(5)
