from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)
my_wait = WebDriverWait(driver, 10)   # Explicit wait declaration

# my_wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                         ElementNotVisibleException,
#                                                         ElementNotSelectableException,
#                                                         Exception
#                                                         ])
# poll_frequency 2:means every two sec it will go and search for the element so it will make
# explicit wait more effective instead of rigidly waiting for 10 sec

# Exception argument will handle the all kind of exception
driver.get("https://www.google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium")
search_box.submit()

my_ele = my_wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
# Condition mentioned above returns the web element if the condition is satisfied
my_ele.click()

driver,quit()

'''
explicit wait : Depends on the condition not on the time based 
Qsn:
1. Why in explicit wait we mention time at the declaration?
    Since the explicit wait is condition based unless the condition is met the statement will keep on
    look for that condition/web element hence code will not execute further so mention the time
    within that time if the condition is not satisfied it will execute further code in module

2. If the element is not present/ there is a bug in application what happens?
    If the element is not present then condition never become true, it will keep on looking
    for an element
    
Note : To handled the exception if the element not found on page then we can modified the 
       declaration.
       
       Explicit statement has to be used multiple time where condition is needed for an element
       It is most effective way of handling synchronization problem

'''