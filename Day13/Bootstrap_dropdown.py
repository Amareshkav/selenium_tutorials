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
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='select2-billing_country-container']").click()
countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print("Total countries :", len(countries_list))

for country in countries_list:
    if country.text == "Yemen":
        country.click()
        break
        
driver.close()