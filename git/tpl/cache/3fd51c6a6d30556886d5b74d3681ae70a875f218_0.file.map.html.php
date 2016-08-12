<?php
/* Smarty version 3.1.30, created on 2016-08-12 23:46:57
  from "E:\code\phpweb\blog\git\tpl\map.html" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_57adef7163fdf4_28747512',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '3fd51c6a6d30556886d5b74d3681ae70a875f218' => 
    array (
      0 => 'E:\\code\\phpweb\\blog\\git\\tpl\\map.html',
      1 => 1471016807,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_57adef7163fdf4_28747512 (Smarty_Internal_Template $_smarty_tpl) {
?>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
	
	<link rel="stylesheet" href="../theme/map/map.css">
	<?php echo '<script'; ?>
 src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"><?php echo '</script'; ?>
>
	<?php echo '<script'; ?>
 type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=HRukRGSbkj7lMvrvPXZI85PG&s=1"><?php echo '</script'; ?>
>
	<?php echo '<script'; ?>
 src = "https://cdn.wilddog.com/js/client/current/wilddog.js" ><?php echo '</script'; ?>
>
	<title>地图</title>
</head>
<body>
	<div id="allmap"></div> 



	<div class="toggle">
		<div class="myimg">
			<img  src="../theme/images/cursor.ico" alt="">
		</div>
	</div>
	<div class="myContainer">
		<div class="myimg">
			<img  src="../theme/images/cursor.ico" alt="">
		</div>
		<div class="write">
			<textarea id="iwantsay"  placeholder="我想说的话"></textarea>
		</div>
	</div>

<?php echo '<script'; ?>
 type="text/javascript" src="../theme/map/map.js">	<?php echo '</script'; ?>
> 
</body>
</html>
<?php }
}
