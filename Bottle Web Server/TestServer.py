from bottle import route, run, static_file, template, request, redirect
from urllib2 import *

@route('/other')
def hello():
    return static_file('Starter Template for Bootstrap.html', root='./')

@route('/')
def home():
    
    return template('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>{{page_title}}</title>
	
	
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
	
  </head>

  <body>
	
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Travelogram</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <!--ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul-->
		 
		 <form class="navbar-form navbar-left" role="search" action="/results" method="post">
			<div class="form-group">
				<input type="text" class="form-control" placeholder="Search" name="searchBar">
			</div>
			<select name = "listItem" class="form-control">
                            <option value="tag">Tag</option>
                            <option value="caption">Caption</option>
                            <option value="username">Username</option>
                            <option value="comment">Comments</option>
                        </select>
                        <button type="submit" class="btn btn-default">Submit</button>
		</form>
		 
        </div><!--/.nav-collapse -->
      </div>
    </nav>
	
	<p>a</p>
	<p>a</p>

	  <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
  </body>
</html>


''', page_title='Travelogram')

@route('/results', method='POST') 
def returnSearchResults():
    '''Query fomats:
        select?q=*:*&fq=FullName:*shi*&wt=json ---> matches any string containing 'shi'
        select?q=*:*&fq=FullName:Ashima&wt=json ---> exactly matches Ashima
        select?q=*:*&fq=LikesCount:[10 *]&wt=json ---> returns docs with 10 or more likes
        select?q=*:*&fq=LikesCount:[10 *]&wt=json&fl=LikesUser,FullName ---> response contains on LikesUser and FullName fields
        select?q=*:*&fq=LikesCount:[* 10]&wt=json ---> returns docs with 10 or less likes
        select?q=*:*&fq=LikesCount:[5 *]&fq=LikesCount:[* 10]&wt=json ---> returns docs with more than 5 and less than 10 likes'''

    searchTerm = request.forms.get('searchBar')
    item =  request.forms.get('listItem')
    print searchTerm
    print item

    rsp = None
    query = None
    server = 'http://localhost:7574/solr/gettingstarted_shard1_replica1/'
    
    if(item=='tag'):
        query = server+'select?q=*:*&fq=CaptionText:*'+searchTerm+'*&wt=json'
    elif(item=='caption'):
        query = server+'select?q=*:*&fq=CaptionText:*?'+searchTerm+'*?&wt=json'
    elif(item=='username'):
        query = server+'select?q=*:*&fq=Username:*'+searchTerm+'*&wt=json'
    elif(item=='comment'):
        query = server+'select?q=*:*&fq=Comments:*'+searchTerm+'*&wt=json'
    else:
        query = server+'select?q='+searchTerm+'&wt=json'

    print query
    
    conn = urlopen(query)
    rsp = eval( conn.read() )

    print "number of matches=", rsp['response']['numFound']

    return template('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>{{page_title}}</title>
	
	
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
	
  </head>

  <body>
	
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
           <a class="navbar-brand" href="#">Travelogram</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <!--ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul-->
		 
		 <form class="navbar-form navbar-left" role="search" action="/results" method="post">
			<div class="form-group">
				<input type="text" class="form-control" placeholder="Search" name="searchBar">
			</div>
			<select name = "listItem" class="form-control">
                            <option value="tag">Tag</option>
                            <option value="caption">Caption</option>
                            <option value="username">Username</option>
                            <option value="comment">Comments</option>
                        </select>
                        <button type="submit" class="btn btn-default">Submit</button>
		</form>
		 
        </div><!--/.nav-collapse -->
      </div>
    </nav>
	
	<p>a</p>
	<p>a</p>

	% for doc in rsp['response']['docs']:
            % comms = []
            % if doc['CommentCount'][0] > 0:
                % comms = doc['Comments'][0].split('~|')
            % end
            % if doc['Type'][0] == 'image':
                % include('imageRow.tpl',username= doc['Username'][0],profile_picture=doc['ProfilePicture'][0],image=doc['ImageStdRes'][0],like_count=doc['LikesCount'][0],text_caption=doc['CaptionText'][0],comments=comms)
            % end
            % if doc['Type'][0] == 'video':
                % include('videoRow.tpl',username= doc['Username'][0],profile_picture=doc['ProfilePicture'][0],video=doc['VideoStdRes'][0],like_count=doc['LikesCount'][0],text_caption=doc['CaptionText'][0],comments=comms)
            % end
        % end
   

	  <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
  </body>
</html>


''', page_title='Travelogram - Results', rsp=rsp)

@route('/other/<name>')
def greet(name):
    return template('Hello <b>{{your_name}}</b>, how are you?', your_name=name)

run(host='localhost', port=8080, debug=True)
