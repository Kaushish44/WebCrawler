'''
Created on 23-Feb-2018

@author: Aditya Kaushish
'''
from Utilities import Crawler, DomainHandle
from FileOperations import FileHandle
from urllib import parse

class Webmaker():
    
    queued_file = ''
    crawled_file = ''
    queued = set()
    crawled = set()
    
    def __init__(self, project_name, base_url, QUEUE_FILE, CRAWLED_FILE):
        Webmaker.project_name = project_name
        Webmaker.base_url = base_url
        Webmaker.queued_file = QUEUE_FILE
        Webmaker.crawled_file = CRAWLED_FILE
        self.boot()
        self.crawl_page('First crawler', Webmaker.base_url)
    
    @staticmethod
    def boot():
        FileHandle.create_dir(Webmaker.project_name)
        FileHandle.create_files(Webmaker.project_name, Webmaker.base_url,  Webmaker.queued_file, Webmaker.crawled_file )
        Webmaker.queued = FileHandle.file_to_set(Webmaker.queued_file)
        Webmaker.crawled = FileHandle.file_to_set(Webmaker.crawled_file)
        
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Webmaker.crawled:
            print(thread_name + ' is crawling ' + page_url)
            print('Queued - ' + str(len(Webmaker.queued)) + ' | Crawled - ' + str(len(Webmaker.crawled)))
            Webmaker.start_crawling(page_url)
            Webmaker.queued.remove(page_url)
            Webmaker.crawled.add(page_url)
    
    @staticmethod
    def start_crawling(page_url):
        finder = Crawler.PageReader(page_url)
        finder.read_url()
        Webmaker.add_links_to_queue(finder.page_links())
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            url = parse.urljoin('http://quotes.toscrape.com/', url)
            if (url in Webmaker.queued) or (url in Webmaker.crawled):
                continue
            if (Webmaker.project_name != DomainHandle.get_domain(url)):
                print('Avoiding other websites - ' + DomainHandle.get_domain(url))
                continue
            Webmaker.queued.add(url)
    
    @staticmethod
    def update_files():
        FileHandle.set_to_file(Webmaker.queued, Webmaker.queued_file)
        FileHandle.set_to_file(Webmaker.crawled, Webmaker.crawled_file)
        