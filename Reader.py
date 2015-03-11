import JsonCrawler as Js

tag = 'football'
counterLimit = 125
#Only need to change tag and the counterLimit (based on how many files were generated from crawling)
counter = 1
mediaList = []

while counter <= counterLimit:
    fileContent = Js.readMedia(tag + str(counter)+'.txt')
    counter = counter + 1
    mediaList.extend(fileContent)

    #Note: Every fileContent contains 20 InstagramMedia objects

print len(mediaList)

"""
#Each media can be accessed as below.
#Refer to class InstagramMedia in JsonCrawler.py for available function
for media in mediaList:
    print media.getLink()
"""
