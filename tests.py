from selenium import webdriver
from functions import get_random_email
import time
from functions import is_display
import const

browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")

browser.get("https://dev.devse.xyz/register")
c = get_random_email()

#Registration Positive scenario__________________________________________________________________
browser.find_element_by_xpath(const.name).send_keys("user")
browser.find_element_by_xpath(const.surname).send_keys("surnamesurname")
browser.find_element_by_xpath(const.email).send_keys(c)
browser.find_element_by_xpath(const.phone).send_keys("0932323432")
browser.find_element_by_xpath(const.password).send_keys("success1234")
browser.find_element_by_xpath(const.submit_password).send_keys("success1234")
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()
time.sleep(3)
page_title = browser.title
print('Positive scenario Registration --- is ok')
assert page_title == 'DEMO'
browser.quit()

#Nagative scenario, Registration already existed email in DB____________________________________
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get("https://dev.devse.xyz/register")

browser.find_element_by_xpath(const.name).send_keys("user")
browser.find_element_by_xpath(const.surname).send_keys("surnamesurname")
browser.find_element_by_xpath(const.email).send_keys(c)
browser.find_element_by_xpath(const.phone).send_keys("0932323432")
browser.find_element_by_xpath(const.password).send_keys("success1234")
browser.find_element_by_xpath(const.submit_password).send_keys("success1234")
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()

time.sleep(3)
page_title = browser.title
assert page_title[2:17] == 'SQLSTATE[23505]'
print('Nagative scenario, Registration already existed email in DB --- is ok')
browser.quit()


# Negative scenario, Registration with invalid data_______________________________________
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get("https://dev.devse.xyz/register")

browser.find_element_by_xpath(const.name).send_keys("12")
browser.find_element_by_xpath(const.surname).send_keys("312231")
browser.find_element_by_xpath(const.email).send_keys('32@fh.n')
browser.find_element_by_xpath(const.phone).send_keys("we")
browser.find_element_by_xpath(const.password).send_keys("21")
browser.find_element_by_xpath(const.submit_password).send_keys("123")
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()

time.sleep(3)

alert1 = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/ul/li[1]")
alert2 = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/ul/li[2]")
alert3 = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/ul/li[2]")

is_display(alert1)
is_display(alert2)
is_display(alert3)
print('Negative scenario, Registration with invalid data --- is ok')
browser.quit()
#Nagative scenario, Registration with different password and submit_password
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")

browser.get("https://dev.devse.xyz/register")
c = get_random_email()

browser.find_element_by_xpath(const.name).send_keys("user")
browser.find_element_by_xpath(const.surname).send_keys("surname")
browser.find_element_by_xpath(const.email).send_keys(c)
browser.find_element_by_xpath(const.phone).send_keys("0932323432")
browser.find_element_by_xpath(const.password).send_keys("success1234")
browser.find_element_by_xpath(const.submit_password).send_keys("success123")
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()

time.sleep(3)
print('Nagative scenario, Registration with different password and submit_password --- is ok')
page_title = browser.title
browser.quit()