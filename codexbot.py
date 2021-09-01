import urllib.request
from colorama import Fore, init
import os
init()

print (Fore.YELLOW + """
     ______   ____     ____     ______   _  __    ____    ____   ______
    / ____/  / __ \   / __ \   / ____/  | |/ /   / __ )  / __ \ /_  __/
   / /      / / / /  / / / /  / __/     |   /   / __  | / / / /  / /   
  / /___   / /_/ /  / /_/ /  / /___    /   |   / /_/ / / /_/ /  / /    
  \____/   \____/  /_____/  /_____/   /_/|_|  /_____/  \____/  /_/                                                                                                                                                                
""" + Fore.RESET)
print(Fore.GREEN + "      A simple script to download "+Fore.BLUE+"World Digital Library"+Fore.GREEN+" books"+ Fore.RESET)
print ("\n")
def userinput():
    try:
        global index
        global page
        global pages
        index = input("Book index (example: 3042): ")
        page = int(input("Start page: "))
        pages = int(input("Final page: "))
    except:
        print(Fore.RED + "ERROR, try again." + Fore.RESET)
        userinput()

userinput()
os.mkdir(str(index))
print(Fore.GREEN + "Downloading pages..." + Fore.RESET)
while page < pages+1:
    url = "https://dl.wdl.org/"+index+"_1_"+str(page)+".png"

    filename = index+"_1_"+str(page)+".png"
    try:
        urllib.request.urlretrieve(url, "./"+str(index)+"/"+filename)
        page += 1
    except:
        os.remove(filename)
        urllib.request.urlretrieve(url, "./"+str(index)+"/"+filename)
        page += 1
