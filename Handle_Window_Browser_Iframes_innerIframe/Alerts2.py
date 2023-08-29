from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://mypage.rediff.com/login/dologin")
# driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='Login']").click() #lOGIN BUTTON
time.sleep(5)
driver.switch_to.alert.accept()

driver.close()

