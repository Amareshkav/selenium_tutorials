from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# Checkboxes:
checkboxes = driver.find_elements(By.XPATH,"//*[@class='form-check']//input[@type='checkbox']")
print(len(checkboxes))

# Selecting all checkboxes
# Approach 1:
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Approach 2:
for checkbox in checkboxes:
    checkbox.click()

# Selecting multiple checkboxes with choices:
# for checkbox in checkboxes:
#     week_name = checkbox.get_attribute("id")
#     if week_name in ["monday", "sunday"]:
#         checkbox.click()
#         print(f"Status of checkboxe {week_name} after checkin:", checkbox.is_selected())

# Selecting last two checkboxes:
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].clickb()

# Clearing all selected checkboxes:
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()



