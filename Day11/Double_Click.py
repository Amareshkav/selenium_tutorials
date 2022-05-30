from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chr_options = Options()
chr_options.add_argument("--disable-notifications")
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://www.tutorialspoint.com/index.htm")
driver.maximize_window()

# Did not find the url hence given an example below
# button = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")
# action = ActionChains(driver)
# action.double_click(button).perform()

