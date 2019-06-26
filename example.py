import urllib.request
from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/trending"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
#a_tags = soup.find_all('a')
a_tags = soup.find_all('a')
for idx in a_tags:
        if(idx.get('title') == None):
                continue
        else:
                print(idx.get('title'))