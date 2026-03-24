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
# driver.get("https://www.zomato.com/jaipur/order")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.XPATH,"//a[text()='Log in']").click()
# sleep(2)
# driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="auth-login-ui"]'))
# driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="Sign in with Google Button"]'))
# driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
# driver.quit()


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
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'(//a[text()="Python 3.14.3"])[4]').click()
