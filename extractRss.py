import requests
from bs4 import BeautifulSoup

def get_rss_feed(website_url):
    if website_url is None:
        print("URL should not be null")
    else:
        source_code = requests.get(website_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")
        for link in soup.find_all("link", {"type" : "application/rss+xml"}):
            href = link.get('href')
            print("RSS feed for " + website_url + " is -->" + str(href))
#The Above function will extract the RSS feed from any link provided to it. And print it out.
#To use the function simple invoke the function with the website URL passed in the string
