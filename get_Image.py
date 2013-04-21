import os 
import urllib
import re

#gets the input from the user
url = raw_input("Type a sub-reddit site or type 0 to exit: ")

while url != '0':
    
    while url.isdigit() == 1: #Checks if the user type a number
        print 'This is not a sub-reddit website!'
        url = raw_input("Type a sub-Reddit site or type 0 to exit: ")
    
    if url.find('http://') != 0:
        url = 'http://' + url
        
    website = urllib.urlopen(url)
    source = website.read()

    imgs = re.findall("id\=\'header-img\'.*?src=\"(.*?)\"\s", source) #finds the website where the alien image can be downloaded
    
    # test to see if it is a sub-Reddit website
    if imgs == []:
        print 'This is not a sub-Reddit website!'

    if not os.getcwd() == 'C:\Users\Public\Pictures':
        os.chdir('C:\Users\Public\Pictures')
    
    #Creates  the directory Reddit Pictures if it doesn't exist
    if not os.path.exists('Reddit Pictures'):
        os.mkdir('Reddit Pictures')

    for img in imgs:
        filename = 'Reddit Pictures/'+ img.split('/')[-1]
        if not os.path.exists(filename):
            urllib.urlretrieve(img,filename)    #download the image 
            
    url = raw_input("Type a sub-reddit site or type 0 to exit: ")
