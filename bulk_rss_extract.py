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
def get_urls(inputfile):
    urls_file = open(inputfile)
    urls = []
    g=''
    for lines in url_file:
        g=g+'\n'
    GRUBER_URLINTEXT_PAT = re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
    urls.append(re.findall(GRUBER_URLINTEXT_PAT, g)[0][0])
    urls_file.close()
    return urls
def get_bulk_links(urls):
    g=""
    for url in urls:
        myrss=get_rss_feed(url)
        if len(myrss)==0:
            g+=url+" has no RSS links\n"
        else:
            for links in myrss:
                g+=url+" ---> " +links
    return g


#The main function 
#Enter the input as well as the output file path
def main():
    print("Enter the input file link")
    inf=input()
    print("Enter the output file link")
    otf=input()
    g=get_bulk_links(get_urls(inf))
    otfile=open(otf,'r+')
    otfile.write(g)
    otfile.close()
    
