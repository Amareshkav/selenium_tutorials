from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
first_name = driver.find_element(By.NAME, "email")
print(first_name.is_displayed())
print(first_name.is_enabled())

driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
rad = driver.find_element(By.XPATH, "//input[@type='radio' and @value='QBP']")
print("Before selecting :", rad.is_selected())
rad.click()
print("After selecting :", rad.is_selected())

