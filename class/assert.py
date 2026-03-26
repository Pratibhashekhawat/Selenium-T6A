'''assert and screenshots
assert --> used to compare actual outcome and expected outcome'''
import os

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
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# print(driver.title)
# #assert
# expected= "Google"
# actual = driver.title
# assert expected == actual,"title mismatch"
# driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("weather today")
# driver.quit()

'''screenshots--> proofs'''
# from time import sleep, time
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
# driver.get("https://www.amazon.in")
# driver.maximize_window()
#driver.save_screenshot("screenshot.png")
# folder= os.path.join(os.getcwd(), "screenshot")
# os.makedirs(folder,exist_ok=True)
#
# driver.save_screenshot(f'{folder}/screenshot_page.png')
#
# #element screenshot
# ele= driver.find_element(By.LINK_TEXT,"Bestsellers")
# #ele.screenshot(f'{folder}/screenshot_page.png')
# timestamp= time.strftime("%Y%m%d-%H%M%S")
# ele.screenshot(f'{folder}/screenshot_ele_{timestamp}.png')
#
# driver.implicitly_wait(10)
#
# driver.find_element(By.LINK_TEXT,"Bestsellers").click()
# expected="https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers"
# actual= driver.current_url
# assert expected == actual,"url mismatch"
# driver.quit()


#screenshot through timestamp
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
import time
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
import os
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)
# driver.save_screenshot('screenshot1.png')
# creating folder named screenshot  to save screenshot.png
folder = os.path.join(os.getcwd(), 'screenshot')
os.makedirs(folder,exist_ok=True) #check whether the folder is there or not

driver.save_screenshot(f"{folder}/screenshot.png") # save screenshot to the particular folder
sleep(2)
ele=driver.find_element(By.XPATH,'//textarea[@title="Search"]')
ele.send_keys("Watch")
# ele.screenshot(f"{folder}/screenshot_ele.png")

timestamp=time.strftime("%Y%m%d-%H%M%S")
ele.screenshot(f"{folder}/screenshot_{timestamp}.png")
