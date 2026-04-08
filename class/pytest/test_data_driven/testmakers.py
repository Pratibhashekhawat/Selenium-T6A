import pytest
from selenium.webdriver.common.by import By
import openpyxl
from sheet02 import get_test_data
'''saucedemo '''
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
@pytest.mark.parametrize('uname,passwd',get_test_data())
def test_login(uname,passwd):
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.ID,'user-name').send_keys(uname)
    driver.find_element(By.ID,'password').send_keys(passwd)
    driver.find_element(By.ID,'login-button').click()
    assert "inventory" in driver.current_url, "Login Failed"









