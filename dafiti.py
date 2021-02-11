from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from access import pathChromedriver

#### como da pra fazer
def teste(driver, path):
    return (driver, 20).until(EC.element_to_be_clickable((By.XPATH, path)))

def closePopUp():
    x = 0
    while ( x == 0):
        time.sleep(10)
        try:
            closePopUpChat = WebDriverWait.until(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_0"]/div/div/div/div/div/div/div[5]/div/span')))
            closePopUpChat.click()
            print(ok)

            closePopUpCupom = WebDriverWait.until(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/div/div/button/i')))
            closePopUpCupom.click()

            x = 1


            time.sleep(10)
            closePopUpCookies = WebDriverWait.until(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/button')))
            closePopUpCookies.click()
        except:
            pass


def dafitiRegister(companyName, customerFirstName, cnpj, site, loginEmail, phone):
    # print('a')
    # cnpjTeste = teste(driver, '//*[@id="company"]')
    # cnpjTeste.send_keys(cnpj)
    # print('b')

    driver = webdriver.Chrome(pathChromedriver())
    url = 'https://www.dafiti.com.br/quero-vender-na-dafiti/'
    driver.get(url)

    ## close pop ups
    ## time to load all pop ups
    time.sleep(2)

    inputCompanyName = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="company"]')))
    inputCompanyName.send_keys(companyName)

    inputFirstName = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="first_name"]')))
    inputFirstName.send_keys(customerFirstName)

    inputCnpj = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2df"]')))
    inputCnpj.send_keys(cnpj)

    closePopUp()

    time.sleep(30)
    selectCategory = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2de"]')))
    selectCategory.click()

    closePopUp()

    time.sleep(3)
    #### select by category
    selectCategoryKids = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2de"]/option[2]')))
    selectCategoryKids.click()

    closePopUp()

    inputSite = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="url"]')))
    inputSite.send_keys(site)

    closePopUp()

    inputEmail = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    inputEmail.send_keys(loginEmail)

    closePopUp()

    inputPhone = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2dw"]')))
    inputPhone.send_keys(phone)

    closePopUp()

    time.sleep(40)

    buttonSend = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="formulario"]/div/form/input[10]')))
    buttonSend.click()

    time.sleep(40)



