"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on the browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            # set chrome driver

            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # set chrome driver

            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver

