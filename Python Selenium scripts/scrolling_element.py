from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollingElement():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        #driver.get(baseURL)
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")

        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)

        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150);")

        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("Location" + str(location))


ff = ScrollingElement()
ff.test()
