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
import time
from pprint import pprint

def get_Items(driver):
    items_Page= []
    items = driver.find_elements_by_css_selector(".product")

    for item in items:
        title = item.find_element_by_css_selector(".item-name").text
        price = item.find_element_by_css_selector(".item-price").text
        image = item.find_element_by_css_selector(".img-thumbnail").get_attribute("src")
        item_Page = {
            "title":title,
            "price":price,
            "image":image
        }
        items_Page.append(item_Page)
    return items_Page

driver = webdriver.Chrome("../chromedriver.exe")
driver.get(config.drivers_config["URL1"])
driver.fullscreen_window()

driver.implicitly_wait(5)
driver.find_element_by_css_selector(".close-dialog").click()
driver.find_element_by_css_selector(".cc-compliance .cc-dismiss").click()
items_Pages = []
next_arrow_button = driver.find_element_by_css_selector(".mat-paginator-navigation-next")
next_arrow_status = next_arrow_button.get_attribute("disabled")

while next_arrow_status is None:
    next_arrow_status = next_arrow_button.get_attribute("disabled")
    items_Pages.extend(get_Items(driver))
    next_arrow_button.click()


pprint(items_Pages)
driver.quit()