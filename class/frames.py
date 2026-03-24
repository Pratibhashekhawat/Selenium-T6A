# #iframe --> mini webpage inside a webpage
# # make three webpages with second's address in first
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common import actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from websocket import send
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
# driver.get("file:///C:/Users/Pratibha/OneDrive/Desktop/html/index.html")
# driver.maximize_window()
# sleep(4)
# driver.find_element(By.ID,"inp1").send_keys("first")
# #switching by class
# driver.switch_to.frame('frame1')
# driver.find_element(By.ID,"inp2").send_keys("second")
# #switching through index
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"inp3").send_keys("third")
#
#
# #switching to parent
# driver.switch_to.parent_frame()
# driver.find_element(By.ID,"inp2").clear()
# driver.find_element(By.ID,"inp2").send_keys("i am back")
# driver.switch_to.parent_frame()
# #to clear
# driver.find_element(By.ID,"inp1").clear()
# driver.find_element(By.ID,"inp1").send_keys("i am back")
#
# #switch to main page
# driver.switch_to.default_content()
# driver.find_element(By.ID,"inp2").send_keys("i am back")

#handling alerts

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
sleep(4)
driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']").click()
alert2= driver.switch_to.alert
alert2.dismiss()
driver.find_element(By.XPATH,"//button[text()='Prompt Alert']").click()
alert3= driver.switch_to.alert
alert3.send_keys("pratibha")
alert3.accept()




