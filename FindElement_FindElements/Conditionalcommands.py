from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#from selenium.webdriver.chrome.service import Service

# serv_object = Service("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed()   is_enabled()

searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display status:", searchbox.is_displayed())  # True
print("Enabled status:", searchbox.is_enabled())  # True

# is_selected() - for radio buttons and check boxes
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("default radio buttons status.....")
print(rd_male.is_selected()) #False
print(rd_female.is_selected()) #False

rd_male.click()  # select male radio button

print("After selecting male radio button.....")
print(rd_male.is_selected()) #True
print(rd_female.is_selected()) #False

rd_female.click()
print("After selecting fe-male radio button.....")
print(rd_male.is_selected()) #False
print(rd_female.is_selected()) #True

driver.quit()
