# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# o.add_argument("headless")
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://www.google.com")
# sleep(2)
# driver.maximize_window()
# driver.implicitly_wait(10)
# links=driver.find_elements(By.TAG_NAME,'a')
# print(links)
# print(len(links))
# for i in links:
#     print(i.text)



#get attribute
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument("headless")
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://www.google.com")
# sleep(2)
# driver.maximize_window()
# driver.implicitly_wait(10)
# ele= driver.find_element(By.CLASS_NAME,"gb_A")
# sleep(2)
# print(ele.get_attribute("aria-label"))

# task
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument("headless")
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://www.amazon.com")
# sleep(2)
# driver.maximize_window()
# driver.implicitly_wait(10)
# links = driver.find_elements(By.XPATH,"//div[@id='nav-xshop']//a")
# for link in links:
#     print(link.get_attribute("href"))


#is_displayed()= visible or not
#is_enabled()= ready for interaction or not
#is_selected()= selected or not

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument("headless")
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# sleep(2)
# elem= driver.find_element(By.XPATH,"//div[@aria-label='Log in']")
# print("displayed:",elem.is_displayed())
# print("enabled:",elem.is_enabled())
# ele=driver.find_element(By.XPATH,"//input[@type='submit']")
# print('displayed: ',ele.is_displayed())
# print('enabled: ',ele.is_enabled())

#checkboxes
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument("headless")
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
# driver.implicitly_wait(10)
# sleep(2)
# ele=driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
# print("selected:",ele.is_selected())
# ele1=driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")
# print("selected:",ele1.is_selected())

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("headless")
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"firstName").send_keys("John")
driver.find_element(By.ID,"lastName").send_keys("Doe")
driver.find_element(By.ID,"userEmail").send_keys("john@gmail.com")
driver.find_element(By.ID,"gender-radio-1").click()
driver.find_element(By.ID,"userNumber").send_keys("123456789")
driver.find_element(By.XPATH,"//div[@aria-label='Choose Saturday, April 4th, 2026']").click()
driver.find_element(By.ID,"react-select-2-placeholder").send_keys("pcm")
driver.find_element(By.XPATH,'//input[@type="checkbox"][1]').click()





