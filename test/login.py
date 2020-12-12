from selenium import webdriver
import const
import time

from selenium.common.exceptions import NoSuchElementException
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return ('login after successfull registration  ---   is dropped')
    return ('login after successfull registration   ---     is ok')


#login after successfull registration______________________________________________________

browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get("https://trading.alfa-one-capital.com/login")

browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/input').send_keys(const.email_value)
browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/input').send_keys(const.pass_value)
browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/button').click()

print(check_exists_by_xpath('/html/body/div/nav/div[1]/div/div[1]/div[1]/a/img'))
time.sleep(3)
browser.quit()