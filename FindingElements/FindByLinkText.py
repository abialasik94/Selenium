from selenium import webdriver


class FindByLinkText():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")
        driver.get(baseUrl)

        elementById = driver.find_element_by_id("Login")

        if elementById is not None:
            print("We found and element")
        elementByLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByLinkText is not None:
            print("We found an element by Name")


ff = FindByName()
ff.test()
