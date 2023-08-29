from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.service import Service

# serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://automationpratice.com/index.php")
driver.maximize_window()

#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
sliders = driver.find_elements(By.CLASS_NAME, "homeslider-containe")

print(len(sliders))  # total number of sliders on home page

lINKS = driver.find_elements(By.TAG_NAME, "a")

print(len(lINKS))  # total number of links on home page
