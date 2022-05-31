from selenium import webdriver

# def headless_chrome():
#     from selenium.webdriver.chrome.service import Service
#     from selenium.webdriver.chrome.options import Options
#     from webdriver_manager.chrome import ChromeDriverManager
#     ser_obj = Service(ChromeDriverManager().install())
#     ops = Options()
#     ops.headless = True
#     driver = webdriver.Chrome(service=ser_obj, options=ops)
#     return driver


# def headless_edge():
#     from selenium.webdriver.edge.service import Service
#     from selenium.webdriver.edge.options import Options
#     from webdriver_manager.microsoft import EdgeChromiumDriverManager
#     ser_obj = Service(EdgeChromiumDriverManager().install())
#     ops = Options()
#     ops.headless = True
#     driver = webdriver.Edge(service=ser_obj, options=ops)
#     return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options
    from webdriver_manager.firefox import GeckoDriverManager
    ser_obj = Service(GeckoDriverManager().install())
    ops = Options()
    ops.headless = True
    driver = webdriver.Firefox(service=ser_obj, options=ops)
    return driver


# driver = headless_chrome()
# driver = headless_edge()
driver = headless_firefox()

driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
