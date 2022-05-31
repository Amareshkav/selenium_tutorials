from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()


# def chrome_setup():
#     from webdriver_manager.chrome import ChromeDriverManager
#     from selenium.webdriver.chrome.options import Options
#     from selenium.webdriver.chrome.service import Service
#     ser_obj = Service(ChromeDriverManager().install())
#     ops = Options()
#     preferences = {"download.default_directory": location}
#     ops.add_experimental_option("detach", True)
#     ops.add_experimental_option("prefs", preferences)
#     driver = webdriver.Chrome(service=ser_obj, options=ops)
#     return driver


def edge_setup():
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from selenium.webdriver.edge.options import Options
    from selenium.webdriver.edge.service import Service
    ser_obj = Service(EdgeChromiumDriverManager().install())
    ops = Options()
    preferences = {"download.default_directory": location}
    ops.add_experimental_option("detach", True)
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(service=ser_obj, options=ops)
    return driver


ch_driver = edge_setup()
ch_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
ch_driver.maximize_window()
ch_driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
