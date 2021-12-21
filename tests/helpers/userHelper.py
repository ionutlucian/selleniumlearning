from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def userRegister(details,driver):
    driver.find_element_by_xpath("//div[@class='mat-typography']/div/button[@class='mat-focus-indicator close-dialog mat-raised-button mat-button-base mat-primary ng-star-inserted']").click()
    driver.find_element_by_xpath("//div[@class='cc-window cc-floating cc-type-info cc-theme-classic cc-bottom cc-right cc-color-override-1934802758 ']/div[@class='cc-compliance']").click()


    driver.find_element_by_xpath("//*[@class='mat-toolbar-row']/button[@class='mat-focus-indicator mat-menu-trigger buttons mat-button mat-button-base']").click()
    driver.find_element_by_id("navbarLoginButton").click()
    
    driver.implicitly_wait(10)
    driver.find_element_by_id('newCustomerLink').click()
    

    driver.implicitly_wait(10)
    
    email = driver.find_element_by_id('emailControl')
    email.clear()
    email.send_keys(details["email"])

    password = driver.find_element_by_id('passwordControl')
    password.clear()
    password.send_keys(details["password"])

    rpassword = driver.find_element_by_id("repeatPasswordControl")
    rpassword.clear()
    rpassword.send_keys(details["password"])

    driver.find_element_by_id("mat-select-2").click()
    driver.find_element_by_id("mat-option-3").click()

    answer = driver.find_element_by_id("securityAnswerControl")
    answer.clear()
    answer.send_keys(details["answer"])

    driver.find_element_by_id("registerButton").click()


def userLogin(details,driver):
    
    driver.implicitly_wait(10)
    
    email = driver.find_element_by_id("email")
    email.clear()
    email.send_keys(details["email"])


    password = driver.find_element_by_id("password")
    password.clear()      
    password.send_keys(details["password"])

    
    driver.find_element_by_class_name("mat-checkbox-inner-container").click()
    driver.find_element_by_id("loginButton").click()


def userLogout(driver):

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[@class='mat-toolbar-row']/button[@class='mat-focus-indicator mat-menu-trigger buttons mat-button mat-button-base']").click()

    logout = driver.find_element_by_id("navbarLogoutButton")
    logout.click()