from selenium import webdriver
import NamesData


class FindEmail():

    names = NamesData.getName()
    print(names[1])
    z = names[1:3]
    e = names[1]
    def openGoogle(self):
        baseUrl = "https://google.com"
        driver = webdriver.Firefox(
            executable_path="/home/adam/Dokumenty/staż/kursy/selenium/geckodriver-v0.24.0-linux64/geckodriver")
        driver.get(baseUrl)

        print("siema" + self.z[1])
        print(type("siema1" + self.z[2]))
        print("siema2" + self.e)
        print(type("siema3" + self.e))

        for i in range(len(self.z)):
            searchBox = driver.find_element_by_xpath(
                "/html[1]/body[1]/div[1]/div[4]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")
            searchButton = driver.find_element_by_xpath(
                "/html[1]/body[1]/div[1]/div[4]/form[1]/div[2]/div[1]/div[3]/center[1]/input[1]")

            searchBox.send_keys(str(self.names[i]) + " management team")
            searchButton.click()
            firstNoAdvertisementElement = driver.find_elements_by_class_name("ellip")
            firstNoAdvertisementElement[0].click()

            driver.get(baseUrl)

Find = FindEmail()
Find.openGoogle()