from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import rpa as r

def carrefuorRegister(cnjp, customerFirstName, customerLastName, displayName, companyName, registrationMunicipal, registrationState, category, platform, loginEmail, phone):
    driver = webdriver.Chrome()
    url = 'https://www.carrefour.com.br/marketplace/inscreva-se'
    driver.get(url)
# page1
    time.sleep(3)
    inputCnpj = driver.find_element_by_xpath('//*[@id="00N6g00000RpFD9"]')
    inputCnpj.send_keys(cnjp)

    inputCustomerFirstName = driver.find_element_by_xpath('//*[@id="first_name"]')
    inputCustomerFirstName.send_keys(customerFirstName)

    inputCustomerLastName = driver.find_element_by_xpath('//*[@id="last_name"]')
    inputCustomerLastName.send_keys(customerLastName)

    inputDisplayName = driver.find_element_by_xpath('//*[@id="00N6g00000RpFDb"]')
    inputDisplayName.send_keys(displayName)

    inputCompanyName = driver.find_element_by_xpath('//*[@id="company"]')
    inputCompanyName.send_keys(companyName)

    if registrationState is None:
        selectRegistrationMunicipal = driver.find_element_by_xpath('//*[@id="00N6g00000RpFDQ"]')
        selectRegistrationMunicipal.click()
    else:
        inputRegistrationMunicipal = driver.find_element_by_xpath('//*[@id="00N6g00000RpFDO"]')
        inputRegistrationMunicipal.send_keys(registrationMunicipal)

    inputRegistrationState = driver.find_element_by_xpath('//*[@id="00N6g00000U1IXi"]')
    inputRegistrationState.send_keys(registrationState)

    selectCategory = driver.find_element_by_xpath('//*[@id="00N6g00000RpFDA"]')
    selectCategory.click()

    inputCategory = driver.find_element_by_xpath('//*[@id="00N6g00000RpFDA"]/option[2]')
    inputCategory.click()
    inputCategory.send_keys(Keys.RETURN)

    clickPlatform = driver.find_element_by_xpath('//*[@id="00N6g00000RpFDP"]')
    clickPlatform.click()

    inputPlatform = driver.find_element_by_xpath('//*[@id="00N6g00000RpFDP"]/option[8]')
    inputPlatform.click()
    inputPlatform.send_keys(Keys.RETURN)

    inputEmail = driver.find_element_by_xpath('//*[@id="email"]')
    inputEmail.send_keys(loginEmail)

    inputPhone = driver.find_element_by_xpath('//*[@id="phone"]')
    inputPhone.send_keys(phone)