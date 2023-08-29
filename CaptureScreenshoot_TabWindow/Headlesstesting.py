from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.headless = True
    driver = webdriver.Chrome(options=options)

    return driver

# def headless_edge():
#     from selenium.webdriver.edge.service import Service
#     ops = webdriver.EdgeOptions()
#     ops.add_experimental_option("detach", True)
#     driver = webdriver.Edge(options=ops)
#     ops.headless=True
#     return driver


# def headless_firefox():
#     from selenium.webdriver.firefox.service import Servic
#     ops = webdriver.FirefoxOptions()
#     ops.headless=True
#     driver = webdriver.Edge(options=ops)
#     return driver

driver=headless_chrome()
#driver=headless_edge()
# driver=headless_firefox()

driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
