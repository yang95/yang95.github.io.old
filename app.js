function refreshLog() {
	$("#logs").scrollTop($("#logs")[0].scrollHeight);
}
//读文字 
function read(obj){ 
	var str = $(obj).text();
    var audio = document.createElement("AUDIO");
    audio.src="http://tts.baidu.com/text2audio?ie=UTF-8&lan=zh&text="+str;
    audio.play();
}
var events =[];
function push(){
	if(arguments.length<1)return false;
	var s = arguments[0];
	var e = arguments[2]?arguments[1]:arguments[0];
	var m = arguments[2]?arguments[2]:arguments[1]
	events.push({
		startDate:new Date(s),
		endDate:new Date(e),
		message:m,
	});
}
function pop_message(date){ 
	var message = "";
	var date_obj = new Date(date);
	for(var i in events){
		if(
		events[i].startDate <= date_obj
		&& events[i].endDate >= date_obj
		){
			message = events[i].message; 
			$("#messages").append((
				function(d,s){
					var a='<div class="alert alert-success" >'+
							'<a href="#" class="close" data-dismiss="alert">'+
							'	&times;'+
							'</a>'+
							'<strong> '+d+' </strong>  <span onclick="read(this)"> '+s+'. </span>'+
						'</div>		';
						return a;
				}
			)(date,message));
		}
	}
}

var begin  = 2017;
for(i=0;i<50;i++){
	var tmp=i+begin;
	$.getScript("/data/"+tmp+".js",function(){
		 
	});  //加载js文件
	 
}
 
 
 setTimeout(function(){
	 $('#calendar').calendar({ 
				enableRangeSelection: true, 
				clickDay: function(e) { 
					pop_message(e.date.toLocaleDateString());
				},
				dataSource: events
	});
 },3000);