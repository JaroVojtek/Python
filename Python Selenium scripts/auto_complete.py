from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test(self):
        baseURL = "https://southwest.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        city = driver.find_element(By.ID, "air-city-departure")
        city.send_keys("New York")
        time.sleep(3)

        itemToSelect = driver.find_element_by_xpath(".//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        itemToSelect.click()

        #time.sleep(3)
        #driver.quit()
        

ff = AutoComplete()
ff.test()