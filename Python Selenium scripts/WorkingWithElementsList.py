from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseURL="https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.implicitly_wait(10)

        radioButtonList = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        sizeList = len(radioButtonList)
        print("Size of the list" + str(sizeList))

        for i in radioButtonList:
            isSelected = i.is_selected()
            if not isSelected:
                i.click()
                time.sleep(2)

ff = WorkingWithElementsList()
ff.test()

