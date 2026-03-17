#explicit wait

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//button[text()='Start']").click()
# wait=WebDriverWait(driver,10)
# # ans=driver.find_element(By.XPATH,"//div[@id='finish']//h4")
# ans = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']")))
# print(ans.text)

#implicit wait


# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://www.decathlon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/shop/Winter-Collection']").click()
# driver.implicitly_wait(10)
# wait=WebDriverWait(driver,10)



from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.flipkart.com")
sleep(2)
driver.maximize_window()
sleep(2)
driver.implicitly_wait(10)
wait=(WebDriverWait(driver,10))
wait.until(EC.visibility_of_element_located(By.CLASS_NAME,'nw1UBF.v1zwn25')).send_keys('barbie phone')