import os
import logging
import requests
from bs4 import BeautifulSoup
from json import loads
from prettytable import PrettyTable
from urllib.request import urlopen, urlretrieve

logging.basicConfig(filename="temp.log", level=logging.DEBUG)


class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url


class NetworkIntelligence(WebCrawler):
    def __init__(self, base_url):
        super().__init__(base_url)

    def network_mapper(self):
        logging.debug("Scan for open ports")
        command = "nmap -F " + self.base_url[8:]  # take out https://
        try:
            process = os.popen(command)
            output = str(process.read())
            style = '-' * 45
            print(style + " NMAP Fast Scan " + style)
            print(output)
        except Exception as e:
            print("Error: ", e)

    def robots_file(self):
        try:
            # robots.txt
            robots_url = self.base_url + "/robots.txt"
            robots_req = urlopen(robots_url)
            robots = robots_req.read()
            bs_robots = BeautifulSoup(robots, "lxml")
            style = "-" * 45
            print(style + " Robots.txt " + style)
            print(bs_robots.get_text())
        except Exception as e:
            print("Error: ", e)

    def who_is(self):
        command = "whois " + self.base_url[8:]
        process = os.popen(command)
        try:
            output = str(process.read())
            style = "-" * 45
            print(style + " Whois info " + style)
            print(output)
        except Exception as e:
            print("Error: ", e)

    def get_ip(self):
        command = "host {}".format(self.base_url[8:])
        process = os.popen(command)
        try:
            output = str(process.read())
            style = "-" * 45
            print(style, " IP ADDRESS OF " + self.base_url[8:], style)
            print(output)
        except Exception as e:
            print("Error: ", e)


class ScraperInfo(WebCrawler):
    def __init__(self, base_url):
        super().__init__(base_url)

    def source_code(self, name='source code'):
        directory = str(os.getcwd())
        request = urlopen(self.base_url)
        bs_obj = BeautifulSoup(request, "lxml")
        html_code = bs_obj.prettify()

        file = "{}.html".format(name)
        with open(os.path.join(directory, file), "w") as f:
            f.write(html_code)
        print("Your file has been saved in {} as {}".format(directory, file))

    def http_headers(self):
        request = urlopen(self.base_url)
        # HTTP headers
        TAB = "\t" * 5
        print(TAB, request.info())

    def site_images(self):
        links = set()
        request = urlopen(self.base_url)
        bs_obj = BeautifulSoup(request, "lxml")
        for link in bs_obj.find_all('a'):
            if 'src' in link.attrs:
                download_url = link.attrs['src']
                print("[+] Storing => {}".format(download_url))
                links.add(download_url)

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
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def get_information(self):
        try:
            url = "https://freegeoip.app/json/" + str(self.ip_address)
            response = requests.get(url)
            json_data = response.json()

            table = PrettyTable()
            table.field_names = [
                "Region", "Country Code", "Latitude",
                "Longitude", "IP Address", "Zip Code",
                "Time Zone", "Country", "City"
            ]
            table.add_row([
                json_data['region_name'], json_data['country_code'],
                json_data['latitude'], json_data['longitude'],
                json_data['ip'], json_data['zip_code'],
                json_data['time_zone'], json_data['country_name'],
                json_data['city']
            ])
            # align to the right
            table.align = "r"
            print(table)
        except Exception as e:
            print("Error: ", e)

