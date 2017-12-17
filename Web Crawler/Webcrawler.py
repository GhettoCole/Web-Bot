class WebCrawler():
    def __init__(self, base_url):
        self.base_url = base_url

    def get_absolute_url(self):
        if self.base_url[:7] == "https://":
            return self.base_url
        elif self.base_url[:6] == "http://":
            return self.base_url
        else:
            return "https://" + self.base_url
