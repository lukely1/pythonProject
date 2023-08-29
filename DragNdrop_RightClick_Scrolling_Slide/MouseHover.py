import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

#Login
#Login
try:
    userNameElement= WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.NAME, "username")))
    userNameElement.send_keys('Admin')
    pwdElement = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.NAME, "password")))
    pwdElement.send_keys('admin123')
    logElement = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
    logElement.click()

    # Admin-->user management-->users
    admin = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))) # //*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a
    admin.click()
    usermgmt = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span"))) # //*[@id='menu_admin_UserManagement']
    usermgmt.click()
    users = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a")))
    #  //*[@id='menu_admin_viewSystemUsers']
    #sys_usr.click()

finally:
    time.sleep(2)

# driver.find_element(By.ID, "txtUsername").send_keys("Admin")
# driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# driver.find_element(By.ID, "btnLogin").click()
# time.sleep(3)

#Admin-->user management-->users
# admin=driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
# usermgmt=driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
# users=driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

#MouseHover
act = ActionChains(driver)
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()


