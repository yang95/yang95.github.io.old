G={
	model:new Wilddog("https://getvideo.wilddogio.com/"),
	url:"http://www.kuaishou.com/rest/photos",
	callback:function(d){
		console.log(d);
	},
};


getvideo={
	load:function(){
		var url=G.url;
		$.getJSON(url,G.callback);		
	}
};

 
 