from selenium import webdriver


class FindByName():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found and element")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by Name")

        elementByClass = driver.find_element_by_class_name("btn-style")
        if elementByClass is not None:
            print("We found an element by Class")

ff = FindByName()
ff.test()
