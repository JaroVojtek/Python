from selenium import webdriver

class FindByXpathCss():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementByXpath = driver.find_element_by_xpath("//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by Xpath!")

        elementByCss = driver.find_element_by_css_selector("#name")

        if elementByCss is not None:
            print("We found an element by CSS")

ff = FindByXpathCss()
ff.test()