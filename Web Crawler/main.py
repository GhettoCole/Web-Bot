from time import sleep
from networkInfo import NetworkIntelligence
from networkInfo import ScraperInfo
from networkInfo import IPLookUp
from Webcrawler import WebCrawler

def main():
    print("""
    \t--> 1: Network Intelligence
        \t--> NMAP Scans
        \t--> Robots.txt
        \t--> Whois information
    \t--> 2: Scraping
        \t--> Source Code
        \t--> HTTP(S) headers
        \t--> Links(Download Images)
    \t--> 3: IP Lookup
        \t--> IP information in table format
        \t--> IP information such as
            \t--> Region
            \t--> Longitude and Latitude
            \t--> City, Country Name and MORE!

    """)
    baseClass = int(input("Choose option:  "))

    if baseClass == 1:
        newAgent = input("Enter URL to perfom Network Intelligence on:   ")
        baseObject = NetworkIntelligence(newAgent)

        print("Perfoming Network Intelligence On {}".format(newAgent))
        sleep(0.8)
        baseObject.network_mapper()
        baseObject.robotsFile()
        baseObject.whoIs()

    elif baseClass == 2:
        newAgent = input("Enter URL to perfom Scraping on:   ")
        baseObject = ScraperInfo(newAgent)

        print("CAUTION: Make Sure You Have A Lot Of Bandwith And A Strong Signal")
        sleep(0.8)
        print("\nPerforming  Web Scraping On {}".format(newAgent))
        sleep(0.2)
        baseObject.HTTP_headers()
        baseObject.sourceCode()
        baseObject.HTTP_headers()
        baseObject.siteImages()

    elif baseClass == 3:
        newAgent = input("Enter IP Address:   ")
        baseObject = IPLookUp(newAgent)

        try:
            sleep(0.4)
            print("Extracting information about {} from Freegeoip.net".format(newAgent))
            baseObject.getInformation()
        except Exception as e:
            print("Error ", e)

    else:
        default = "https://google.com/index.html"
        baseObject = WebCrawler(default)
        baseObject.get_absolute_url()

if __name__ == "__main__":
    main()
