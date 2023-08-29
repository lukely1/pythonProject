from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

#from selenium.webdriver.chrome.service import Service

# serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.snapdeal.com")
driver.get("http://www.amazon.com")

driver.back()  # go back to snapdeal
driver.forward() # go to amazon

driver.refresh()

driver.quit()