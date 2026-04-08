from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
def test_register():
    driver.find_element(By.LINK_TEXT,"Register").click()
def test_gender():
    driver.find_element(By.ID,"gender-male").click()
def test_firstname():
    driver.find_element(By.ID,"FirstName").send_keys("Pratibha")
def test_lastname():
    driver.find_element(By.ID,"LastName").send_keys("shekhawat")
def test_email():
    driver.find_element(By.ID,"Email").send_keys("pratibha@gmail.com")
def test_password():
    driver.find_element(By.ID,"Password").send_keys("123456")
def test_pass2():
    driver.find_element(By.ID,"ConfirmPassword").send_keys("123456")
def test_register2():
    driver.find_element(By.ID,"register-button").click()