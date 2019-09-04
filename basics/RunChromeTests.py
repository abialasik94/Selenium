from selenium import webdriver
import os
import time

class RunFFTests():

    def testMethod(self):
        driverLocation = "/home/adam/Dokumenty/staż/kursy/selenium/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        #initiate the driver instance
        driver = webdriver.Chrome(driverLocation)
            #executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")


        driver.get("http://www.letskodeit.com")
        time.sleep(30)

ff = RunFFTests()
ff.testMethod()