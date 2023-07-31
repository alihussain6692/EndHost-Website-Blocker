import time
from datetime import datetime as dt

hosts_temp= "hosts"

# path for windows OS
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"

# Path for host file on Linux/Mac OS 

redirect="127.0.0.1"

## Websites List to be blocked during the given time at end device

website_list=["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]
b =4
while True:
    if(b == 5):
    #if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 19):
        print("Blocking websites according to given time!")
        with open (hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
                    
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()  
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Enabling websites according to time!")
    
    time.sleep(5)                              