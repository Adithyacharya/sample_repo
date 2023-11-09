import imaplib
import email
from dateutil import parser
from utils.commons import read_data_from_config

def test_get_the_email():
    # Read test data from config file
    config = read_data_from_config("./mmp_config.ini")
    user,password = config['test_data']['email'],config['test_data']['pwd']

    # URL for IMAP Connection
    imap_url = 'imap.gmail.com'
    # Connection with GMAIL using SSL
    gmail = imaplib.IMAP4_SSL(imap_url)

    # Login to gmail
    gmail.login(user,password)

    # Select Inbox to fetch messages
    gmail.select('Inbox')

    key ='FROM'
    value = 'do-not-reply'
    _,data = gmail.search(None, key, value)

    mail_id_list = data[0].split()
    messages = []
    for num in mail_id_list:
        # RFC822 is used to return whole message body
        mail_type,mail_data = gmail.fetch(num,'(RFC822)') 
        messages.append(mail_data)
    
    for msg in messages[::-1]:
        for response in msg:
            if type(response) is tuple:
                actual_message = email.message_from_bytes((response[1]))
                print("\n")
                print("------------------------------")
                # print(actual_message)
                print("SUB : "+actual_message['subject'])
                date_msg=parser.parse(str(actual_message['date'])).strftime("%Y-%m-%d %H:%M:%S")
                print("TIMESTAMP : "+date_msg)

