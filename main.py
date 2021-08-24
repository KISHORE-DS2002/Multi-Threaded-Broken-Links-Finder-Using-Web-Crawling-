import threading# each thread is a worker
from queue import Queue# the queue is the job
from workers import Spider
from domain_name_extractor import *
from Basic_file_and_path_generator import *

PROJECT_NAME = input("Enter the Project's Name: ")
HOMEPAGE = input("Enter the Home Page URL: ")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/working.txt'
BROKEN_FILE = PROJECT_NAME + '/broken.txt'
NUMBER_OF_THREADS = int(input("Enter the No. of Worker Spiders/Threads You Want to Work: "))
queue = Queue() #thread queue or job
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME) #main spider exlusive of the thread
# it creates the project directory, crawles the home page

#create worker threads and they die when main exits
def create_workers():
    for _ in range(NUMBER_OF_THREADS): # _ because just we need to loop 8 times
        t = threading.Thread(target=work)
        t.daemon = True  # die whenever main exits
        t.start() #to start the thread


#do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url) #threading.current_thread().name
        # predefined in python
        queue.task_done() #says the next waiting worker when his task is done


#each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)#taking and sticking the links in thread queue
    queue.join()
    parse()


# check if there are items in the queue, if so crawl them
def parse():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
parse()
