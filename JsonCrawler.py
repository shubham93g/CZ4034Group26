#No need to run this file. Run CrawlerUI.py for crawling from instagram

import urllib2
import json

class InstagramMedia:
    tags = 0
    location= 0
    comments= 0
    created_time= 0
    link= 0
    likes= 0
    users_in_photo= 0
    caption= 0
    images= 0
    media_type= 0
    media_links= 0
    user= 0

    def __init__(self,media):
        self.tags = media['tags']
        self.location = media['location']
        self.comments = media['comments']
        self.created = media['created_time']
        self.link = media['link']
        self.likes = media['likes']
        self.users_in_photo = media['users_in_photo']
        self.caption = media['caption']
        self.images = media['images']
        self.media_type = media['type']
        if(self.media_type == 'image'):
            self.media_links = self.images
        else:
            self.media_links = media['videos']
        self.user = media['user']

    def getTags(self):
        return self.tags

    def getLocation(self):
        return self.location

    def getComments(self):
        return self.comments

    def getCreatedTime(self):
        return self.created_time

    def getLink(self):
        return self.link

    def getLikes(self):
        return self.likes

    def getUsersInPhoto(self):
        return self.users_in_photo

    def getCaption(self):
        return self.caption

    def getImages(self):
        return self.images

    def getType(self):
        return self.media_type

    def getMediaLinks(self):
        return self.media_links

    def getUser(self):
        return self.user

    def printMedia(self):
        print self.getTags()
        print self.getLocation()
        print self.getComments()
        print self.getCreatedTime()
        print self.getLink()
        print self.getLikes()
        print self.getUsersInPhoto()
        print self.getCaption()
        print self.getImages()
        print self.getType()
        print self.getMediaLinks()
        print self.getUser()
    
def getJsonResults(url):
    response = urllib2.urlopen(url)
    result = json.load(response)
    return result

def crawlInstagram(tag,count):
    url = 'https://api.instagram.com/v1/tags/' + str(tag) + '/media/recent?client_id=2635546e823342c7a76f083db94a8555'
    counter = 0
    counterLimit = count
    while(counter<counterLimit):
        result = getJsonResults(url)
        fileToWrite = open(tag+str(counter/20+1)+'.txt','w')
        json.dump(result, fileToWrite)
        fileToWrite.close()
        counter = counter + 20
        url = result['pagination']['next_url']

def readMedia(fileName):
    fileToRead = open(fileName)
    results = json.load(fileToRead)
    fileToRead.close()
    mediaList = []
    for media in results['data']:
        mediaList.append(InstagramMedia(media))
    return mediaList

"""
crawlInstagram('food',20)

mediaList = readMedia('1.txt')
for media in mediaList:
    print media.getLink()
"""
