from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

# o=ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://demoqa.com/webtables")
# driver.maximize_window()
# sleep(4)
#traversing in xpath

#forward--> parent to child-->/ or //
#backward-->child to parent--> /..
# dep=driver.find_element(By.XPATH,"//td[text()='Vega']/..//td[6]")
# print(dep.text)
# sleep(2)

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
sleep(4)

# dep=driver.find_element(By.XPATH,"//td[text()='Frank']/..//td[4]")
# print(dep.text)
# sleep(4)

#sibling--> following -->below
# preceding-->above
dep=driver.find_element(By.XPATH,"//td[text()='Frank']/following-sibling::td[2]")
print(dep.text)
sleep(4)


