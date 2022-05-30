from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

# 1) Locator matching with single element
# ele = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# ele.send_keys("Apple mac book")

# 2) Locators matching with multiple elements
# ele = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(ele.text)

# 3) Element not avilable then throws NoSuchElementException
# log = driver.find_element(By.LINK_TEXT,"Log")
# log.click()

######   Find Elements returns multiple elements in a list #######

# 1) Locators matching wiht single element
# eles = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(eles)  # Return the

# 2) Locators matching with multiple elements
# eles = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(eles))
# for each in eles:
#     print(each.text)

# 3) If no element matches it will not throw an exception instead returns the empty list
log = driver.find_elements(By.LINK_TEXT,"Log")
print(len(log))
