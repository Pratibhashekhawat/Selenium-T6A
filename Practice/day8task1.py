#open twitter sign up with google

from time import sleep
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
driver.get("https://www.twitter.com")
driver.maximize_window()
sleep(2)
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//span[text()='Sign up with Google']").click()
driver.quit()
