import pytest
from selenium.webdriver import Chrome, ChromeOptions
@pytest.fixture
def driver():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    o.add_argument("--disable-notifications")
    driver = Chrome(options=o)

    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

