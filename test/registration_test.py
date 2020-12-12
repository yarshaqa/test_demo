from selenium import webdriver
from functions import random_name_surname, is_display, check_exists_by_xpath
import time
import const
from selenium.common.exceptions import NoSuchElementException

#Registration Positive scenario__________________________________________________________________1
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get("https://dev.devse.xyz/register")

browser.find_element_by_xpath(const.name).send_keys(const.name_value)
browser.find_element_by_xpath(const.surname).send_keys(const.name_value)
browser.find_element_by_xpath(const.email).send_keys(const.email_value)
browser.find_element_by_xpath(const.phone).send_keys("0932")
browser.find_element_by_xpath(const.password).send_keys(const.pass_value)
browser.find_element_by_xpath(const.submit_password).send_keys(const.pass_value)
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()
print('Credentials registered:', const.email_value, const.pass_value )
time.sleep(3)
page_title = browser.title
assert page_title == 'DEMO'
browser.quit()
print('Positive scenario Registration --- is ok, 1')


#login after successfull registration______________________________________________________2

browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get("https://trading.alfa-one-capital.com/login")

browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/input').send_keys(const.email_value)
browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/input').send_keys(const.pass_value)
browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/button').click()


try:
    browser.find_element_by_xpath('/html/body/div/nav/div[1]/div/div[1]/div[1]/a/img')
    if True:
        print('login after successfull registration   ---     is ok')
except NoSuchElementException:
    print('login after successfull registration  ------------------------------------------------------------------   DROPPED')
print('Credentials:', const.email_value, const.pass_value)
time.sleep(3)
browser.quit()



#Nagative scenario, Registration already existed data in DB____________________________________3
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get("https://dev.devse.xyz/register")

browser.find_element_by_xpath(const.name).send_keys(const.name_value)
browser.find_element_by_xpath(const.surname).send_keys(const.name_value)
browser.find_element_by_xpath(const.email).send_keys(const.email_value)
browser.find_element_by_xpath(const.phone).send_keys("0932323432")
browser.find_element_by_xpath(const.password).send_keys("success1234")
browser.find_element_by_xpath(const.submit_password).send_keys("success1234")
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()


print(const.email_value, const.name_value)
time.sleep(3)
page_title = browser.title
assert page_title[2:17] == 'SQLSTATE[23505]'
print('Nagative scenario, Registration already existed email in DB --- is ok, 3')
browser.quit()


#Negative scenario, Registration with already registered email_________________________________4

browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get("https://dev.devse.xyz/register")

browser.find_element_by_xpath(const.name).send_keys(random_name_surname())
browser.find_element_by_xpath(const.surname).send_keys(random_name_surname())
browser.find_element_by_xpath(const.email).send_keys(const.email_value)
browser.find_element_by_xpath(const.phone).send_keys("0932323432")
browser.find_element_by_xpath(const.password).send_keys("success1234")
browser.find_element_by_xpath(const.submit_password).send_keys("success1234")
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()


print(const.email_value, random_name_surname())
time.sleep(3)
page_title = browser.title
assert page_title[2:17] == 'SQLSTATE[23505]'
print('Nagative scenario, Registration already existed email in DB --- is ok, 4')
browser.quit()


# Negative scenario, Registration with invalid data_______________________________________5
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
print('Negative scenario, Registration with invalid data --- is ok 5')
browser.quit()


#Negative scenario, Registration with different password and submit_password_____________________________6
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")

browser.get("https://dev.devse.xyz/register")

browser.find_element_by_xpath(const.name).send_keys("user")
browser.find_element_by_xpath(const.surname).send_keys("surname")
browser.find_element_by_xpath(const.email).send_keys(const.email_value)
browser.find_element_by_xpath(const.phone).send_keys("0932323432")
browser.find_element_by_xpath(const.password).send_keys("success1234")
browser.find_element_by_xpath(const.submit_password).send_keys("success123")
browser.find_element_by_xpath(const.checkbox).click()
browser.find_element_by_xpath(const.submit).click()

time.sleep(3)
print('Negative scenario, Registration with different password and submit_password --- is ok 6')
page_title = browser.title
browser.quit()