from selenium import webdriver
from selenium.webdriver.common.by import By
from handyWrappers import handyWrappers
import time

class UsingWrappers():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        hw = handyWrappers(driver)

        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']",locatorType="xpath")
        textField2.clear()


ff = UsingWrappers()
ff.test()