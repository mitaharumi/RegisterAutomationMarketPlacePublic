from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import rpa as r


def magazineLuizaRegister(displayName, platform, cnpj, companyName, tradeName, site, cep,
                          officerCommercialName, officerCommercialEmail, officerCommercialPhone,
                          officerSacName, officerSacEmail, officerSacPhone,
                          officerFinancialName, officerFinancialEmail, officerFinancialPhone,
                          officerLegalName, officerLegalEmail, officerLegalPhone,
                          officerTiName, officerTiEmail, officerTiPhone,
                          bank, agency, agencyDigit, currentAccount, currentAccountDigit):

    driver = webdriver.Chrome()
    url = 'https://marketplace-vendamais.magazineluiza.com.br/form.html'
    driver.get(url)
# page1
    inputDisplayName = driver.find_element_by_xpath('//*[@id="00Nf100000CJDD5"]')
    inputDisplayName.send_keys(displayName)

    selectPlatform = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div')
    selectPlatform.click()

    inputPlatform = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div/div/input')
    inputPlatform.send_keys(platform)
    inputPlatform.send_keys(Keys.RETURN)

    # ## find by text WebElement plataforma = driver.findElement(By.xpath("//*[text()='bring']"))
    # keyboard = Controller()
    # keyboard.press(Key.enter)

    inputCnpj = driver.find_element_by_xpath('//*[@id="00Nf100000C3mAj"]')
    inputCnpj.send_keys(cnpj)

    inputCompanyName = driver.find_element_by_xpath('//*[@id="company"]')
    inputCompanyName.send_keys(companyName)

    inputTradeName = driver.find_element_by_xpath('//*[@id="00Nf100000C3mAe"]')
    inputTradeName.send_keys(tradeName)

    inputSite = driver.find_element_by_xpath('//*[@id="URL"]')
    inputSite.send_keys(site)

    inputCep = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCf"]')
    inputCep.send_keys(cep)

    try:
        buttonNext1 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="step-template-continuar"]')))
        buttonNext1.click()
    except:
        driver.quit()
#page2
    inputOfficerCommercialName = driver.find_element_by_xpath('//*[@id="last_name"]')
    inputOfficerCommercialName.send_keys(officerCommercialName)

    inputOfficerCommercialEmail = driver.find_element_by_xpath('//*[@id="email"]')
    inputOfficerCommercialEmail.send_keys(officerCommercialEmail)

    inputOfficerCommercialPhone = driver.find_element_by_xpath('//*[@id="phone"]')
    inputOfficerCommercialPhone.send_keys(officerCommercialPhone)

    inputOfficerSacName = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCv"]')
    inputOfficerSacName.send_keys(officerSacName)

    inputOfficerSacEmail = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCp"]')
    inputOfficerSacEmail.send_keys(officerSacEmail)

    inputOfficerSacPhone = driver.find_element_by_xpath('//*[@id="00Nf100000CJDD2"]')
    inputOfficerSacPhone.send_keys(officerSacPhone)
    
    inputOfficerFinancialName = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCt"]')
    inputOfficerFinancialName.send_keys(officerFinancialName)

    inputOfficerFinancialEmail = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCn"]')
    inputOfficerFinancialEmail.send_keys(officerFinancialEmail)

    inputOfficerFinancialPhone = driver.find_element_by_xpath('//*[@id="00Nf100000CJDD0"]')
    inputOfficerFinancialPhone.send_keys(officerFinancialPhone)

    inputOfficerLegalName = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCu"]')
    inputOfficerLegalName.send_keys(officerLegalName)

    inputOfficerLegalEmail = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCo"]')
    inputOfficerLegalEmail.send_keys(officerLegalEmail)

    inputOfficerLegalPhone = driver.find_element_by_xpath('//*[@id="00Nf100000CJDD1"]')
    inputOfficerLegalPhone.send_keys(officerLegalPhone)

    if officerTiName is None:
        selectTi = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[9]/div/label/div')
        selectTi.click()


    buttonNext2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div/div[5]/button[2]')))
    buttonNext2.click()
# page3
    time.sleep(1)

    ## tribo urbana standart: monthly, day 10.
    selectMonthly = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div/label[1]/div')
    selectMonthly.click()

    selectMonthlyDay = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="dayTransferMonth"]/label[10]/span')))
    selectMonthlyDay.click()

    ## tribo urbana standart: 6x
    selectInterest = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[3]/div/div')
    selectInterest.click()

    selectInterestTimes = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div[3]/div/div/div/div/ul/li[6]')))
    selectInterestTimes.click()

    selectLegalPerson = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[4]/div[1]/label/div')
    selectLegalPerson.click()

    time.sleep(1)
    selectBank = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[6]/div[1]/div/a/span')
    selectBank.click()

    inputBank = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div[6]/div[1]/div/div/input')))
    inputBank.send_keys(bank)
    inputBank.send_keys(Keys.RETURN)

    inputAgency = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCx"]')
    inputAgency.send_keys(agency)

    if agencyDigit is not None:
        inputAgencyDigit = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCg"]')
        inputAgencyDigit.send_keys(agencyDigit)

    inputCurrentAccount = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCy"]')
    inputCurrentAccount.send_keys(currentAccount)

    if currentAccount is not None:
        inputCurrentAccountDigit = driver.find_element_by_xpath('//*[@id="00Nf100000CJDCm"]')
        inputCurrentAccountDigit.send_keys(currentAccountDigit)
    else:
        selectCurrentAccountDigit = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[8]/div[3]/div/label/div')
        selectCurrentAccountDigit.click()

    buttonNext3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[6]/button[3]')))
    buttonNext3.click()
    time.sleep(10)


def magazineLuizaRegister(displayName, platform, cnpj, companyName, tradeName, site, cep,
                          officerCommercialName, officerCommercialEmail, officerCommercialPhone,
                          officerSacName, officerSacEmail, officerSacPhone,
                          officerFinancialName, officerFinancialEmail, officerFinancialPhone,
                          officerLegalName, officerLegalEmail, officerLegalPhone,
                          officerTiName, officerTiEmail, officerTiPhone,
                          bank, agency, agencyDigit, currentAccount, currentAccountDigit):
    url = 'https://marketplace-vendamais.magazineluiza.com.br/form.html'
    r.init()
    r.url(url)

    # input display name
    r.type('//*[@id="00Nf100000CJDD5"]', str(displayName))
    r.wait(2.0)

    # click platform
    r.click('//*[@id="app"]/div[1]/div[3]/div')
    # type platform
    r.type('//*[@id="app"]/div[1]/div[3]/div/div/div/input', platform + '[enter]')

    r.wait(3.0)