import requests
from datetime import datetime
import os
import sys

DATE = datetime.now().strftime('%d%m%Y')
NEWSPAPERS = {
    "telegraph": "https://epaper.telegraphindia.com/epaperimages",
    "anandabazar": "https://epaper.anandabazar.com/epaperimages",
}

PAGES = 30

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

def get_newspaper(date = DATE):
    for k,v in NEWSPAPERS.items():
        if not os.path.exists(f'{k}-{date}'):
            os.makedirs(f'{k}-{date}')
        for page in range(1, PAGES+1):
            url = f"{v}////{date}////{date}-md-hr-{page}ll.png"
            print(url)
            response = requests.get(url, headers=HEADERS)
            if response.headers.get("content-type") != "image/png":
                print(f"last page reached: {page-1}")
                break
            else:
                print(f"Downloading page {k} {page}")
                with open(f"{k}-{date}/{date}-md-hr-{page}ll.png", "wb") as f:
                    f.write(response.content)
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        get_newspaper()
        exit()
    input_date = sys.argv[1]
    try:
        datetime.strptime(input_date, '%d%m%Y')
    except ValueError:
        print("Invalid date format. Please enter in DDMMYYYY format")
        exit()
    get_newspaper(date=input_date)

