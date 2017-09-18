from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ExplicitWait():

    def test(self):
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(.5)
        driver.get(baseURL)

        driver.find_element(By.ID, "tab-flight-tab").click()

ff = ExplicitWait()
ff.test()