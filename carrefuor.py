from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from access import pathChromedriver
import rpa as r


def carrefuorRegister(cnpj, customerFirstName, customerLastName, displayName, companyName,
                      registrationMunicipal, registrationState, category, platform, loginEmail, phone):
    url = 'https://www.carrefour.com.br/marketplace/inscreva-se'

    driver = webdriver.Chrome(pathChromedriver())
    driver.get(url)

    time.sleep(3)
    allowCookies = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
    allowCookies.click()

    inputCnpj = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/form')))
    print('a')
    inputCnpj.click()

    print(cnpj)




    # input = driver.find_element_by_xpath('')
    # input.send_keys()
    #
    # input = driver.find_element_by_xpath('')
    # input.send_keys()
    #
    # input = driver.find_element_by_xpath('')
    # input.send_keys()
    #
    # input = driver.find_element_by_xpath('')
    # input.send_keys()
    #
    # input = driver.find_element_by_xpath('')
    # input.send_keys()

def carrefuorRegisterRpa(cnpj, customerFirstName, customerLastName, displayName, companyName,
                      registrationMunicipal, registrationState, category, platform, loginEmail, phone):
    url = 'https://www.carrefour.com.br/marketplace/inscreva-se'

    r.init()
    r.url(url)

    time.sleep(10)
    r.click('//*[@id="onetrust-accept-btn-handler"]')

    time.sleep(3)
    r.click('//*[@id="00N6g00000RpFD9"]')
    r.click('//*[@id="00N6g00000RpFD9"]')