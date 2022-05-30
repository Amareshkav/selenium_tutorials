from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://www.facebook.com/")
driver.maximize_window()

print("facebook title is :", driver.title)
driver.back()  # Navigates to orangepage
time.sleep(3)
print("Orange title is :", driver.title)
driver.forward()  # Navigatges to facebook
time.sleep(3)
print("facebook title is :", driver.title)
driver.refresh()
driver.close()
