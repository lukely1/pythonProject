from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  #switch to frame

#driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2022") #mm/dd/yyyy

year="2023"
month="October"
date="10"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click() # opens datepicker


while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #Next arrow
        #driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() # Previous Arrow - old date

#select date

dates=driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break

