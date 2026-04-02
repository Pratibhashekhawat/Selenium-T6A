from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
ele= driver.find_element(By.LINK_TEXT,"Facebook")
actions=ActionChains(driver)
#scroll to facebook
actions.scroll_to_element(ele).perform()
sleep(2)
actions.click(ele).perform()
#switch to facebook window
driver.switch_to.window(driver.window_handles[1])
#entering email and password
driver.find_element(By.XPATH,"(//label[@class='x78zum5 xh8yej3'])[1]/descendant::input").send_keys("pratibha@gmail.com")
driver.find_element(By.XPATH,"(//label[@class='x78zum5 xh8yej3'])[2]/descendant::input").send_keys("123")
driver.find_element(By.XPATH,"(//span[.='Log in'])[6]").click()
driver.quit()
