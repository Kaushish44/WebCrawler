import threading
from queue import Queue
from Spider import Spiders
from Utilities import DomainHandle
from FileOperations import FileHandle

HOMEPAGE = 'http://quotes.toscrape.com/'
PROJECT_NAME = DomainHandle.get_domain(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queued.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4
queue = Queue()
Spiders.Webmaker(PROJECT_NAME, HOMEPAGE, QUEUE_FILE, CRAWLED_FILE)

def thread_creation():
    for i in range(1, NUMBER_OF_THREADS+1):
        print('Thread Number ' + str(i) +' Created')
        t = threading.Thread(target=start_work)
        t.daemon = True
        t.start()
    
def start_work():
    while True:
        try:
            url = queue.get(timeout=1)
            print('Starting Crawl - ' + url)
            Spiders.Webmaker.crawl_page(threading.current_thread().name, url)
            queue.task_done()
        except:
            break
    FileHandle.delete_file_contents(QUEUE_FILE)
    Spiders.Webmaker.update_files()
    print('checking again') 
    check_links()  
    

def create_job(queued_links):
    for link in queued_links:
        queue.put(link)
    print('New Queue created')
    start_work()
    
def check_links():
    queued_links = FileHandle.file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print('Another ' + str(len(queued_links)) + ' Links detected')
        create_job(queued_links)
        
                        
thread_creation()
check_links()
print('No other links found - PROCESS COMPLETE!')