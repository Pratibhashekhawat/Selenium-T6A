from time import sleep, time
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common import actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from websocket import send



o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
import os
driver.get("https://www.lenskart.com")
driver.maximize_window()
driver.implicitly_wait(10)
folder=os.path.join(os.getcwd(), "Pictures")
os.makedirs(folder,exist_ok=True)
driver.find_element(By.ID,"lrd1").click()
expected= "https://www.lenskart.com/eyeglasses.html"
actual = driver.current_url
assert expected == actual,"incorrect url"
driver.find_element(By.XPATH,"//option[text()='Most Viewed']").click()
driver.save_screenshot(f"{folder}/mostviewed.png")
