from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from access import pathChromedriver


def madeiraMadeiraRegister(customerName, tradeName, cnpj, site, loginEmail, phone):

    driver = webdriver.Chrome(pathChromedriver())
    url = 'https://www.madeiramadeira.com.br/marketplace'
    driver.get(url)

    time.sleep(3)

    allowCookies = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lgpd-button-agree"]')))
    allowCookies.click()

    inputCustomerName = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-text_field-y6sStFpJHNKMnAkW0k89TA"]')))
    inputCustomerName.send_keys(customerName)

    inputTradeName = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-text_field-Fs1FrBf93ywrSX4X4YpafA"]')))
    inputTradeName.send_keys(tradeName)

    inputCnpj = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-number_field-IF2bhKXG5afi2Tjt_TZBVQ"]')))
    inputCnpj.send_keys(cnpj)

    inputSite = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-text_field-zDpe1qFc1hCEk0JpmzamZg"]')))
    inputSite.send_keys(site)

    inputLoginEmail = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-email_field-BBQ_i7fFN_jhU7N0mvjCLQ"]')))
    inputLoginEmail.send_keys(loginEmail)

    inputPhone = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-phone_field-evNkCGMRQ8WqTvCVnlB3YA"]')))
    inputPhone.send_keys(phone)

    #### conditional category
    ## list category, conditional

    selectCategory = driver.find_element_by_xpath('//*[@id="rd-checkboxes_field-b8Fk8IMIA2zWo_UMBsWa3g_Ar_e_Ventilação"]')
    selectCategory.click()

    selectPlatform = driver.find_element_by_xpath('//*[@id="rd-select_field-4TiIOXCDCIdqycWdEhf_gw"]')
    selectPlatform.click()
    selectPlatformBling = driver.find_element_by_xpath('//*[@id="rd-select_field-4TiIOXCDCIdqycWdEhf_gw"]/option[7]')
    selectPlatformBling.click()

    selectErp = driver.find_element_by_xpath('//*[@id="rd-select_field-v6Fg-1clWcHWKTn9GteR0w"]')
    selectErp.click()

    selectErpBling = driver.find_element_by_xpath('//*[@id="rd-select_field-v6Fg-1clWcHWKTn9GteR0w"]/option[4]')
    selectErpBling.click()

    ## set as option yes
    selectDevelopmentApi = driver.find_element_by_xpath('//*[@id="rd-radio_buttons_field-Ahfhu2QlM2joInM2CNcSxQ_Sim"]')
    selectDevelopmentApi.click()

    selectManualIntegration = driver.find_element_by_xpath('//*[@id="rd-radio_buttons_field-ZD7Mtbj9YOyvqhrPSGL4BA_Sim"]')
    selectManualIntegration.click()

    buttonRegister = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rd-K5y4LJ6EBRDP6KI720nnEA"]')))
    buttonRegister.click()

    time.sleep(50)

