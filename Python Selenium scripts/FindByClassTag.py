from selenium import webdriver

class FindByClassTag():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementByClass = driver.find_element_by_class_name("displayed-class")
        elementByClass.send_keys("Testing the element")

        if elementByClass is not None:
            print("We found an element by Class name!")

        elementByTag = driver.find_element_by_tag_name("h1")
        text = elementByTag.text

        if elementByTag is not None:
            print("We found an element by Partial Tag name and its text is : " + text)

ff = FindByClassTag()
ff.test()