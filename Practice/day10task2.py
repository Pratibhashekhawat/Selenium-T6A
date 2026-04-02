from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Apparel & Shoes").click()
dropdown= driver.find_element(By.ID,"products-orderby")
option= Select(dropdown)
option.select_by_index(1)
dropdown2= driver.find_element(By.ID,"products-pagesize")
option2 = Select(dropdown2)
option2.select_by_value('https://demowebshop.tricentis.com/apparel-shoes?orderby=5&pagesize=4')
dropdown3= driver.find_element(By.ID,"products-viewmode")
option3 = Select(dropdown3)
option3.select_by_index(1)
driver.quit()