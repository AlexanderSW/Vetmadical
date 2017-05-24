import unittest
from selenium import webdriver

class ResultPage(object):

    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element_by_id('user_link_vetmedical').text

class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self, param1, param2):
        self.driver.find_element_by_id('sign_in').click()
        self.driver.find_element_by_id("ips_username").send_keys(param1)
        self.driver.find_element_by_id('ips_password').send_keys(param2)
        self.driver.find_element_by_id("b-login__submit-form").click()
        return ResultPage(self.driver)

class Login(unittest.TestCase):

    def setUp(self):
        chrome_path = r"C:\Chromedriver\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.get("http://dev.vetmedical.ru/")
        self.driver.implicitly_wait(20)

    def test_login(self):
        home = HomePage(self.driver)
        result = home.login("Alexander Podobulkin", "210785ap")
        assert ("Alexander Podobulkin") in result.username()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
