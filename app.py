# import requests
from passwordgenerator import pwgenerator
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
import names
import random

driver = webdriver.Chrome()
temp_mails = 'https://www.temp-mails.com'
facebook = 'https://www.facebook.com'
# Create temporary email
driver.get(temp_mails)
time.sleep(3)
driver.find_element_by_id("generateEmail").click()
time.sleep(5)
fake_email = driver.find_elements_by_class_name("email_lab")
time.sleep(5)
fake_email = str(fake_email[0].text)
# Create facebook account
driver.get(facebook)
driver.find_element_by_class_name("_4jy2 ").click()
time.sleep(5)
firstname = driver.find_element_by_name("firstname")
lastname = driver.find_element_by_name("lastname")
email = driver.find_element_by_name("reg_email__")
email_confirmation = driver.find_element_by_name("reg_email_confirmation__")
password = driver.find_element_by_name("reg_passwd__")
birthday_day = driver.find_element_by_name("birthday_day")
birthday_month = driver.find_element_by_name("birthday_month")
birthday_year = driver.find_element_by_name("birthday_year")
gender = driver.find_element_by_name("sex")
# Password
password_gen = pwgenerator.generate();

firstname.send_keys(names.get_first_name(gender=random.choice(['male', 'female'])))
lastname.send_keys(names.get_last_name())
email.send_keys(fake_email)
if email_confirmation:
    email_confirmation.send_keys(fake_email)
password.send_keys(password_gen)
birthday_day.click()
birthday_day.send_keys(random.randint(1, 31))
birthday_day.send_keys(Keys.RETURN)
birthday_month.click()
birthday_month.send_keys(random.choice(["J", "F", "M", "A", "MM", "J", "JJ", "AA", "S", "O", "N", "D"]))
birthday_month.send_keys(Keys.RETURN)
birthday_year.click()
birthday_year.send_keys(random.randint(1905, 2005))
birthday_year.send_keys(Keys.RETURN)
gender.click()

driver.find_element_by_name('websubmit').click()

print( f'Email : {fake_email}' )
print( f'Password : {password_gen}')