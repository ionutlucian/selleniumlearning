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

#EMAIL

email = driver.find_element_by_id("email")
email.clear()
email.send_keys("ion_lucik@yahoo.com")

#PASSWORD

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("Lovitura123!")

#Checkbox

time.sleep(1)
check = driver.find_element_by_class_name("mat-checkbox-inner-container").click()

#LOGIN button

login = driver.find_element_by_id("loginButton").click()