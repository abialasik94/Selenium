from selenium import webdriver
class RunFFTests():

    def testMethod(self):
        #initiate the driver instance
        driver = webdriver.Firefox(
            executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")


        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()