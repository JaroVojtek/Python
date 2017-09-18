from selenium import webdriver
from selenium.webdriver.common.by import By
from handyWrappers import *
import time

class ElementPresentCheck():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        hw = handyWrappers(driver)

        elementResult = hw.isElementPresent("name",By.ID)
        print(str(elementResult))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()