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
import json





#details = {
#    "email": "bagasaaaaaa@test.com",
#    "password": "asaasaas",
#    "answer": "da"
#}
file = open("data.json")
data = json.load(file)

for i in range(len(data)):

    driver = webdriver.Chrome("../chromedriver.exe")

    driver.get(config.drivers_config["URL"])
#driver.(getattr(config.drivers_config["fullscreen"]))()
    driver.fullscreen_window()
#print(data["first"]["email"])
    userHelp.userRegister(data[i], driver)

    userHelp.userLogin(data[i],driver)

    userHelp.userLogout(driver)
    driver.quit()