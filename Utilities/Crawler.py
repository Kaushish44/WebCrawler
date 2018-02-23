'''
Created on 22-Feb-2018

@author: Aditya Kaushish
'''
import bs4
from urllib.request import urlopen 


#reading the page
class PageReader():
    
    def __init__(self, url):
        self.links = set()
        self.url = url
        
    def read_url(self):
        page_data = urlopen(self.url)
        page_html = page_data.read()
        page_data.close()
        soup_parser = bs4.BeautifulSoup(page_html, "html.parser")
        containers = soup_parser.findAll("a", href=True)
        for a in containers:
            self.links.add(a['href'])
        
    def page_links(self):
        return self.links
        