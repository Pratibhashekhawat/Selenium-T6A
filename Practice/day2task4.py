# #task1
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://selenium.dev')
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,'Downloads').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'gl').click()
sleep(2)
driver.find_element(By.LINK_TEXT, "Register Now").click()
sleep(2)
print(driver.title)
driver.quit()