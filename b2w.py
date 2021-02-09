import pyautogui as p
import rpa as r

from emailReader import readEmailToHtml
from emailCodeReader import emailCodeB2w


def b2wRegister (cnpj, loginEmail, customerName, customerCpf, customerPhone, customerPosition, site, mei, registrationState):
    r.init()
    r.url('https://www.b2wmarketplace.com.br/v3/registre-se')
    p.sleep(15)

    p.sleep(3)
    
# page1
    # cnpj
    r.type('/html/body/app-root/div/app-signup/main/section[2]/div/div/div/form[1]/div/div[1]/div/input', str(cnpj))
    # loginEmail
    r.type('/html/body/app-root/div/app-signup/main/section[2]/div/div/div/form[1]/div/div[2]/div/input', str(loginEmail))
    r.wait(5.0)

    p.screenshot('b2wCadastroPrimeiraParte.png')
    r.wait(3.0)

    # submit
    r.click('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[1]/div/div[4]/button')
    r.click('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[1]/div/div[4]/button')
    r.wait(5.0)
# page2
    if mei == True:
        # click checkbox mei
        r.click('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[2]/div/div/div/input')
    else:
        #inscriçãoEstadual
        r.type('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[2]/div/div/input', str(registrationState))
    # customerName
    r.type('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[3]/div/input', str(customerName))
    '''
        for tribo urbana, client role never will be:
        'Colaborador(a) da Empresa'
        only: owner or partner
        so, do not need a conditional for input 'Colaborador(a) da Empresa' role
    '''
    # customerPosition
    r.type('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[4]/div/select', str(customerPosition))
    # customerCpf
    r.type('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[6]/div/input', str(customerCpf))
    # customerPhone
    r.type('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[8]/div/input', str(customerPhone))
    # site
    r.type('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[7]/div/input', str(site))

    p.screenshot('b2wCadastroSegundaParte.png')

    # submit
    r.click('//*[@id="main"]/app-signup/main/section[2]/div/div/div/form[2]/div/div[11]/button')
    p.sleep(10)

    #read email, get code and confirm
    readEmailToHtml()
    p.sleep(12)
    p.hotkey('alt', 'tab')

    p.sleep(1)
    # clickEmailCodeInput()
    r.click('//*[@id="confirmEmail"]/div/div/div[2]/div/div/input')
    r.click('//*[@id="confirmEmail"]/div/div/div[2]/div/div/input')
    r.type('//*[@id="confirmEmail"]/div/div/div[2]/div/div/input', str(emailCodeB2w()))
    p.sleep(3)
    # p.write(codeEmailB2w())
    p.sleep(3)
    # clickEmailCodeConfirm()
    r.click('//*[@id="confirmEmail"]/div/div/div[3]/div[2]/button')
    r.click('//*[@id="confirmEmail"]/div/div/div[3]/div[2]/button')

    r.wait(10.0)
    p.screenshot('b2wTerceiraParte.png')
    r.wait(1.0)
    r.close()