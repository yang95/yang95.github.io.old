<?php
//header('Content-type:text/json;char-set:utf-8;');
require_once("../lib/common.php");
$route=filter("func");
switch($route){
	case "demo":demo();break; 
	case "see":see();break; 
	default:
	break;
}
function demo(){
	$tpl=T();
	$tpl->assign("data","index"); 
	$tpl->MakeHtmlFile("index1.html","index.html");
	header("location: ".SHOWAPP);
}
function see(){
	$key=filter("key"); 
	$tpl=T();
	$a=F($key);
	$data=$a->get(); 
	$tpl->assign("data",$data["content"]); 
	$name=date("Y-m-d-H-i-s",$key).".html";
	$tpl->MakeHtmlFile($name,"article.html");
	header("location: ".SHOWAPP."/".$name);
}

?>