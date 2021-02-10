from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from access import pathChromedriver, loginPassword
import rpa as r


def merdadoLivreRegister(cnpj, companyName, loginEmail):
    url = 'https://cutt.ly/4kwYWL5'

    driver = webdriver.Chrome(pathChromedriver())
    driver.get(url)

    time.sleep(3)

    inputCnpj = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="tax_id"]')))
    inputCnpj.send_keys(cnpj)


    inputCompanyName = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="business_name"]')))
    inputCompanyName.send_keys(companyName)

    inputLoginEmail = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    inputLoginEmail.send_keys(loginEmail)

    inputPassword = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
    inputPassword.send_keys(loginPassword())

    # ##### cant accept terms
    # selectTerms = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="root-app"]/div/form/div[2]/div/div[2]/div[1]/div/div[5]/label/span[2]')))
    # selectTerms.click()
    #
    # ##### robot verification
    # selectRobot = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[4]')))
    # selectRobot.click()

    time.sleep(50)
