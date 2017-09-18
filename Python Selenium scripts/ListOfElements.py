from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementListByClassName = driver.find_elements_by_class_name("inputs")
        lenght1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("Size of the list is: "+ str(lenght1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "h1")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("Size of the list is " + str(length2))

ff = ListOfElements()
ff.test()