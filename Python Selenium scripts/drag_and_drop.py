from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragAndDrop():

    def test(self):
        baseURL = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)
        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            #actions.drag_and_drop(fromElement,toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and Drop Element successfull")
            time.sleep(2)
        except:
            print("Drag and Drop failed on element")


ff = DragAndDrop()
ff.test()