from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://automationpractice.com/index.php/")
slider_img = driver.find_elements(By.XPATH,"//ul[@id='homeslider']/li/a/img")
print(len(slider_img))
for each in slider_img:
   # print(each)
    img_txt = each.get_attribute("src")
    print(img_txt)