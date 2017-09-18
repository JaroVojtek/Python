#.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseURL="https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)

        login_link = driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()
        driver.implicitly_wait(10)

        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("test")

        password_field = driver.find_element(By.ID, "user_password")
        password_field.send_keys("test")

        time.sleep(3)

        email_field.clear()

        time.sleep(3)

        email_field.send_keys("second test")

ff = ClickAndSendKeys()
ff.test()

