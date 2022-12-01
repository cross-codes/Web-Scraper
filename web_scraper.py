# web_scraper.py

import requests
from bs4 import BeautifulSoup as BS
from lxml import etree

i = 1

BASE_URL = "https://www.myntra.com/shoes?p={pg_no}".format(pg_no=i)
header_param = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
# The above parameter(s) was necessary because I had to pretend to be a real user, in order to access the site.

source = requests.get(BASE_URL, headers = header_param).text
soup = BS(source, "lxml")

tree = etree.fromstring(soup.prettify()) 
tree.xpath('.//div[@class="product-productMetaInfo"]/text()')
[' test\n                 ']


