import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
'''
switch_to.window(window_id)

current_window_handle    >> will return the windowId of focused window
window_handles           >> returns the list of all browser window ids

Note : Everytime the window id will be changed i,e its dynamic in nature
'''
# print(driver.current_window_handle)

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
window_ids = driver.window_handles
#
# for window in window_ids:
#     driver.switch_to.window(window)
#     print(driver.title)

# Switching desired windows
# open three windows by navigating to parent window
for i in range(3):
    driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
    driver.switch_to.window(window_ids[0])

# close desired window by specifying index
all_windows = driver.window_handles
# time.sleep(5)
# driver.switch_to.window(all_windows[-1])
# driver.close()

# close the window using title name
for win in all_windows:
    driver.switch_to.window(win)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS":
        driver.close()




