#task
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("headless")
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.amazon.com")
sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)
links = driver.find_elements(By.XPATH,"//div[@id='nav-xshop']//a")
for link in links:
    print(link.get_attribute("href"))
driver.quit()