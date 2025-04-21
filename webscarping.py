import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        try:
            # Open and read the webpage
            r = urllib.request.urlopen(self.site)
            html = r.read()

            # Parse HTML
            parser = "html.parser"
            sp = BeautifulSoup(html, parser)

            # Find and print article links
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                if "articles" in url:
                    print("\nhttps://news.google.com" + url)
        except Exception as e:
            print("Error:", e)


# Instantiate and run the scraper
news = "https://news.google.com/"
Scraper(news).scrape()
  
