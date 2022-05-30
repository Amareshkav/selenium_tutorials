'''
Locators:

Locators are the address of an element on the html page

Different ways to identify an elements:

1. Id
2. Name
3. LinkText
4. Partial Link text
5. ClassName
6. Tagname
7. CSSSelector
8. Xpath

Upto 4 >> we can locate it directly
5, 6 >> we use for locating multiple elements on webpage
7, 8 >> Customised locator used if we unable to find locator by using rest of locators

7. CSS Selector:
a. Tag  ID             Tagname#valueOftheId    Ex: input#email
b. Tag class
c. Tag attribute
d. Tag Class attribute

Note : Tag is not mandatory

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chr_options)
driver.get("https://www.facebook.com/login/")
driver.maximize_window()

#driver.find_element(By.CSS_SELECTOR,'input#email').send_keys("amaresh")
#driver.find_element(By.CSS_SELECTOR,'#email').send_keys("amaresh")

# Tag and class
# If some space in the class name >> just remove from space part
#driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys("amaresh")
# driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys("amaresh")

# Tag attribute >> tagname[attribute=value]

# driver.find_element(By.CSS_SELECTOR,'input[name=email]').send_keys("amaresh")
# driver.find_element(By.CSS_SELECTOR,'[name=email]').send_keys("amaresh")

# Tag class attribute  >> tagname.classname[attribute=value]
# If we have same Tag and class name but attributes are different then we can go for this option

driver.find_element(By.CSS_SELECTOR,'input.inputtext[name=email]').send_keys("amaresh")

