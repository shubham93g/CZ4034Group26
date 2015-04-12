README

************Detailed instructions to execute crawling:*********************
1. Set up database using MySql in XAMPP(host='localhost',user='root',passwd='').
2. Name the database 'instagram'	
3. As long there is an internet connection and Instagram is up and working, run CrawlerUI.py(Crawling folder) to crawl. Key in the tag and the number of records to be crawled in the simple Tkinter UI.
4. Note that if the MySql hostname, user or password is not the same as mentioned in point 1 above, JsonCrawlerWithSQL.py file needs to be updated with the correct hostname, user and password.
5. A table 'traveldata' is created using the structure mentioned in crawling documentation with 'id' made the primary key. This table is necessary to temporarily store crawled data. The crawler will crawl Instagram api and store results in the table.
6.	Warnings are displayed if the database and/or table already exists. These can be safely ignored. Errors might be displayed during the crawling process. This is caught in the exception, this might be due to duplicate images or if the text contains non-ascii characters. This data is skipped and not stored.

**************Detailed Instructions to perform indexing:****************** 
1. Install Bitnami Solr.
2. Start solr from Solr panel. 
3. The Solr panel should have numDocs and maxDocs 0. 
3. Ensure that the MySQLdatabase exists and is running with the dataset. 
4. Open command line. 
5. (change path to Solr example folder) and start Solr by typing the command java -jar start.jar 
6. Open Eclipse IDE , run the Indexing.java file as a Java Application
7. Check IDE console and Solr, 10000 documents should be indexed on Solr with a corresponding notofication message in the IDE console. 

**************Detailed Instructions to run Travelogram:******************
1. Go to (path) and double-click on testserver.py file.
2. Open your web browser and key in 52.74.115.74:8080 in the address bar and press enter
3. There you go! You have successfully started our application! 
