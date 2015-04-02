'''import solr

# create a connection to a solr server
s = solr.SolrConnection('http://localhost:8983/solr')

add a document to the index
s.add(id=1, title='Lucene in Action', author=['Erik Hatcher', 'Otis Gospodnetić'])
s.commit()

# do a search
response = s.query('tag:indianfood')
for hit in response.results:
    print hit['tag']'''

from urllib2 import *
conn = urlopen('http://localhost:7574/solr/gettingstarted_shard1_replica1/select?q=food&wt=json')
rsp = eval( conn.read() )

print "number of matches=", rsp['response']['numFound']

#print out the name field for each returned document
for doc in rsp['response']['docs']:
  print 'matched data =', doc['CaptionText']
