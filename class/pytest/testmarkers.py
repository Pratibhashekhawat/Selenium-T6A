'''markers'''

import pytest
from selenium.webdriver.common.by import By
import openpyxl

#smoke test
# @pytest.mark.smoke
# def test_equal():
#     #assert
#     assert 'hello' == 'hello'
#
# #regression test
# @pytest.mark.regression
# def test_addition():
#     assert 5 + 5 == 10

#skip test
# @pytest.mark.skip
# def test_in():
#     l=[1,2,3]
#     assert 3 in l, "not in the list"

'''skip if'''
# @pytest.mark.skipif(True, reason="not in list")
# def test_in():
#     l=[1,2,3]
#     assert 3 in l, "in the list"

#parameterized markers
# @pytest.mark.parametrize('a,b',[(1,2),(2,3)])
# def test_add(a,b):
#     print(a+b)

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

'''fixture'''
# @pytest.fixture
# def greet():
#     print('hello world')
#     yield
#     print('good bye')
# def test_morning(greet):
#     print('morning')
# def test_evening(greet):
#     print('evening')

''' with fixture'''

# from selenium.webdriver.common.by import By
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium import webdriver
# @pytest.fixture(scope='class')
# def setup():
#     o = ChromeOptions()
#     o.add_experimental_option("detach", True)
#     driver = Chrome(options=o)
#
#     driver.get("https://demowebshop.tricentis.com/register")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.close()
#
#
# class TestRegister():
#     def test_gender(self, setup):
#         setup.find_element(By.ID, "gender-female").click()
#
#     def test_firstname(self, setup):
#         setup.find_element(By.ID, 'FirstName').send_keys("Pratibha")
#
#     def test_lastname(self, setup):
#         setup.find_element(By.ID, 'LastName').send_keys("Shekhawat")
#
#     def test_email(self, setup):
#         setup.find_element(By.ID, 'Email').send_keys("harshita@gmail.com")
#
#     def test_password(self,setup):
#         setup.find_element(By.ID, 'Password').send_keys("abcdefgh")
#
#     def test_confirmpass(self, setup):
#         setup.find_element(By.ID, 'ConfirmPassword').send_keys("abcdefgh")
#
#     def test_submit(self, setup):
#         setup.find_element(By.ID, "register-button").click()






