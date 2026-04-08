# import pytest
# from excel2 import get_test_data
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
# from time import sleep
# @pytest.mark.parametrize("username,password",get_test_data())
# def test_log(username,password):
#     o = ChromeOptions()
#     o.add_experimental_option("detach", True)
#     driver = Chrome(options=o)
#     driver.get("https://www.saucedemo.com")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     # actual=password
#     # expected="secret_sauce"
#     # assert actual==expected
#     driver.find_element(By.ID,"user-name").send_keys(username)
#     driver.find_element(By.ID,"password").send_keys(password)
#     driver.find_element(By.ID,"login-button").click()
#     assert "inventory" in driver.current_url

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from excel2 import get_test_data
from conftest import driver
@pytest.mark.parametrize("username,password",get_test_data())
def test_login(driver,username,password):
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    assert "inventory" in driver.current_url

