from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

ele = driver.find_element(By.NAME,"Email")
print("Text value is : ", ele.text)
print("Attribute value of ele : ", ele.get_attribute("value"))

driver.quit()

## text >> is used to get the inner text of an web element
#<input class="email">LogIn></input>  :: Here Login is a inner text

# get_attribute() is used to get the attribute value of the web elements
