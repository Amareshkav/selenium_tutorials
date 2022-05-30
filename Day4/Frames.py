'''
Frame : when we working with windows application we call it as frame
Iframe : when we working with other web application we call it as Iframe

Selenium 4:
switch_to.frame(name of the frame)
switch_to.frame(id of the frame)
switch_to.frame(web element of the frame)
switch_to.frame(index of the frame)
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()


driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium').click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "//div[@class='topNav']//a[normalize-space()='Help']").click()

