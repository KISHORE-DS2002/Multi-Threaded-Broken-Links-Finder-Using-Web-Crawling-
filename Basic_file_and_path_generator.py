import os #importing os module
#Each Website Crawling Will Store The Data In Separate Folder.
def create_project_dir(directory):
    if not os.path.exists(directory):  #Create Only If It Doesn't Exists, So That We Fetch The Data Even If It Is Half Way Done And Is Shut Done A 'Back Up' Is There.
        print('Creating directory ' + directory)
        os.makedirs(directory)


#Creation of Queue and Crawl(Only If Not Created).
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"working.txt")
    broken = os.path.join(project_name, "broken.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url) #create the file if not existing already
    if not os.path.isfile(crawled):
        write_file(crawled, '')  #create the file if not existing already
    if not os.path.isfile(broken):
            write_file(broken, '')  # create the file if not existing already
#Creating A New File
def write_file(path, data):
    with open(path, 'w') as f:  #The 'path' Denotes The File Name And 'w' Helps To Turn On The Write Mode, So That We Write Data To It
        f.write(data)  #Writing The 'data' To It


#Add Data To The Existing File So That We Don't Create A New File For Every Webpage
def append_to_file(path, data):
    with open(path, 'a') as file:  #'a' Helps To Turn On The Append Mode, So That The Data Gets Appended To
        # The Opened File 'as file' Is Used To Have A Reference To The File That We Have Opened
        file.write(data + '\n')  #'\n' So That Every Link Gets To The Next Line


# Delete/Clear The Contents Of A File
def delete_file_contents(path):
    open(path, 'w').close()

# 'writing to' operations in python are relatively slower and since we use files to save things that would be relativly slower when compared with that of using simple variables but the files takes over an advantage of backing up the data even if the device shuts down but the data gets deleted when the device shuts down if we use variables


# Read a file and convert each line to set items
def file_to_set(file_name): # set can only have unique elements
    results = set()
    with open(file_name, 'rt') as f: #rt denotes read text file
        for line in f:
            results.add(line.replace('\n', '')) #new line character is not needed in a set
    return results


#Conversion Of The Set Into A File-->Iterate Through A Set, Each Item In The Set Will Be A New Line In The File
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links): #sorting links would make it look better and organised
            f.write(l+"\n")
