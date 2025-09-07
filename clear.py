import requests

RED = "\033[91m"
RESET = "\033[0m"

def clear_logs():
    url = "https://vmpx.top/tools/clear.php"  

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(RED + "Logs cleared successfully!" + RESET)
            print("Server response:", response.text)
        else:
            print(RED + f"Failed to clear logs. Status code: {response.status_code}" + RESET)
    except Exception as e:
        print(RED + f"Error clearing logs: {e}" + RESET)

if __name__ == "__main__":
    clear_logs()
