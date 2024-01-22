#>>-------------------------------------->>

#*OTP ProJect
import math
import os
import random

from twilio.rest import Client

rno = ""
valed = 0

def genrno():
    digits = "0123456789"
    global rno
    for grno in range(6):
        rno += digits[math.floor(random.randint(0,9))]
    
    return rno

genrno()

# print("Random No. is " + rno)


ACCOUNTSID= os.environ.get('ACCOUNT SID')
AUTHTOKEN = os.environ.get('AUTH TOKEN')

sendto = +919579931406

def mssender(*sendto):

    client = Client(ACCOUNTSID, AUTHTOKEN) 
    message = client.messages.create(  
                                  messaging_service_sid='MG0c21cbee2b79e83e01f9ce5456938d10', 
                                  body='Hi There Your OTP is- '+ rno,      
                                  to=sendto 
                              ) 
    print("OTP Has Been Sent To- ",sendto)

mssender(sendto)

ui = input("Input- ")

def uival():
    global rno
    global valed
    if rno == ui:
        valed = 1
        print("Ok Auth Done!! ")
    else:
        print("Nope")
        valed = 0
        

uival()

