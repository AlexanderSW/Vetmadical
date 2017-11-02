# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://dev.vetmedical.ru/")
    wd.find_element_by_css_selector("#sign_in").click()
    wd.find_element_by_css_selector("#ips_username").click()
    wd.find_element_by_css_selector("#ips_username").clear()
    wd.find_element_by_css_selector("#ips_username").send_keys("Alexander Podobulkin")
    wd.find_element_by_css_selector("#ips_password").click()
    wd.find_element_by_css_selector("#ips_password").clear()
    wd.find_element_by_css_selector("#ips_password").send_keys("210785ap")
    wd.find_element_by_css_selector("#b-login__submit-form").click()
    wd.refresh()
    wd.get("https://dev.vetmedical.ru/index.php?/forum/9-%D0%BE%D0%B1%D1%89%D0%B8%D0%B5-%D0%BE%D0%B1%D1%81%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F/")
    wd.find_element_by_css_selector("#tabs-container > header > div.b-control-buttons > a").click()
    if wd.find_element_by_css_selector("#main > div > h1").text != "*Создание темы в разделе Общие обсуждения*":
        raise Exception("not assertText failed")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
