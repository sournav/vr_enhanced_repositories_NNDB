"""

Written by Sournav Sekhar Bhattacharya

GIG THEM AGRICULTURALISTS
"""
import urllib.request
#data_links.txt is the location of your text file that has all of the
#links to the images you're going to use
#seperate links by writing them on different lines
file = open('data_links.txt','r')
lines = file.read().splitlines()
i=0
#SAVE_DIR is the folder where the images are going to get downloaded
SAVE_DIR="test_data"
while i<len(lines):
    filename = SAVE_DIR+"/image"+str(i+1)+".jpg"
    urllib.request.urlretrieve(lines[i], filename)
    i+=1
    
