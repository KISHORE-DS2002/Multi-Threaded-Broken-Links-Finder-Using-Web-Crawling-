from html.parser import HTMLParser #parse through the html file
from urllib import parse #parse through the URLs
# This HTMLParser Class Takes A Look At A Bunch Of HTML Codes And Sifts Through It

class LinkFinder(HTMLParser):# Inheriting The HTML Parser Into The Class Helps In Accessing All The Functionalities Of THe HTML Parser And We Add Some More Functionalities To It

    def __init__(self, base_url, page_url):#self is used to represent the instance of the class.
        # With the self key word u can access the attributes and methods of the class in python
        super().__init__()#Superclass Initialistaion and the super class gives access to methods
        # and properties of a parent class
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):#Deals Only With The Starting Tag ie., For Example '<head>' Is Only Considered Not '</head>'
        if tag == 'a':#Print The Tag Whenever You Encouter A Starting Tag 'a' ie., The Staring Tag Of Links In Html
            for (attribute, value) in attrs:#'href'-> Is The Attribute | 'url'-> Is The Value || HTMLParser Gives You The Attribute(attrs) And We Are Extracting And Using It Here
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)#If It Is A Relative URL It Would Add The Base URL In Front
                    self.links.add(url)#The Properly Formatted Link Is Added To The 'self.links' Set
    def page_links(self):

        return self.links
    def error(self, message):
        pass
