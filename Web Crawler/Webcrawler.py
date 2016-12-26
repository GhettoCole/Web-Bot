# Project: Web crawler
# Programmer: Given Lepita
# Python Version: 3.x
# Date: 2016
import os
from random import randint
import urllib.request
import urllib
from urllib.error import URLError
from bs4 import BeautifulSoup




def crawler():
    web_url = str(input('Enter URL to crawl: '))
    correct_url = 'http://' + web_url  # concat with http protocol for valid url
    request = urllib.request.urlopen(correct_url)
    # http header
    print("-------------------HTTP HEADERS-----------------")
    print(request.info())
    
    soup_object = BeautifulSoup(request, 'lxml')
    
    file = open('Response Code.html', 'w')
    file.write(str(request))
    file.close()
    
    print("\n------------------- IP Address -------------------")
    cmd = "host " + correct_url  # linux command to find url's ip address
    process = os.popen(cmd)
    ip_add = str(process.read())
    count = 14
    index_lvl = ip_add.find('has address') + count
    print('IP Address: ' + ip_add[index_lvl:])


    print("\n--------------------- RETRIEVING LINKS ---------------")
    try:
        link_number= 1
        for link in soup_object.find_all('a'):

            print("Link {}'s Title: {}".format(link_number, link.text))
            link_number += 1
    except KeyError:
        print("No \'href\' Attributes found")

    print('\n------------------------ RETRIEVING PARAGRAPHS ----------------------------')

    for para in soup_object.find_all('p'):
        print(para.text)

try:
    crawler()
except (URLError, ImportError, RuntimeError):
    print("An error due to URLError, ImporError or RuntimeError Has Occurred.\nPlease Install The Necessary Modules")
except:
    print("An \'Unknown\' Error Occurred")        


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



