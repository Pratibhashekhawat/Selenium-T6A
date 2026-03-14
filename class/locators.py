# entering values in demoqa



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
# driver.find_element(By.ID, "userName").send_keys("Pratibha")
# sleep(2)
# driver.find_element(By.ID, "userEmail").send_keys("Pratibha@gmail.com")
# sleep(2)
# driver.find_element(By.ID, "currentAddress").send_keys("60")
# sleep(2)
# driver.find_element(By.ID, "permanentAddress").send_keys("60")
# sleep(2)
# driver.find_element(By.ID, "submit").click()
#



#search in amazon
#by id


from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
# driver.get("https://www.amazon.com")
# driver.maximize_window()
# sleep(2)
#
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys("shirts")
#
# driver.find_element(By.ID, "twotabsearchtextbox").click()

#by class name


# driver.find_element(By.CLASS_NAME,'nav-searchbar.nav-progressive-attribute').send_keys('shoes')
# sleep(2)
# #river.find_element(By.CLASS_NAME,'nav-searchbar nav-progressive-attribute').click()
# driver.find_element(By.ID, "twotabsearchtextbox").click()
# sleep(2)
# driver.quit()
# driver = Chrome(options=o)
# driver.get("https://www.amazon.com")

#link  text
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.LINK_TEXT,'Mobiles').click()
# sleep(2)
# driver.find_element(By.LINK_TEXT,'Customer Service').click()
# driver.quit()

#partial link text
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Kitchen").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"ay").click()

#using css selector
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Amazon.in"]').send_keys("shoes")








