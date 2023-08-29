from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

#from selenium.webdriver.chrome.service import Service

# serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(5)

#driver.close()
driver.quit()