from bs4 import BeautifulSoup
from access import emailPathB2w

def emailCodeB2w():
    with open(emailPathB2w(), 'r') as email:
        contentsEmail = email.read()
        soup = BeautifulSoup(contentsEmail, 'lxml')
        code = soup.strong.text

        code = code.replace(" ", "")

        return code

def emailCodeAmazon():
    print('a')