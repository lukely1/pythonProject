from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth") # syntax

driver.maximize_window()

