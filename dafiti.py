from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from access import pathChromedriver

def dafitiRegister(companyName, customerFirstName, cnpj, site, loginEmail, phone):

    driver = webdriver.Chrome(pathChromedriver())
    url = 'https://www.dafiti.com.br/quero-vender-na-dafiti/'
    driver.get(url)

    ## close pop ups
    ## time to load all pop ups
    time.sleep(2)

    try:
        closePopUpCupom = WebDriverWait.until(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div/div/div/button')))
        closePopUpCupom.click()

        time.sleep(10)
        closePopUpChat = WebDriverWait.until(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_0"]/div/div/div/div/div/div/div[1]/div[3]/div[2]')))
        closePopUpChat.click()

        time.sleep(10)
        closePopUpCookies = WebDriverWait.until(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/button')))
        closePopUpCookies.click()
    except:
        print('error pop up')

    inputCompanyName = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="company"]')))
    inputCompanyName.send_keys(companyName)

    inputFirstName = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="first_name"]')))
    inputFirstName.send_keys(customerFirstName)

    inputCnpj = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2df"]')))
    inputCnpj.send_keys(cnpj)

    time.sleep(30)
    selectCategory = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2de"]')))
    selectCategory.click()

    time.sleep(3)
    #### select by category
    selectCategoryKids = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2de"]/option[2]')))
    selectCategoryKids.click()

    inputSite = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="url"]')))
    inputSite.send_keys(site)

    inputEmail = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    inputEmail.send_keys(loginEmail)

    inputPhone = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="00N5w00000RM2dw"]')))
    inputPhone.send_keys(phone)

    buttonSend = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="formulario"]/div/form/input[10]')))
    buttonSend.click()

    time.sleep(40)



