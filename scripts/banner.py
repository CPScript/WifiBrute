import os
import platform
from scripts import colors
c = colors


logo = f"""
 ▄█     █▄   ▄█     ▄████████  ▄█                             
███     ███ ███    ███    ███ ███                             
███     ███ ███▌   ███    █▀  ███▌                            
███     ███ ███▌  ▄███▄▄▄     ███▌                            
███     ███ ███▌ ▀▀███▀▀▀     ███▌                            
███     ███ ███    ███        ███                             
███ ▄█▄ ███ ███    ███        ███                             
 ▀███▀███▀  █▀     ███        █▀                              
                                                              
▀█████████▄     ▄████████ ███    █▄      ███        ▄████████ 
  ███    ███   ███    ███ ███    ███ ▀█████████▄   ███    ███ 
  ███    ███   ███    ███ ███    ███    ▀███▀▀██   ███    █▀  
 ▄███▄▄▄██▀   ▄███▄▄▄▄██▀ ███    ███     ███   ▀  ▄███▄▄▄     
▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ███    ███     ███     ▀▀███▀▀▀     
  ███    ██▄ ▀███████████ ███    ███     ███       ███    █▄  
  ███    ███   ███    ███ ███    ███     ███       ███    ███ 
▄█████████▀    ███    ███ ████████▀     ▄████▀     ██████████ 
               ███    ███                                     
                          {c.c + "Author: "+c.y+"CPScript"}                                                                                                                                   
"""
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")


def banner():
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, "  [+] About CPScript ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] CPS is a coder that works on Networking, Malware, and Hacks ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] You can find more here--> https://github.com/CPScript/", "- " * 3+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    print(c.ran + '-'*63)
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, "  [+] About CPScript ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] CPS is a coder that works on Networking, Malware, and Hacks ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] You can find more here--> https://github.com/CPScript/", "- " * 3+c.ran + "|")
def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
