from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(
            executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "carselect")

        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "//label[@for='bmw']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Sign Up")

        if elementByLinkText is not None:
            print("We found an element by LinkText")

ff = ByDemo()
ff.test()