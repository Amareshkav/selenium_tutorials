'''
Web table are having tag "table"
th : table header
tr : table row
td : table data

web tables are static or dynamic in nature
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count no. of Rows and Columns
total_row = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
total_column = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th")
print("rows", len(total_row))
print("column", len(total_column))

# Read data of rows and column
# for r in range(2,len(total_row)+1):
#     for c in range(1, len(total_column)+1):
#         txt_data = driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{r}]/td[{c}]").text
#         print(txt_data, end="       ")
#     print()

# Read the data based on conditions (List books whose author is Mukesh)
for r in range(2,len(total_row)+1):
    txt_data = driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{r}]/td[2]").text
    if txt_data == "Mukesh":
        book_name = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[1]").text
        print(book_name)

driver.close()

