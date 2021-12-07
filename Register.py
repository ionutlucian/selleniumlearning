from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome(options = chromeOptions)


driver.get("http://localhost:3000")

# inchide prostiile
element = driver.find_element_by_xpath("//div[@class='mat-typography']/div/button[@class='mat-focus-indicator close-dialog mat-raised-button mat-button-base mat-primary ng-star-inserted']").click()
element = driver.find_element_by_xpath("//div[@class='cc-window cc-floating cc-type-info cc-theme-classic cc-bottom cc-right cc-color-override-1934802758 ']/div[@class='cc-compliance']").click()

#deschide loginul

element = driver.find_element_by_xpath("//*[@class='mat-toolbar-row']/button[@class='mat-focus-indicator mat-menu-trigger buttons mat-button mat-button-base']").click()
element = driver.find_element_by_id("navbarLoginButton").click()
time.sleep(2)

#redirect pentru register

element = driver.find_element_by_id("newCustomerLink").click()

#register

time.sleep(10)

#EMAIL
email = driver.find_element_by_id('emailControl')
email.clear()
email.send_keys("ion_lucik@yahoo.com")

#PASSWORD

password = driver.find_element_by_id('passwordControl')
password.clear()
password.send_keys("Lovitura123!")

#REPEAT PASS

rpassword = driver.find_element_by_id("repeatPasswordControl")
rpassword.clear()
rpassword.send_keys("Lovitura123!")

#MAT-SELECT

select = driver.find_element_by_id("mat-select-2").click()
option = driver.find_element_by_id("mat-option-3").click()

# for option in options:
#     if option.get_attribute("id") =="mat-option-3":
#         option.click()

#ANSWER

answer = driver.find_element_by_id("securityAnswerControl")
answer.clear()
answer.send_keys("Ramona")

#Register Button

register = driver.find_element_by_id("registerButton").click()





