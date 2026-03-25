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
#o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
sleep(2)

driver.switch_to.new_window()
driver.get("https://www.amazon.in")


print(driver.title)
print(driver.current_url)
sleep(2)
driver.switch_to.new_window()
driver.get("https://www.flipkart.in")
print(driver.title)
print(driver.current_url)


sleep(2)
driver.close()

driver.switch_to.window(driver.window_handles[1])
sleep(2)
driver.close()

driver.switch_to.window(driver.window_handles[0])
sleep(2)
driver.quit()

