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
driver.get("https://www.nike.com")
driver.maximize_window()

hover=driver.find_element(By.XPATH,"//span[text()='Kids']")

actions=ActionChains(driver)
actions.move_to_element(hover).pause(2).click(hover).perform()
driver.switch_to.window(driver.window_handles[1])
shop=driver.find_element(By.XPATH,"//a[text()='Shop']")
actions.scroll_to_element(shop).click(shop).perform()
driver.find_element(By.XPATH,"(//div[@class='css-owizmr'])[1]").click()
driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH,"//label[text()='UK 1.5']").click()
driver.find_element(By.XPATH,"//button[text()='Add to Bag']").click()
driver.quit()

