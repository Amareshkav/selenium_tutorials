from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import XLUtils

ops = Options()
ops.add_experimental_option("detach", True)
ser_call = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=ser_call, options=ops)
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)

file = ".//Interest.xlsx"
rows = XLUtils.getRowCount(file, "Sheet1")

for r in range(2, rows + 1):
    # Read data from Excel
    princ = XLUtils.readData(file, "Sheet1", r, 1)
    rate_of_interest = XLUtils.readData(file, "Sheet1", r, 2)
    period = XLUtils.readData(file, "Sheet1", r, 3)
    expected_ret = XLUtils.readData(file, "Sheet1", r, 5)

    # Passing values to application
    driver.find_element(By.ID, "principal").send_keys(princ)
    driver.find_element(By.ID, "interest").send_keys(rate_of_interest)
    driver.find_element(By.ID, "tenure").send_keys(period)
    years = driver.find_element(By.ID, "tenurePeriod")
    year = Select(years)
    year.select_by_value("1")
    ele_freq = driver.find_element(By.ID, "frequency")
    Select(ele_freq).select_by_value("0")
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    mat_val = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text
    if float(expected_ret) == float(mat_val):
        XLUtils.writeData(file, "Sheet1", r, 7, "Passed")
        XLUtils.fillGreenColor(file, "Sheet1", r, 7)
    else:
        XLUtils.writeData(file, "Sheet1", r, 7, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 7)

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()  # Clear
