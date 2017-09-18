from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test(self):
        baseURL = "https://expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(.5)
        driver.get(baseURL)

        driver.find_element(By.ID, "tab-flight-tab").click()
        departingField = driver.find_element(By.ID, "flight-departing")
        departingField.click()

        dateToSelect = driver.find_element(By.XPATH, "")

        time.sleep(3)
        driver.quit()


ff = CalendarSelection()
ff.test()