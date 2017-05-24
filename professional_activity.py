import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class ResultPage(object):

    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element_by_id('regstepwise_step2').id

    def birthday(self):
        return self.driver.find_element_by_name('bday_day', 'bday_month', 'bday_year').text


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def enter_registration_date(self, param1, param2, param3, param4):
        self.driver.find_element_by_name('login').send_keys(param1)
        self.driver.find_element_by_name('email').send_keys(param2)
        self.driver.find_element_by_name('pass').send_keys(param3)
        self.driver.find_element_by_name('pass_two').send_keys(param4)
        return ResultPage(self.driver)

    def select_by_value(self, param1, param2, param3):
        self.driver.find_element_by_id('bday_day').select_by_value(param1)
        self.driver.find_element_by_id('bday_month').select_by_value(param2)
        self.driver.find_element_by_id('bday_year').select_by_value(param3)
        return ResultPage(self.driver)

class ProfessionalActivity(unittest.TestCase):

    def setUp(self):
        chrome_path = r"C:\Chromedriver\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.get("http://dev.vetmedical.ru/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def registration_with_choose_activity(self):
        home = HomePage(self.driver)
        registration = home.enter_registration_date('AlexanderSW', 'podobulkin@ukr.net', '210785ap', '210785ap')
        select_1 = Select.select_by_value(value="21")
        assert ("AlexanderSW") in registration.username()
        assert ('21', '07', '1985') in select_1.birthday()
        self.driver.find_element_by_id('b-fast-registration__reg-button').click()

if __name__ == '__main__':
    unittest.main()
