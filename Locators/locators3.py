from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.service import Service

# serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.facebook.com")
driver.maximize_window()
# tag and class
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# tag and attribute

