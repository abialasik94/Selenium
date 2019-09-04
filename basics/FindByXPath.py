from selenium import webdriver


class FindByXpathCss():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found and Xpath element")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print("We found an element by Css")

        elementByClass = driver.find_element_by_class_name("btn-style")
        if elementByClass is not None:
            print("We found an element by Class")

ff = FindByXpathCss()
ff.test()
