from bottle import route, run, static_file, template
from urllib2 import *

@route('/other')
def hello():
    return static_file('Starter Template for Bootstrap.html', root='./')
    #return

@route('/')
def home():
    conn = urlopen('http://localhost:7574/solr/gettingstarted_shard1_replica1/select?q=food&wt=json')
    rsp = eval( conn.read() )

    print "number of matches=", rsp['response']['numFound']

    #print out the name field for each returned document
    for doc in rsp['response']['docs']:
        print 'matched data =', doc['CaptionText']
        
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
          <a class="navbar-brand" href="#">Project name</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <!--ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul-->
		 
		 <form class="navbar-form navbar-left" role="search">
			<div class="form-group">
				<input type="text" class="form-control" placeholder="Search">
			</div>
			<button type="submit" class="btn btn-default">Submit</button>
		</form>
		<ul class="nav navbar-nav navbar-right">
			<li class="dropdown">
			<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>
			<ul class="dropdown-menu" role="menu">
				<li><a href="#">Action</a></li>
				<li><a href="#">Another action</a></li>
				<li><a href="#">Something else here</a></li>
				<li class="divider"></li>
				<li><a href="#">Separated link</a></li>
			</ul>
			</li>
		</ul>
		 
        </div><!--/.nav-collapse -->
      </div>
    </nav>
	
	<p>a</p>
	<p>a</p>

        % for doc in rsp['response']['docs']:
        % include('imageRow.tpl',username=doc['CaptionText'][0])
        % end
   
        

	  <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
  </body>
</html>


''', page_title='Shubham\'s template', rsp = rsp)

@route('/other/<name>')
def greet(name):
    return template('Hello <b>{{your_name}}</b>, how are you?', your_name=name)

run(host='localhost', port=8080, debug=True)
