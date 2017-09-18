from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GenericScreenshoots():

    def test(self):
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)

    def takeScreenshot(self,driver):
        """Take screenshot of the current open web page
        :param driver
        :return :
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Jaroslav Vojtek HPE\\Learning\\Python\\Selenium Course\\seleniumwd2\\findingelements\\"
        destinationFileName = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFileName)
            print("Sreenshoot saved to directory --> ::" + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")


ff = GenericScreenshoots()
ff.test()
