$(function(){
	var html = $("body").html();
	$("body").html(marked(html));
});