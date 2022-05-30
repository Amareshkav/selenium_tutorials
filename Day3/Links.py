'''
Links:
1) Internal Link : Link which redirects to same webpage of different page
2) External Link : Link which redirects to external webpage/link
3) Broken Link : Link which does not have target page
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Click on the Link:
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# Find number of links in a webpage
total_links = driver.find_elements(By.TAG_NAME, "a")
print(len(total_links))  # 90

# Print link text of all links
for link in total_links:
    print(link.text)
