import subprocess
import re
import datetime
import time
from twilio.rest import Client

account_sid = 'ACa16c887dd15c265f7f57fccd457e769e' 
auth_token = '77dc779bb675a287736df02b53234b70' 
client = Client(account_sid, auth_token) 

a=subprocess.check_output("apcaccess")
b=a.decode("utf-8")
statrgx=re.compile(r'\bSTATUS\s+:\s(\w+)')
stat=statrgx.findall(b)
curr=str(stat[0])
print(curr)
cnt=1
badcnt=1

while True:
    a=subprocess.check_output("apcaccess")
    b=a.decode("utf-8")
    statrgx=re.compile(r'\bSTATUS\s+:\s(\w+)')
    stat=statrgx.findall(b)
    curr=str(stat[0])
    print(curr)
    d=datetime.datetime.today()

    if "ONLINE" not in curr:
        print("WE ARE OFFLINE")
        badcnt=badcnt+1
        
    else:
        badcnt=1
        print("WE ARE GOOD")        
        if(cnt % 1800 == 0):
            message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='the time is  '+ str(d) +' and we are ONLINE. This will be sent every 30 minutes',
                                  #body='online we good',
                                  to='whatsapp:+919884847419'
                                  ) 
            print(message.sid)
            

    if(badcnt==2):
        d_off=datetime.datetime.today()
        message = client.messages.create( 
                                      from_='whatsapp:+14155238886',  
                                      body='we went offline at ' + str(d_off),      
                                      to='whatsapp:+919884847419' 
                                      ) 
        print(message.sid)
        
    time.sleep(1)
    cnt=cnt+1   

        
    print(cnt)
    print(badcnt)
    


