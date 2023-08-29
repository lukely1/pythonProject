from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.service import Service

# serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)  #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/
print(driver.page_source)

driver.quit()