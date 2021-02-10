from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from access import pathChromedriver

def viaVarejoRegister(customerName, tradeName, cnpj, site, loginEmail, phone):

    driver = webdriver.Chrome(pathChromedriver())
    url = 'https://pas.viavarejo.com.br/cadastro/quero-vender'
    driver.get(url)

    time.sleep(3)
    windowEvaluation = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/button')))
    windowEvaluation.click()

    inputLoginEmail = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-email_field-BBQ_i7fFN_jhU7N0mvjCLQ"]')))
    inputLoginEmail.send_keys(loginEmail)

    