import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWeatherAppWithSelenium(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        # ignore SSL
        options.add_argument('ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.instance = self.driver.get("http://localhost:80")
        self.input_box = self.driver.find_element(By.NAME, "city")
        self.button = self.driver.find_element(By.TAG_NAME, "button")

    def tearDown(self):
        self.driver.quit()
        self.input_box = None
        self.button = None
        self.driver = None
        self.instance = None


    def test_positive_search(self):
        self.input_box.send_keys("Haifa")
        self.button.click()

        try:
            print(self.instance)
            self.driver.find_element(By.ID,"weather-info")

            search = True
        except Exception:
            search = False

        self.assertTrue(search,"Search for Haifa was not successful")

    def test_negative_search(self):
        self.input_box.send_keys("")
        self.button.click()
        try:
            self.driver.find_element(By.ID,"weather-info")
            search = True
        except Exception:
            search = False

        self.assertFalse(search,"Search was successful, but it shouldn't!")
