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

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")
print("Location of slider before moving")
print("min slider :", min_slider.location)  #{'x': 59, 'y': 250}
print("max slider :", max_slider.location)  #{'x': 510, 'y': 250}

action = ActionChains(driver)
action.drag_and_drop_by_offset(min_slider, 100, 0).perform()
action.drag_and_drop_by_offset(max_slider, -38, 0).perform()

print("Location of slider After moving")
print("min slider :", min_slider.location)  # {'x': 159, 'y': 250}
print("max slider :", max_slider.location)  # {'x': 470, 'y': 250}