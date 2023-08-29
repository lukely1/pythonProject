from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10) # seconds  # implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')

searchbox.send_keys("Selenium")
searchbox.submit()


driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()

driver.quit()