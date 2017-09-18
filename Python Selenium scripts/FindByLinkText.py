from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementByLink = driver.find_element_by_partial_link_text("Login")

        if elementByLink is not None:
            print("We found an element by Link text!")

        elementByPartialLink = driver.find_element_by_link_text("Pract  ")

        if elementByPartialLink is not None:
            print("We found an element by Partial Link text")

ff = FindByLinkText()
ff.test()