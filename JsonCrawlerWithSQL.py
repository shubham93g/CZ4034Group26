#No need to run this file. Run CrawlerUI.py for crawling from instagram
import MySQLdb
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
    #Connect to  sql database
    try:
	db = MySQLdb.connect(charset='utf8',host="localhost", user="root",passwd="admin", db="Instagram") 
    except Exception as e:
	print e
# you must create a Cursor object
    cur = db.cursor() 
    LikesCount=CommentsCount=0
    LikesUser=Link=Comments=CaptionText=Latitude=Longitude=Created_time=Username=ProfilePicture=FullName=Type=ImageLowRes=ImageThumbnail=''
    ImageStdRes=VideoLowRes=VideoStdRes=VideoLowBandW=''
    row_count = 0
    counter = 0
    counterLimit = count
    while(counter<counterLimit):
        result = getJsonResults(url)
        fileToWrite = open(tag+str(counter/20+1)+'.txt','w')
        json.dump(result, fileToWrite)
        
        fileToWrite.close()
        for item in result["data"]:
            LikesCount=item['likes']['count']

            LikesUserArr = []
            for likes in item['likes']['data']:
                LikesUserArr.append(likes['username'])
            LikesUser=(',').join(LikesUserArr)
            print "LikesUser: "+LikesUser

            CommentsArr=[]
            CommentsCount=item['comments']['count']
            for com in item['comments']['data']:
                x = ""
                y = com['text']
                x = str(unicode(y).encode('ascii','ignore').decode('unicode-escape')).replace("'", "''")
                print 'test replace: ' + x
                CommentsArr.append(x)
            Comments=('~|').join(CommentsArr)
            print "Comments: "+Comments

            Link=item['link']
            if(item['location']):
                if('longitude' in item['location']):
                    Longitude=str(item['location']['longitude'])
                else:
                    Longitude='1000'
                if('latitude' in item['location']):
                    Latitude=str(item['location']['latitude'])
                else:
                    Latitude='1000'
            else:
                Latitude=Longitude='1000'
             
            if(item['caption']):
                try:
                    c = ""
                    c = str(unicode(item['caption']['text']).encode('ascii','ignore').decode('unicode-escape')).replace("'","''")
                    CaptionText=str(unicode(item['caption']['text']).encode('ascii','ignore').decode('unicode-escape')).replace("'","''")
                    print "Caption: "+CaptionText
                except:
                    CaptionText="None"
                    print "in except"
                Created_time=item['caption']['created_time']
            else:
                CaptionText="None"
                Created_time="None"
            Username=item['user']['username']
            print Username
            ProfilePicture=item['user']['profile_picture']
            FullName=str(item['user']['full_name'].encode('ascii','ignore').decode('unicode-escape')).replace("'","''")
            print FullName
            Type=item['type']
            ImageLowRes=item['images']['low_resolution']['url']
            ImageStdRes=item['images']['standard_resolution']['url']
            ImageThumbnail=item['images']['thumbnail']['url']
            if(Type=='video'):
                if(item['videos']['low_bandwidth']):
                    VideoLowBandW=item['videos']['low_bandwidth']['url']
                if(item['videos']['low_resolution']):    
                    VideoLowRes=item['videos']['low_resolution']['url']      
                if(item['videos']['standard_resolution']):
                    VideoStdRes=item['videos']['standard_resolution']['url']
            else:
                VideoLowBandW=VideoLowRes=VideoStdRes="None"
                        
	    d1=tag
	    d2=LikesCount
	    d3=LikesUser
	    d4=CommentsCount
	    d5=Comments
	    d6=Link
	    d7=Longitude
	    d8=Latitude
	    d9=CaptionText
	    d10=Created_time
	    d11=Username
	    d12=ProfilePicture
	    d13=FullName
	    d14=Type
	    d15=ImageLowRes
	    d16=ImageStdRes
	    d17=ImageThumbnail
	    d18=VideoLowBandW
	    d19=VideoLowRes
	    d20=VideoStdRes
	    
	    query="INSERT INTO crawleddata(tag,LikesCount,LikesUser,CommentCount,Comments,Link,Longitude,Latitude,CaptionText,CreatedTime,Username,ProfilePicture,\
	    FullName,Type,ImageLowRes,ImageStdRes,ImageThumbnail,VideoLowBandW,VideoLowRes,VideoStdRes)\
	    VALUES('%s','%d','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20)
            cur.execute(query)
	    db.commit()
	    row_count=row_count+1
        counter = counter + 20
        url = result['pagination']['next_url']
        db.close()

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
