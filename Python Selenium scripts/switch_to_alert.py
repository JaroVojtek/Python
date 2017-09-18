from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToAlert():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        driver.find_element(By.ID, "name").send_keys("Anil")

        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)

        alert1 = driver.switch_to.alert()
        alert1.accept()
        time.sleep(2)

        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        confirm1 = driver.switch_to.alert()
        confirm1.dismiss()

ff = SwitchToAlert()
ff.test()
