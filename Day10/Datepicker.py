from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


ops = Options()
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ops)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(0)
driver.find_element(By.ID, "datepicker").click()

expected_month = "July"
expected_year = 2023

while True:
    month = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']//span[1]").text
    year = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']//span[2]").text
    if expected_year == int(year) and expected_month == month:
        break
    else:
        # prev click
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()
        # next click
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()

# Selecting the dates
all_dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
expected_date = 23

for date in all_dates:
    if int(date.text) == expected_date:
        date.click()

driver.close()