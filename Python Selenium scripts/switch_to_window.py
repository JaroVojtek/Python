from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        parentHandle = driver.current_window_handle
        print("Parent Handle" + parentHandle)

        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        handles = driver.window_handles

        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window: " + handle)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successfull")


ff = SwitchToWindow()
ff.test()
