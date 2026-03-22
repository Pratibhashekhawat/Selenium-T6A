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
wait.until(EC.visibility_of_element_located((By.NAME,'q'))).send_keys('barbie phone')
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'XFwMiH'))).click()
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'UCc1lI'))).click()
driver.quit()