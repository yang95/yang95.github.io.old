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
	var e = arguments[1]?arguments[1]:arguments[0];
	var m = arguments[2]?arguments[2]:arguments[0]
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
$(function() {
	$('#calendar').calendar({ 
		enableRangeSelection: true,
		renderEnd: function(e) {
			if($('#render-end').prop('checked'))
			{
				$('#logs').append('<div class="render-end" style="color:#1C7C26">Render end (' + e.currentYear + ')</div');
				refreshLog();
			}
		},
		renderDay: function(e) {
			if($('#render-day').prop('checked'))
			{
				$('#logs').append('<div class="render-day" style="color:#FF5B9D">Render day (' + e.date.toLocaleDateString() + ')</div');
				refreshLog();
			}
		},
		clickDay: function(e) {
			if($('#click').prop('checked'))
			{
				$('#logs').append('<div class="click" style="color:#1F80C1">Click (' + e.date.toLocaleDateString() + ')</div');
				refreshLog();
			}
			pop_message(e.date.toLocaleDateString());
		},
		dayContextMenu: function(e) {
			if($('#contextmenu').prop('checked'))
			{
				$('#logs').append('<div class="contextmenu" style="color:#9D29B2">Context menu (' + e.date.toLocaleDateString() + ')</div');
				refreshLog();
			}
		},
		selectRange: function(e) {
			if($('#range').prop('checked'))
			{
				$('#logs').append('<div class="range" style="color:#34A522">Select range (' + e.startDate.toLocaleDateString() +  ' -> ' + e.endDate.toLocaleDateString() +')</div');
				refreshLog();
			}
		},
		mouseOnDay: function(e) {
			if($('#mouse-on').prop('checked'))
			{
				$('#logs').append('<div class="mouse-on" style="color:#F95902">Mouse on (' + e.date.toLocaleDateString() + ')</div');
				refreshLog();
			}
		},
		mouseOutDay: function(e) {
			if($('#mouse-out').prop('checked'))
			{
				$('#logs').append('<div class="mouse-out" style="color:#F90202">Mouse out (' + e.date.toLocaleDateString() + ')</div');
				refreshLog();
			}
		},
		dataSource: events
	});
	
	$('.log-display').click(function() { refreshLog(); });
}); 