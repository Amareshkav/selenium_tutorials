# for finding the broken links : we need to install requests module/Library
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
total_links = len(all_links)

# Finding number of broken links in a webpage
count = 0
for link in all_links:
    url = link.get_attribute("href")
    try:
        response = requests.head(url)
    except:
        None

    if response.status_code >= 400:
        count += 1

print("Number of broken links are : ", count)
print("Number of valid links are : ", (total_links-count))