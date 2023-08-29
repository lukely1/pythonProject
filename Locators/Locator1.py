from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.service import Service

# serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.LINK_TEXT, "Register").click()
# OR
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
#driver.close()
#driver.quit()
#


