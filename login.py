from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://dev.moyveterinar.ru/')

driver.find_element_by_name('login').clear()
driver.find_element_by_name('login').send_keys('AlexanderSW')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('podobulkin@ukr.net')
driver.find_element_by_name('pass').clear()
driver.find_element_by_name('pass').send_keys('210785ap')
driver.find_element_by_name('pass_two').clear()
driver.find_element_by_name('pass_two').send_keys('210785ap')
driver.find_element_by_name('bday_day').click()
select_1 = Select(driver.find_element_by_name('bday_day'))
select_1.select_by_value('21')
driver.find_element_by_name('bday_month').click()
select_2 = Select(driver.find_element_by_name('bday_month'))
select_2.select_by_value('7')
driver.find_element_by_name('bday_year').click()
select_3 = Select(driver.find_element_by_name('bday_year'))
select_3.select_by_value('1985')
driver.find_element_by_id('b-fast-registration__reg-button').click()
time.sleep(2)
driver.find_element_by_name('field_3').send_keys('Alexander')
driver.find_element_by_name('field_4').send_keys('Podobulkin')
driver.find_element_by_name('field_5').send_keys('Vladimirovich')
driver.find_element_by_name('field_2').send_keys('QA Engineer')
driver.find_element_by_name('field_11').send_keys('KNTEU')
select_4 = Select(driver.find_element_by_name('field_13'))
select_4.select_by_value('UA')
driver.find_element_by_name('field_12').send_keys('Kiev')
driver.find_element_by_id('regstepwise_step2_submit').click()
time.sleep(2)
driver.find_element_by_name('field_30').send_keys('(050)1234567')
driver.find_element_by_name('field_7').send_keys('Radushnaya str. 61')
driver.find_element_by_name('field_8').send_keys('+38(044)111-11-11')
driver.find_element_by_name('field_9').send_keys('Doctor')
driver.find_element_by_name('field_10').send_keys('Testing & Co')
driver.find_element_by_id('regstepwise_step3_submit').click()
time.sleep(2)
driver.find_element_by_id('agree_tos').click()
driver.find_element_by_id('regstepwise_step4_submit').click()
time.sleep(2)
driver.find_element_by_id('regstepwise_close_button').click()
time.sleep(4)
driver.close()
print ('Test PASSED')