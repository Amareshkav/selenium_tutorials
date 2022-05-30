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

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

## LogIn
driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

## Mouse hover
admin = driver.find_element(By.XPATH ,"//*[@id='menu_admin_viewAdminModule']/b")
usr_mng = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

action = ActionChains(driver)
# mv_admin = action.move_to_element(admin)
# mv_mgt = mv_admin.move_to_element(usr_mng)
# mv_usr = mv_mgt.move_to_element(users)
# mv_usr.click().perform()

action.move_to_element(admin).move_to_element(usr_mng).move_to_element(users).click().perform()

