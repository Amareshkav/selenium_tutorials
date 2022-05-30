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

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

soeul = driver.find_element(By.XPATH, "//*[@id='box5']")
south_korea = driver.find_element(By.XPATH, "//*[@id='box105']")
rome = driver.find_element(By.XPATH, "//*[@id='box6']")
italy = driver.find_element(By.XPATH, "//*[@id='box106']")

action = ActionChains(driver)
action.drag_and_drop(soeul,south_korea).perform()
action.drag_and_drop(rome,italy).perform()
