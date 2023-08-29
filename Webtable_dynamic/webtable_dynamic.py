from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()


#Login
try:
    userNameElement= WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.NAME, "username")))
    userNameElement.send_keys('Admin')
    pwdElement = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.NAME, "password")))
    pwdElement.send_keys('admin123')
    logElement = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
    logElement.click()

    # Admin-->user management-->users
    adm = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))) # //*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a
    adm.click()
    usr_mg = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span"))) # //*[@id='menu_admin_UserManagement']
    usr_mg.click()
    sys_usr = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a")))
    #  //*[@id='menu_admin_viewSystemUsers']
    sys_usr.click()
finally:
    time.sleep(2)

#driver.find_element(By.ID, "txtUsername").send_keys("Admin")
#driver.find_element(By.ID, "txtPassword").send_keys("admin123")
#driver.find_element(By.ID, "btnLogin").click()
#time.sleep(3)

# Admin-->user management-->users
# driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b").click()
# driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']").click()
# driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']").click()

#total rows n a table
#rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody/tr"))
rows = WebDriverWait(driver, 2).until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div")))
print("total number of rows in a table:", len(rows))

count = 0
for r in range(1, len(rows)+1):
    status = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div["+str(r)+"]/div/div[5]/div"))).text # //*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div
    print(status)
    if status == "Enabled":
        count = count+1

print("Total Number of users:", len(rows))
print("Number of enabled users:", count)
print("Number of disabled users:", (len(rows)-count))

# for r in range(1, rows+1):
#     status=driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
#     if status=="Enabled":
#         count=count+1
#
# print("Total Number of users:",rows)
# print("Number of enabled users:",count)
# print("Number of disabled users:",(rows-count))


# driver.close()