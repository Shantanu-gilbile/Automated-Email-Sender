import ssl
import schedule
import time
from email.message import EmailMessage
import smtplib

def maill():
    email_sender = 'shangil2711@gmail.com'

    email_password = ''

    email_recevier = 'shantanu.gilbile2003@gmail.com','pratikbd18@gmail.com','adityamsahane07@gmail.com','digvijaymudde123@gmail.com'


    subject = 'check out my mail'

    body = """ 
    hii how are you??
    mail sended using Python!!!!!
    """

    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = email_recevier
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_recevier,em.as_string())

    print("Mail Sended Successfully")


def main():
    print("Inside task schedule")
    schedule.every(1).minutes.do(maill)

    while(True):  #Unconditional infinite loop
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()