"""

Written by Sournav Sekhar Bhattacharya

GIG THEM AGRICULTURALISTS
"""
#SAVE_DIR is the folder where the images are going to get downloaded
SAVE_DIR="test_data"
import urllib.request
from tkinter import *
import os
import threading
def window0():
    def click():
        #data_links.txt is the location of your text file that has all of the
        #links to the images you're going to use
        #seperate links by writing them on different lines
        SAVE_DIR=textentry2.get()
        file = open(textentry.get(),'r')
        lines = file.read().splitlines()
        length=len(lines)
        third=round(length/3)
        twothird=(third*2)
        i=0
        def Splitter(i,third):
                while i<third:
                    filename = SAVE_DIR+"/image"+str(i+1)+".jpg"
                    if (textentry4.get()=="1") and os.path.exists(filename):
                        i+=1
                        continue
                    
                    urllib.request.urlretrieve(lines[i], filename)
                    i+=1
                    textentry4.delete(0, END)
                    
                    textentry4.insert(0,str((i/length)*100))
        def FirstFunction():
                Splitter(i,third)
        def SecondFunction():
                Splitter(third,twothird)
        def ThirdFunction():
                Splitter(twothird,length)
##        FirstFunction()
##        SecondFunction()
##        ThirdFunction()
        
        threads = []
        t = threading.Thread(target=FirstFunction)
        threads.append(t)
        t.start()
        t1 = threading.Thread(target=SecondFunction)
        threads.append(t1)
        t1.start()
        t2 = threading.Thread(target=ThirdFunction)
        threads.append(t2)
        t2.start()
                
    def click2():
        file = open(textentry.get(),'a')
        file.write("\n"+textentry3.get())
    window0=Tk();
    window0.title("NNDB 1.0")
    window0.minsize(width=300, height=250)
    Label(window0,text="Input Data File Location:").place(x=10,y=10)
    textentry = Entry(window0,width=20, bg="white")
    textentry.place(x=10,y=40)
    textentry.insert(0,'data_links.txt')
    Label(window0,text="Output DIR:").place(x=10,y=65)
    textentry2 = Entry(window0,width=20, bg="white")
    textentry2.place(x=10,y=95)
    textentry2.insert(0,'test_data')
    Label(window0,text="Image URL To Add:").place(x=10,y=125)
    textentry3 = Entry(window0,width=20, bg="white")
    textentry3.place(x=10,y=150)
    textentry4 = Entry(window0,width=3, bg="white")
    textentry4.place(x=200,y=100)
    button1=Button(window0,text="SUBMIT",width=6, command=click)
    button1.place(x=10,y=180)
    button2=Button(window0,text="ADD",width=6, command=click2)
    button2.place(x=90,y=180)
    mainloop()
window0()
