<!doctype html>
<html class="no-js">
<head>
  <meta charset="utf-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"> 
  <link rel="icon" type="image/png" href="assets/i/favicon.png">
  <link rel="apple-touch-icon-precomposed" href="assets/i/app-icon72x72@2x.png">
  <meta name="apple-mobile-web-app-title" content="Amaze UI" />
  <link rel="stylesheet" href="assets/css/amazeui.min.css"/>
  <link rel="stylesheet" href="assets/css/admin.css"> 
</head>
<body>
<!--[if lte IE 9]>
<p class="browsehappy">你正在使用<strong>过时</strong>的浏览器，Amaze UI 暂不支持。 请 <a href="http://browsehappy.com/" target="_blank">升级浏览器</a>
  以获得更好的体验！</p>
<![endif]-->
<?php require_once("header.php");?>
<?php require_once("slider.php");?>
<!-- content start -->
<div class="admin-content">

  <div class="am-cf am-padding">
    <div class="am-fl am-cf"><strong class="am-text-primary am-text-lg">统计</strong> / <small>account</small></div>
  </div>

  <div class="am-tabs am-margin" data-am-tabs id="container">    
  </div>

  
  
<a class="am-icon-btn " onClick="getvideo.load()" >加载更多</a>
   
</div>
<!-- content end -->

</div>

<a class="am-icon-btn am-icon-th-list am-show-sm-only admin-menu" data-am-offcanvas="{target: '#admin-offcanvas'}"></a>

<?php require_once("footer.php");?>

<!--[if lt IE 9]>
<script src="http://libs.baidu.com/jquery/1.11.1/jquery.min.js"></script>
<script src="http://cdn.staticfile.org/modernizr/2.8.3/modernizr.js"></script>
<script src="assets/js/polyfill/rem.min.js"></script>
<script src="assets/js/polyfill/respond.min.js"></script>
<script src="assets/js/amazeui.legacy.js"></script>
<![endif]-->

<!--[if (gte IE 9)|!(IE)]><!-->
<script src="assets/js/jquery.min.js"></script> 
 
<script>
   
   container=$("#container");
   url="../core/src/video.php?func=getvideo";
   getvideo={
	   load:function(){
		   var me=this;
		   $.getJSON(url,function(d,e){
			   console.log(d);
			   me.success(d);
		   });
	   },
	   success:function(d){
		   var me=this;
		   $.each(d.photos,function(k,v){
			   me.tpl(v);
		   });
	   },
	   tpl:function(v){
		   var str="<a href='"+v.mp4Url+"'><img style='height:300px' src='"+v.thumbnailUrl+"'/>"+v.caption+"</a>";
		   container.append(str);
	   }
   };
   
   getvideo.load();
</script>
</body>
</html>
