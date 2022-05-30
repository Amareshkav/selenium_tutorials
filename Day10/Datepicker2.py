from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


ops = Options()
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ops)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
wait = WebDriverWait(driver,10)

driver.find_element(By.ID,"departon").click()

ele_month = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']")
ele_year = driver.find_elements(By.XPATH, "//div[@class='ui-datepicker-title']/select[2]/option")
print(len(ele_year))
expected_month = "Sep"
expected_year = "1993"

month = Select(ele_month)
month.select_by_visible_text(expected_month)
for year in ele_year:
    if year.text == expected_year:
        year.click()



# date selection
expected_date = "6"
all_dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for date in all_dates:
    if date.text == expected_date:
        date.click()
