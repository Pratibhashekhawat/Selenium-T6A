from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.amazon.com")
sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("watch")
driver.find_element(By.ID,"nav-search-submit-button").click()
links= driver.find_elements(By.TAG_NAME,"img")
print(links)
print(len(links))
links[4].click()
