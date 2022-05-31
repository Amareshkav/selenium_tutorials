from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

ops = Options()
ops.add_experimental_option("detach", True)
ser_call = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=ser_call, options=ops)
driver.get("https://www.nopcommerce.com/en/demo")
driver.maximize_window()

# Below are the methods to get the screenshots
driver.save_screenshot(os.getcwd()+"\\HomePage.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\HomePage.png")
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()

driver.close()
