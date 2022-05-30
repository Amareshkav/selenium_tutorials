from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)
driver.implicitly_wait(10)     # time in sec

driver.get("https://www.google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium")
search_box.submit()

# time.sleep(5)   # Inserted to pause the code for 5 sec
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()


'''
I) time:
    Adv:
    1) Simple to use
    Dis Adv:
    1) Performance of the script is very poor
    2) If the element is not present within the mentioned time , there is a chance of getting
       an exception
       
II) implicit wait:
    driver.implicitly_wait(10)
    Adv:
    1) Single statement applicable for all driver elements
    2) Performance will not be reduced (If the element is found within the mentioned time it 
    proceeds to execute further statements)
    Dis Adv:
    1) If the element is not present within the mentioned time , there is a chance of getting
       an exception
       
Note : If the element is not present in the page it will throw an exception that can be 
       handled using try and except block
    
'''