# Project: Web Crawler
# Programmer: Given Lepita
# Python Version: 3
# Date: 2016
import os, urllib, requests, time, logging
from random import *
from urllib.request import *
from bs4 import BeautifulSoup
import urllib.parse
from urllib.error import URLError, HTTPError

class WebCrawler():
    def __init__(self, base_url):
        self.base_url = 'https://' + base_url
        
    def crawling_spider(self):
        logging.basicConfig(filename='web_crawler.log', level=logging.DEBUG)
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        
        logging.debug('Step 1 - Define headers and URL to avoid restrictions as a robot')
        request_politely = urllib.request.Request(self.base_url, headers=headers)
        request = urlopen(request_politely)
        logging.info('URL parsed successfully with no problems')
        html = request
        print("--------------------------------------- HTTP HEADERS ---------------------------------------")
        print(request.info())
        
        beautiful_soup_object = BeautifulSoup(request, 'lxml')
        source_code = requests.get(self.base_url)
        print("\n\n\t\t\t\tSaving The Source Code\n")
        time.sleep(3)
        print("Your directory before saving files: "+str(os.listdir()))
        logging.debug('Step 2 - Writing the source code to the specified file in binary mode')
        file_id = self.base_url[8:19]
        contents = open(str(file_id)+' Source code.html', 'wb')
        for bits in source_code.iter_content(10000):
            contents.write(bits)
            
        contents.close()
        logging.info('Source File successfully written and saved')
        time.sleep(3)
        print("Source Code Saved To The Current Working Directory\n")
        print("Your directory After saving files: "+str(os.listdir()))
        print("--------------------------------------- IP ADDRESS ---------------------------------------")
        logging.warning('sites with several ip address might not be successful to optain their ip')
        cmd = 'nslookup ' + self.base_url
        process = os.popen(cmd)
        ip_address = str(process.read())
        print('\t\t\t\t\tIP ADDRESS\t\t\t\t\n', ip_address)
        
        print("\n--------------------------------------- RETRIEVING LINKS ---------------------------------------\n")
        logging.debug('Step 3 - Find all links')
        try:
            link_id = 1
            for link in beautiful_soup_object.find_all('a'):
                if 'href' in link.attrs:
                    print("TITLE: {}".format(link.text), end=" ")
                    print(" --- Link {}: {}\n".format(link_id, link['href']))
                link_id += 1
            logging.info('Links printed successfully')
        except Exception as e:
            print("An error occurred\n", str(e))
            
        print('\n---------------------------------------  RETRIEVING PARAGRAPHS ---------------------------------------\n')
        logging.debug('Step 4 - Find all text with tags defined')
        for paragraph in beautiful_soup_object.find_all({'p', 'div', 'span'}):
            print(paragraph.text)
            
def take_img(url):
    start_n = randint(1, 9000)
    end_n = str(start_n) + "image.jpg" # if need be, change the image extension such as jpeg, jpg, png ect.
    urllib.request.urlretrieve(url, end_n)


print('\n------------------------ DOWNLOADING IMAGES ----------------------------')
download = str(input("Enter the URL of the image to download: "))



        
def Main():
    url = str(input("Enter URL to crawl: "))
    spider = WebCrawler(url)
    spider.crawling_spider()
    logging.info('Crawled success fully')
    try:
        take_img(download)
    except:
        print("An \'Unknown\' Error Occurred.")
if __name__ == '__main__':
    Main()
