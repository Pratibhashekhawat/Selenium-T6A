from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("headless")
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\Pratibha\Downloads\Weekly_Assessment_1 (1).md"+"/n"+r"C:\Users\Pratibha\Downloads\Problem_Statement_1 (1).md")
driver.find_element(By.ID,"multipleFilesInput").send_keys(r'C:\Users\Pratibha\Downloads\Weekly_Assessment_1 (1).md'+ '\n' + r"C:\Users\Pratibha\Downloads\pexels-lukas-rodriguez-1845331-3573351.jpg" )
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.quit()
