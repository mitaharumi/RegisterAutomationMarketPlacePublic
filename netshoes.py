from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from access import pathChromedriver

def netshoesRegister(companyName, cnpj, address, site):
    driver = webdriver.Chrome(pathChromedriver())
    url = 'https://www.netshoes.com.br/marketplace'
    driver.get(url)

    try:
        inputCompanyName = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/form/div[2]/div/input')))
        inputCompanyName.send_keys(companyName)
    except:
        error = 'ERROR COMPANY NAME'
        print(error)
    try:
        inputCnpj = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div/input')))
        inputCnpj.send_keys(cnpj)
    except:
        error = 'ERROR CNPJ'
        print(error)
    try:
        inputaddress = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="V2ViRm9ybUNhcHR1cmVCbG9jazo4MTdiOWMxMi0zZWQ1LTExZWItOThlZi0zYmY1N2NhYTQ3ZWE"]')))
        inputaddress.send_keys(address)
    except:
        error = 'ERROR address'
        print(error)
    #### chose by category
    try:
        selectCategory= WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="V2ViRm9ybUNhcHR1cmVCbG9jazo4MTdiYzMyMC0zZWQ1LTExZWItOThlZi0zYmY1N2NhYTQ3ZWE"]')))
        selectCategory.click()

        selectCategoryArtes = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="524"]')))
        selectCategoryArtes.click()

    except:
        error = 'ERROR CATEGORY'
        print(error)
    try:
        inputSite = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="V2ViRm9ybUNhcHR1cmVCbG9jazo4MTdiYzMyMS0zZWQ1LTExZWItOThlZi0zYmY1N2NhYTQ3ZWE"]')))
        inputSite.send_keys(site)
    except:
        error = 'ERROR SITE'
        print(error)
    try:
        selectBranch = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="V2ViRm9ybUNhcHR1cmVCbG9jazo4MTdiYzMyMC0zZWQ1LTExZWItOThlZi0zYmY1N2NhYTQ3ZWE"]')))
        selectBranch.click()

        ### can select more tan 1
        selectBranchVarejista = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="232"]')))
        selectBranchVarejista.click()

    except:
        error = 'ERROR BRANCH COMPANY'
        print(error)

    # try:
    #     input = WebDriverWait(driver, 20).until(
    #         EC.element_to_be_clickable((By.XPATH, '')))
    #     input.send_keys()
    # except:
    #     error = 'ERROR '
    #     print(error)
    #
    # try:
    #     input = WebDriverWait(driver, 20).until(
    #         EC.element_to_be_clickable((By.XPATH, '')))
    #     input.send_keys()
    # except:
    #     error = 'ERROR '
    #     print(error)