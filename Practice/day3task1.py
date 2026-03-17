from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://amazon.com")
driver.maximize_window()
sleep(4)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("mobiles")
sleep(2)
driver.find_element(By.ID, "nav-search-submit-button").click()
#driver.find_element(By.XPATH,"//span[text()='Motorola razr+ | 2023 | Unlocked | Made for US 8/256 | 32 MPCamera |Blue']").click()
price=driver.find_element(By.XPATH, '//h2[contains(@aria-label, "Samsung Galaxy S26")]/../../..//span[@class="a-price-whole"]')
print(price.text)
driver.quit()
