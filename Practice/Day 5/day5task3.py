from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("headless")
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"ico-register").click()
driver.find_element(By.XPATH,"(//input[@type='radio'])[2]").click()
driver.find_element(By.ID,"FirstName").send_keys("Pratibha")
driver.find_element(By.ID,"LastName").send_keys("shekhawat")
driver.find_element(By.ID,"Email").send_keys("pratibha@gmail.com")
driver.find_element(By.ID,"Password").send_keys("123456")
driver.find_element(By.ID,"ConfirmPassword").send_keys("123456")
driver.find_element(By.ID,"register-button").click()
driver.quit()