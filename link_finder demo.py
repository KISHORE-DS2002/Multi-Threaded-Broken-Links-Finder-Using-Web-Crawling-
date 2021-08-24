from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self): #self is used to represent the instance of the class.
        # With the self key word u can access the attributes and methods of the class in python
        super().__init__() #gives access to methods and properties of a parent class

    def handle_starttag(self, tag, attrs):
        print(tag)

    def error(self, message):
        pass
finder = LinkFinder()
finder.feed('<html><head><title>Demo</title></head><body><h1>link_finder demo</h1></body></html>')