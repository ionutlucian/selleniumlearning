from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import helpers.userHelper as userHelp
import helpers.config as config


details = {
    "email": "bagasaaaaaa@test.com",
    "password": "asaasaas",
    "answer": "da"
}
driver = webdriver.Chrome("../chromedriver.exe")

driver.get(config.drivers_config["URL"])
#driver.(getattr(config.drivers_config["fullscreen"]))()
driver.fullscreen_window()

userHelp.userRegister(details, driver)

userHelp.userLogin(details,driver)

userHelp.userLogout(driver)
driver.quit()