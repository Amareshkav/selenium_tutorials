from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensourcetxtUsername-demo.orangehrmlive.com/")
usr_name = driver.find_element(By.ID, "txtUsername")
usr_name.clear()
usr_name.send_keys("Admin")
password = driver.find_element(By.ID, "txtPassword")
password.clear()
password.send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
print(driver.title)
if driver.title == "OrangeHRM":
    print("Test case is passed")
else:
    print("Test case is failed")
driver.close()
