from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import helpers.registerhelper as reghelper
import helpers.userHelper as userHelp


details = {
    "email": "bagidsssasasdaaaaaa@test.com",
    "password": "asaasaas",
    "answer": "da"
}
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome("../chromedriver.exe",options = chromeOptions)


driver.get("http://localhost:3000")



userHelp.userRegister(details, driver)

userHelp.userLogin(details,driver)

userHelp.userLogout(driver)
driver.quit()