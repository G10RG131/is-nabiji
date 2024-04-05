import requests
import concurrent.futures
import time
import multiprocessing
import threading
from multiprocessing import Process, Pool


urls = [
    'https://commondatastorage.googleapis.com/codeskulptor-assets/week7-button.m4a',
    'https://codeskulptor-demos.commondatastorage.googleapis.com/pang/paza-moduless.mp3',
    'https://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/theme_01.mp3'
]


def download(urls):
    data = requests.get(urls).content
    name = urls.split('/')[3]
    name = f"{name}.mp3"
    with open(name, "wb") as mp3:
        mp3.write(data)
        print(f"{name} downloaded successfully")


start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, urls)


end = time.time()
print("Time taken: ", end - start)

def find_even():
    even_numbers = [num for num in range(30, 51) if num % 2 == 0]
    print("Even numbers:", even_numbers)

def find_odd():
    odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
    print("Odd numbers:", odd_numbers)


t1 = threading.Thread(target=find_even)
t2 = threading.Thread(target=find_odd)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program finished.")