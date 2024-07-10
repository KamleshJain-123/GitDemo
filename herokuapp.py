import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# Chrome Options
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("ignore-certificate-errors")
chrome_option.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_option)


# switch window example
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Click Here").click()
# windowOpen = driver.window_handles
# driver.switch_to.window(windowOpen[1])
# print(driver.find_element(By.TAG_NAME, "h3").text)
# driver.close()
# driver.switch_to.window(windowOpen[0])
# print(driver.find_element(By.TAG_NAME, "h3").text)
# assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

# iframe example
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(3)
# driver.maximize_window()
driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH, "//a[text()='Register']").click()
driver.switch_to.default_content()
page = (driver.find_element(By.XPATH, "//h1[text()='Practice Page']").text)
print(page)
driver.execute_script("window.scroll(0, document.body.scrollHeight)")
# Take Screenshot
driver.get_screenshot_as_file("screenshot.png")

time.sleep(10)
