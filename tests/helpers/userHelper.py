from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec



def userRegister(details,driver):
    
    def fillIn(id,value):
       element = driver.find_element_by_id(id)
       element.clear()
       element.send_keys(details[value])
    #driver.find_element_by_xpath("//div[@class='mat-typography']/div/button[@class='mat-focus-indicator close-dialog mat-raised-button mat-button-base mat-primary ng-star-inserted']").click()
    #driver.find_element_by_xpath("//div[@class='cc-window cc-floating cc-type-info cc-theme-classic cc-bottom cc-right cc-color-override-1934802758 ']/div[@class='cc-compliance']").click()
    #driver.find_element_by_xpath("//*[@class='mat-toolbar-row']/button[@class='mat-focus-indicator mat-menu-trigger buttons mat-button mat-button-base']").click()
    
    driver.find_element_by_css_selector("#mat-dialog-0 > app-welcome-banner > div > div:nth-child(3) > button.mat-focus-indicator.close-dialog.mat-raised-button.mat-button-base.mat-primary.ng-star-inserted").click()
    driver.find_element_by_css_selector("a[class='cc-btn cc-dismiss']").click()
    driver.find_element_by_id("navbarAccount").click()
    driver.find_element_by_id("navbarLoginButton").click()
    
    driver.implicitly_wait(10)
    driver.find_element_by_id('newCustomerLink').click()
    

    driver.implicitly_wait(10)
    
    fillIn('emailControl',"email")

    fillIn('passwordControl',"password")

    fillIn("repeatPasswordControl","password")

    driver.find_element_by_id("mat-select-2").click()
    driver.find_element_by_id("mat-option-3").click()

    fillIn("securityAnswerControl","answer")

    driver.find_element_by_id("registerButton").click()


def userLogin(details,driver):
    
    driver.implicitly_wait(10)

    
    def fillIn(id,value):
       element = driver.find_element_by_id(id)
       element.clear()
       element.send_keys(details[value])
    
    fillIn("email","email")

    fillIn("password","password")

    driver.find_element_by_class_name("mat-checkbox-inner-container").click()
    driver.find_element_by_id("loginButton").click()


def userLogout(driver):

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[@class='mat-toolbar-row']/button[@class='mat-focus-indicator mat-menu-trigger buttons mat-button mat-button-base']").click()

    logout = driver.find_element_by_id("navbarLogoutButton")
    logout.click()