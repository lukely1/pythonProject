import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)

act.context_click(button).perform()  # right click

time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click() # copy
time.sleep(3)
driver.switch_to.alert.accept()

