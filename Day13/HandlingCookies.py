'''
Cookies are the temporary files created by the browser.Helps the user to remember the information
and stored by the browser.
Cookies have attributes like name , expiry_date , value etc
'''


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

ops = Options()
ops.add_experimental_option("detach", True)
ser_call = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=ser_call, options=ops)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture all cookies stored by the browser
cookies = driver.get_cookies()
print("Size of Cookies : ", len(cookies)) #3

# Print cookie information
# for c in cookies:
#     print(c)
#     print(c.get("name"), ";", c.get("value"))

# Add new cookie to the browser
driver.add_cookie({"name": "My_Cookie", "value": "12345"})
cookies = driver.get_cookies()
print("After adding cookie", len(cookies)) #4

# Delete specific cookie from the browser
driver.delete_cookie("My_Cookie")
cookies = driver.get_cookies()
print("After deleting cookie", len(cookies))

# Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("After deleting all cookie", len(cookies))

driver.close()

