""" 
This scripts will give you the items which are 
unavailable in stock at every 1 minutes of time interval
"""
import requests
import time
import json
from datetime import datetime

API_URL = 'http://localhost:8000/api/items/?unavailable=true'

def fetch_unavailable_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        items = response.json()
        filename = f"unavailable_items_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(items, f, indent=4)
        print(f"Saved unavailable items to {filename}")
    else:
        print("Error fetching data:", response.status_code)

if __name__ == '__main__':
    while True:
        fetch_unavailable_items()
        time.sleep(60)
