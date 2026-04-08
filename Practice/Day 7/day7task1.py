
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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
hover= driver.find_element(By.XPATH,"//button[@class='dropbtn']")
actions = ActionChains(driver)
actions.move_to_element(hover).perform()
sleep(2)
dclick= driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions= ActionChains(driver)
actions.double_click(dclick).perform()
sleep(2)
drag= driver.find_element(By.ID,"draggable")
drop= driver.find_element(By.ID,"droppable")
actions= ActionChains(driver)
actions.drag_and_drop(drag,drop).perform()
sleep(2)
driver.quit()