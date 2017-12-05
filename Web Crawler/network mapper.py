# Programmer: Given Lepita
import os, logging, requests, time
from urllib.request import urlretrieve, urlopen, Request
from crawler import WebCrawler
from bs4 import BeautifulSoup


# Subclass of the crawler
class NetworkIntelligence(WebCrawler):

	def __init__(self, base_url):
    	# inherit superclass variable
		super().__init__(base_url)

	def network_mapper(self):
		# Do a fast NMAP scan
		logging.debug("Scan for open ports")
		command = "nmap -F" + self.base_url[8:]  # take out https://
		try:
			process = os.popen(command)
			output = str(process.read())
			# -----------------
			style = '-' * 45
			# -----------------
			print(style + " NMAP Fast Scan " + style)
			print(output)
		except Exception as e:
			print("Error:	", e)

	def robotsFile(self):
		# robots
		try:
			robotsReq = urllib.request.urlopen(self.base_url+"/robots")
			robots = robotsReq # store page
			if robotsReq != None:
				bsRobots = BeautfulSoup(robots, "lxml")
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
			print("Error:	", e)


class ScraperInfo(WebCrawler):
	def __init__(self, base_url):
		super().__init__(base_url)

	def sourceCode(self, directory='/', name='source code'):
		request = urllib.urlopen(self.base_url)
		# create a bs4 object, change feature to HTML.parser
		# if necessary
		bsObj = BeautifulSoup(request, "lxml")
		htmlCode = bsObj.prettify()

		file = "{}.html".format(name)
		with open(str(directory)+file, "w") as f:
			f.write(htmlCode)
		# flush and close
		f.flush()
		f.close()
		print("Your file has been saved in {} as {}".format(directory, file))
	
	def HTTP_headers(self):
    	request = urllib.urlopen(self.base_url)
		# HTTP headers
		TAB = "\t" * 5
		print(TAB, request.info())
	
	def siteImages(self):
		links = set()
		request = urllib.urlopen(self.base_url)
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
	
			