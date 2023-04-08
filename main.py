import colorama
import pyautogui
import time
from colorama import Fore, Back, Style


colorama.init()

def main():
    while True:
        command = input(Fore.RED + "Enter a command: " + Style.RESET_ALL)
        if command == "start":
            time.sleep(1)
            print(Fore.GREEN + "Starting..." + Style.RESET_ALL)

            data = open("./data/countries.txt", "r")

            for j in data:
                pyautogui.typewrite(j)
                pyautogui.press("enter")
            
            print(Fore.GREEN + "Done!" + Style.RESET_ALL)
        elif command == "help":
            print(Fore.GREEN + "Commands:" + Style.RESET_ALL)
            print(Fore.GREEN + "start - Start's the program." + Style.RESET_ALL)
            print(Fore.GREEN + "help - Display's this message." + Style.RESET_ALL)
            print(Fore.GREEN + "exit - Exit's the program." + Style.RESET_ALL)
            print(Fore.GREEN + "credits - Display credits." + Style.RESET_ALL)
        elif command == "exit":
            print('Exiting...')
            break
        elif command == "credits":
            print(Fore.GREEN + "Credits:" + Style.RESET_ALL)
            print(Fore.GREEN + "Made by: ItsNotAlexy | https://github.com/ItsNotAlexy" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid command!" + Style.RESET_ALL)

main()
