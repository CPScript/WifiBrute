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
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, "  [+] Message from creator ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Please be responsible when hacking or using any software as it could get you in trouble or be malware ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Follow me -- https://github.com/CPScript", "- " * 3+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    print(c.ran + '-'*63)
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, "  [+] Message from creator ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Please be responsible when hacking or using any software as it could get you in trouble or be malware ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Follow me -- https://github.com/CPScript", "- " * 3+c.ran + "|")

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
