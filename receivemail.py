import easyimap
import smtplib
import requests
from django.http import HttpResponse


# return HttpResponse("Failed")

class getmailclass():
    def getmailfunc():
        login = 'govtechinternship@gmail.com'
        print("login assigned")
        password = 'mcONLINE123'
        print("password assigned")
        imapper = easyimap.connect('imap.gmail.com', login, password)
        print("imap connect successful")
        for mail_id in imapper.listids(limit=1):
            print("inside for loop")
            mail = imapper.mail(mail_id)
            print(mail.body)
            return mail.body
            break
        return mail.body

