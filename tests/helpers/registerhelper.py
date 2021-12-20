import time
def register(details, driver):
    
    element = driver.find_element_by_xpath("//div[@class='mat-typography']/div/button[@class='mat-focus-indicator close-dialog mat-raised-button mat-button-base mat-primary ng-star-inserted']").click()
    element = driver.find_element_by_xpath("//div[@class='cc-window cc-floating cc-type-info cc-theme-classic cc-bottom cc-right cc-color-override-1934802758 ']/div[@class='cc-compliance']").click()


    element = driver.find_element_by_xpath("//*[@class='mat-toolbar-row']/button[@class='mat-focus-indicator mat-menu-trigger buttons mat-button mat-button-base']").click()
    element = driver.find_element_by_id("navbarLoginButton").click()
    time.sleep(2)


    element = driver.find_element_by_id("newCustomerLink").click()

    time.sleep(2)

    email = driver.find_element_by_id('emailControl')
    email.clear()
    email.send_keys(details["email"])


    password = driver.find_element_by_id('passwordControl')
    password.clear()
    password.send_keys(details["password"])


    rpassword = driver.find_element_by_id("repeatPasswordControl")
    rpassword.clear()
    rpassword.send_keys(details["password"])


    select = driver.find_element_by_id("mat-select-2").click()
    option = driver.find_element_by_id("mat-option-3").click()

    # for option in options:
    #     if option.get_attribute("id") =="mat-option-3":
    #         option.click()


    answer = driver.find_element_by_id("securityAnswerControl")
    answer.clear()
    answer.send_keys(details["answer"])

    register = driver.find_element_by_id("registerButton").click()

    