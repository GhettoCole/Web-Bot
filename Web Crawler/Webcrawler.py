# Project: Web Bot
# Programmer: Given Lepita
# Python Version: 3.x
# Date: 2017

import os, urllib, requests, time, logging
from random import *
from urllib.request import *
from bs4 import BeautifulSoup
import urllib.parse
from urllib.error import URLError, HTTPError

class WebCrawler():
    def __init__(self, base_url):
        # concatinate with protocol
        self.base_url = 'https://' + base_url

    def crawling_spider(self):
        # create the log file for debugging
        logging.basicConfig(filename='web_crawler.log', level=logging.DEBUG)
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

        logging.debug('Step 1 - Define headers and URL to avoid restrictions as a robot')
        # Add headers to avoid restrictions of robots and bypass the API
        request_politely = urllib.request.Request(self.base_url, headers=headers)
        request = urlopen(request_politely)
        logging.info('URL parsed successfully with no problems')
        html = request
        # HTTP HEADERS FOR INFORMATIONAL PURPOSES
        print("--------------------------------------- HTTP HEADERS ---------------------------------------")
        print(request.info())

        # BeatifulSoup object with a feature of lxml as default
        # change to HTML.parser if necessary
        beautiful_soup_object = BeautifulSoup(request, 'lxml')
        source_code = requests.get(self.base_url)
        # adding tabs for viewers purpose and cleaner display
        print("\n\n\t\t\t\tSaving The Source Code\n")
        time.sleep(3) # sleep while saving

        # View the directory for showing the current files before saving
        print("Your directory before saving files: "+str(os.listdir()))
        logging.debug('Step 2 - Writing the source code to the specified file in binary mode')
        file_id = self.base_url[8:19]  # take out https:// from the url for naming purposes
        contents = open(str(file_id)+' Source code.html', 'wb')
        # write the info bit by bit
        for bits in source_code.iter_content(10000):
            contents.write(bits)

        contents.close() # close file after writing to it
        logging.info('Source File successfully written and saved')
        time.sleep(3)
        # View the directory for showing the files after saving
        # added files -
        # 1 - web_clawler.log
        # 2 - www.example.Source.html
        print("Source Code Saved To The Current Working Directory\n")
        print("Your directory After saving files: "+str(os.listdir()))
        print("--------------------------------------- IP ADDRESS ---------------------------------------")
        # IP address might not be shown due to sites with several IP address
        logging.warning('sites with several ip address might not be successful to optain their ip')
        # nslookup command for linux and Macintosh OS'es, for windows change to ping
        cmd = 'nslookup ' + self.base_url
        process = os.popen(cmd)
        ip_address = str(process.read())
        print('\t\t\t\t\tIP ADDRESS\t\t\t\t\n', ip_address)

        print("\n--------------------------------------- RETRIEVING LINKS ---------------------------------------\n")
        logging.debug('Step 3 - Find all links')
        try:
            link_id = 1
            links = set()
            for link in beautiful_soup_object.find_all('a'):
                if 'href' in link.attrs:
                    # count for a new page url link
                    page_url = link.attrs['href']
                    print("Link {}: {}".format(link_id, page_url))
                    links.add(page_url)
                    link_id += 1
            logging.info('Links printed successfully')
            # saving links to a file
            links_found = open('page_links.txt', 'w')
            for each in links:
                links_found.write(each+"\n") # not sure
            links_found.close()
        except Exception as e:
            print("An error occurred:\n", str(e))

        print('\n---------------------------------------  RETRIEVING PARAGRAPHS ---------------------------------------\n')
        logging.debug('Step 4 - Find all text with tags defined')
        for paragraph in beautiful_soup_object.find_all('p'):
            print(paragraph.text)


        print("\n-------------------------------------- IMAGE Links For " + str(self.base_url) + " -------------------------------------\n")
        logging.debug("Step 5 - Find all links of this pages images")
        # works for the images stored on the same server as of the web page
        image_urls = set()
        for image in beautiful_soup_object.find_all('img'):
            image_links = self.base_url + "/" + image['src']
            print(image_links)
            image_urls.add(image_links)

        image_links = open('image_links.txt', 'w')
        for each in image_urls:
            image_links.write(each+"\n")

        image_links.close()

    def network_mapper(self):
        """Fast nmap scan"""
        logging.debug("nmap scan for open ports")
        command = "nmap -F " + self.base_url[8:] #https:// - taken out
        process = os.popen(command)
        output = str(process.read())
        print("\n------------------------------------------------ Nmap Fast Scan Results ---------------------------------------")
        print(output+"\n")

    def whois(self):
        """Fast nmap scan"""
        command = "whois " + self.base_url[8:] #https:// - taken out
        process = os.popen(command)
        output = str(process.read())
        print("\n------------------------------------------------ Whois info Results ---------------------------------------")
        print(output+"\n")

    def crawler_robots(self):
        "Robots.txt"
        try:
            request = urllib.request.urlopen(self.base_url+'/robots.txt')
            answer = request
            bs_robots = BeautifulSoup(answer, 'lxml')
            print("\n------------------------------------------------ Robots information (For caution while scraping) ------------------------------------------------")
            print(bs_robots.string)
        except Exception as e:
            print("Error: ", str(e))

def take_img(url):
    start_n = name
    end_n = str(start_n) + "image.jpg" # if need be, change the image extension such as jpeg, jpg, png ect.
    urllib.request.urlretrieve(url, end_n)


print('\n------------------------ DOWNLOADING IMAGES ----------------------------')
name = input("Enter name to give to your image: ")
download = str(input("Enter the URL of the image to download: "))


def Main():
    try:
        url = str(input("Enter URL to crawl: "))
        bot = WebCrawler(url)
        bot.crawling_spider()
        bot.crawler_robots()
        bot.network_mapper()
        bot.whois()
        logging.info('Crawled successfully')
    except (URLError, HTTPError):
        print("An error occurred. It may be due to an HTTPError, check if your internet connection is running.")
        print("If its not due to the internet connection, It may be due to a URLError, check if you enter a correct URL")
        print("Valid URL example: www.example.com/your_query_page/your_query_document.html")
        print("Invalid URL example: ww.shdk.om/hfjja.hj/")
    try:
        take_img(download)
    except Exception as e:
        print("Error: ", str(e))
if __name__ == '__main__':
    Main()
