# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
#
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Pratibha")# for class we use . and for id we use #
from attr import attributes

# xpath
# we can traverse backward and forward
# locate elements based on textwraplocate elements based on attributes
# used for dynamic element
#absolute --> start with/ and root node
# relative -->start with // to represent the current attribute

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
#
# o=ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("Pratibha")
# sleep(2)
# driver.find_element(By.XPATH,"//button[text()='Submit']").click()


# using text function
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.amazon.com")
driver.maximize_window()
sleep(4)
# driver.find_element(By.XPATH,"//span[.='Easter baskets']").click()
# sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'Easter bunny')]").click()
sleep(2)
driver.find_element(By.XPATH,"//span[contains(@class,'a-size-small')]")
sleep(2)
driver.find_element(By.XPATH,"(//div[@class='navFooterColHead'])[2]")

