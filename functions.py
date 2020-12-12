import random
import string
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver



def random_email():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(7))
    return(result_str+'@email.com')


def random_name_surname():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(7))
    return (result_str)


def random_pass():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return (result_str)


def is_display(a):
    if True:
        print (a, '  - displayed')
    else:
        print(a, '  - not displayed')


def check_exists_by_xpath(xpath):
    browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return ('login after successfull registration  ------------------------------------------------------------------   DROPPED')
    return ('login after successfull registration   ---     is ok')