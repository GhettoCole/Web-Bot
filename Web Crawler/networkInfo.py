import os
import logging
import requests
import time
from bs4 import BeautifulSoup
from json import loads
from prettytable import PrettyTable
from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError
from Webcrawler import WebCrawler


# log file
logging.basicConfig(filename="temp.log", level=logging.DEBUG)


# Subclass of the crawler
class NetworkIntelligence(WebCrawler):

    def __init__(self, base_url):
        # inherit superclass variable
        super().__init__(base_url)

    def network_mapper(self):
        # Do a fast NMAP scan
        logging.debug("Scan for open ports")
        command = "nmap -F " + self.base_url[8:]  # take out https://
        try:
            process = os.popen(command)
            output = str(process.read())
            # -----------------
            style = '-' * 45
            # -----------------
            print(style + " NMAP Fast Scan " + style)
            print(output)
        except Exception as e:
            print("Error:   ", e)

    def robotsFile(self):
        # robots
        try:
            # robots.txt
            robotsReq = urlopen(self.base_url+"/robots.txt")
            robots = robotsReq # store page
            if robotsReq is not None:
                bsRobots = BeautifulSoup(robots, "lxml")
                style = ("-" * 45)
                print(style + " Robots.txt " + style)
                print(bsRobots.string)
            else:
                print("Robots.txt not found!")
        except Exception as e:
            print("Error:   ", e)

    def whoIs(self):
        # whois information [extras]
        command = "whois " + self.base_url[8:]
        process = os.popen(command)
        try:
            output = str(process.read())
            style = "-" * 45
            print(style + " Whos is info " + style)
            print(output)
        except Exception as e:
            print("Error:   ", e)

    def getIP(self):
        # getting an ip through the host service
        command = "host {}".format(self.base_url[8:])
        process = os.popen(command)
        try:
            output = str(process.read())
            style = "-" * 45
            print(style, " IP ADDRESS OF " + self.base_url[8:], style)
            print(output)
        except Exception as e:
            print("Error ", e)


class ScraperInfo(WebCrawler):

    def __init__(self, base_url):
        super().__init__(base_url)

    def sourceCode(self, name='source code'):
        directory = str(os.getcwd())
        request = urlopen(self.base_url)
        # create a bs4 object, change feature to HTML.parser
        # if necessary
        bsObj = BeautifulSoup(request, "lxml")
        htmlCode = bsObj.prettify()

        file = "{}.html".format(name)
        with open(directory+file, "w") as f:
            f.write(htmlCode)
        # close
        f.close()
        print("Your file has been saved in {} as {}".format(directory, file))

    def HTTP_headers(self):
        request = urlopen(self.base_url)
        # HTTP headers
        TAB = "\t" * 5
        print(TAB, request.info())

    def siteImages(self):
        links = set()
        request = urlopen(self.base_url)
        bsObj = BeautifulSoup(request, "lxml")
        for link in bsObj.find_all('a'):
            if 'src' in link.attrs:
                # image has source
                downloadURL = link.attrs['src']
                print("[+] Storing => {}".format(downloadURL))
                links.add(downloadURL)
            else:
                pass

        index = 0
        name = "{} .jpg".format(str(index))
        directory = os.getcwd()
        try:
            for link in links:
                urlretrieve(link, name)
                index += 1
        except Exception as e:
            print("Error => ", e)


class IPLookUp(WebCrawler):

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress

    def getInformation(self):
        # JSON FILE using Freegeoip API

        request = urlopen("https://freegeoip.net/json/"+str(self.ipAddress))
        request = request.read().decode("utf-8")
        jsonFile = loads(request)

        region = jsonFile['region_name']
        countryCode = jsonFile['country_code']
        latitude = jsonFile['latitude']
        longitude = jsonFile['longitude']
        ipAddr = jsonFile['ip']
        zipCode = jsonFile['zip_code']
        timeZone = jsonFile['time_zone']
        countryName = jsonFile['country_name']
        city = jsonFile['city']

        table = PrettyTable()
        table.field_names = [
            "Region", "Country Code", "Latitude",
            "Longitude", "IP Address", "Zip Code",
            "Time Zone", "Country", "City"
        ]
        table.add_row(
            [
                region, countryCode, latitude,
                longitude, ipAddr, zipCode,
                timeZone, countryName, city
                ]
        )
        # align to the right
        table.align = "r"
        print(table)
