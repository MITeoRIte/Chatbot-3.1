import easyimap
import smtplib
import requests
from django.http import HttpResponse
import email, imaplib




# return HttpResponse("Failed")

class getmailclass():
    def getmailfunc():
        login = 'example@gmail.com'
        print("login assigned")
        password = 'password'
        print("password assigned")
        imapper = easyimap.connect('imap.gmail.com', login, password)
        print("imap connect successful")
        for mail_id in imapper.listids(limit=1):
            print("inside for loop")
            mail = imapper.mail(mail_id)
            return mail.body, mail.from_addr
            break
        return mail.body, mail.from_addr


    
