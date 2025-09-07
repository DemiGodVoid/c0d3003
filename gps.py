import requests
import time
import os

RED = "\033[91m"
RESET = "\033[0m"

def fetch_logs():
    base_url = "https://vmpx.top/tools/"
    logs_file = "logs.txt"

    print(RED + "Use this link: https://vmpx.top/tools/weather.php" + RESET)

    while True:
        try:
            r = requests.get(base_url + logs_file, timeout=5)
            if r.status_code == 200 and r.text.strip():
                os.system("cls" if os.name == "nt" else "clear")
                print(RED + "Use this link: https://vmpx.top/tools/weather.php" + RESET)
                print(RED + "Log found!" + RESET)
                print("\n--- logs.txt ---")
                print(r.text.strip())

                
                choice = input(RED + "\nPress 'c' to clear logs or Enter to continue: " + RESET).strip().lower()
                if choice == "c":
                    try:
                        requests.post(base_url + logs_file, data="")  
                        print(RED + "Logs cleared remotely!" + RESET)
                    except Exception:
                        print(RED + "Failed to clear logs." + RESET)

            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(RED + "Use this link: https://vmpx.top/tools/weather.php" + RESET)
                print(RED + "Waiting for logs..." + RESET)
        except Exception:
            os.system("cls" if os.name == "nt" else "clear")
            print(RED + "Use this link: https://vmpx.top/tools/weather.php" + RESET)
            print(RED + "Waiting for logs..." + RESET)

        time.sleep(5)

if __name__ == "__main__":
    try:
        fetch_logs()
    except KeyboardInterrupt:
        print("\n" + RED + "Stopped by user." + RESET)
