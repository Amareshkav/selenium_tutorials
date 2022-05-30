from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

search_input = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
search_input.send_keys("Selenium")
search_input.submit()

## click on each search
search_ele = driver.find_elements(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-results']//a")
print(search_ele)
for each in search_ele:
    each.click()

all_windowsId = driver.window_handles
for window in all_windowsId:
    driver.switch_to.window(window)
    print(driver.title)
    driver.close()

