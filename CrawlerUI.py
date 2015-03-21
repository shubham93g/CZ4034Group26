#Note: Run this for crawling from instagram
#You may need to ensure your firewall is not blocking urllib2 from accessing the internet
#Needs to be run separately for each tag
#Example: tag = football and count = 200
#We will get 10 files named as football1.txt football2.txt....football10.txt
#Each file contains 20 media from Instagram
#Refer to Reader.py for reading from the files

from Tkinter import *
import JsonCrawler as Js
import JsonCrawlerWithSQL as Js1

root = Tk()

def search():
    Js1.crawlInstagram(str(E1.get()),int(E2.get()))

L1 = Label(root, text="Tag Name")
L1.grid(row=1, column=1) 
E1 = Entry(root, bd =5)
E1.grid(row=1, column=2)



L2 = Label(root, text="Count")
L2.grid(row=2, column=1) 
E2 = Entry(root, bd =5)
E2.grid(row=2, column=2)

"""
L1 = Label(root, text="File Location")
L1.grid(row=3, column=1) 
E1 = Entry(root, bd =5)
E1.grid(row=3, column=2)
"""

B = Button(root, text = "Search", command = search)
B.grid(row=4, column=2)

root.mainloop()
