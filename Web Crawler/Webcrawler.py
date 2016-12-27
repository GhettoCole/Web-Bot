# Project: Web crawler
# Programmer: Given Lepita
# Python Version: 3.x
# Date: 2016
import os, threading, urllib, requests
from random import *
from urllib.request import *
from bs4 import BeautifulSoup
from urllib.error import URLError
import time

class WebCrawler(threading.Thread):
    def __init__(self, base_url):
        threading.Thread.__init__(self)
        self.base_url = "http://" + base_url
        

        
    def run(self):
        request = urlopen(self.base_url)
        html = request
        print("------------------- HTTP HEADERS -----------------\n")
        print(request.info())
        
        beautiful_soup_object = BeautifulSoup(request, 'lxml')
        source_code = requests.get(self.base_url)
        
        print("Saving The Source Code")
        time.sleep(3)
        contents = open('Source Code.txt', 'wb')
        for bits in source_code.iter_content(10000):
            contents.write(bits)

        contents.close()
        
        time.sleep(3)
        print("Source Code Saved As \'Source Code.txt\'")
        
        print("\n------------------------- IP ADDRESS -------------------------\n")
        cmd = "nslookup " + self.base_url
        process = os.popen(cmd)
        ip_address = str(process.read())
        print('IP ADDRESS: ', ip_address)
        
        print("\n---------------------- RETRIEVING LINKS ----------------------\n")
        try:
            link_number = 1
            for link in beautiful_soup_object.find_all('a'):
                print("Link {}'s Title: {}".format(link_number, link.text))
                link_number += 1
        except NameError:
            print("Links Not Found")
            
        print('\n------------------------------- RETRIEVING PARAGRAPHS ------------------------------')
        for paragraph in beautiful_soup_object.find_all('p'):
            print(paragraph.text)
            

def Main():
    first_url = str(input("Enter URL To Crawl: "))
    
    
    first_thread = WebCrawler(first_url)
    first_thread.run()
    
    second_url = str(input("Enter Another URL To Crawl: "))
    
    second_thread = WebCrawler(second_url)
    second_thread.run()
    
    
    third_url = str(input("Enter Another URL To Crawl: "))
    third_thread = WebCrawler(third_url)
    third_thread.run()
    

if __name__ == '__main__':
    Main()


def take_img(url):
    start_n = randint(1, 9000)
    end_n = str(start_n) + "image.jpg" # if need be, change the image extension such as jpeg, jpg, png ect.
    urllib.request.urlretrieve(url, end_n)


print('\n------------------------ DOWNLOADING IMAGES ----------------------------')
download = str(input("Enter the URL of the image to download: "))


try:
    take_img(download)
except:
    print("An \'Unknown\' Error Occurred.")

