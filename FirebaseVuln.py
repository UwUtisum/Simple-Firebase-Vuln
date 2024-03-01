import requests
import os
from colorama import Fore
os.system('cls')
print(Fore.RED+"Please note: this script is for educational purposes only")
#---------user inputs--------#
FB_URL = input(Fore.GREEN+"Please enter the Firebase URL you want to write to (Example of URL: https://XXXXXXX.firebaseio.com/.json): ")
data = input(Fore.GREEN+"please enter the data you want to write (preferably write Json data here): ")
#----writeing to Database----#
rsp = requests.put(FB_URL,json=data)
#--------status codes--------#
if rsp.status_code == 200:
    print (Fore.GREEN+"Data Successfully written to Firebase server")
elif rsp.status_code == 401:
    print (Fore.RED+"Error: 401 Accsess Denied")
elif rsp.status_code == 404:
    print (Fore.RED+"Error: 404 Firebase Database Not Found")
else:
    print (Fore.RED+"Error: An Unknown Error Occurred, unable to send data")
#--Script made by leah Kemp--#