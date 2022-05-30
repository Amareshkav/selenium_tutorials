from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

'''
Authentication popups are one where username and password has to given inorder to
access the particular websites
Syntax : https://username:password@test.com
'''
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()


