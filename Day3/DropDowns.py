from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# drp_ele = driver.find_element(By.CSS_SELECTOR, "#input-country")
# drp_obj = Select(drp_ele)

# Options to select the drop downs
# drp_obj.select_by_visible_text("India")
# drp_obj.select_by_index(10)
# drp_obj.select_by_value("value")

# Select all the options
# each option returns the web elements
# all_opts = drp_obj.options  # List of all options web elements
# print("Total number of all options : ", len(all_opts))

# for opt in all_opts:
#     print(opt.text)

# Select options from Dropdowns without built in methods:
# for opt in all_opts:
#     if opt.text == "India":
#         opt.click()
#         break

'''
If the select tag is not available then we can locate the drop down options by xpath
'''
# all_options = driver.find_elements(By.XPATH,"//select[@id='input-country']/option")  # 242 elements
india = driver.find_element(By.XPATH, "//select[@id='input-country']//option[text()='India']").click()


driver.close()

