from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

ops = Options()
ops.add_experimental_option("detach", True)
ser_call = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=ser_call, options=ops)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Opening register link in new tab , here RETURN > Enter Key
# register = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH, "//a[normalize-space()='Register']").send_keys(register)

# New Tab - Selenium 4 : Opens new tab and switched to new window
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://pypi.org/project/webdriver-manager/#use-with-edge")

# Open new browser window and switches to new window
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://pypi.org/project/webdriver-manager/#use-with-edge")


