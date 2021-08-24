from urllib.request import urlopen# Helps To Connect To Web Pages Using Python and this module returns the results in bytes i.e., 1s and 0s
from link_extractor import LinkFinder
from domain_name_extractor import *# '*' Denotes 'All'
from Basic_file_and_path_generator import *

class Spider:# Spider Will Grab A Link From The Several Links In Queue And Connect To a Page,
    # Fetch All The HTMLs And Through Them To The Link Finder And Link Finder Parses Through The Links
    #Class Variables(Shared Among All Instances ie.,Spiders)

    project_name = ''
    base_url = ''
    domain_name = ''# So That We Are Connecting To A Valid Webpage Without Generating A Bunch Of Errors
    queue_file = ''# Text File And It Is Not Written Every Single Time During Every Link Analysis Since That Is Very Very Slow And It Is Not Efficient, But The Data Is Stored Permanantly
    crawled_file = ''# Text File And It Is Not Written Every Single Time During Every Link Analysis Since That Is Very Very Slow And It Is Not Efficient, But The Data Is Stored Permanantly
    broken_file = ''
    queue = set()#This Is Updated A Lot More Faster, But The Data Is Temporary
    crawled = set()#This Is Updated A Lot More Faster, But The Data Is Temporary

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/working.txt'
        Spider.broken_file = Spider.project_name + '/broken.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url) # 1st Spider

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot(): # def boot(self)->before || self Is Not Used Inside We Remove That And Add '@staticmethod' and we arent using self.something inside and is just a proper coding convention
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)# 'base_url' Is Mentioned So That It Gets Added Up To The Queue And The First Spider Recognises It
        Spider.queue = file_to_set(Spider.queue_file) # The Spider Converts The Links In The File And Save It As Set
        Spider.crawled = file_to_set(Spider.crawled_file) # The Spider Converts The Links In The File And Save It As Set

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):# 'thread name' Would Be The Spider Name That Is Currently Crawling And The 'page_url' Denotes The Page That It Is Crawling
        if page_url not in Spider.crawled:# Checking If The Spider Is Not In The Crawled Set(Note That It Is Checking With The Set For Faster Operations)
            print('\n' + thread_name + ' is crawling ' + ' | URL: ' + page_url)
            print('\n' + 'Queue -->' + str(len(Spider.queue)) + ' | Crawled -->' + str(len(Spider.crawled))) # Converting The Number Of Links ie., The Length Of The Sets Into Strings And Displaying Them Under The Respective Categories
            Spider.add_links_to_queue(Spider.gather_links(page_url))# 'add_links_to_queue' Is Going To Add Up The Links To The Queue And 'spider.gather_link' Is A Function That Is Going To Connect To A Web Page And Return A Set Of All Of The links That Are Present On The Webpage And Is Given To 'add_links_to_queue' And That Adds Up the Links To The Waiting List And All the Spiders Will Be Able To See That Waiting List And In That Way They Can All Be Synchronised
            Spider.queue.remove(page_url)# Remove The Page That We Have Crawled
            Spider.crawled.add(page_url) # And We Add Those Removed Pages From Queue(Waiting List) To Crawled(Crawled List)
            Spider.update_files()# This Function Is Going To Call Both Of The Sets('queue And crawles') And Convert Them Into A File

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = '' # the computer returns the html in terms of 1's and 0's and so that we will convert them to human readable string and store them

        try:
            response = urlopen(page_url)# it will connect to the webpage ie., page_url and store the response
            if 'text/html' in response.getheader('Content-Type'):#makes sure that we connect to a webpage(html) and not to any unwanted files like pdfs, etc
                html_bytes = response.read()#reads the html bytes
                html_string = html_bytes.decode("utf-8") #converts them into a human readable string and utf-8 does that task
            finder = LinkFinder(Spider.base_url, page_url) #this goes to the link finder
            finder.feed(html_string)#the html data is passed in and it is going to get parsed and the all other links can be returned
        except Exception as e:
            append_to_file(Spider.broken_file,'URL: '+ page_url + ' | Error Response: ' + str(e) )
            print('\n' + str(e) + ' | URL: ' + page_url)#If there are no links in the page or the page does'nt hold any proper link
            return set()#return an empty set

        return finder.page_links()#returns as long as there is'nt any issues

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):#function to add the links to the queue
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):#if the link is already in the queue ie., in the waiting list or #if the link is already in the crawled list
                continue
            if Spider.domain_name != get_domain_name(url): #if the domain name is not in the url it would stop because if suppose u provide the instagram link
                continue# in the web page it would just go on to scan the instagram which should not happen and it should scan only the links present in a particular website
            Spider.queue.add(url) #if all the above conditions are fine then this happens

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)#update and add or move the links in queue set to the queue file
        set_to_file(Spider.crawled, Spider.crawled_file)#update and add or move the links in crawled set to the crawled file
