from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://flipkart.com")
driver.maximize_window()
sleep(7)
driver.find_element(By.CLASS_NAME,"nw1UBF.v1zwn25").send_keys("skating shoes")
sleep(2)
driver.find_element(By.CLASS_NAME,"XFwMiH").click()
price=driver.find_element(By.XPATH,"//a[text()='viel spiel High quality in-line have different size wit...']/../..//div[@class='hZ3P6w']")
print(price.text)
