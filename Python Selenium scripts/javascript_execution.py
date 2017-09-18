from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        #driver.get(baseURL)
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")

        #element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementByID('name')")
        element.send_keys("Test")

ff = JavaScriptExecution()
ff.test()
