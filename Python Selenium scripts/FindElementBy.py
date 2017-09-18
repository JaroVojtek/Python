from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementBy():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by Class name!")

        elementByXpath = driver.find_element(By.XPATH, ".//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by Partial ")

ff = FindElementBy()
ff.test()