from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from websocket import send

o=ChromeOptions()
o.add_experimental_option("detach",True)

#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.bmrc.co.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[.='English']").click()

dropdown= driver.find_element(By.XPATH,'//select[@class="form-control select fare-selects"]')
options = Select(dropdown)
options.select_by_visible_text("Whitefield")
dropdown2= driver.find_element(By.XPATH,'(//select[@class="form-control select fare-selects"])[2]')
option2 = Select(dropdown2)
option2.select_by_visible_text("Halasuru")
driver.find_element(By.XPATH, '//button[@class="app-btn-box"]').click()
sleep(2)
driver.quit()