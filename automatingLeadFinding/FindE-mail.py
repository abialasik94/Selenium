from selenium import webdriver
import NamesData


class FindEmail():

    names = NamesData.getName()
    print(names[1])
    z = names[1:5]
    e = names[1]
    def openGoogle(self):

        baseUrl = "https://google.com"
        driver = webdriver.Firefox(
            executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")
        driver.get(baseUrl)

        searchBox = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[4]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")
        searchButton = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[4]/form[1]/div[2]/div[1]/div[3]/center[1]/input[1]")

        #for i in range(self.z):
        searchBox.send_keys(self.e)
        searchButton.click()
        #       driver.get(baseUrl)
Find = FindEmail()
Find.openGoogle()