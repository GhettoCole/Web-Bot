class WebCrawler():
    def __init__(self, base_url):
        self.base_url = base_url

    def get_absolute_url(self):
        if self.base_url.startswith(("http://", "https://")):
            return self.base_url
        return "https://" + self.base_url
