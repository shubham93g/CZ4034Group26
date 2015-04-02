<!-- Image row-->

<div class="row">
		<div class="col-sm-4" align="right">
			{{username}}
			<img src="{{profile_picture}}" width ="40" height="40"/>
		</div>
		<div class="col-sm-4">
			<div class="thumbnail">
				<img src="{{image}}" class="img-rounded centre-block"/>
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
						% for comment in comments:
						<li class="list-group-item">{{comment}}</li>
						% end
					</ul>
				</p>
			</div>
		</div>
		<div class="col-sm-4"></div>
</div>