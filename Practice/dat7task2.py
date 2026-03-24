
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
driver.get("https://www.flipkart.com")
driver.maximize_window()
sleep(4)
#driver.find_element(By.XPATH,"//button[text()='✕']").click()
scroll= driver.find_element(By.XPATH,"//div[@class='x3q9HG']")
actions= ActionChains(driver)
actions.scroll_to_element(scroll).perform()
sleep(5)
driver.find_element(By.XPATH,"//a[text()='Myntra']").click()
driver.switch_to.window(driver.window_handles[1])
print("Myntra:")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[0])
print("flipkart:")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)

driver.find_element(By.XPATH,"//a[text()='Shopsy']").click()
driver.switch_to.window(driver.window_handles[2])
sleep(2)
print("shopsy:")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,"//a[text()='Cleartrip']").click()
driver.switch_to.window(driver.window_handles[3])
print("cleartrip:")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)
driver.quit()





