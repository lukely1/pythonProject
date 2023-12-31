from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.get("https://admin-demo.nopcommerce.com/login")

# emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
#
# emailbox.clear()
# emailbox.send_keys("abc@gmail.com")
#
# print("result of text:",emailbox.text)  # printed nothing
# print("result of get_attribute():",emailbox.get_attribute('value')) #abc@gmail.com

button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("result of text:", button.text)
print("result of get_attribute():", button.get_attribute('value'))
print("result of get_attribute():", button.get_attribute('type'))

