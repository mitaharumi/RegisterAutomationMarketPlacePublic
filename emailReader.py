'''
researches:
read email in python: https://www.thepythoncode.com/articlereading-emails-in-python
RFC 822: https://tools.ietf.org/html/rfc822
'''
'''
Através do uso do tipo multipart, MIME permite mensagens com vários tipos de construções em árvore, onde os nós da folha são qualquer tipo de mensagem multipart e os nós não-folha são alguma variante do tipo multipart. Veja alguns mecanismos suportados: 
    Textos simples usando text/plain (este é o valor padrão para o "Content-type:")
    Texto com arquivos (ficheiros) anexos (multipart/mixed com uma parte text/plain e outra não-textual). Uma mensagem MIME incluindo um arquivo anexo geralmente é indicada o nome original do anexo no "Content-disposition:" dentro do cabeçalho.
    Respostas com anexos originais (multipart/mixed com uma parte text/plain e a mensagem original como um MIME message/rfc822)
    Conteúdo alternativo, é usado quando uma mensagem é enviada em texto simples e, por exemplo, um cliente de email a transforma em HTML para o destino, o MIME será (multipart/alternative com o mesmo conteúdo do texto simples em text/plain mas o MIME transformado em text/html)
    Muitas outras construções de mensagens.
'''

import imaplib #pip install python - imap
import email #pip install emails
from email.header import decode_header #standard library
import webbrowser
import os

from access import emailUser, emailPassword

# function to create folders without spaces and special characters.
def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

def readEmailToHtml():
    username = emailUser()
    password = emailPassword()

    ## connect to the IMAP server

    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
    ## list of IMAP servers for most commonly used email providers https://www.systoolsgroup.com/imap/

    ## for Gmail account: allow less secure apps on account
    ## manage google account > security > less secure


    # imap.select() method, which selects a mailbox (Inbox, spam, etc.), we've chose INBOX folder
    ## imap.list() method to see the available mailboxes
    # message variable: contains number of total messages in that folder (inbox folder)
    # status is just a message that indicates whether we received the message successfully
    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 1 # variable is the number of top email messages want to retrieve
    # total number of emails
    messages = int(messages[0])

    # range(messages, messages-N, -1):
    #   means going from the top to the bottom
    #   the newest email messages got the highest id number,
    #   the first email message has an ID of 1,
    ## to extract the oldest email addresses change it to something like range(N)

    for i in range(messages, messages-N, -1):
        # imap.fetch() method fetches the email message by ID (using the standard format specified in RFC 822)
        res, msg = imap.fetch(str(i), "(RFC822)")

        for response in msg:
            if isinstance(response, tuple):
                # parse the bytes returned by the fetch() method to a proper message object
                msg = email.message_from_bytes(response[1])

                # decode the email subject
                ## decode_header() to decode the subject of the email address to human readable unicode
                subject, encoding = decode_header(msg["Subject"])[0]

                # if it's a bytes, decode to str
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)

                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                print("From:", From)

                # if the email message is multipart
                ## means it contains multiple parts
                ##  for instance: an email message can contain the text/html content and text/plain parts
                ##  which means it has the HTML version and plain text version of the message.
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            print(body)
                        elif "attachment" in content_disposition:
                            # download attachment
                            filename = part.get_filename()
                            if filename:
                                folder_name = clean(subject)
                                if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(folder_name)
                                filepath = os.path.join(folder_name, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))

                # if the email message is not multipart
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)

                if content_type == "text/html":
                    # if it's HTML, create a new HTML file and open it in browser
                    folder_name = clean(subject)
                    if not os.path.isdir(folder_name):
                        # make a folder for this email (named after the subject)
                        os.mkdir(folder_name)
                    filename = "index.html"
                    filepath = os.path.join(folder_name, filename)
                    # write the file
                    open(filepath, "w").write(body)
                    # open in the default browser
                    webbrowser.open(filepath)
                print("="*100)
    # close the connection and logout
    imap.close()
    imap.logout()