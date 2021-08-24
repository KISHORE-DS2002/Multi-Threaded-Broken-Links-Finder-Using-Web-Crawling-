from urllib.parse import urlparse #python function for parsing urls(urlparse)


#get domain name(example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.') # we call the get_sub_domain_name function and split the link into
        # name, example, com and extract the last two alone
        return results[-2] + '.' + results[-1]# return secondlast.last ie., example.com
    except:
        return '' # it should return something that's why

#get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc#netloc-network location
    except:
        return '' # it should return something that's why

# chumma try ---> print(get_domain_name('https://tamil.indiatyping.com/'))