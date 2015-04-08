<!-- Video row -->

<div class="row">
		<div class="col-sm-4" align="right">
			{{username}}
			<img src="{{profile_picture}}" width ="40" height="40"> </img>
		</div>
		<div class="col-sm-4">
			<div class="thumbnail">
				<div class="embed-responsive embed-responsive-4by3">
				<!--iframe class="embedded-responsive-item" src="http://scontent.cdninstagram.com/hphotos-xaf1/t50.2886-16/11031375_349775345223242_90672752_n.mp4"></iframe-->
				
					<video class="embedded-responsive-item" width="640" height="640" preload="none" controls>
						<source src="{{video}}" type="video/mp4">
					</video>
				</div>
			</div>
			<div class="caption">
				<p>
				<button type="button" class="btn btn-default" aria-label="Left Align">
					<span class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></span>
					{{like_count}}
				</button>
				{{text_caption}}
				</p>
			
				<p>
					<ul class="list-group">
						<li class="list-group-item"><img src="./Google.jpg" width="20" height="10"> </li>
						% for comment in comments:
							<li class="list-group-item">{{comment}}</li>
						% end
					</ul>
				</p>
			</div>
		</div>
		<div class="col-sm-4"></div>
</div>