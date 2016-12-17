import requests
from bs4 import BeautifulSoup

def get_rss_feed(website_url):
    rsslinks=[]
    if website_url is None:
        print("URL should not be null")
    else:
        source_code = requests.get(website_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")
        for link in soup.find_all("link", {"type" : "application/rss+xml"}):
            href = link.get('href')
            rsslinks.append(href)
        return rsslinks
            """
            Function to extract the feed URL
            """
  
